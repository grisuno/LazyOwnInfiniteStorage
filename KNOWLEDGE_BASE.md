# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 5 | **Total Symbols Extracted:** 97 | **Total Imports:** 45

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
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
    app_py["app.py (py)"]
    class app_py mod;
    app_py_EncodeDecodeForm["EncodeDecodeForm"]
    class app_py_EncodeDecodeForm cls;
    app_py --> app_py_EncodeDecodeForm
    app_py_sanitize_filename["sanitize_filename"]
    class app_py_sanitize_filename fn;
    app_py --> app_py_sanitize_filename
    app_py_index["index"]
    class app_py_index fn;
    app_py --> app_py_index
    app_py_download_file["download_file"]
    class app_py_download_file fn;
    app_py --> app_py_download_file
    app_py_add_security_headers["add_security_headers"]
    class app_py_add_security_headers fn;
    app_py --> app_py_add_security_headers
    gui_py["gui.py (py)"]
    class gui_py mod;
    gui_py_MainWindow["MainWindow"]
    class gui_py_MainWindow cls;
    gui_py --> gui_py_MainWindow
    gui_py___init__["__init__"]
    class gui_py___init__ fn;
    gui_py --> gui_py___init__
    gui_py_initUI["initUI"]
    class gui_py_initUI fn;
    gui_py --> gui_py_initUI
    gui_py_create_encode_ui["create_encode_ui"]
    class gui_py_create_encode_ui fn;
    gui_py --> gui_py_create_encode_ui
    gui_py_create_decode_ui["create_decode_ui"]
    class gui_py_create_decode_ui fn;
    gui_py --> gui_py_create_decode_ui
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    app_py -.->|imports| ext_re
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    app_py -.->|imports| ext_tempfile
    ext_flask["flask"]
    class ext_flask ext;
    app_py -.->|imports| ext_flask
    ext_flask_wtf["flask_wtf"]
    class ext_flask_wtf ext;
    app_py -.->|imports| ext_flask_wtf
    ext_wtforms["wtforms"]
    class ext_wtforms ext;
    app_py -.->|imports| ext_wtforms
    ext_wtforms_validators["wtforms.validators"]
    class ext_wtforms_validators ext;
    app_py -.->|imports| ext_wtforms_validators
    ext_flask_bootstrap["flask_bootstrap"]
    class ext_flask_bootstrap ext;
    app_py -.->|imports| ext_flask_bootstrap
    ext_werkzeug_utils["werkzeug.utils"]
    class ext_werkzeug_utils ext;
    app_py -.->|imports| ext_werkzeug_utils
    ext_lazyown_infinitestorage["lazyown_infinitestorage"]
    class ext_lazyown_infinitestorage ext;
    app_py -.->|imports| ext_lazyown_infinitestorage
    ext_sys["sys"]
    class ext_sys ext;
    gui_py -.->|imports| ext_sys
    gui_py -.->|imports| ext_os
    ext_PyQt5_QtWidgets["PyQt5.QtWidgets"]
    class ext_PyQt5_QtWidgets ext;
    gui_py -.->|imports| ext_PyQt5_QtWidgets
    ext_PyQt5_QtCore["PyQt5.QtCore"]
    class ext_PyQt5_QtCore ext;
    gui_py -.->|imports| ext_PyQt5_QtCore
    gui_py -.->|imports| ext_lazyown_infinitestorage
    ext_argparse["argparse"]
    class ext_argparse ext;
    lazyown_infinitestorage_py -.->|imports| ext_argparse
    ext_binascii["binascii"]
    class ext_binascii ext;
    lazyown_infinitestorage_py -.->|imports| ext_binascii
    ext_math["math"]
    class ext_math ext;
    lazyown_infinitestorage_py -.->|imports| ext_math
    lazyown_infinitestorage_py -.->|imports| ext_os
    lazyown_infinitestorage_py -.->|imports| ext_re
    ext_struct["struct"]
    class ext_struct ext;
    lazyown_infinitestorage_py -.->|imports| ext_struct
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    lazyown_infinitestorage_py -.->|imports| ext_subprocess
    lazyown_infinitestorage_py -.->|imports| ext_sys
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
    lazyown_infinitestorage_py -.->|imports| ext_flask
    lazyown_infinitestorage_py -.->|imports| ext_PyQt5_QtWidgets
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
```

---

## Architecture Reference

### PY (4 files)

#### `app.py`
**Path:** `app.py`

**Classes:**
- `EncodeDecodeForm` (line 13) `class EncodeDecodeForm(FlaskForm)`

**Functions:**
- `sanitize_filename` (line 29) `def sanitize_filename(filename)`
- `index` (line 50) `def index()`
- `download_file` (line 88) `def download_file(filename)`
- `add_security_headers` (line 98) `def add_security_headers(response)`
- `upload_file` (line 120) `def upload_file()`

#### `gui.py`
**Path:** `gui.py`

**Classes:**
- `MainWindow` (line 10) `class MainWindow(QWidget)`

**Functions:**
- `__init__` (line 11) `def __init__(self)`
- `initUI` (line 15) `def initUI(self)`
- `create_encode_ui` (line 34) `def create_encode_ui(self)`
- `create_decode_ui` (line 64) `def create_decode_ui(self)`
- `create_common_ui` (line 86) `def create_common_ui(self)`
- `change_mode` (line 111) `def change_mode(self)`
- `clear_layout` (line 132) `def clear_layout(self, layout)`
- `browse_input_file` (line 138) `def browse_input_file(self)`
- `start_process` (line 148) `def start_process(self)`
- `show_message` (line 167) `def show_message(self, message)`

#### `lazyown_infinitestorage.py`
**Path:** `lazyown_infinitestorage.py`

**Classes:**
- `LazyOwnConfig` (line 132) `class LazyOwnConfig` - *Centralized immutable configuration constants for LazyOwnInfiniteStorage.*
- `SecurityValidator` (line 209) `class SecurityValidator` - *Validates file paths and inputs to prevent path traversal and abuse.*
- `ErrorCorrector` (line 245) `class ErrorCorrector` - *Implements Hamming(8,4) extended error correction for byte streams.*
- `FrameEncoder` (line 303) `class FrameEncoder` - *Encodes bit strings into numpy grayscale frames.*
- `FrameDecoder` (line 334) `class FrameDecoder` - *Decodes grayscale frames into bit strings.*
- `FFmpegPipeline` (line 366) `class FFmpegPipeline` - *Manages FFmpeg subprocess communication without intermediate frame files.*
- `ProtocolHandler` (line 456) `class ProtocolHandler` - *Abstract base for encoding and decoding protocol implementations.*
- `LegacyProtocolHandler` (line 468) `class LegacyProtocolHandler(ProtocolHandler)` - *Implements the original v1 protocol with filename-based resolution and end marker.*
- `SecureProtocolHandler` (line 493) `class SecureProtocolHandler(ProtocolHandler)` - *Implements the v2 protocol with structured headers, CRC32, and Hamming error correction.*
- `LazyOwnInfiniteStorage` (line 547) `class LazyOwnInfiniteStorage` - *Main orchestrator for encoding and decoding files to and from video.*
- `CLIRunner` (line 669) `class CLIRunner` - *Command-line interface runner for LazyOwnInfiniteStorage.*
- `Worker` (line 717) `class Worker(QThread)` - *Background worker thread for non-blocking GUI operations.*
- `GUIRunner` (line 736) `class GUIRunner(QWidget)` - *PyQt5 graphical user interface for LazyOwnInfiniteStorage.*
- `GUIRunner` (line 872) `class GUIRunner` - *Stub GUI runner when PyQt5 is unavailable.*
- `WebRunner` (line 883) `class WebRunner` - *Flask web server interface for LazyOwnInfiniteStorage.*
- `WebRunner` (line 969) `class WebRunner` - *Stub web runner when Flask is unavailable.*

**Functions:**
- `run_tests` (line 979) `def run_tests()` - *Executes built-in round-trip tests for both protocols.*
- `main` (line 1027) `def main()` - *Entry point for LazyOwnInfiniteStorage.*
- `__init__` (line 212) `def __init__(self, config)`
- `validate_file_path` (line 215) `def validate_file_path(self, file_path, must_exist)` - *Resolves and validates an absolute file path.*
- `validate_size` (line 225) `def validate_size(self, size)` - *Ensures the file size is within acceptable limits.*
- `sanitize_filename` (line 230) `def sanitize_filename(self, filename)` - *Sanitizes a filename to remove unsafe characters.*
- `validate_extension` (line 238) `def validate_extension(self, file_path, allowed_extensions)` - *Ensures the file extension is in the allowed set.*
- `__init__` (line 248) `def __init__(self, config)`
- `encode_data` (line 251) `def encode_data(self, data)` - *Encodes a byte sequence using Hamming(8,4) correction.*
- `decode_data` (line 261) `def decode_data(self, data)` - *Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.*
- `_encode_nibble` (line 272) `def _encode_nibble(self, nibble)`
- `_decode_nibble` (line 283) `def _decode_nibble(self, byte_val)`
- `__init__` (line 306) `def __init__(self, config)`
- `bits_to_frames` (line 309) `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` - *Yields grayscale frames from a bit string.*
- `_create_frame` (line 324) `def _create_frame(self, bits, width, height, block_size, blocks_per_row)`
- `__init__` (line 337) `def __init__(self, config)`
- `extract_bits_from_raw_frames` (line 340) `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)` - *Extracts a bit string from rawvideo grayscale bytes.*
- `__init__` (line 369) `def __init__(self, config)`
- `get_video_info` (line 372) `def get_video_info(self, input_path)` - *Retrieves native resolution and metadata from a video file.*
- `get_metadata` (line 386) `def get_metadata(self, input_path)` - *Extracts custom lazyown metadata from a video file using ffprobe.*
- `encode_video` (line 405) `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)` - *Encodes a generator of frames into a video file via FFmpeg stdin.*
- `extract_raw_frames` (line 432) `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)` - *Extracts raw grayscale frames from a video file via FFmpeg stdout.*
- `pack` (line 459) `def pack(self, data, frame_width, frame_height, block_size, fps)` - *Packs raw data into a bit string.*
- `unpack` (line 463) `def unpack(self, bit_string, block_size)` - *Unpacks a bit string into raw data.*
- `__init__` (line 471) `def __init__(self, config)`
- `pack` (line 474) `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `unpack` (line 479) `def unpack(self, bit_string, block_size)`
- `__init__` (line 496) `def __init__(self, config, corrector)`
- `pack` (line 500) `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `unpack` (line 519) `def unpack(self, bit_string, block_size)`
- `__init__` (line 550) `def __init__(self, config)`
- `encode` (line 560) `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)` - *Encodes a file into a video using the specified protocol.*
- `decode` (line 588) `def decode(self, input_path, output_path, block_size, protocol_version)` - *Decodes a video back into the original file using the specified protocol.*
- `_validate_encoding_parameters` (line 599) `def _validate_encoding_parameters(self, frame_width, frame_height, fps, block_size)`
- `_detect_protocol` (line 609) `def _detect_protocol(self, input_path, block_size)`
- `_decode_legacy` (line 642) `def _decode_legacy(self, input_path, output_path, block_size)`
- `_decode_secure` (line 655) `def _decode_secure(self, input_path, output_path, block_size)`
- `__init__` (line 672) `def __init__(self, storage)`
- `run` (line 675) `def run(self)`
- `__init__` (line 723) `def __init__(self, func)`
- `run` (line 729) `def run(self)`
- `__init__` (line 739) `def __init__(self, storage)`
- `_init_ui` (line 745) `def _init_ui(self)`
- `_change_mode` (line 813) `def _change_mode(self)`
- `_browse_input` (line 824) `def _browse_input(self)`
- `_start` (line 834) `def _start(self)`
- `_on_finished` (line 857) `def _on_finished(self, message)`
- `_on_error` (line 862) `def _on_error(self, message)`
- `run` (line 867) `def run(self)`
- `__init__` (line 875) `def __init__(self, storage)`
- `run` (line 878) `def run(self)`
- `__init__` (line 886) `def __init__(self, storage)`
- `_setup_routes` (line 891) `def _setup_routes(self)`
- `run` (line 964) `def run(self, host, port)`
- `__init__` (line 972) `def __init__(self, storage)`
- `run` (line 975) `def run(self, host, port)`
- `index` (line 897) `def index()`
- `download` (line 944) `def download(filename)`
- `add_security_headers` (line 952) `def add_security_headers(response)`

#### `tools.py`
**Path:** `skill_lazyown_infinitestorage/tools.py`

**Functions:**
- `lazyown_infinitestorage_encode` (line 34) `def lazyown_infinitestorage_encode(params)` - *Encode a file into a video using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_decode` (line 101) `def lazyown_infinitestorage_decode(params)` - *Decode a video back into the original file using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_upload_to_youtube` (line 152) `def lazyown_infinitestorage_upload_to_youtube(params)` - *Upload a video to YouTube using browser automation.*
- `get_tool` (line 302) `def get_tool(name)` - *Get a tool by name.*
- `list_tools` (line 306) `def list_tools()` - *List all available tools.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
