# root

root groups 10 files (py) around LazyOwnConfig, SecurityValidator, __init__, validate_file_path, validate_size. LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.

```mermaid
graph LR
    root["root"]
    skill_lazyown_infinitestorage["skill_lazyown_infinitestorage"]
    tests["tests"]
    skill_lazyown_infinitestorage -- "calls into" --> root
    tests -- "calls into" --> root
```

## root (1.1)

root groups 3 files (py) around LazyOwnConfig, SecurityValidator, __init__, validate_file_path, validate_size. LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.

## skill_lazyown_infinitestorage (1.2)

skill_lazyown_infinitestorage groups 1 files (py) around _parse_frame_size, _protocol_value, lazyown_infinitestorage_encode, lazyown_infinitestorage_decode, lazyown_zip_to_video. MCP tools for LazyOwnInfiniteStorage integration.

## tests (1.3)

tests groups 6 files (py) around TestErrorCorrector, setup, test_encode_data_doubles_length, test_decode_data_reverses_encoding, test_decode_data_with_single_bit_error. Unit tests for ErrorCorrector Hamming(8,4) implementation.

**Files**:

- lazyown_infinitestorage.py
- mcp_server.py
- skill_lazyown_infinitestorage/tools.py
- tests/test_error_correction.py
- tests/test_frames.py
- tests/test_integration.py
- tests/test_protocols.py
- tests/test_security.py
- tests/test_zip.py
- wsgi_app.py
