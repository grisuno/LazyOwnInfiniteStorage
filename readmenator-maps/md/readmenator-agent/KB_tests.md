# Subsystem: tests

## tests/test_error_correction.py
- Doc: Unit tests for ErrorCorrector Hamming(8,4) implementation.
- Layer: testing
- Language: py
- Symbols:
  - `TestErrorCorrector` (class, line 7) `class TestErrorCorrector`
  - `setup` (method, line 11) `def setup(self)`
  - `test_encode_data_doubles_length` (method, line 15) `def test_encode_data_doubles_length(self)`
  - `test_decode_data_reverses_encoding` (method, line 20) `def test_decode_data_reverses_encoding(self)`
  - `test_decode_data_with_single_bit_error` (method, line 26) `def test_decode_data_with_single_bit_error(self)`
  - `test_decode_data_rejects_odd_length` (method, line 33) `def test_decode_data_rejects_odd_length(self)`
  - `test_encode_nibble_all_values` (method, line 37) `def test_encode_nibble_all_values(self)`
  - `test_decode_nibble_all_values` (method, line 42) `def test_decode_nibble_all_values(self)`
  - `test_roundtrip_various_inputs` (method, line 49) `def test_roundtrip_various_inputs(self, data)`
  - `test_single_bit_error_per_nibble` (method, line 55) `def test_single_bit_error_per_nibble(self, nibble)`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_frames.py
- Doc: Unit tests for FrameEncoder and FrameDecoder.
- Layer: testing
- Language: py
- Symbols:
  - `TestFrameEncoder` (class, line 8) `class TestFrameEncoder`
  - `TestFrameDecoder` (class, line 54) `class TestFrameDecoder`
  - `setup` (method, line 12) `def setup(self)`
  - `test_bits_to_frames_yields_correct_number_of_frames` (method, line 16) `def test_bits_to_frames_yields_correct_number_of_frames(self)`
  - `test_each_frame_has_correct_dimensions` (method, line 28) `def test_each_frame_has_correct_dimensions(self)`
  - `test_bit_one_produces_white_block` (method, line 33) `def test_bit_one_produces_white_block(self)`
  - `test_bit_zero_produces_black_block` (method, line 38) `def test_bit_zero_produces_black_block(self)`
  - `test_padding_zeros_fill_incomplete_frame` (method, line 43) `def test_padding_zeros_fill_incomplete_frame(self)`
  - `setup` (method, line 58) `def setup(self)`
  - `test_extract_bits_from_empty_raises` (method, line 62) `def test_extract_bits_from_empty_raises(self)`
  - `test_extract_bits_from_raw_frames_basic` (method, line 66) `def test_extract_bits_from_raw_frames_basic(self)`
  - `test_extract_bits_respects_expected_bits` (method, line 74) `def test_extract_bits_respects_expected_bits(self)`
  - `test_extract_bits_from_resized_frame` (method, line 82) `def test_extract_bits_from_resized_frame(self)`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_integration.py
- Doc: Integration tests for full encode/decode roundtrip and web interface.
- Layer: testing
- Language: py
- Symbols:
  - `TestEncodeDecodeRoundtrip` (class, line 18) `class TestEncodeDecodeRoundtrip`
  - `TestWebRunner` (class, line 131) `class TestWebRunner`
  - `setup` (method, line 22) `def setup(self)`
  - `test_secure_protocol_roundtrip` (method, line 26) `def test_secure_protocol_roundtrip(self)`
  - `test_legacy_protocol_roundtrip` (method, line 44) `def test_legacy_protocol_roundtrip(self)`
  - `test_secure_protocol_resilient_to_resolution_change` (method, line 62) `def test_secure_protocol_resilient_to_resolution_change(self)`
  - `test_protocol_auto_detection_prefers_secure` (method, line 83) `def test_protocol_auto_detection_prefers_secure(self)`
  - `test_empty_file_roundtrip` (method, line 96) `def test_empty_file_roundtrip(self)`
  - `test_large_file_roundtrip` (method, line 110) `def test_large_file_roundtrip(self)`
  - `setup` (method, line 135) `def setup(self)`
  - `test_index_get` (method, line 142) `def test_index_get(self)`
  - `test_encode_upload` (method, line 147) `def test_encode_upload(self)`
  - `test_decode_upload` (method, line 167) `def test_decode_upload(self)`
  - `test_security_headers_present` (method, line 193) `def test_security_headers_present(self)`
  - `test_download_not_found` (method, line 199) `def test_download_not_found(self)`
  - `test_missing_file_error` (method, line 203) `def test_missing_file_error(self)`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_protocols.py
