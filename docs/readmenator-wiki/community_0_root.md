# root

*Community 0 | 8 files | cohesion 1.00*

## Definition

This community groups 8 file(s) rooted at `tests` with dominant language py (cohesion 1.00). Central symbols: `CLIRunner`, `ErrorCorrector`, `FFmpegPipeline`, `FrameDecoder`, `FrameEncoder`, `GUIRunner`, `LazyOwnConfig`, `LazyOwnInfiniteStorage`. Core file: `lazyown_infinitestorage.py` (78 symbols). Documented purpose: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `lazyown_infinitestorage.py` | py | presentation | 78 | yes |
| `skill_lazyown_infinitestorage/tools.py` | py | utility | 5 | yes |
| `tests/test_error_correction.py` | py | testing | 10 | yes |
| `tests/test_frames.py` | py | testing | 13 | yes |
| `tests/test_integration.py` | py | testing | 16 | yes |
| `tests/test_protocols.py` | py | testing | 12 | yes |
| `tests/test_security.py` | py | testing | 18 | yes |
| `wsgi_app.py` | py | utility | 1 | yes |

## Key Symbols

- `LazyOwnConfig` (class, `lazyown_infinitestorage.py:66`) `class LazyOwnConfig` - Centralized immutable configuration constants for LazyOwnInfiniteStorage.
- `SecurityValidator` (class, `lazyown_infinitestorage.py:143`) `class SecurityValidator` - Validates file paths and inputs to prevent path traversal and abuse.
- `__init__` (method, `lazyown_infinitestorage.py:146`) `def __init__(self, config)`
- `validate_file_path` (method, `lazyown_infinitestorage.py:149`) `def validate_file_path(self, file_path, must_exist)` - Resolves and validates an absolute file path.
- `validate_size` (method, `lazyown_infinitestorage.py:159`) `def validate_size(self, size)` - Ensures the file size is within acceptable limits.
- `sanitize_filename` (method, `lazyown_infinitestorage.py:164`) `def sanitize_filename(self, filename)` - Sanitizes a filename to remove unsafe characters.
- `validate_extension` (method, `lazyown_infinitestorage.py:172`) `def validate_extension(self, file_path, allowed_extensions)` - Ensures the file extension is in the allowed set.
- `ErrorCorrector` (class, `lazyown_infinitestorage.py:179`) `class ErrorCorrector` - Implements Hamming(8,4) extended error correction for byte streams.
- `__init__` (method, `lazyown_infinitestorage.py:182`) `def __init__(self, config)`
- `encode_data` (method, `lazyown_infinitestorage.py:185`) `def encode_data(self, data)` - Encodes a byte sequence using Hamming(8,4) correction.
- `decode_data` (method, `lazyown_infinitestorage.py:195`) `def decode_data(self, data)` - Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.
- `_encode_nibble` (method, `lazyown_infinitestorage.py:206`) `def _encode_nibble(self, nibble)`
- `_decode_nibble` (method, `lazyown_infinitestorage.py:217`) `def _decode_nibble(self, byte_val)`
- `FrameEncoder` (class, `lazyown_infinitestorage.py:237`) `class FrameEncoder` - Encodes bit strings into numpy grayscale frames.
- `__init__` (method, `lazyown_infinitestorage.py:240`) `def __init__(self, config)`
- `bits_to_frames` (method, `lazyown_infinitestorage.py:243`) `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` - Yields grayscale frames from a bit string.
- `_create_frame` (method, `lazyown_infinitestorage.py:258`) `def _create_frame(self, bits, width, height, block_size, blocks_per_row)`
- `FrameDecoder` (class, `lazyown_infinitestorage.py:268`) `class FrameDecoder` - Decodes grayscale frames into bit strings.
- `__init__` (method, `lazyown_infinitestorage.py:271`) `def __init__(self, config)`
- `extract_bits_from_raw_frames` (method, `lazyown_infinitestorage.py:274`) `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, exp` - Extracts a bit string from rawvideo grayscale bytes.
- `FFmpegPipeline` (class, `lazyown_infinitestorage.py:300`) `class FFmpegPipeline` - Manages FFmpeg subprocess communication without intermediate frame files.
- `__init__` (method, `lazyown_infinitestorage.py:303`) `def __init__(self, config)`
- `get_video_info` (method, `lazyown_infinitestorage.py:306`) `def get_video_info(self, input_path)` - Retrieves native resolution and metadata from a video file.
- `get_metadata` (method, `lazyown_infinitestorage.py:320`) `def get_metadata(self, input_path)` - Extracts custom lazyown metadata from a video file using ffprobe.
- `encode_video` (method, `lazyown_infinitestorage.py:339`) `def encode_video(self, frame_generator, output_path, frame_width, frame_height,` - Encodes a generator of frames into a video file via FFmpeg stdin.
- `extract_raw_frames` (method, `lazyown_infinitestorage.py:366`) `def extract_raw_frames(self, input_path, target_width, target_height, max_frames` - Extracts raw grayscale frames from a video file via FFmpeg stdout.
- `ProtocolHandler` (class, `lazyown_infinitestorage.py:390`) `class ProtocolHandler` - Abstract base for encoding and decoding protocol implementations.
- `pack` (method, `lazyown_infinitestorage.py:393`) `def pack(self, data, frame_width, frame_height, block_size, fps)` - Packs raw data into a bit string.
- `unpack` (method, `lazyown_infinitestorage.py:397`) `def unpack(self, bit_string, block_size)` - Unpacks a bit string into raw data.
- `LegacyProtocolHandler` (class, `lazyown_infinitestorage.py:402`) `class LegacyProtocolHandler(ProtocolHandler)` - Implements the original v1 protocol with filename-based resolution and end marker.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 7
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [taint high] `lazyown_infinitestorage.py` -> `lazyown_infinitestorage.py` via `subprocess` (0 hops)
- [taint high] `skill_lazyown_infinitestorage/tools.py` -> `skill_lazyown_infinitestorage/tools.py` via `subprocess` (0 hops)
- [taint high] `skill_lazyown_infinitestorage/tools.py` -> `lazyown_infinitestorage.py` via `subprocess` (1 hops)
- [taint high] `tests/test_integration.py` -> `tests/test_integration.py` via `subprocess` (0 hops)
- [taint high] `tests/test_integration.py` -> `lazyown_infinitestorage.py` via `subprocess` (1 hops)
- [layer strict] `tests/test_error_correction.py` (testing) -> `lazyown_infinitestorage.py` (presentation)
- [layer strict] `tests/test_frames.py` (testing) -> `lazyown_infinitestorage.py` (presentation)
- [layer strict] `tests/test_integration.py` (testing) -> `lazyown_infinitestorage.py` (presentation)
- [layer strict] `tests/test_protocols.py` (testing) -> `lazyown_infinitestorage.py` (presentation)
- [layer strict] `tests/test_security.py` (testing) -> `lazyown_infinitestorage.py` (presentation)

## Open Questions

- Is the dangerous import `subprocess` in `lazyown_infinitestorage.py` still required, or can it be isolated?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `lazyown_infinitestorage.py`
- `skill_lazyown_infinitestorage/tools.py`
- `tests/test_error_correction.py`
- `tests/test_frames.py`
- `tests/test_integration.py`
- `tests/test_protocols.py`
- `tests/test_security.py`
- `wsgi_app.py`
