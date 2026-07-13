"""Unit tests for ErrorCorrector Hamming(8,4) implementation."""

import pytest
from lazyown_infinitestorage import LazyOwnConfig, ErrorCorrector


class TestErrorCorrector:
    """Specification: ErrorCorrector encodes bytes into Hamming(8,4) and corrects single-bit errors."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.corrector = ErrorCorrector(self.config)

    def test_encode_data_doubles_length(self):
        data = b'\x00\xff\x42'
        encoded = self.corrector.encode_data(data)
        assert len(encoded) == len(data) * 2

    def test_decode_data_reverses_encoding(self):
        data = b'\x00\xff\x42\x99'
        encoded = self.corrector.encode_data(data)
        decoded = self.corrector.decode_data(encoded)
        assert decoded == data

    def test_decode_data_with_single_bit_error(self):
        data = b'\x42'
        encoded = bytearray(self.corrector.encode_data(data))
        encoded[0] ^= 0b00000100
        decoded = self.corrector.decode_data(bytes(encoded))
        assert decoded == data

    def test_decode_data_rejects_odd_length(self):
        with pytest.raises(ValueError, match='even'):
            self.corrector.decode_data(b'\x01\x02\x03')

    def test_encode_nibble_all_values(self):
        for nibble in range(16):
            encoded = self.corrector._encode_nibble(nibble)
            assert encoded >= 0 and encoded <= 255

    def test_decode_nibble_all_values(self):
        for nibble in range(16):
            encoded = self.corrector._encode_nibble(nibble)
            decoded = self.corrector._decode_nibble(encoded)
            assert decoded == nibble

    @pytest.mark.parametrize('data', [b'', b'\x00', b'\xff' * 256, b'random bytes here!'])
    def test_roundtrip_various_inputs(self, data):
        encoded = self.corrector.encode_data(data)
        decoded = self.corrector.decode_data(encoded)
        assert decoded == data

    @pytest.mark.parametrize('nibble', range(16))
    def test_single_bit_error_per_nibble(self, nibble):
        encoded = self.corrector._encode_nibble(nibble)
        for bit in range(8):
            corrupted = encoded ^ (1 << bit)
            corrected = self.corrector._decode_nibble(corrupted)
            assert corrected == nibble, f"Failed for nibble {nibble}, bit {bit}"
