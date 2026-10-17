"""Tests for zip pipeline and security hardening in LazyOwnInfiniteStorage."""

import os
import tempfile
import zipfile

import pytest

from lazyown_infinitestorage import LazyOwnConfig, LazyOwnInfiniteStorage, SecurityValidator


class TestZipRoundtrip:
    """Specification: zip -> video -> zip must recover the original files bit-identical."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.storage = LazyOwnInfiniteStorage(self.config)

    def _make_source_dir(self, tmpdir):
        source = os.path.join(tmpdir, 'source_dir')
        os.makedirs(source)
        with open(os.path.join(source, 'a.txt'), 'wb') as f:
            f.write(b'hello world')
        with open(os.path.join(source, 'b.bin'), 'wb') as f:
            f.write(os.urandom(256))
        sub = os.path.join(source, 'sub')
        os.makedirs(sub)
        with open(os.path.join(sub, 'c.txt'), 'wb') as f:
            f.write(b'nested file')
        return source

    def test_zip_to_video_roundtrip_secure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = self._make_source_dir(tmpdir)
            video = os.path.join(tmpdir, 'archive')
            self.storage.zip_to_video(source, video, 320, 240, 15, 4, self.config.PROTOCOL_VERSION_SECURE)
            candidates = [f for f in os.listdir(tmpdir) if f.startswith('archive') and f.endswith('.mp4')]
            assert len(candidates) == 1
            encoded = os.path.join(tmpdir, candidates[0])
            restored = os.path.join(tmpdir, 'restored')
            self.storage.video_to_zip(encoded, restored, 4, self.config.PROTOCOL_VERSION_SECURE)
            recovered = os.path.join(restored, 'source_dir', 'a.txt')
            assert os.path.exists(recovered)
            with open(recovered, 'rb') as f:
                assert f.read() == b'hello world'
            recovered_bin = os.path.join(restored, 'source_dir', 'b.bin')
            with open(recovered_bin, 'rb') as f:
                assert len(f.read()) == 256
            recovered_nested = os.path.join(restored, 'source_dir', 'sub', 'c.txt')
            assert os.path.exists(recovered_nested)

    def test_create_and_extract_zip_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = self._make_source_dir(tmpdir)
            zip_path = os.path.join(tmpdir, 'bundle.zip')
            self.storage.create_zip(source, zip_path)
            assert os.path.exists(zip_path)
            with zipfile.ZipFile(zip_path) as zf:
                names = zf.namelist()
                assert 'a.txt' in names or 'source_dir/a.txt' in names
            out_dir = os.path.join(tmpdir, 'extracted')
            self.storage.extract_zip(zip_path, out_dir)
            assert os.path.isdir(out_dir)


class TestZipSecurity:
    """Specification: Zip extraction blocks zip slip and zip bombs."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.storage = LazyOwnInfiniteStorage(self.config)

    def test_extract_zip_blocks_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, 'evil.zip')
            out_dir = os.path.join(tmpdir, 'out')
            os.makedirs(out_dir)
            target_outside = os.path.join(tmpdir, 'outside.txt')
            with zipfile.ZipFile(zip_path, 'w') as zf:
                info = zipfile.ZipInfo('../outside.txt')
                zf.writestr(info, b'malicious')
            with pytest.raises(ValueError, match='escapes target directory'):
                self.storage.extract_zip(zip_path, out_dir)
            assert not os.path.exists(target_outside)

    def test_extract_zip_blocks_uncompressed_bomb(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, 'bomb.zip')
            out_dir = os.path.join(tmpdir, 'out')
            os.makedirs(out_dir)
            big = b'0' * (self.config.MAX_ZIP_UNCOMPRESSED_BYTES + 1)
            with zipfile.ZipFile(zip_path, 'w') as zf:
                zf.writestr('big.txt', big)
            with pytest.raises(ValueError, match='exceeds maximum uncompressed size'):
                self.storage.extract_zip(zip_path, out_dir)


class TestEncodeOutputValidation:
    """Specification: The final encoded output path is validated, not just the requested one."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.storage = LazyOwnInfiniteStorage(self.config)

    def test_encode_rejects_output_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = os.path.join(tmpdir, 'source.bin')
            with open(source, 'wb') as f:
                f.write(b'data')
            output = os.path.join(tmpdir, '..', '..', 'tmp', 'evil.mp4')
            with pytest.raises(ValueError, match='Path traversal'):
                self.storage.encode(source, output, 64, 64, 1, 1, self.config.PROTOCOL_VERSION_SECURE)


class TestSecurityValidatorUnchanged:
    """Specification: Existing security validator behavior is preserved."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.validator = SecurityValidator(self.config)

    def test_rejects_traversal(self):
        with pytest.raises(ValueError, match='Path traversal'):
            self.validator.validate_file_path('../../etc/passwd')

    def test_sanitizes_filename(self):
        assert self.validator.sanitize_filename('../../../evil.sh') == 'evil.sh'
