"""Unit tests for FrameEncoder and FrameDecoder."""

import numpy as np
import pytest
from lazyown_infinitestorage import LazyOwnConfig, FrameEncoder, FrameDecoder


class TestFrameEncoder:
    """Specification: FrameEncoder converts bit strings into grayscale frames."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.encoder = FrameEncoder(self.config)

    def test_bits_to_frames_yields_correct_number_of_frames(self):
        bits = '1' * 100
        frame_width = 16
        frame_height = 16
        block_size = 4
        effective_w = (frame_width // block_size) * block_size
        effective_h = (frame_height // block_size) * block_size
        blocks_per_frame = (effective_w // block_size) * (effective_h // block_size)
        expected_frames = (len(bits) + blocks_per_frame - 1) // blocks_per_frame
        frames = list(self.encoder.bits_to_frames(bits, frame_width, frame_height, block_size))
        assert len(frames) == expected_frames

    def test_each_frame_has_correct_dimensions(self):
        bits = '10101010'
        frames = list(self.encoder.bits_to_frames(bits, 640, 480, 4))
        assert all(f.shape == (480, 640) for f in frames)

    def test_bit_one_produces_white_block(self):
        bits = '1'
        frames = list(self.encoder.bits_to_frames(bits, 16, 16, 4))
        assert frames[0][0, 0] == 255

    def test_bit_zero_produces_black_block(self):
        bits = '0'
        frames = list(self.encoder.bits_to_frames(bits, 16, 16, 4))
        assert frames[0][0, 0] == 0

    def test_padding_zeros_fill_incomplete_frame(self):
        bits = '1' * 3
        block_size = 4
        frames = list(self.encoder.bits_to_frames(bits, 16, 16, block_size))
        flat = frames[0].flatten()
        white_pixels = np.sum(flat == 255)
        black_pixels = np.sum(flat == 0)
        assert white_pixels == 3 * block_size * block_size
        assert black_pixels == len(flat) - white_pixels


class TestFrameDecoder:
    """Specification: FrameDecoder extracts bit strings from rawvideo grayscale bytes."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.decoder = FrameDecoder(self.config)

    def test_extract_bits_from_empty_raises(self):
        with pytest.raises(ValueError, match='Invalid frame dimensions'):
            self.decoder.extract_bits_from_raw_frames(b'', 0, 480, 4)

    def test_extract_bits_from_raw_frames_basic(self):
        bits = '1010' * 16
        encoder = FrameEncoder(self.config)
        frames = list(encoder.bits_to_frames(bits, 16, 16, 4))
        raw = b''.join(f.tobytes() for f in frames)
        extracted = self.decoder.extract_bits_from_raw_frames(raw, 16, 16, 4)
        assert extracted[:len(bits)] == bits

    def test_extract_bits_respects_expected_bits(self):
        bits = '1' * 100
        encoder = FrameEncoder(self.config)
        frames = list(encoder.bits_to_frames(bits, 16, 16, 4))
        raw = b''.join(f.tobytes() for f in frames)
        extracted = self.decoder.extract_bits_from_raw_frames(raw, 16, 16, 4, expected_bits=50)
        assert len(extracted) == 50

    def test_extract_bits_from_resized_frame(self):
        bits = '1' * 10 + '0' * 10
        encoder = FrameEncoder(self.config)
        frames = list(encoder.bits_to_frames(bits, 640, 480, 4))
        raw = b''.join(f.tobytes() for f in frames)
        extracted = self.decoder.extract_bits_from_raw_frames(raw, 640, 480, 4, expected_bits=len(bits))
        assert extracted == bits
