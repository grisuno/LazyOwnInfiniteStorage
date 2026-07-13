"""Integration tests for full encode/decode roundtrip and web interface."""

import hashlib
import os
import random
import subprocess
import tempfile

import pytest

from lazyown_infinitestorage import (
    LazyOwnConfig,
    LazyOwnInfiniteStorage,
    LazyOwnInfiniteStorage as Storage,
)


class TestEncodeDecodeRoundtrip:
    """Specification: Files encoded to video and decoded back must be bit-identical."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.storage = Storage(self.config)

    def test_secure_protocol_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            data = os.urandom(1024)
            with open(source, 'wb') as f:
                f.write(data)
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            assert len(candidates) == 1
            encoded = os.path.join(tmpdir, candidates[0])
            assert os.path.exists(encoded)
            decoded = os.path.join(tmpdir, 'decoded.bin')
            self.storage.decode(encoded, decoded, 4, self.config.PROTOCOL_VERSION_SECURE)
            with open(decoded, 'rb') as f:
                recovered = f.read()
            assert recovered == data

    def test_legacy_protocol_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            data = os.urandom(512)
            with open(source, 'wb') as f:
                f.write(data)
            base = os.path.join(tmpdir, 'legacy')
            self.storage.encode(source, base, 320, 240, 15, 4, self.config.PROTOCOL_VERSION_LEGACY)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('legacy') and f.endswith('.mp4')]
            assert len(candidates) == 1
            encoded = os.path.join(tmpdir, candidates[0])
            assert os.path.exists(encoded)
            decoded = os.path.join(tmpdir, 'decoded.bin')
            self.storage.decode(encoded, decoded, 4, self.config.PROTOCOL_VERSION_LEGACY)
            with open(decoded, 'rb') as f:
                recovered = f.read()
            assert recovered == data

    def test_secure_protocol_resilient_to_resolution_change(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            data = os.urandom(1024)
            with open(source, 'wb') as f:
                f.write(data)
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            encoded = os.path.join(tmpdir, candidates[0])
            resized = os.path.join(tmpdir, 'resized_640x480.mp4')
            subprocess.run(
                ['ffmpeg', '-y', '-i', encoded, '-vf', 'scale=320:240', resized],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            decoded = os.path.join(tmpdir, 'decoded.bin')
            self.storage.decode(resized, decoded, 4, self.config.PROTOCOL_VERSION_SECURE)
            with open(decoded, 'rb') as f:
                recovered = f.read()
            assert recovered == data

    def test_protocol_auto_detection_prefers_secure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            data = b'auto detect test'
            with open(source, 'wb') as f:
                f.write(data)
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            encoded = os.path.join(tmpdir, candidates[0])
            detected = self.storage._detect_protocol(encoded, 4)
            assert detected == self.config.PROTOCOL_VERSION_SECURE

    def test_empty_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'empty.bin')
            with open(source, 'wb'):
                pass
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            encoded = os.path.join(tmpdir, candidates[0])
            decoded = os.path.join(tmpdir, 'decoded.bin')
            self.storage.decode(encoded, decoded, 4, self.config.PROTOCOL_VERSION_SECURE)
            with open(decoded, 'rb') as f:
                assert f.read() == b''

    def test_large_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'large.bin')
            data = os.urandom(64 * 1024)
            with open(source, 'wb') as f:
                f.write(data)
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            encoded = os.path.join(tmpdir, candidates[0])
            decoded = os.path.join(tmpdir, 'decoded.bin')
            self.storage.decode(encoded, decoded, 4, self.config.PROTOCOL_VERSION_SECURE)
            with open(decoded, 'rb') as f:
                recovered = f.read()
            assert hashlib.sha256(recovered).hexdigest() == hashlib.sha256(data).hexdigest()


@pytest.mark.skipif(
    not __import__('lazyown_infinitestorage', fromlist=['HAS_FLASK']).HAS_FLASK,
    reason='Flask not installed',
)
class TestWebRunner:
    """Specification: Web interface accepts uploads, encodes/decodes, and serves downloads."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.storage = Storage(self.config)
        self.runner = self.storage.create_web_runner()
        self.runner.run_setup()
        self.client = self.runner._app.test_client()

    def test_index_get(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'LazyOwnInfiniteStorage' in response.data

    def test_encode_upload(self):
        import io
        data = io.BytesIO(b'test payload')
        response = self.client.post(
            '/',
            data={
                'action': 'encode',
                'protocol': 'secure',
                'input_file': (data, 'test.bin'),
                'output_file_name': 'output',
                'frame_width': '640',
                'frame_height': '480',
                'fps': '30',
                'block_size': '4',
            },
            content_type='multipart/form-data',
        )
        assert response.status_code == 200
        assert b'Operation completed successfully' in response.data

    def test_decode_upload(self):
        import io
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            with open(source, 'wb') as f:
                f.write(b'decode test')
            base = os.path.join(tmpdir, 'encoded')
            self.storage.encode(source, base, 640, 480, 30, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('encoded') and f.endswith('.mp4')]
            encoded = os.path.join(tmpdir, candidates[0])
            with open(encoded, 'rb') as f:
                video = io.BytesIO(f.read())
            response = self.client.post(
                '/',
                data={
                    'action': 'decode',
                    'protocol': 'secure',
                    'input_file': (video, 'encoded_640x480.mp4'),
                    'output_file_name': 'decoded',
                    'block_size': '4',
                },
                content_type='multipart/form-data',
            )
            assert response.status_code == 200
            assert b'Operation completed successfully' in response.data

    def test_security_headers_present(self):
        response = self.client.get('/')
        assert response.headers.get('X-Content-Type-Options') == 'nosniff'
        assert response.headers.get('X-Frame-Options') == 'DENY'
        assert response.headers.get('Strict-Transport-Security')

    def test_download_not_found(self):
        response = self.client.get('/download/nonexistent.bin')
        assert response.status_code == 404

    def test_missing_file_error(self):
        response = self.client.post(
            '/',
            data={
                'action': 'encode',
                'protocol': 'secure',
                'output_file_name': 'output',
                'frame_width': '640',
                'frame_height': '480',
                'fps': '30',
                'block_size': '4',
            },
            content_type='multipart/form-data',
        )
        assert response.status_code == 200
        assert b'Error' in response.data
