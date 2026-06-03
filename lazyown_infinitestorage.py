#!/usr/bin/env python3
"""LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder."""

import argparse
import binascii
import math
import os
import re
import struct
import subprocess
import sys
import tempfile
import hashlib
import random
import shutil
from typing import Optional, Tuple, List, Generator

import cv2
import numpy as np

try:
    from flask import Flask, request, send_file, render_template_string
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

try:
    from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                                 QPushButton, QFileDialog, QSpinBox, QComboBox, QMessageBox,
                                 QProgressBar)
    from PyQt5.QtCore import QThread, pyqtSignal, Qt
    HAS_PYQT5 = True
except ImportError:
    HAS_PYQT5 = False


BANNER = """
 ▄█          ▄████████  ▄███████▄  ▄██   ▄    ▄██████▄   ▄█     █▄  ███▄▄▄▄
 ███         ███    ███ ██▀     ▄██ ███   ██▄ ███    ███ ███     ███ ███▀▀▀██▄
 ███         ███    ███       ▄███▀ ███▄▄▄███ ███    ███ ███     ███ ███   ███
 ███         ███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███ ███    ███ ███     ███ ███   ███
 ███       ▀███████████   ▄███▀   ▀ ▄██   ███ ███    ███ ███     ███ ███   ███
 ███         ███    ███ ▄███▀       ███   ███ ███    ███ ███     ███ ███   ███
 ███▌    ▄   ███    ███ ███▄     ▄█ ███   ███ ███    ███ ███ ▄█▄ ███ ███   ███
 █████▄▄██   ███    █▀   ▀████████▀  ▀█████▀   ▀██████▀   ▀███▀███▀   ▀█   █▀
  ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█      ███        ▄████████
 ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███  ▀█████████▄   ███    ███
 ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌    ▀███▀▀██   ███    █▀
 ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌     ███   ▀  ▄███▄▄▄
 ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌     ███     ▀▀███▀▀▀
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    █▄
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    ███
 █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀      ▄████▀     ██████████
    ▄████████     ███      ▄██████▄     ▄████████    ▄████████    ▄██████▄     ▄████████
   ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
   ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███   ███    █▀    ███    █▀
   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███  ▄███         ▄███▄▄▄
 ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀
          ███     ███     ███    ███ ▀███████████   ███    ███   ███    ███   ███    █▄
    ▄█    ███     ███     ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
  ▄████████▀     ▄████▀    ▀██████▀    ███    ███   ███    █▀    ████████▀    ██████████
"""


