# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 9 | **Total Symbols Extracted:** 153 | **Total Imports:** 51
 | **Resolved Imports:** 7


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [God Nodes](#god-nodes)
4. [Community Analysis](#community-analysis)
5. [Suggested Questions](#suggested-questions)
6. [Structural Knowledge Map](#structural-knowledge-map)
7. [Architecture Reference](#architecture-reference)
    - [PY (8 files)](#py-8-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 9 |
| Total Symbols | 153 |
| Total Imports | 51 |
| Call Edges | 854 |
| Inheritance Edges | 4 |
| Languages | 2 |
| Avg Symbols/File | 17.0 |
| Avg Imports/File | 5.7 |
| Resolved Imports | 7 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `lazyown_infinitestorage.py` | 19 | 78 | py |
| `tools.py` | 11 | 5 | py |
| `test_integration.py` | 9 | 16 | py |
| `test_frames.py` | 3 | 13 | py |
| `test_security.py` | 3 | 18 | py |
| `test_error_correction.py` | 2 | 10 | py |
| `test_protocols.py` | 2 | 12 | py |
| `wsgi_app.py` | 2 | 1 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| testing | 5 |
| utility | 2 |
| presentation | 1 |
| data_access | 1 |

### utility

- `install.sh` (sh, 0 symbols)
- `wsgi_app.py` (py, 1 symbols)

### presentation

- `lazyown_infinitestorage.py` (py, 78 symbols)

### data_access

- `tools.py` (py, 5 symbols)

### testing

- `test_error_correction.py` (py, 10 symbols)
- `test_frames.py` (py, 13 symbols)
- `test_integration.py` (py, 16 symbols)
- `test_protocols.py` (py, 12 symbols)
- `test_security.py` (py, 18 symbols)

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections |
|------|-------|-------------|
| `lazyown_infinitestorage.py` | 21.8 | |
| `test_security.py` | 3.8 | |
| `test_integration.py` | 3.6 | |
| `test_frames.py` | 3.3 | |
| `test_protocols.py` | 3.2 | |
| `test_error_correction.py` | 3.0 | |
| `tools.py` | 2.5 | |
| `wsgi_app.py` | 2.1 | |
| `install.sh` | 0.0 | |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### tests (Cohesion: 1.00)

**8 files** in this community:

- `lazyown_infinitestorage.py` (py, 78 symbols)
- `tools.py` (py, 5 symbols)
- `test_error_correction.py` (py, 10 symbols)
- `test_frames.py` (py, 13 symbols)
- `test_integration.py` (py, 16 symbols)
- `test_protocols.py` (py, 12 symbols)
- `test_security.py` (py, 18 symbols)
- `wsgi_app.py` (py, 1 symbols)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does lazyown_infinitestorage.py depend on, and what depends on it? (7 connections)
- What does test_security.py depend on, and what depends on it? (1 connections)
- What does test_integration.py depend on, and what depends on it? (1 connections)
- How are the 8 files in 'tests' related to each other?
- What is LazyOwnConfig in lazyown_infinitestorage.py and how is it used?

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_0 ["tests"]
    lazyown_infinitestorage_py["lazyown_infinitestorage.py (py)"]
    class lazyown_infinitestorage_py mod;
    lazyown_infinitestorage_py_LazyOwnConfig["LazyOwnConfig"]
    class lazyown_infinitestorage_py_LazyOwnConfig cls;
    lazyown_infinitestorage_py --> lazyown_infinitestorage_py_LazyOwnConfig
    lazyown_infinitestorage_py_SecurityValidator["SecurityValidator"]
    class lazyown_infinitestorage_py_SecurityValidator cls;
    lazyown_infinitestorage_py --> lazyown_infinitestorage_py_SecurityValidator
    lazyown_infinitestorage_py_ErrorCorrector["ErrorCorrector"]
    class lazyown_infinitestorage_py_ErrorCorrector cls;
    lazyown_infinitestorage_py --> lazyown_infinitestorage_py_ErrorCorrector
    lazyown_infinitestorage_py_FrameEncoder["FrameEncoder"]
    class lazyown_infinitestorage_py_FrameEncoder cls;
    lazyown_infinitestorage_py --> lazyown_infinitestorage_py_FrameEncoder
    lazyown_infinitestorage_py_FrameDecoder["FrameDecoder"]
    class lazyown_infinitestorage_py_FrameDecoder cls;
    lazyown_infinitestorage_py --> lazyown_infinitestorage_py_FrameDecoder
    skill_lazyown_infinitestorage_tools_py["tools.py (py)"]
    class skill_lazyown_infinitestorage_tools_py mod;
    skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_encode["lazyown_infinitestorage_encode"]
    class skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_encode fn;
    skill_lazyown_infinitestorage_tools_py --> skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_encode
    skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_decode["lazyown_infinitestorage_decode"]
    class skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_decode fn;
    skill_lazyown_infinitestorage_tools_py --> skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_decode
    skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_upload_to_youtube["lazyown_infinitestorage_upload_to_youtube"]
    class skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_upload_to_youtube fn;
    skill_lazyown_infinitestorage_tools_py --> skill_lazyown_infinitestorage_tools_py_lazyown_infinitestorage_upload_to_youtube
    skill_lazyown_infinitestorage_tools_py_get_tool["get_tool"]
    class skill_lazyown_infinitestorage_tools_py_get_tool fn;
    skill_lazyown_infinitestorage_tools_py --> skill_lazyown_infinitestorage_tools_py_get_tool
    skill_lazyown_infinitestorage_tools_py_list_tools["list_tools"]
    class skill_lazyown_infinitestorage_tools_py_list_tools fn;
    skill_lazyown_infinitestorage_tools_py --> skill_lazyown_infinitestorage_tools_py_list_tools
    tests_test_integration_py["test_integration.py (py)"]
    class tests_test_integration_py mod;
    tests_test_integration_py_TestEncodeDecodeRoundtrip["TestEncodeDecodeRoundtrip"]
    class tests_test_integration_py_TestEncodeDecodeRoundtrip cls;
    tests_test_integration_py --> tests_test_integration_py_TestEncodeDecodeRoundtrip
    tests_test_integration_py_TestWebRunner["TestWebRunner"]
    class tests_test_integration_py_TestWebRunner cls;
    tests_test_integration_py --> tests_test_integration_py_TestWebRunner
    tests_test_integration_py_setup["setup"]
    class tests_test_integration_py_setup fn;
    tests_test_integration_py --> tests_test_integration_py_setup
    tests_test_integration_py_test_secure_protocol_roundtrip["test_secure_protocol_roundtrip"]
    class tests_test_integration_py_test_secure_protocol_roundtrip fn;
    tests_test_integration_py --> tests_test_integration_py_test_secure_protocol_roundtrip
    tests_test_integration_py_test_legacy_protocol_roundtrip["test_legacy_protocol_roundtrip"]
    class tests_test_integration_py_test_legacy_protocol_roundtrip fn;
    tests_test_integration_py --> tests_test_integration_py_test_legacy_protocol_roundtrip
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    tests_test_security_py_TestLazyOwnConfig["TestLazyOwnConfig"]
    class tests_test_security_py_TestLazyOwnConfig cls;
    tests_test_security_py --> tests_test_security_py_TestLazyOwnConfig
    tests_test_security_py_TestSecurityValidator["TestSecurityValidator"]
    class tests_test_security_py_TestSecurityValidator cls;
    tests_test_security_py --> tests_test_security_py_TestSecurityValidator
    tests_test_security_py_test_magic_bytes_are_valid["test_magic_bytes_are_valid"]
    class tests_test_security_py_test_magic_bytes_are_valid fn;
    tests_test_security_py --> tests_test_security_py_test_magic_bytes_are_valid
    tests_test_security_py_test_protocol_versions_are_distinct["test_protocol_versions_are_distinct"]
    class tests_test_security_py_test_protocol_versions_are_distinct fn;
    tests_test_security_py --> tests_test_security_py_test_protocol_versions_are_distinct
    tests_test_security_py_test_default_values_within_bounds["test_default_values_within_bounds"]
    class tests_test_security_py_test_default_values_within_bounds fn;
    tests_test_security_py --> tests_test_security_py_test_default_values_within_bounds
    tests_test_frames_py["test_frames.py (py)"]
    class tests_test_frames_py mod;
    tests_test_frames_py_TestFrameEncoder["TestFrameEncoder"]
    class tests_test_frames_py_TestFrameEncoder cls;
    tests_test_frames_py --> tests_test_frames_py_TestFrameEncoder
    tests_test_frames_py_TestFrameDecoder["TestFrameDecoder"]
    class tests_test_frames_py_TestFrameDecoder cls;
    tests_test_frames_py --> tests_test_frames_py_TestFrameDecoder
    tests_test_frames_py_setup["setup"]
    class tests_test_frames_py_setup fn;
    tests_test_frames_py --> tests_test_frames_py_setup
    tests_test_frames_py_test_bits_to_frames_yields_correct_number_of_frames["test_bits_to_frames_yields_correct_number_of_frames"]
    class tests_test_frames_py_test_bits_to_frames_yields_correct_number_of_frames fn;
    tests_test_frames_py --> tests_test_frames_py_test_bits_to_frames_yields_correct_number_of_frames
    tests_test_frames_py_test_each_frame_has_correct_dimensions["test_each_frame_has_correct_dimensions"]
    class tests_test_frames_py_test_each_frame_has_correct_dimensions fn;
    tests_test_frames_py --> tests_test_frames_py_test_each_frame_has_correct_dimensions
    tests_test_protocols_py["test_protocols.py (py)"]
    class tests_test_protocols_py mod;
    tests_test_protocols_py_TestLegacyProtocolHandler["TestLegacyProtocolHandler"]
    class tests_test_protocols_py_TestLegacyProtocolHandler cls;
    tests_test_protocols_py --> tests_test_protocols_py_TestLegacyProtocolHandler
    tests_test_protocols_py_TestSecureProtocolHandler["TestSecureProtocolHandler"]
    class tests_test_protocols_py_TestSecureProtocolHandler cls;
    tests_test_protocols_py --> tests_test_protocols_py_TestSecureProtocolHandler
    tests_test_protocols_py_setup["setup"]
    class tests_test_protocols_py_setup fn;
    tests_test_protocols_py --> tests_test_protocols_py_setup
    tests_test_protocols_py_test_pack_includes_end_marker["test_pack_includes_end_marker"]
    class tests_test_protocols_py_test_pack_includes_end_marker fn;
    tests_test_protocols_py --> tests_test_protocols_py_test_pack_includes_end_marker
    tests_test_protocols_py_test_unpack_strips_end_marker["test_unpack_strips_end_marker"]
    class tests_test_protocols_py_test_unpack_strips_end_marker fn;
    tests_test_protocols_py --> tests_test_protocols_py_test_unpack_strips_end_marker
    tests_test_error_correction_py["test_error_correction.py (py)"]
    class tests_test_error_correction_py mod;
    tests_test_error_correction_py_TestErrorCorrector["TestErrorCorrector"]
    class tests_test_error_correction_py_TestErrorCorrector cls;
    tests_test_error_correction_py --> tests_test_error_correction_py_TestErrorCorrector
    tests_test_error_correction_py_setup["setup"]
    class tests_test_error_correction_py_setup fn;
    tests_test_error_correction_py --> tests_test_error_correction_py_setup
    tests_test_error_correction_py_test_encode_data_doubles_length["test_encode_data_doubles_length"]
    class tests_test_error_correction_py_test_encode_data_doubles_length fn;
    tests_test_error_correction_py --> tests_test_error_correction_py_test_encode_data_doubles_length
    tests_test_error_correction_py_test_decode_data_reverses_encoding["test_decode_data_reverses_encoding"]
    class tests_test_error_correction_py_test_decode_data_reverses_encoding fn;
    tests_test_error_correction_py --> tests_test_error_correction_py_test_decode_data_reverses_encoding
    tests_test_error_correction_py_test_decode_data_with_single_bit_error["test_decode_data_with_single_bit_error"]
    class tests_test_error_correction_py_test_decode_data_with_single_bit_error fn;
    tests_test_error_correction_py --> tests_test_error_correction_py_test_decode_data_with_single_bit_error
    wsgi_app_py["wsgi_app.py (py)"]
    class wsgi_app_py mod;
    wsgi_app_py_get_wsgi_app["get_wsgi_app"]
    class wsgi_app_py_get_wsgi_app fn;
    wsgi_app_py --> wsgi_app_py_get_wsgi_app
    install_sh["install.sh (sh)"]
    class install_sh mod;
    end
    skill_lazyown_infinitestorage_tools_py -- resolved_imports --> lazyown_infinitestorage_py
    tests_test_error_correction_py -- resolved_imports --> lazyown_infinitestorage_py
    tests_test_frames_py -- resolved_imports --> lazyown_infinitestorage_py
    tests_test_integration_py -- resolved_imports --> lazyown_infinitestorage_py
    tests_test_protocols_py -- resolved_imports --> lazyown_infinitestorage_py
    tests_test_security_py -- resolved_imports --> lazyown_infinitestorage_py
    wsgi_app_py -- resolved_imports --> lazyown_infinitestorage_py
    ext_argparse["argparse"]
    class ext_argparse ext;
    lazyown_infinitestorage_py -.->|imports| ext_argparse
    ext_binascii["binascii"]
    class ext_binascii ext;
    lazyown_infinitestorage_py -.->|imports| ext_binascii
    ext_math["math"]
    class ext_math ext;
    lazyown_infinitestorage_py -.->|imports| ext_math
    ext_os["os"]
    class ext_os ext;
    lazyown_infinitestorage_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    lazyown_infinitestorage_py -.->|imports| ext_re
    ext_struct["struct"]
    class ext_struct ext;
    lazyown_infinitestorage_py -.->|imports| ext_struct
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    lazyown_infinitestorage_py -.->|imports| ext_subprocess
    ext_sys["sys"]
    class ext_sys ext;
    lazyown_infinitestorage_py -.->|imports| ext_sys
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    lazyown_infinitestorage_py -.->|imports| ext_tempfile
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    lazyown_infinitestorage_py -.->|imports| ext_hashlib
    ext_random["random"]
    class ext_random ext;
    lazyown_infinitestorage_py -.->|imports| ext_random
    ext_shutil["shutil"]
    class ext_shutil ext;
    lazyown_infinitestorage_py -.->|imports| ext_shutil
    ext_typing["typing"]
    class ext_typing ext;
    lazyown_infinitestorage_py -.->|imports| ext_typing
    ext_cv2["cv2"]
    class ext_cv2 ext;
    lazyown_infinitestorage_py -.->|imports| ext_cv2
    ext_numpy["numpy"]
    class ext_numpy ext;
    lazyown_infinitestorage_py -.->|imports| ext_numpy
    ext_flask["flask"]
    class ext_flask ext;
    lazyown_infinitestorage_py -.->|imports| ext_flask
    ext_PyQt5_QtWidgets["PyQt5.QtWidgets"]
    class ext_PyQt5_QtWidgets ext;
    lazyown_infinitestorage_py -.->|imports| ext_PyQt5_QtWidgets
    ext_PyQt5_QtCore["PyQt5.QtCore"]
    class ext_PyQt5_QtCore ext;
    lazyown_infinitestorage_py -.->|imports| ext_PyQt5_QtCore
    ext_json["json"]
    class ext_json ext;
    lazyown_infinitestorage_py -.->|imports| ext_json
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_os
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_sys
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_subprocess
    ext_time["time"]
    class ext_time ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_time
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_typing
    ext_lazyown_infinitestorage["lazyown_infinitestorage"]
    class ext_lazyown_infinitestorage ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_lazyown_infinitestorage
    ext_selenium["selenium"]
    class ext_selenium ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_selenium
    ext_selenium_webdriver_common_by["selenium.webdriver.common.by"]
    class ext_selenium_webdriver_common_by ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_selenium_webdriver_common_by
    ext_selenium_webdriver_support_ui["selenium.webdriver.support.ui"]
    class ext_selenium_webdriver_support_ui ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_selenium_webdriver_support_ui
    ext_selenium_webdriver_support["selenium.webdriver.support"]
    class ext_selenium_webdriver_support ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_selenium_webdriver_support
    ext_selenium_webdriver_chrome_service["selenium.webdriver.chrome.service"]
    class ext_selenium_webdriver_chrome_service ext;
    skill_lazyown_infinitestorage_tools_py -.->|imports| ext_selenium_webdriver_chrome_service
    ext_pytest["pytest"]
    class ext_pytest ext;
    tests_test_error_correction_py -.->|imports| ext_pytest
    tests_test_error_correction_py -.->|imports| ext_lazyown_infinitestorage
    tests_test_frames_py -.->|imports| ext_numpy
    tests_test_frames_py -.->|imports| ext_pytest
    tests_test_frames_py -.->|imports| ext_lazyown_infinitestorage
    tests_test_integration_py -.->|imports| ext_hashlib
    tests_test_integration_py -.->|imports| ext_os
    tests_test_integration_py -.->|imports| ext_random
    tests_test_integration_py -.->|imports| ext_subprocess
    tests_test_integration_py -.->|imports| ext_tempfile
    tests_test_integration_py -.->|imports| ext_pytest
    tests_test_integration_py -.->|imports| ext_lazyown_infinitestorage
    ext_io["io"]
    class ext_io ext;
    tests_test_integration_py -.->|imports| ext_io
    tests_test_integration_py -.->|imports| ext_io
    tests_test_protocols_py -.->|imports| ext_pytest
    tests_test_protocols_py -.->|imports| ext_lazyown_infinitestorage
    tests_test_security_py -.->|imports| ext_os
    tests_test_security_py -.->|imports| ext_pytest
    tests_test_security_py -.->|imports| ext_lazyown_infinitestorage
    wsgi_app_py -.->|imports| ext_os
    wsgi_app_py -.->|imports| ext_lazyown_infinitestorage
```

---

## Architecture Reference

### PY (8 files)

#### `lazyown_infinitestorage.py`
**Path:** `lazyown_infinitestorage.py`

**Classes:**
- `LazyOwnConfig` (line 66) `class LazyOwnConfig` - *Centralized immutable configuration constants for LazyOwnInfiniteStorage.*
- `SecurityValidator` (line 143) `class SecurityValidator` - *Validates file paths and inputs to prevent path traversal and abuse.*
- `ErrorCorrector` (line 179) `class ErrorCorrector` - *Implements Hamming(8,4) extended error correction for byte streams.*
- `FrameEncoder` (line 237) `class FrameEncoder` - *Encodes bit strings into numpy grayscale frames.*
- `FrameDecoder` (line 268) `class FrameDecoder` - *Decodes grayscale frames into bit strings.*
- `FFmpegPipeline` (line 300) `class FFmpegPipeline` - *Manages FFmpeg subprocess communication without intermediate frame files.*
- `ProtocolHandler` (line 390) `class ProtocolHandler` - *Abstract base for encoding and decoding protocol implementations.*
- `LegacyProtocolHandler` (line 402) `class LegacyProtocolHandler(ProtocolHandler)` - *Implements the original v1 protocol with filename-based resolution and end marker.*
- `SecureProtocolHandler` (line 427) `class SecureProtocolHandler(ProtocolHandler)` - *Implements the v2 protocol with structured headers, CRC32, and Hamming error correction.*
- `LazyOwnInfiniteStorage` (line 481) `class LazyOwnInfiniteStorage` - *Main orchestrator for encoding and decoding files to and from video.*
- `CLIRunner` (line 604) `class CLIRunner` - *Command-line interface runner for LazyOwnInfiniteStorage.*
- `Worker` (line 654) `class Worker(QThread)` - *Background worker thread for non-blocking GUI operations.*
- `GUIRunner` (line 673) `class GUIRunner(QWidget)` - *PyQt5 graphical user interface for LazyOwnInfiniteStorage.*
- `GUIRunner` (line 809) `class GUIRunner` - *Stub GUI runner when PyQt5 is unavailable.*
- `WebRunner` (line 820) `class WebRunner` - *Flask web server interface for LazyOwnInfiniteStorage.*
- `WebRunner` (line 933) `class WebRunner` - *Stub web runner when Flask is unavailable.*

**Methods:**
- `run_tests` (line 943) `def run_tests()` - *Executes built-in round-trip tests for both protocols.*
- `main` (line 991) `def main()` - *Entry point for LazyOwnInfiniteStorage.*
- `__init__` (line 146) `def __init__(self, config)`
- `validate_file_path` (line 149) `def validate_file_path(self, file_path, must_exist)` - *Resolves and validates an absolute file path.*
- `validate_size` (line 159) `def validate_size(self, size)` - *Ensures the file size is within acceptable limits.*
- `sanitize_filename` (line 164) `def sanitize_filename(self, filename)` - *Sanitizes a filename to remove unsafe characters.*
- `validate_extension` (line 172) `def validate_extension(self, file_path, allowed_extensions)` - *Ensures the file extension is in the allowed set.*
- `__init__` (line 182) `def __init__(self, config)`
- `encode_data` (line 185) `def encode_data(self, data)` - *Encodes a byte sequence using Hamming(8,4) correction.*
- `decode_data` (line 195) `def decode_data(self, data)` - *Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.*
- `_encode_nibble` (line 206) `def _encode_nibble(self, nibble)`
- `_decode_nibble` (line 217) `def _decode_nibble(self, byte_val)`
- `__init__` (line 240) `def __init__(self, config)`
- `bits_to_frames` (line 243) `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` - *Yields grayscale frames from a bit string.*
- `_create_frame` (line 258) `def _create_frame(self, bits, width, height, block_size, blocks_per_row)`
- `__init__` (line 271) `def __init__(self, config)`
- `extract_bits_from_raw_frames` (line 274) `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)` - *Extracts a bit string from rawvideo grayscale bytes.*
- `__init__` (line 303) `def __init__(self, config)`
- `get_video_info` (line 306) `def get_video_info(self, input_path)` - *Retrieves native resolution and metadata from a video file.*
- `get_metadata` (line 320) `def get_metadata(self, input_path)` - *Extracts custom lazyown metadata from a video file using ffprobe.*
- `encode_video` (line 339) `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)` - *Encodes a generator of frames into a video file via FFmpeg stdin.*
- `extract_raw_frames` (line 366) `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)` - *Extracts raw grayscale frames from a video file via FFmpeg stdout.*
- `pack` (line 393) `def pack(self, data, frame_width, frame_height, block_size, fps)` - *Packs raw data into a bit string.*
- `unpack` (line 397) `def unpack(self, bit_string, block_size)` - *Unpacks a bit string into raw data.*
- `__init__` (line 405) `def __init__(self, config)`
- `pack` (line 408) `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `unpack` (line 413) `def unpack(self, bit_string, block_size)`
- `__init__` (line 430) `def __init__(self, config, corrector)`
- `pack` (line 434) `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `unpack` (line 453) `def unpack(self, bit_string, block_size)`
- `__init__` (line 484) `def __init__(self, config)`
- `create_web_runner` (line 494) `def create_web_runner(self)` - *Return a WebRunner for WSGI or local web server use.*
- `encode` (line 498) `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)` - *Encodes a file into a video using the specified protocol.*
- `decode` (line 523) `def decode(self, input_path, output_path, block_size, protocol_version)` - *Decodes a video back into the original file using the specified protocol.*
- `_validate_encoding_parameters` (line 534) `def _validate_encoding_parameters(self, frame_width, frame_height, fps, block_size)`
- `_detect_protocol` (line 544) `def _detect_protocol(self, input_path, block_size)`
- `_decode_legacy` (line 577) `def _decode_legacy(self, input_path, output_path, block_size)`
- `_decode_secure` (line 590) `def _decode_secure(self, input_path, output_path, block_size)`
- `__init__` (line 607) `def __init__(self, storage)`
- `run` (line 610) `def run(self)`
- `__init__` (line 660) `def __init__(self, func)`
- `run` (line 666) `def run(self)`
- `__init__` (line 676) `def __init__(self, storage)`
- `_init_ui` (line 682) `def _init_ui(self)`
- `_change_mode` (line 750) `def _change_mode(self)`
- `_browse_input` (line 761) `def _browse_input(self)`
- `_start` (line 771) `def _start(self)`
- `_on_finished` (line 794) `def _on_finished(self, message)`
- `_on_error` (line 799) `def _on_error(self, message)`
- `run` (line 804) `def run(self)`
- `__init__` (line 812) `def __init__(self, storage)`
- `run` (line 815) `def run(self)`
- `__init__` (line 823) `def __init__(self, storage)`
- `run_setup` (line 834) `def run_setup(self)` - *Create directories and validate environment.*
- `_setup_routes` (line 840) `def _setup_routes(self)`
- `run` (line 928) `def run(self, host, port)`
- `__init__` (line 936) `def __init__(self, storage)`
- `run` (line 939) `def run(self, host, port)`
- `_validate_upload` (line 845) `def _validate_upload(input_file, action)`
- `index` (line 863) `def index()`
- `download` (line 908) `def download(filename)`
- `add_security_headers` (line 916) `def add_security_headers(response)`

#### `tools.py`
**Path:** `skill_lazyown_infinitestorage/tools.py`

**Functions:**
- `lazyown_infinitestorage_encode` (line 34) `def lazyown_infinitestorage_encode(params)` - *Encode a file into a video using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_decode` (line 101) `def lazyown_infinitestorage_decode(params)` - *Decode a video back into the original file using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_upload_to_youtube` (line 152) `def lazyown_infinitestorage_upload_to_youtube(params)` - *Upload a video to YouTube using browser automation.*
- `get_tool` (line 302) `def get_tool(name)` - *Get a tool by name.*
- `list_tools` (line 306) `def list_tools()` - *List all available tools.*

#### `test_error_correction.py`
**Path:** `tests/test_error_correction.py`

**Classes:**
- `TestErrorCorrector` (line 7) `class TestErrorCorrector` - *Specification: ErrorCorrector encodes bytes into Hamming(8,4) and corrects single-bit errors.*

**Methods:**
- `setup` (line 11) `def setup(self)`
- `test_encode_data_doubles_length` (line 15) `def test_encode_data_doubles_length(self)`
- `test_decode_data_reverses_encoding` (line 20) `def test_decode_data_reverses_encoding(self)`
- `test_decode_data_with_single_bit_error` (line 26) `def test_decode_data_with_single_bit_error(self)`
- `test_decode_data_rejects_odd_length` (line 33) `def test_decode_data_rejects_odd_length(self)`
- `test_encode_nibble_all_values` (line 37) `def test_encode_nibble_all_values(self)`
- `test_decode_nibble_all_values` (line 42) `def test_decode_nibble_all_values(self)`
- `test_roundtrip_various_inputs` (line 49) `def test_roundtrip_various_inputs(self, data)`
- `test_single_bit_error_per_nibble` (line 55) `def test_single_bit_error_per_nibble(self, nibble)`

#### `test_frames.py`
**Path:** `tests/test_frames.py`

**Classes:**
- `TestFrameEncoder` (line 8) `class TestFrameEncoder` - *Specification: FrameEncoder converts bit strings into grayscale frames.*
- `TestFrameDecoder` (line 54) `class TestFrameDecoder` - *Specification: FrameDecoder extracts bit strings from rawvideo grayscale bytes.*

**Methods:**
- `setup` (line 12) `def setup(self)`
- `test_bits_to_frames_yields_correct_number_of_frames` (line 16) `def test_bits_to_frames_yields_correct_number_of_frames(self)`
- `test_each_frame_has_correct_dimensions` (line 28) `def test_each_frame_has_correct_dimensions(self)`
- `test_bit_one_produces_white_block` (line 33) `def test_bit_one_produces_white_block(self)`
- `test_bit_zero_produces_black_block` (line 38) `def test_bit_zero_produces_black_block(self)`
- `test_padding_zeros_fill_incomplete_frame` (line 43) `def test_padding_zeros_fill_incomplete_frame(self)`
- `setup` (line 58) `def setup(self)`
- `test_extract_bits_from_empty_raises` (line 62) `def test_extract_bits_from_empty_raises(self)`
- `test_extract_bits_from_raw_frames_basic` (line 66) `def test_extract_bits_from_raw_frames_basic(self)`
- `test_extract_bits_respects_expected_bits` (line 74) `def test_extract_bits_respects_expected_bits(self)`
- `test_extract_bits_from_resized_frame` (line 82) `def test_extract_bits_from_resized_frame(self)`

#### `test_integration.py`
**Path:** `tests/test_integration.py`

**Classes:**
- `TestEncodeDecodeRoundtrip` (line 18) `class TestEncodeDecodeRoundtrip` - *Specification: Files encoded to video and decoded back must be bit-identical.*
- `TestWebRunner` (line 131) `class TestWebRunner` - *Specification: Web interface accepts uploads, encodes/decodes, and serves downloads.*

**Methods:**
- `setup` (line 22) `def setup(self)`
- `test_secure_protocol_roundtrip` (line 26) `def test_secure_protocol_roundtrip(self)`
- `test_legacy_protocol_roundtrip` (line 44) `def test_legacy_protocol_roundtrip(self)`
- `test_secure_protocol_resilient_to_resolution_change` (line 62) `def test_secure_protocol_resilient_to_resolution_change(self)`
- `test_protocol_auto_detection_prefers_secure` (line 83) `def test_protocol_auto_detection_prefers_secure(self)`
- `test_empty_file_roundtrip` (line 96) `def test_empty_file_roundtrip(self)`
- `test_large_file_roundtrip` (line 110) `def test_large_file_roundtrip(self)`
- `setup` (line 135) `def setup(self)`
- `test_index_get` (line 142) `def test_index_get(self)`
- `test_encode_upload` (line 147) `def test_encode_upload(self)`
- `test_decode_upload` (line 167) `def test_decode_upload(self)`
- `test_security_headers_present` (line 193) `def test_security_headers_present(self)`
- `test_download_not_found` (line 199) `def test_download_not_found(self)`
- `test_missing_file_error` (line 203) `def test_missing_file_error(self)`

#### `test_protocols.py`
**Path:** `tests/test_protocols.py`

**Classes:**
- `TestLegacyProtocolHandler` (line 7) `class TestLegacyProtocolHandler` - *Specification: Legacy v1 protocol packs data with end-marker, unpacks by filename resolution.*
- `TestSecureProtocolHandler` (line 35) `class TestSecureProtocolHandler` - *Specification: Secure v2 protocol packs data with header, CRC32, and Hamming correction.*

**Methods:**
- `setup` (line 11) `def setup(self)`
- `test_pack_includes_end_marker` (line 15) `def test_pack_includes_end_marker(self)`
- `test_unpack_strips_end_marker` (line 21) `def test_unpack_strips_end_marker(self)`
- `test_unpack_with_trailing_zeros` (line 27) `def test_unpack_with_trailing_zeros(self)`
- `setup` (line 39) `def setup(self)`
- `test_pack_produces_bit_string` (line 44) `def test_pack_produces_bit_string(self)`
- `test_unpack_recovers_original_data` (line 49) `def test_unpack_recovers_original_data(self)`
- `test_unpack_detects_corrupted_header` (line 55) `def test_unpack_detects_corrupted_header(self)`
- `test_unpack_detects_corrupted_payload` (line 66) `def test_unpack_detects_corrupted_payload(self)`
- `test_roundtrip_various_sizes` (line 80) `def test_roundtrip_various_sizes(self, size)`

#### `test_security.py`
**Path:** `tests/test_security.py`

**Classes:**
- `TestLazyOwnConfig` (line 9) `class TestLazyOwnConfig` - *Specification: Configuration constants are centralized and immutable.*
- `TestSecurityValidator` (line 37) `class TestSecurityValidator` - *Specification: SecurityValidator prevents path traversal, validates sizes and extensions.*

**Methods:**
- `test_magic_bytes_are_valid` (line 12) `def test_magic_bytes_are_valid(self)`
- `test_protocol_versions_are_distinct` (line 15) `def test_protocol_versions_are_distinct(self)`
- `test_default_values_within_bounds` (line 18) `def test_default_values_within_bounds(self)`
- `test_header_offsets_are_consistent` (line 24) `def test_header_offsets_are_consistent(self)`
- `test_max_file_size_is_reasonable` (line 31) `def test_max_file_size_is_reasonable(self)`
- `setup` (line 41) `def setup(self)`
- `test_validate_file_path_resolves_absolute` (line 45) `def test_validate_file_path_resolves_absolute(self)`
- `test_validate_file_path_rejects_traversal` (line 50) `def test_validate_file_path_rejects_traversal(self)`
- `test_validate_file_path_must_exist_when_required` (line 54) `def test_validate_file_path_must_exist_when_required(self)`
- `test_validate_size_rejects_oversized_files` (line 58) `def test_validate_size_rejects_oversized_files(self)`
- `test_validate_size_accepts_maximum` (line 62) `def test_validate_size_accepts_maximum(self)`
- `test_sanitize_filename_strips_unsafe_characters` (line 65) `def test_sanitize_filename_strips_unsafe_characters(self)`
- `test_sanitize_filename_preserves_safe_characters` (line 70) `def test_sanitize_filename_preserves_safe_characters(self)`
- `test_sanitize_filename_fallback` (line 74) `def test_sanitize_filename_fallback(self)`
- `test_validate_extension_accepts_allowed` (line 77) `def test_validate_extension_accepts_allowed(self)`
- `test_validate_extension_rejects_disallowed` (line 81) `def test_validate_extension_rejects_disallowed(self)`

#### `wsgi_app.py`
**Path:** `wsgi_app.py`

**Functions:**
- `get_wsgi_app` (line 7) `def get_wsgi_app()` - *Factory function returning a gunicorn-compatible Flask application.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`
**File Doc:** *Verificar si Python está instalado*

*No symbols extracted*
