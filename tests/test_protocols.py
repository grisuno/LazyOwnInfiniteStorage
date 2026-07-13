"""Unit tests for LegacyProtocolHandler and SecureProtocolHandler."""

import pytest
from lazyown_infinitestorage import LazyOwnConfig, ErrorCorrector, LegacyProtocolHandler, SecureProtocolHandler


class TestLegacyProtocolHandler:
    """Specification: Legacy v1 protocol packs data with end-marker, unpacks by filename resolution."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.handler = LegacyProtocolHandler(self.config)

    def test_pack_includes_end_marker(self):
        data = b'hello'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        byte_count = len(bit_string) // 8
        assert byte_count == len(data) + len(self.config.END_MARKER_LEGACY)

    def test_unpack_strips_end_marker(self):
        data = b'test data bytes'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        unpacked = self.handler.unpack(bit_string, 4)
        assert unpacked == data

    def test_unpack_with_trailing_zeros(self):
        data = b'short'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        padded = bit_string + '0' * 64
        unpacked = self.handler.unpack(padded, 4)
        assert unpacked == data


class TestSecureProtocolHandler:
    """Specification: Secure v2 protocol packs data with header, CRC32, and Hamming correction."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        corrector = ErrorCorrector(self.config)
        self.handler = SecureProtocolHandler(self.config, corrector)

    def test_pack_produces_bit_string(self):
        data = b'secure payload'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        assert len(bit_string) > self.config.HEADER_TOTAL_SIZE * 16

    def test_unpack_recovers_original_data(self):
        data = b'secure payload for testing v2 protocol'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        unpacked = self.handler.unpack(bit_string, 4)
        assert unpacked == data

    def test_unpack_detects_corrupted_header(self):
        data = b'test'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        hamming_bytes = bytearray()
        for i in range(0, len(bit_string), 8):
            hamming_bytes.append(int(bit_string[i:i + 8], 2))
        hamming_bytes[self.config.HEADER_OFFSET_MAGIC] ^= 0xFF
        corrupted = ''.join(format(b, '08b') for b in hamming_bytes)
        with pytest.raises(ValueError, match='Header CRC mismatch'):
            self.handler.unpack(corrupted, 4)

    def test_unpack_detects_corrupted_payload(self):
        data = b'payload to corrupt'
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        hamming_bytes = bytearray()
        for i in range(0, len(bit_string), 8):
            hamming_bytes.append(int(bit_string[i:i + 8], 2))
        header_hamming = self.config.HEADER_TOTAL_SIZE * 2
        hamming_bytes[header_hamming + 4] ^= 0xFF
        hamming_bytes[header_hamming + 5] ^= 0xFF
        corrupted = ''.join(format(b, '08b') for b in hamming_bytes)
        with pytest.raises(ValueError, match='Payload CRC mismatch'):
            self.handler.unpack(corrupted, 4)

    @pytest.mark.parametrize('size', [0, 1, 1024, 65536])
    def test_roundtrip_various_sizes(self, size):
        data = bytes(range(256)) * (size // 256) + bytes(range(size % 256))
        bit_string = self.handler.pack(data, 640, 480, 4, 30)
        unpacked = self.handler.unpack(bit_string, 4)
        assert unpacked == data