WEB_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LazyOwn Infinite Storage</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container py-5">
<h1 class="mb-4">LazyOwn Infinite Storage</h1>
<form method="post" enctype="multipart/form-data">
<div class="mb-3">
<label class="form-label">Mode</label>
<select name="action" class="form-select">
<option value="encode">Encode</option>
<option value="decode">Decode</option>
</select>
</div>
<div class="mb-3">
<label class="form-label">Input File</label>
<input type="file" name="input_file" class="form-control" required>
</div>
<div class="mb-3">
<label class="form-label">Output Filename</label>
<input type="text" name="output_file_name" class="form-control" required>
</div>
<div class="mb-3">
<label class="form-label">Protocol</label>
<select name="protocol" class="form-select">
<option value="secure">Secure (v2)</option>
<option value="legacy">Legacy (v1)</option>
</select>
</div>
<div class="row">
<div class="col-md-6 mb-3">
<label class="form-label">Frame Width</label>
<input type="number" name="frame_width" class="form-control" value="640" min="64" max="4096">
</div>
<div class="col-md-6 mb-3">
<label class="form-label">Frame Height</label>
<input type="number" name="frame_height" class="form-control" value="480" min="64" max="4096">
</div>
</div>
<div class="row">
<div class="col-md-6 mb-3">
<label class="form-label">FPS</label>
<input type="number" name="fps" class="form-control" value="30" min="1" max="120">
</div>
<div class="col-md-6 mb-3">
<label class="form-label">Block Size</label>
<input type="number" name="block_size" class="form-control" value="4" min="1" max="64">
</div>
</div>
<button type="submit" class="btn btn-primary">Start</button>
</form>
{% if result %}
<div class="alert alert-info mt-4">{{ result }}</div>
{% endif %}
{% if download_url %}
<a href="{{ download_url }}" class="btn btn-success mt-2">Download Output</a>
{% endif %}
</div>
</body>
</html>"""


class LazyOwnConfig:
    """Centralized immutable configuration constants for LazyOwnInfiniteStorage."""

    MAGIC_BYTES = b'LAZY'
    PROTOCOL_VERSION_LEGACY = 1
    PROTOCOL_VERSION_SECURE = 2

    DEFAULT_FRAME_WIDTH = 640
    DEFAULT_FRAME_HEIGHT = 480
    DEFAULT_FPS = 30
    DEFAULT_BLOCK_SIZE = 4

    MIN_FRAME_WIDTH = 64
    MIN_FRAME_HEIGHT = 64
    MAX_FRAME_WIDTH = 4096
    MAX_FRAME_HEIGHT = 4096
    MIN_BLOCK_SIZE = 1
    MAX_BLOCK_SIZE = 64
    MIN_FPS = 1
    MAX_FPS = 120

    MAX_INPUT_FILE_SIZE = 1024 * 1024 * 1024

    HEADER_OFFSET_MAGIC = 0
    HEADER_SIZE_MAGIC = 4
    HEADER_OFFSET_VERSION = 4
    HEADER_SIZE_VERSION = 1
    HEADER_OFFSET_FLAGS = 5
    HEADER_SIZE_FLAGS = 1
    HEADER_OFFSET_RESERVED = 6
    HEADER_SIZE_RESERVED = 2
    HEADER_OFFSET_FILE_SIZE = 8
    HEADER_SIZE_FILE_SIZE = 8
    HEADER_OFFSET_WIDTH = 16
    HEADER_SIZE_WIDTH = 4
    HEADER_OFFSET_HEIGHT = 20
    HEADER_SIZE_HEIGHT = 4
    HEADER_OFFSET_BLOCK_SIZE = 24
    HEADER_SIZE_BLOCK_SIZE = 2
    HEADER_OFFSET_FPS = 26
    HEADER_SIZE_FPS = 2
    HEADER_OFFSET_PAYLOAD_CRC = 28
    HEADER_SIZE_PAYLOAD_CRC = 4
    HEADER_OFFSET_HEADER_CRC = 32
    HEADER_SIZE_HEADER_CRC = 4
    HEADER_TOTAL_SIZE = 36

    HAMMING_ENCODED_HEADER_BYTES = HEADER_TOTAL_SIZE * 2
    HAMMING_ENCODED_HEADER_BITS = HAMMING_ENCODED_HEADER_BYTES * 8

    PROTOCOL_DETECTION_BITS = 2048
    CANDIDATE_BLOCK_SIZES = [4, 8, 16, 2, 1, 32]

    TEMP_DIR_PREFIX = 'lazyown_'

    END_MARKER_LEGACY = b'\x80'

    FFMPEG_ENCODE_INPUT_FORMAT = 'rawvideo'
    FFMPEG_ENCODE_PIXEL_FORMAT = 'gray'
    FFMPEG_ENCODE_CODEC = 'libx264'
    FFMPEG_ENCODE_PIXEL_FORMAT_OUTPUT = 'yuv420p'
    FFMPEG_ENCODE_MOVFLAGS = 'faststart'

    FFMPEG_DECODE_PIX_FMT = 'gray'
    FFMPEG_DECODE_FORMAT = 'rawvideo'

    ALLOWED_ENCODE_EXTENSIONS = {'.zip', '.tar', '.gz', '.bz2', '.xz', '.7z', '.bin', '.dat', ''}
    ALLOWED_DECODE_EXTENSIONS = {'.mp4', '.avi', '.mkv', '.mov'}
    ALLOWED_OUTPUT_ENCODE_EXTENSIONS = {'.mp4'}
    ALLOWED_OUTPUT_DECODE_EXTENSIONS = {'.zip', '.bin', '.dat'}

    WEB_MAX_CONTENT_LENGTH = 100 * 1024 * 1024
    WEB_UPLOAD_FOLDER = 'uploads'
    WEB_DOWNLOAD_FOLDER = 'downloads'
    WEB_SECRET_KEY_ENV = 'LAZYOWN_SECRET_KEY'


class SecurityValidator:
    """Validates file paths and inputs to prevent path traversal and abuse."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def validate_file_path(self, file_path: str, must_exist: bool = False) -> str:
        """Resolves and validates an absolute file path."""
        absolute = os.path.abspath(file_path)
        normalized = os.path.normpath(absolute)
        if '..' in normalized.split(os.sep):
            raise ValueError("Path traversal detected")
        if must_exist and not os.path.exists(normalized):
            raise FileNotFoundError(f"File not found: {normalized}")
        return normalized

    def validate_size(self, size: int) -> None:
        """Ensures the file size is within acceptable limits."""
        if size > self._config.MAX_INPUT_FILE_SIZE:
            raise ValueError(f"File size exceeds maximum allowed {self._config.MAX_INPUT_FILE_SIZE} bytes")

    def sanitize_filename(self, filename: str) -> str:
        """Sanitizes a filename to remove unsafe characters."""
        name = os.path.basename(filename)
        sanitized = re.sub(r'[^a-zA-Z0_\-\.]', '', name)
        if not sanitized:
            sanitized = 'file'
        return sanitized

    def validate_extension(self, file_path: str, allowed_extensions: set) -> None:
        """Ensures the file extension is in the allowed set."""
        _, ext = os.path.splitext(file_path.lower())
        if ext not in allowed_extensions:
            raise ValueError(f"Disallowed file extension: {ext}")


