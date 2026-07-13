"""Unit tests for LazyOwnConfig and SecurityValidator."""

import os
import pytest

from lazyown_infinitestorage import LazyOwnConfig, SecurityValidator


class TestLazyOwnConfig:
    """Specification: Configuration constants are centralized and immutable."""

    def test_magic_bytes_are_valid(self):
        assert LazyOwnConfig.MAGIC_BYTES == b'LAZY'

    def test_protocol_versions_are_distinct(self):
        assert LazyOwnConfig.PROTOCOL_VERSION_LEGACY != LazyOwnConfig.PROTOCOL_VERSION_SECURE

    def test_default_values_within_bounds(self):
        assert LazyOwnConfig.MIN_FRAME_WIDTH <= LazyOwnConfig.DEFAULT_FRAME_WIDTH <= LazyOwnConfig.MAX_FRAME_WIDTH
        assert LazyOwnConfig.MIN_FRAME_HEIGHT <= LazyOwnConfig.DEFAULT_FRAME_HEIGHT <= LazyOwnConfig.MAX_FRAME_HEIGHT
        assert LazyOwnConfig.MIN_FPS <= LazyOwnConfig.DEFAULT_FPS <= LazyOwnConfig.MAX_FPS
        assert LazyOwnConfig.MIN_BLOCK_SIZE <= LazyOwnConfig.DEFAULT_BLOCK_SIZE <= LazyOwnConfig.MAX_BLOCK_SIZE

    def test_header_offsets_are_consistent(self):
        total = 0
        for name in dir(LazyOwnConfig):
            if name.startswith('HEADER_SIZE_'):
                total += getattr(LazyOwnConfig, name)
        assert total == LazyOwnConfig.HEADER_TOTAL_SIZE

    def test_max_file_size_is_reasonable(self):
        assert LazyOwnConfig.MAX_INPUT_FILE_SIZE > 0
        assert LazyOwnConfig.WEB_MAX_CONTENT_LENGTH > 0
        assert LazyOwnConfig.WEB_MAX_CONTENT_LENGTH <= LazyOwnConfig.MAX_INPUT_FILE_SIZE


class TestSecurityValidator:
    """Specification: SecurityValidator prevents path traversal, validates sizes and extensions."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = LazyOwnConfig()
        self.validator = SecurityValidator(self.config)

    def test_validate_file_path_resolves_absolute(self):
        result = self.validator.validate_file_path('file.txt')
        assert os.path.isabs(result)
        assert os.path.normpath(result) == result

    def test_validate_file_path_rejects_traversal(self):
        with pytest.raises(ValueError, match='Path traversal'):
            self.validator.validate_file_path('../../etc/passwd')

    def test_validate_file_path_must_exist_when_required(self):
        with pytest.raises(FileNotFoundError):
            self.validator.validate_file_path('/nonexistent/path/file.bin', must_exist=True)

    def test_validate_size_rejects_oversized_files(self):
        with pytest.raises(ValueError, match='exceeds maximum'):
            self.validator.validate_size(self.config.MAX_INPUT_FILE_SIZE + 1)

    def test_validate_size_accepts_maximum(self):
        self.validator.validate_size(self.config.MAX_INPUT_FILE_SIZE)

    def test_sanitize_filename_strips_unsafe_characters(self):
        assert self.validator.sanitize_filename('../../../evil.sh') == 'evil.sh'
        assert self.validator.sanitize_filename('file<name>.txt') == 'filename.txt'
        assert self.validator.sanitize_filename('hello world.zip') == 'helloworld.zip'

    def test_sanitize_filename_preserves_safe_characters(self):
        assert self.validator.sanitize_filename('file_123.zip') == 'file_123.zip'
        assert self.validator.sanitize_filename('test-file.tar.gz') == 'test-file.tar.gz'

    def test_sanitize_filename_fallback(self):
        assert self.validator.sanitize_filename('<>!@#$%') == 'file'

    def test_validate_extension_accepts_allowed(self):
        self.validator.validate_extension('test.zip', self.config.ALLOWED_ENCODE_EXTENSIONS)
        self.validator.validate_extension('data.bin', self.config.ALLOWED_ENCODE_EXTENSIONS)

    def test_validate_extension_rejects_disallowed(self):
        with pytest.raises(ValueError, match='Disallowed'):
            self.validator.validate_extension('test.exe', self.config.ALLOWED_ENCODE_EXTENSIONS)
