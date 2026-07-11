# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 5 | **Total Symbols Extracted:** 97 | **Total Imports:** 45

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
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

**Classs:**
- `EncodeDecodeForm` (line 13)

**Functions:**
- `sanitize_filename` (line 29)
- `index` (line 50)
- `download_file` (line 88)
- `add_security_headers` (line 98)
- `upload_file` (line 120)

#### `gui.py`
**Path:** `gui.py`

**Classs:**
- `MainWindow` (line 10)

**Functions:**
- `__init__` (line 11)
- `initUI` (line 15)
- `create_encode_ui` (line 34)
- `create_decode_ui` (line 64)
- `create_common_ui` (line 86)
- `change_mode` (line 111)
- `clear_layout` (line 132)
- `browse_input_file` (line 138)
- `start_process` (line 148)
- `show_message` (line 167)

#### `lazyown_infinitestorage.py`
**Path:** `lazyown_infinitestorage.py`

**Classs:**
- `LazyOwnConfig` (line 132) - *Centralized immutable configuration constants for LazyOwnInfiniteStorage.*
- `SecurityValidator` (line 209) - *Validates file paths and inputs to prevent path traversal and abuse.*
- `ErrorCorrector` (line 245) - *Implements Hamming(8,4) extended error correction for byte streams.*
- `FrameEncoder` (line 303) - *Encodes bit strings into numpy grayscale frames.*
- `FrameDecoder` (line 334) - *Decodes grayscale frames into bit strings.*
- `FFmpegPipeline` (line 366) - *Manages FFmpeg subprocess communication without intermediate frame files.*
- `ProtocolHandler` (line 456) - *Abstract base for encoding and decoding protocol implementations.*
- `LegacyProtocolHandler` (line 468) - *Implements the original v1 protocol with filename-based resolution and end marker.*
- `SecureProtocolHandler` (line 493) - *Implements the v2 protocol with structured headers, CRC32, and Hamming error correction.*
- `LazyOwnInfiniteStorage` (line 547) - *Main orchestrator for encoding and decoding files to and from video.*
- `CLIRunner` (line 669) - *Command-line interface runner for LazyOwnInfiniteStorage.*
- `Worker` (line 717) - *Background worker thread for non-blocking GUI operations.*
- `GUIRunner` (line 736) - *PyQt5 graphical user interface for LazyOwnInfiniteStorage.*
- `GUIRunner` (line 872) - *Stub GUI runner when PyQt5 is unavailable.*
- `WebRunner` (line 883) - *Flask web server interface for LazyOwnInfiniteStorage.*
- `WebRunner` (line 969) - *Stub web runner when Flask is unavailable.*

**Functions:**
- `run_tests` (line 979) - *Executes built-in round-trip tests for both protocols.*
- `main` (line 1027) - *Entry point for LazyOwnInfiniteStorage.*
- `__init__` (line 212)
- `validate_file_path` (line 215) - *Resolves and validates an absolute file path.*
- `validate_size` (line 225) - *Ensures the file size is within acceptable limits.*
- `sanitize_filename` (line 230) - *Sanitizes a filename to remove unsafe characters.*
- `validate_extension` (line 238) - *Ensures the file extension is in the allowed set.*
- `__init__` (line 248)
- `encode_data` (line 251) - *Encodes a byte sequence using Hamming(8,4) correction.*
- `decode_data` (line 261) - *Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.*
- `_encode_nibble` (line 272)
- `_decode_nibble` (line 283)
- `__init__` (line 306)
- `bits_to_frames` (line 309) - *Yields grayscale frames from a bit string.*
- `_create_frame` (line 324)
- `__init__` (line 337)
- `extract_bits_from_raw_frames` (line 340) - *Extracts a bit string from rawvideo grayscale bytes.*
- `__init__` (line 369)
- `get_video_info` (line 372) - *Retrieves native resolution and metadata from a video file.*
- `get_metadata` (line 386) - *Extracts custom lazyown metadata from a video file using ffprobe.*
- `encode_video` (line 405) - *Encodes a generator of frames into a video file via FFmpeg stdin.*
- `extract_raw_frames` (line 432) - *Extracts raw grayscale frames from a video file via FFmpeg stdout.*
- `pack` (line 459) - *Packs raw data into a bit string.*
- `unpack` (line 463) - *Unpacks a bit string into raw data.*
- `__init__` (line 471)
- `pack` (line 474)
- `unpack` (line 479)
- `__init__` (line 496)
- `pack` (line 500)
- `unpack` (line 519)
- `__init__` (line 550)
- `encode` (line 560) - *Encodes a file into a video using the specified protocol.*
- `decode` (line 588) - *Decodes a video back into the original file using the specified protocol.*
- `_validate_encoding_parameters` (line 599)
- `_detect_protocol` (line 609)
- `_decode_legacy` (line 642)
- `_decode_secure` (line 655)
- `__init__` (line 672)
- `run` (line 675)
- `__init__` (line 723)
- `run` (line 729)
- `__init__` (line 739)
- `_init_ui` (line 745)
- `_change_mode` (line 813)
- `_browse_input` (line 824)
- `_start` (line 834)
- `_on_finished` (line 857)
- `_on_error` (line 862)
- `run` (line 867)
- `__init__` (line 875)
- `run` (line 878)
- `__init__` (line 886)
- `_setup_routes` (line 891)
- `run` (line 964)
- `__init__` (line 972)
- `run` (line 975)
- `index` (line 897)
- `download` (line 944)
- `add_security_headers` (line 952)

#### `tools.py`
**Path:** `skill_lazyown_infinitestorage/tools.py`

**Functions:**
- `lazyown_infinitestorage_encode` (line 34) - *Encode a file into a video using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_decode` (line 101) - *Decode a video back into the original file using LazyOwnInfiniteStorage.*
- `lazyown_infinitestorage_upload_to_youtube` (line 152) - *Upload a video to YouTube using browser automation.*
- `get_tool` (line 302) - *Get a tool by name.*
- `list_tools` (line 306) - *List all available tools.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