class ErrorCorrector:
    """Implements Hamming(8,4) extended error correction for byte streams."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def encode_data(self, data: bytes) -> bytes:
        """Encodes a byte sequence using Hamming(8,4) correction."""
        result = bytearray()
        for byte_val in data:
            high = self._encode_nibble((byte_val >> 4) & 0x0F)
            low = self._encode_nibble(byte_val & 0x0F)
            result.append(high)
            result.append(low)
        return bytes(result)

    def decode_data(self, data: bytes) -> bytes:
        """Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction."""
        if len(data) % 2 != 0:
            raise ValueError("Hamming encoded data length must be even")
        result = bytearray()
        for i in range(0, len(data), 2):
            high_nibble = self._decode_nibble(data[i])
            low_nibble = self._decode_nibble(data[i + 1])
            result.append((high_nibble << 4) | low_nibble)
        return bytes(result)

    def _encode_nibble(self, nibble: int) -> int:
        d1 = (nibble >> 3) & 1
        d2 = (nibble >> 2) & 1
        d3 = (nibble >> 1) & 1
        d4 = nibble & 1
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        p4 = p1 ^ p2 ^ d1 ^ p3 ^ d2 ^ d3 ^ d4
        return (p1 << 7) | (p2 << 6) | (d1 << 5) | (p3 << 4) | (d2 << 3) | (d3 << 2) | (d4 << 1) | p4

    def _decode_nibble(self, byte_val: int) -> int:
        b = [(byte_val >> (7 - i)) & 1 for i in range(8)]
        s1 = b[0] ^ b[2] ^ b[4] ^ b[6]
        s2 = b[1] ^ b[2] ^ b[5] ^ b[6]
        s3 = b[3] ^ b[4] ^ b[5] ^ b[6]
        s4 = b[0] ^ b[1] ^ b[2] ^ b[3] ^ b[4] ^ b[5] ^ b[6] ^ b[7]
        syndrome = (s3 << 2) | (s2 << 1) | s1
        if syndrome == 0:
            if s4 == 1:
                b[7] ^= 1
        else:
            if s4 == 1 and 1 <= syndrome <= 7:
                b[syndrome - 1] ^= 1
        d1 = b[2]
        d2 = b[4]
        d3 = b[5]
        d4 = b[6]
        return (d1 << 3) | (d2 << 2) | (d3 << 1) | d4


class FrameEncoder:
    """Encodes bit strings into numpy grayscale frames."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def bits_to_frames(self, bit_string: str, frame_width: int, frame_height: int, block_size: int) -> Generator[np.ndarray, None, None]:
        """Yields grayscale frames from a bit string."""
        effective_w = (frame_width // block_size) * block_size
        effective_h = (frame_height // block_size) * block_size
        blocks_per_row = effective_w // block_size
        blocks_per_col = effective_h // block_size
        bits_per_frame = blocks_per_row * blocks_per_col
        total_bits = len(bit_string)
        frame_count = (total_bits + bits_per_frame - 1) // bits_per_frame
        for i in range(frame_count):
            chunk = bit_string[i * bits_per_frame:(i + 1) * bits_per_frame]
            if len(chunk) < bits_per_frame:
                chunk = chunk + '0' * (bits_per_frame - len(chunk))
            yield self._create_frame(chunk, effective_w, effective_h, block_size, blocks_per_row)

    def _create_frame(self, bits: str, width: int, height: int, block_size: int, blocks_per_row: int) -> np.ndarray:
        frame = np.zeros((height, width), dtype=np.uint8)
        for idx, bit in enumerate(bits):
            x = (idx % blocks_per_row) * block_size
            y = (idx // blocks_per_row) * block_size
            color = 255 if bit == '1' else 0
            frame[y:y + block_size, x:x + block_size] = color
        return frame


class FrameDecoder:
    """Decodes grayscale frames into bit strings."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def extract_bits_from_raw_frames(self, raw_bytes: bytes, width: int, height: int, block_size: int, expected_bits: Optional[int] = None) -> str:
        """Extracts a bit string from rawvideo grayscale bytes."""
        frame_pixel_count = width * height
        if frame_pixel_count == 0:
            raise ValueError("Invalid frame dimensions")
        if len(raw_bytes) % frame_pixel_count != 0:
            valid_len = (len(raw_bytes) // frame_pixel_count) * frame_pixel_count
            raw_bytes = raw_bytes[:valid_len]
        frame_count = len(raw_bytes) // frame_pixel_count
        if frame_count == 0:
            return ''
        frames = np.frombuffer(raw_bytes, dtype=np.uint8).reshape((frame_count, height, width))
        valid_h = (height // block_size) * block_size
        valid_w = (width // block_size) * block_size
        frames = frames[:, :valid_h, :valid_w]
        blocks_h = valid_h // block_size
        blocks_w = valid_w // block_size
        reshaped = frames.reshape(frame_count, blocks_h, block_size, blocks_w, block_size)
        block_means = reshaped.mean(axis=(2, 4))
        bits_arr = (block_means > 127).astype(np.uint8)
        bits_flat = bits_arr.reshape(-1)
        if expected_bits is not None and len(bits_flat) > expected_bits:
            bits_flat = bits_flat[:expected_bits]
        return ''.join(str(b) for b in bits_flat)


class FFmpegPipeline:
    """Manages FFmpeg subprocess communication without intermediate frame files."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def get_video_info(self, input_path: str) -> dict:
        """Retrieves native resolution and metadata from a video file."""
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise RuntimeError(f"Cannot open video: {input_path}")
        info = {
            'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            'fps': cap.get(cv2.CAP_PROP_FPS),
            'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        }
        cap.release()
        return info

    def get_metadata(self, input_path: str) -> dict:
        """Extracts custom lazyown metadata from a video file using ffprobe."""
        metadata = {}
        try:
            proc = subprocess.run(
                ['ffprobe', '-v', 'error', '-show_entries', 'format_tags', '-of', 'json', input_path],
                capture_output=True, text=True, timeout=30
            )
            if proc.returncode == 0:
                import json
                info = json.loads(proc.stdout)
                tags = info.get('format', {}).get('tags', {})
                for key, value in tags.items():
                    if key.startswith('lazyown_'):
                        metadata[key] = value
        except Exception:
            pass
        return metadata

    def encode_video(self, frame_generator: Generator[np.ndarray, None, None], output_path: str, frame_width: int, frame_height: int, fps: int) -> None:
        """Encodes a generator of frames into a video file via FFmpeg stdin."""
        cmd = [
            'ffmpeg', '-y',
            '-f', self._config.FFMPEG_ENCODE_INPUT_FORMAT,
            '-pix_fmt', self._config.FFMPEG_ENCODE_PIXEL_FORMAT,
            '-s', f'{frame_width}x{frame_height}',
            '-r', str(fps),
            '-i', '-',
            '-c:v', self._config.FFMPEG_ENCODE_CODEC,
            '-pix_fmt', self._config.FFMPEG_ENCODE_PIXEL_FORMAT_OUTPUT,
            '-movflags', self._config.FFMPEG_ENCODE_MOVFLAGS,
            output_path
        ]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            for frame in frame_generator:
                proc.stdin.write(frame.tobytes())
        except BrokenPipeError:
            pass
        finally:
            proc.stdin.close()
            stderr = proc.stderr.read()
            proc.wait()
            if proc.returncode != 0:
                raise RuntimeError(f"ffmpeg encoding failed: {stderr.decode('utf-8', errors='replace')}")

    def extract_raw_frames(self, input_path: str, target_width: Optional[int] = None, target_height: Optional[int] = None, max_frames: Optional[int] = None) -> bytes:
        """Extracts raw grayscale frames from a video file via FFmpeg stdout."""
        cmd = [
            'ffmpeg', '-y', '-i', input_path,
            '-f', self._config.FFMPEG_DECODE_FORMAT,
            '-pix_fmt', self._config.FFMPEG_DECODE_PIX_FMT
        ]
        if target_width and target_height:
            cmd.extend(['-s', f'{target_width}x{target_height}'])
        if max_frames is not None:
            cmd.extend(['-frames:v', str(max_frames)])
        cmd.append('-')
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            raw_bytes = proc.stdout.read()
        finally:
            proc.stdout.close()
            proc.wait()
            if proc.returncode != 0:
                stderr = proc.stderr.read().decode('utf-8', errors='replace')
                raise RuntimeError(f"ffmpeg decoding failed: {stderr}")
        return raw_bytes


class ProtocolHandler:
    """Abstract base for encoding and decoding protocol implementations."""

    def pack(self, data: bytes, frame_width: int, frame_height: int, block_size: int, fps: int) -> str:
        """Packs raw data into a bit string."""
        raise NotImplementedError

    def unpack(self, bit_string: str, block_size: int, **kwargs) -> bytes:
        """Unpacks a bit string into raw data."""
        raise NotImplementedError


class LegacyProtocolHandler(ProtocolHandler):
    """Implements the original v1 protocol with filename-based resolution and end marker."""

    def __init__(self, config: LazyOwnConfig):
        self._config = config

    def pack(self, data: bytes, frame_width: int, frame_height: int, block_size: int, fps: int) -> str:
        data_with_marker = data + self._config.END_MARKER_LEGACY
        bit_string = ''.join(format(byte, '08b') for byte in data_with_marker)
        return bit_string

    def unpack(self, bit_string: str, block_size: int, **kwargs) -> bytes:
        byte_data = bytearray()
        for i in range(0, len(bit_string), 8):
            chunk = bit_string[i:i + 8]
            if len(chunk) < 8:
                break
            byte_data.append(int(chunk, 2))
        end_marker = self._config.END_MARKER_LEGACY[0]
        end = byte_data.rfind(end_marker)
        if end != -1:
            byte_data = byte_data[:end]
        return bytes(byte_data)


class SecureProtocolHandler(ProtocolHandler):
    """Implements the v2 protocol with structured headers, CRC32, and Hamming error correction."""

    def __init__(self, config: LazyOwnConfig, corrector: ErrorCorrector):
        self._config = config
        self._corrector = corrector

    def pack(self, data: bytes, frame_width: int, frame_height: int, block_size: int, fps: int) -> str:
        header = bytearray(self._config.HEADER_TOTAL_SIZE)
        header[self._config.HEADER_OFFSET_MAGIC:self._config.HEADER_OFFSET_MAGIC + self._config.HEADER_SIZE_MAGIC] = self._config.MAGIC_BYTES
        header[self._config.HEADER_OFFSET_VERSION] = self._config.PROTOCOL_VERSION_SECURE
        struct.pack_into('>Q', header, self._config.HEADER_OFFSET_FILE_SIZE, len(data))
        struct.pack_into('>I', header, self._config.HEADER_OFFSET_WIDTH, frame_width)
        struct.pack_into('>I', header, self._config.HEADER_OFFSET_HEIGHT, frame_height)
        struct.pack_into('>H', header, self._config.HEADER_OFFSET_BLOCK_SIZE, block_size)
        struct.pack_into('>H', header, self._config.HEADER_OFFSET_FPS, fps)
        payload = self._corrector.encode_data(data)
        payload_crc = binascii.crc32(data) & 0xFFFFFFFF
        struct.pack_into('>I', header, self._config.HEADER_OFFSET_PAYLOAD_CRC, payload_crc)
        header_crc = binascii.crc32(bytes(header[:self._config.HEADER_OFFSET_HEADER_CRC])) & 0xFFFFFFFF
        struct.pack_into('>I', header, self._config.HEADER_OFFSET_HEADER_CRC, header_crc)
        full_data = bytes(header) + payload
        full_data_hamming = self._corrector.encode_data(full_data)
        bit_string = ''.join(format(byte, '08b') for byte in full_data_hamming)
        return bit_string

    def unpack(self, bit_string: str, block_size: int, **kwargs) -> bytes:
        hamming_bytes = bytearray()
        for i in range(0, len(bit_string), 8):
            chunk = bit_string[i:i + 8]
            if len(chunk) < 8:
                break
            hamming_bytes.append(int(chunk, 2))
        full_data = self._corrector.decode_data(bytes(hamming_bytes))
        if len(full_data) < self._config.HEADER_TOTAL_SIZE:
            raise ValueError("Insufficient data for secure header")
        header = full_data[:self._config.HEADER_TOTAL_SIZE]
        payload = full_data[self._config.HEADER_TOTAL_SIZE:]
        stored_header_crc = struct.unpack_from('>I', header, self._config.HEADER_OFFSET_HEADER_CRC)[0]
        calc_header_crc = binascii.crc32(header[:self._config.HEADER_OFFSET_HEADER_CRC]) & 0xFFFFFFFF
        if stored_header_crc != calc_header_crc:
            raise ValueError("Header CRC mismatch")
        file_size = struct.unpack_from('>Q', header, self._config.HEADER_OFFSET_FILE_SIZE)[0]
        inner_decoded = self._corrector.decode_data(payload)
        if file_size > len(inner_decoded):
            raise ValueError("File size exceeds decoded payload length")
        actual_data = inner_decoded[:file_size]
        stored_payload_crc = struct.unpack_from('>I', header, self._config.HEADER_OFFSET_PAYLOAD_CRC)[0]
        calc_payload_crc = binascii.crc32(actual_data) & 0xFFFFFFFF
        if stored_payload_crc != calc_payload_crc:
            raise ValueError("Payload CRC mismatch")
        return actual_data


class LazyOwnInfiniteStorage:
    """Main orchestrator for encoding and decoding files to and from video."""

    def __init__(self, config: Optional[LazyOwnConfig] = None):
        self.config = config or LazyOwnConfig()
        self._validator = SecurityValidator(self.config)
        self._corrector = ErrorCorrector(self.config)
        self._frame_encoder = FrameEncoder(self.config)
        self._frame_decoder = FrameDecoder(self.config)
        self._ffmpeg = FFmpegPipeline(self.config)
        self._legacy_handler = LegacyProtocolHandler(self.config)
        self._secure_handler = SecureProtocolHandler(self.config, self._corrector)

    def encode(self, input_path: str, output_path: str, frame_width: int, frame_height: int, fps: int, block_size: int, protocol_version: Optional[int] = None) -> None:
        """Encodes a file into a video using the specified protocol."""
        input_path = self._validator.validate_file_path(input_path, must_exist=True)
        output_path = self._validator.validate_file_path(output_path, must_exist=False)
        self._validator.validate_size(os.path.getsize(input_path))
        self._validate_encoding_parameters(frame_width, frame_height, fps, block_size)
        if protocol_version is None:
            protocol_version = self.config.PROTOCOL_VERSION_SECURE
        if protocol_version == self.config.PROTOCOL_VERSION_LEGACY:
            handler = self._legacy_handler
            base, ext = os.path.splitext(output_path)
            output_path = f"{base}_{frame_width}x{frame_height}{ext}"
        else:
            handler = self._secure_handler
        with open(input_path, 'rb') as f:
            data = f.read()
        bit_string = handler.pack(data, frame_width, frame_height, block_size, fps)
        frame_generator = self._frame_encoder.bits_to_frames(bit_string, frame_width, frame_height, block_size)
        if protocol_version == self.config.PROTOCOL_VERSION_LEGACY:
            base, ext = os.path.splitext(output_path)
            if f"_{frame_width}x{frame_height}" not in base:
                output_path = f"{base}_{frame_width}x{frame_height}{ext}"
        else:
            base, ext = os.path.splitext(output_path)
            if f"_{frame_width}x{frame_height}" not in base:
                output_path = f"{base}_{frame_width}x{frame_height}{ext}"
        self._ffmpeg.encode_video(frame_generator, output_path, frame_width, frame_height, fps)

    def decode(self, input_path: str, output_path: str, block_size: int, protocol_version: Optional[int] = None) -> None:
        """Decodes a video back into the original file using the specified protocol."""
        input_path = self._validator.validate_file_path(input_path, must_exist=True)
        output_path = self._validator.validate_file_path(output_path, must_exist=False)
        if protocol_version is None:
            protocol_version = self._detect_protocol(input_path, block_size)
        if protocol_version == self.config.PROTOCOL_VERSION_LEGACY:
            self._decode_legacy(input_path, output_path, block_size)
        else:
            self._decode_secure(input_path, output_path, block_size)

    def _validate_encoding_parameters(self, frame_width: int, frame_height: int, fps: int, block_size: int) -> None:
        if not (self.config.MIN_FRAME_WIDTH <= frame_width <= self.config.MAX_FRAME_WIDTH):
            raise ValueError(f"Frame width must be between {self.config.MIN_FRAME_WIDTH} and {self.config.MAX_FRAME_WIDTH}")
        if not (self.config.MIN_FRAME_HEIGHT <= frame_height <= self.config.MAX_FRAME_HEIGHT):
            raise ValueError(f"Frame height must be between {self.config.MIN_FRAME_HEIGHT} and {self.config.MAX_FRAME_HEIGHT}")
        if not (self.config.MIN_FPS <= fps <= self.config.MAX_FPS):
            raise ValueError(f"FPS must be between {self.config.MIN_FPS} and {self.config.MAX_FPS}")
        if not (self.config.MIN_BLOCK_SIZE <= block_size <= self.config.MAX_BLOCK_SIZE):
            raise ValueError(f"Block size must be between {self.config.MIN_BLOCK_SIZE} and {self.config.MAX_BLOCK_SIZE}")

    def _detect_protocol(self, input_path: str, block_size: Optional[int]) -> int:
        candidates = [block_size] if block_size else self.config.CANDIDATE_BLOCK_SIZES
        try:
            info = self._ffmpeg.get_video_info(input_path)
            native_w, native_h = info['width'], info['height']
            for bs in candidates:
                if bs is None:
                    continue
                try:
                    bits_needed = self.config.HAMMING_ENCODED_HEADER_BITS
                    blocks_per_frame = (native_w // bs) * (native_h // bs)
                    if blocks_per_frame == 0:
                        continue
                    frames_needed = math.ceil(bits_needed / blocks_per_frame) + 1
                    raw = self._ffmpeg.extract_raw_frames(input_path, native_w, native_h, max_frames=frames_needed)
                    bits = self._frame_decoder.extract_bits_from_raw_frames(raw, native_w, native_h, bs, expected_bits=bits_needed)
                    if len(bits) < bits_needed:
                        continue
                    hamming_bytes = bytearray()
                    for i in range(0, len(bits), 8):
                        hamming_bytes.append(int(bits[i:i + 8], 2))
                    min_needed = self.config.HAMMING_ENCODED_HEADER_BYTES
                    if len(hamming_bytes) < min_needed:
                        continue
                    decoded = self._corrector.decode_data(bytes(hamming_bytes[:min_needed + (len(hamming_bytes) % 2)]))
                    if decoded[:len(self.config.MAGIC_BYTES)] == self.config.MAGIC_BYTES:
                        return self.config.PROTOCOL_VERSION_SECURE
                except Exception:
                    continue
        except Exception:
            pass
        return self.config.PROTOCOL_VERSION_LEGACY

    def _decode_legacy(self, input_path: str, output_path: str, block_size: int) -> None:
        file_name = os.path.splitext(os.path.basename(input_path))[0]
        resolution_str = file_name.split('_')[-1]
        try:
            width, height = map(int, resolution_str.split('x'))
        except ValueError:
            raise ValueError("Legacy decode requires resolution in filename like name_640x480.mp4")
        raw_bytes = self._ffmpeg.extract_raw_frames(input_path, width, height)
        bit_string = self._frame_decoder.extract_bits_from_raw_frames(raw_bytes, width, height, block_size)
        data = self._legacy_handler.unpack(bit_string, block_size)
        with open(output_path, 'wb') as f:
            f.write(data)

    def _decode_secure(self, input_path: str, output_path: str, block_size: int) -> None:
        file_name = os.path.splitext(os.path.basename(input_path))[0]
        resolution_str = file_name.split('_')[-1]
        try:
            width, height = map(int, resolution_str.split('x'))
        except ValueError:
            raise ValueError("Secure decode requires resolution in filename like name_640x480.mp4")
        raw_bytes = self._ffmpeg.extract_raw_frames(input_path, width, height)
        bit_string = self._frame_decoder.extract_bits_from_raw_frames(raw_bytes, width, height, block_size)
        data = self._secure_handler.unpack(bit_string, block_size)
        with open(output_path, 'wb') as f:
            f.write(data)


class CLIRunner:
    """Command-line interface runner for LazyOwnInfiniteStorage."""

    def __init__(self, storage: LazyOwnInfiniteStorage):
        self._storage = storage

    def run(self) -> None:
        parser = argparse.ArgumentParser(description='LazyOwnInfiniteStorage')
        parser.add_argument('--mode', choices=['encode', 'decode', 'test'], required=True, help='Operation mode')
        parser.add_argument('--input', help='Input file path')
        parser.add_argument('--output', help='Output file path')
        parser.add_argument('--frame_size', type=int, nargs=2, help='Frame width and height')
        parser.add_argument('--fps', type=int, default=LazyOwnConfig.DEFAULT_FPS, help='Frames per second')
        parser.add_argument('--block_size', type=int, default=LazyOwnConfig.DEFAULT_BLOCK_SIZE, help='Block size in pixels')
        parser.add_argument('--protocol', choices=['legacy', 'secure'], default='secure', help='Protocol version')
        parser.add_argument('--gui', action='store_true', help='Launch graphical user interface')
        parser.add_argument('--serve', action='store_true', help='Launch web server')
        parser.add_argument('--host', default='0.0.0.0', help='Web server host')
        parser.add_argument('--port', type=int, default=5000, help='Web server port')
        args = parser.parse_args()

        if args.gui:
            GUIRunner(self._storage).run()
            return
        if args.serve:
            WebRunner(self._storage).run(args.host, args.port)
            return
        if args.mode == 'test':
            run_tests()
            return

        protocol_map = {
            'legacy': self._storage.config.PROTOCOL_VERSION_LEGACY,
            'secure': self._storage.config.PROTOCOL_VERSION_SECURE
        }
        protocol_version = protocol_map[args.protocol]

        if args.mode == 'encode':
            if not args.input or not args.output or not args.frame_size:
                parser.error('--input, --output, and --frame_size are required for encode')
            self._storage.encode(args.input, args.output, args.frame_size[0], args.frame_size[1], args.fps, args.block_size, protocol_version)
        elif args.mode == 'decode':
            if not args.input or not args.output:
                parser.error('--input and --output are required for decode')
            self._storage.decode(args.input, args.output, args.block_size, protocol_version)


if HAS_PYQT5:
    class Worker(QThread):
        """Background worker thread for non-blocking GUI operations."""

        finished = pyqtSignal(str)
        error = pyqtSignal(str)

        def __init__(self, func, *args, **kwargs):
            super().__init__()
            self.func = func
            self.args = args
            self.kwargs = kwargs

        def run(self):
            try:
                self.func(*self.args, **self.kwargs)
                self.finished.emit("Operation completed successfully")
            except Exception as exc:
                self.error.emit(str(exc))

    class GUIRunner(QWidget):
        """PyQt5 graphical user interface for LazyOwnInfiniteStorage."""

        def __init__(self, storage: LazyOwnInfiniteStorage):
            super().__init__()
            self._storage = storage
            self._worker = None
            self._init_ui()

        def _init_ui(self):
            self.setWindowTitle("LazyOwn Infinite Storage")
            layout = QVBoxLayout()
            self.setLayout(layout)

            self.mode_combo = QComboBox()
            self.mode_combo.addItems(["encode", "decode"])
            self.mode_combo.currentIndexChanged.connect(self._change_mode)
            layout.addWidget(QLabel("Mode:"))
            layout.addWidget(self.mode_combo)

            self.input_label = QLabel("Input file:")
            self.input_edit = QLineEdit()
            self.input_button = QPushButton("Browse")
            self.input_button.clicked.connect(self._browse_input)
            input_layout = QHBoxLayout()
            input_layout.addWidget(self.input_edit)
            input_layout.addWidget(self.input_button)
            layout.addWidget(self.input_label)
            layout.addLayout(input_layout)

            self.output_label = QLabel("Output file:")
            self.output_edit = QLineEdit()
            layout.addWidget(self.output_label)
            layout.addWidget(self.output_edit)

            self.protocol_combo = QComboBox()
            self.protocol_combo.addItems(["secure", "legacy"])
            layout.addWidget(QLabel("Protocol:"))
            layout.addWidget(self.protocol_combo)

            size_layout = QHBoxLayout()
            self.width_spin = QSpinBox()
            self.width_spin.setRange(self._storage.config.MIN_FRAME_WIDTH, self._storage.config.MAX_FRAME_WIDTH)
            self.width_spin.setValue(self._storage.config.DEFAULT_FRAME_WIDTH)
            self.height_spin = QSpinBox()
            self.height_spin.setRange(self._storage.config.MIN_FRAME_HEIGHT, self._storage.config.MAX_FRAME_HEIGHT)
            self.height_spin.setValue(self._storage.config.DEFAULT_FRAME_HEIGHT)
            size_layout.addWidget(QLabel("Width:"))
            size_layout.addWidget(self.width_spin)
            size_layout.addWidget(QLabel("Height:"))
            size_layout.addWidget(self.height_spin)
            layout.addLayout(size_layout)

            self.fps_label = QLabel("FPS:")
            self.fps_spin = QSpinBox()
            self.fps_spin.setRange(self._storage.config.MIN_FPS, self._storage.config.MAX_FPS)
            self.fps_spin.setValue(self._storage.config.DEFAULT_FPS)
            layout.addWidget(self.fps_label)
            layout.addWidget(self.fps_spin)

            self.block_label = QLabel("Block size:")
            self.block_spin = QSpinBox()
            self.block_spin.setRange(self._storage.config.MIN_BLOCK_SIZE, self._storage.config.MAX_BLOCK_SIZE)
            self.block_spin.setValue(self._storage.config.DEFAULT_BLOCK_SIZE)
            layout.addWidget(self.block_label)
            layout.addWidget(self.block_spin)

            self.progress = QProgressBar()
            self.progress.setRange(0, 100)
            layout.addWidget(self.progress)

            self.start_button = QPushButton("Start")
            self.start_button.clicked.connect(self._start)
            layout.addWidget(self.start_button)

            self._change_mode()

        def _change_mode(self):
            mode = self.mode_combo.currentText()
            if mode == "encode":
                self.input_label.setText("Input file:")
                self.fps_label.show()
                self.fps_spin.show()
            else:
                self.input_label.setText("Video file:")
                self.fps_label.hide()
                self.fps_spin.hide()

        def _browse_input(self):
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            if self.mode_combo.currentText() == "encode":
                file_path, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", "All Files (*)", options=options)
            else:
                file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mkv *.mov);;All Files (*)", options=options)
            if file_path:
                self.input_edit.setText(file_path)

        def _start(self):
            input_path = self.input_edit.text()
            output_path = self.output_edit.text()
            frame_width = self.width_spin.value()
            frame_height = self.height_spin.value()
            block_size = self.block_spin.value()
            fps = self.fps_spin.value()
            protocol_str = self.protocol_combo.currentText()
            protocol_version = self._storage.config.PROTOCOL_VERSION_LEGACY if protocol_str == "legacy" else self._storage.config.PROTOCOL_VERSION_SECURE
            mode = self.mode_combo.currentText()

            self.progress.setValue(0)
            self.start_button.setEnabled(False)

            if mode == "encode":
                self._worker = Worker(self._storage.encode, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)
            else:
                self._worker = Worker(self._storage.decode, input_path, output_path, block_size, protocol_version)

            self._worker.finished.connect(self._on_finished)
            self._worker.error.connect(self._on_error)
            self._worker.start()

        def _on_finished(self, message):
            self.progress.setValue(100)
            self.start_button.setEnabled(True)
            QMessageBox.information(self, "Result", message)

        def _on_error(self, message):
            self.progress.setValue(0)
            self.start_button.setEnabled(True)
            QMessageBox.critical(self, "Error", message)

        def run(self):
            app = QApplication(sys.argv)
            self.show()
            sys.exit(app.exec_())
else:
    class GUIRunner:
        """Stub GUI runner when PyQt5 is unavailable."""

        def __init__(self, storage: LazyOwnInfiniteStorage):
            self._storage = storage

        def run(self):
            print("PyQt5 is not installed. GUI unavailable.")


if HAS_FLASK:
    class WebRunner:
        """Flask web server interface for LazyOwnInfiniteStorage."""

        def __init__(self, storage: LazyOwnInfiniteStorage):
            self._storage = storage
            self._app = Flask(__name__)
            self._setup_routes()

        def _setup_routes(self):
            cfg = self._storage.config
            self._app.config['SECRET_KEY'] = os.environ.get(cfg.WEB_SECRET_KEY_ENV, os.urandom(32).hex())
            self._app.config['MAX_CONTENT_LENGTH'] = cfg.WEB_MAX_CONTENT_LENGTH

            @self._app.route('/', methods=['GET', 'POST'])
            def index():
                result = None
                download_url = None
                if request.method == 'POST':
                    try:
                        action = request.form.get('action', 'encode')
                        protocol_str = request.form.get('protocol', 'secure')
                        protocol_version = cfg.PROTOCOL_VERSION_LEGACY if protocol_str == 'legacy' else cfg.PROTOCOL_VERSION_SECURE
                        input_file = request.files.get('input_file')
                        output_name = request.form.get('output_file_name', 'output')
                        frame_width = int(request.form.get('frame_width', cfg.DEFAULT_FRAME_WIDTH))
                        frame_height = int(request.form.get('frame_height', cfg.DEFAULT_FRAME_HEIGHT))
                        fps = int(request.form.get('fps', cfg.DEFAULT_FPS))
                        block_size = int(request.form.get('block_size', cfg.DEFAULT_BLOCK_SIZE))
                        if not input_file or not input_file.filename:
                            result = "No input file provided"
                            return render_template_string(WEB_TEMPLATE, result=result, download_url=None)
                        sanitized_output = self._storage._validator.sanitize_filename(output_name)
                        tmp_dir = tempfile.mkdtemp(prefix=cfg.TEMP_DIR_PREFIX)
                        try:
                            input_path = os.path.join(tmp_dir, 'upload')
                            input_file.save(input_path)
                            output_path = os.path.join(tmp_dir, sanitized_output)
                            if action == 'encode':
                                self._storage.encode(input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)
                                if protocol_version == cfg.PROTOCOL_VERSION_LEGACY:
                                    candidates = [f for f in os.listdir(tmp_dir) if f != 'upload']
                                    if candidates:
                                        output_path = os.path.join(tmp_dir, candidates[0])
                            else:
                                self._storage.decode(input_path, output_path, block_size, protocol_version)
                            download_name = self._storage._validator.sanitize_filename(os.path.basename(output_path))
                            dest_dir = cfg.WEB_DOWNLOAD_FOLDER
                            os.makedirs(dest_dir, exist_ok=True)
                            dest_path = os.path.join(dest_dir, download_name)
                            shutil.move(output_path, dest_path)
                            download_url = f"/download/{download_name}"
                            result = "Operation completed successfully"
                        except Exception as exc:
                            result = f"Error: {exc}"
                        finally:
                            shutil.rmtree(tmp_dir, ignore_errors=True)
                    except Exception as exc:
                        result = f"Error: {exc}"
                return render_template_string(WEB_TEMPLATE, result=result, download_url=download_url)

            @self._app.route('/download/<filename>')
            def download(filename):
                safe_name = self._storage._validator.sanitize_filename(filename)
                file_path = os.path.join(cfg.WEB_DOWNLOAD_FOLDER, safe_name)
                if os.path.exists(file_path):
                    return send_file(file_path, as_attachment=True)
                return render_template_string(WEB_TEMPLATE, result="File not found", download_url=None), 404

            @self._app.after_request
            def add_security_headers(response):
                response.headers['X-Content-Type-Options'] = 'nosniff'
                response.headers['X-Frame-Options'] = 'DENY'
                response.headers['X-XSS-Protection'] = '1; mode=block'
                response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
                response.cache_control.no_cache = True
                response.cache_control.no_store = True
                response.cache_control.must_revalidate = True
                response.headers['Pragma'] = 'no-cache'
                response.headers['Expires'] = '0'
                return response

        def run(self, host: str, port: int) -> None:
            os.makedirs(self._storage.config.WEB_UPLOAD_FOLDER, exist_ok=True)
            os.makedirs(self._storage.config.WEB_DOWNLOAD_FOLDER, exist_ok=True)
            self._app.run(host=host, port=port, debug=False)
else:
    class WebRunner:
        """Stub web runner when Flask is unavailable."""

        def __init__(self, storage: LazyOwnInfiniteStorage):
            self._storage = storage

        def run(self, host: str, port: int) -> None:
            print("Flask is not installed. Web server unavailable.")


def run_tests() -> None:
    """Executes built-in round-trip tests for both protocols."""
    config = LazyOwnConfig()
    storage = LazyOwnInfiniteStorage(config)

    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, 'source.bin')
        data = bytes(random.randint(0, 255) for _ in range(1024))
        with open(source_path, 'wb') as f:
            f.write(data)
        md5_source = hashlib.md5(data).hexdigest()

        secure_base = os.path.join(tmpdir, 'secure.mp4')
        secure_dec = os.path.join(tmpdir, 'secure_decoded.bin')
        storage.encode(source_path, secure_base, 640, 480, 30, 4, config.PROTOCOL_VERSION_SECURE)
        secure_candidates = [f for f in os.listdir(tmpdir) if f.startswith('secure') and f.endswith('.mp4')]
        assert len(secure_candidates) == 1, "Secure encoded file not found"
        secure_enc = os.path.join(tmpdir, secure_candidates[0])
        storage.decode(secure_enc, secure_dec, 4, config.PROTOCOL_VERSION_SECURE)
        with open(secure_dec, 'rb') as f:
            md5_secure = hashlib.md5(f.read()).hexdigest()
        assert md5_source == md5_secure, "Secure protocol round-trip failed"
        print("Secure protocol round-trip passed")

        resized_path = os.path.join(tmpdir, 'resized_640x480.mp4')
        subprocess.run(['ffmpeg', '-y', '-i', secure_enc, '-vf', 'scale=320:240', resized_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        secure_dec2 = os.path.join(tmpdir, 'secure_resized_decoded.bin')
        storage.decode(resized_path, secure_dec2, 4, config.PROTOCOL_VERSION_SECURE)
        with open(secure_dec2, 'rb') as f:
            md5_resized = hashlib.md5(f.read()).hexdigest()
        assert md5_source == md5_resized, "Secure protocol resized decode failed"
        print("Secure protocol resized round-trip passed")

        legacy_base = os.path.join(tmpdir, 'legacy.mp4')
        legacy_dec = os.path.join(tmpdir, 'legacy_decoded.bin')
        storage.encode(source_path, legacy_base, 640, 480, 30, 4, config.PROTOCOL_VERSION_LEGACY)
        legacy_candidates = [f for f in os.listdir(tmpdir) if f.startswith('legacy') and f.endswith('.mp4')]
        assert len(legacy_candidates) == 1, "Legacy encoded file not found"
        legacy_enc = os.path.join(tmpdir, legacy_candidates[0])
        storage.decode(legacy_enc, legacy_dec, 4, config.PROTOCOL_VERSION_LEGACY)
        with open(legacy_dec, 'rb') as f:
            md5_legacy = hashlib.md5(f.read()).hexdigest()
        assert md5_source == md5_legacy, "Legacy protocol round-trip failed"
        print("Legacy protocol round-trip passed")

        print("All tests passed")


def main() -> None:
    """Entry point for LazyOwnInfiniteStorage."""
    print(BANNER)
    storage = LazyOwnInfiniteStorage()
    runner = CLIRunner(storage)
    runner.run()


if __name__ == '__main__':
    main()