- Doc: Unit tests for LegacyProtocolHandler and SecureProtocolHandler.
- Layer: testing
- Language: py
- Symbols:
  - `TestLegacyProtocolHandler` (class, line 7) `class TestLegacyProtocolHandler`
  - `TestSecureProtocolHandler` (class, line 35) `class TestSecureProtocolHandler`
  - `setup` (method, line 11) `def setup(self)`
  - `test_pack_includes_end_marker` (method, line 15) `def test_pack_includes_end_marker(self)`
  - `test_unpack_strips_end_marker` (method, line 21) `def test_unpack_strips_end_marker(self)`
  - `test_unpack_with_trailing_zeros` (method, line 27) `def test_unpack_with_trailing_zeros(self)`
  - `setup` (method, line 39) `def setup(self)`
  - `test_pack_produces_bit_string` (method, line 44) `def test_pack_produces_bit_string(self)`
  - `test_unpack_recovers_original_data` (method, line 49) `def test_unpack_recovers_original_data(self)`
  - `test_unpack_detects_corrupted_header` (method, line 55) `def test_unpack_detects_corrupted_header(self)`
  - `test_unpack_detects_corrupted_payload` (method, line 66) `def test_unpack_detects_corrupted_payload(self)`
  - `test_roundtrip_various_sizes` (method, line 80) `def test_roundtrip_various_sizes(self, size)`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_security.py
- Doc: Unit tests for LazyOwnConfig and SecurityValidator.
- Layer: testing
- Language: py
- Symbols:
  - `TestLazyOwnConfig` (class, line 9) `class TestLazyOwnConfig`
  - `TestSecurityValidator` (class, line 37) `class TestSecurityValidator`
  - `test_magic_bytes_are_valid` (method, line 12) `def test_magic_bytes_are_valid(self)`
  - `test_protocol_versions_are_distinct` (method, line 15) `def test_protocol_versions_are_distinct(self)`
  - `test_default_values_within_bounds` (method, line 18) `def test_default_values_within_bounds(self)`
  - `test_header_offsets_are_consistent` (method, line 24) `def test_header_offsets_are_consistent(self)`
  - `test_max_file_size_is_reasonable` (method, line 31) `def test_max_file_size_is_reasonable(self)`
  - `setup` (method, line 41) `def setup(self)`
  - `test_validate_file_path_resolves_absolute` (method, line 45) `def test_validate_file_path_resolves_absolute(self)`
  - `test_validate_file_path_rejects_traversal` (method, line 50) `def test_validate_file_path_rejects_traversal(self)`
  - `test_validate_file_path_must_exist_when_required` (method, line 54) `def test_validate_file_path_must_exist_when_required(self)`
  - `test_validate_size_rejects_oversized_files` (method, line 58) `def test_validate_size_rejects_oversized_files(self)`
  - `test_validate_size_accepts_maximum` (method, line 62) `def test_validate_size_accepts_maximum(self)`
  - `test_sanitize_filename_strips_unsafe_characters` (method, line 65) `def test_sanitize_filename_strips_unsafe_characters(self)`
  - `test_sanitize_filename_preserves_safe_characters` (method, line 70) `def test_sanitize_filename_preserves_safe_characters(self)`
  - `test_sanitize_filename_fallback` (method, line 74) `def test_sanitize_filename_fallback(self)`
  - `test_validate_extension_accepts_allowed` (method, line 77) `def test_validate_extension_accepts_allowed(self)`
  - `test_validate_extension_rejects_disallowed` (method, line 81) `def test_validate_extension_rejects_disallowed(self)`
- Depends on: `lazyown_infinitestorage.py`
