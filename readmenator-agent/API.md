# API

## lazyown_infinitestorage.py
Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`
- `SecurityValidator.__init__` (method) `lazyown_infinitestorage.py:151` `def __init__(self, config)`
- `SecurityValidator.validate_file_path` (method) `lazyown_infinitestorage.py:154` `def validate_file_path(self, file_path, must_exist)` -- Resolves and validates an absolute file path.
- `SecurityValidator.validate_size` (method) `lazyown_infinitestorage.py:164` `def validate_size(self, size)` -- Ensures the file size is within acceptable limits.
- `SecurityValidator.sanitize_filename` (method) `lazyown_infinitestorage.py:169` `def sanitize_filename(self, filename)` -- Sanitizes a filename to remove unsafe characters.
- `SecurityValidator.validate_extension` (method) `lazyown_infinitestorage.py:177` `def validate_extension(self, file_path, allowed_extensions)` -- Ensures the file extension is in the allowed set.
- `ErrorCorrector.__init__` (method) `lazyown_infinitestorage.py:187` `def __init__(self, config)`
- `ErrorCorrector.encode_data` (method) `lazyown_infinitestorage.py:190` `def encode_data(self, data)` -- Encodes a byte sequence using Hamming(8,4) correction.
- `ErrorCorrector.decode_data` (method) `lazyown_infinitestorage.py:200` `def decode_data(self, data)` -- Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.
- `FrameEncoder.__init__` (method) `lazyown_infinitestorage.py:245` `def __init__(self, config)`
- `FrameEncoder.bits_to_frames` (method) `lazyown_infinitestorage.py:248` `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` -- Yields grayscale frames from a bit string.
- `FrameDecoder.__init__` (method) `lazyown_infinitestorage.py:276` `def __init__(self, config)`
- `FrameDecoder.extract_bits_from_raw_frames` (method) `lazyown_infinitestorage.py:279` `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)` -- Extracts a bit string from rawvideo grayscale bytes.
- `FFmpegPipeline.__init__` (method) `lazyown_infinitestorage.py:308` `def __init__(self, config)`
- `FFmpegPipeline.get_video_info` (method) `lazyown_infinitestorage.py:311` `def get_video_info(self, input_path)` -- Retrieves native resolution and metadata from a video file.
- `FFmpegPipeline.get_metadata` (method) `lazyown_infinitestorage.py:347` `def get_metadata(self, input_path)` -- Extracts custom lazyown metadata from a video file using ffprobe.
- `FFmpegPipeline.encode_video` (method) `lazyown_infinitestorage.py:366` `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)` -- Encodes a generator of frames into a video file via FFmpeg stdin.
- `FFmpegPipeline.extract_raw_frames` (method) `lazyown_infinitestorage.py:393` `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)` -- Extracts raw grayscale frames from a video file via FFmpeg stdout.
- `ProtocolHandler.pack` (method) `lazyown_infinitestorage.py:420` `def pack(self, data, frame_width, frame_height, block_size, fps)` -- Packs raw data into a bit string.
- `ProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:424` `def unpack(self, bit_string, block_size)` -- Unpacks a bit string into raw data.
- `LegacyProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:432` `def __init__(self, config)`
- `LegacyProtocolHandler.pack` (method) `lazyown_infinitestorage.py:435` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `LegacyProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:440` `def unpack(self, bit_string, block_size)`
- `SecureProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:457` `def __init__(self, config, corrector)`
- `SecureProtocolHandler.pack` (method) `lazyown_infinitestorage.py:461` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `SecureProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:480` `def unpack(self, bit_string, block_size)`
- `LazyOwnInfiniteStorage.__init__` (method) `lazyown_infinitestorage.py:511` `def __init__(self, config)`
- `LazyOwnInfiniteStorage.create_web_runner` (method) `lazyown_infinitestorage.py:521` `def create_web_runner(self)` -- Return a WebRunner for WSGI or local web server use.
- `LazyOwnInfiniteStorage.encode` (method) `lazyown_infinitestorage.py:525` `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)` -- Encodes a file into a video using the specified protocol.
- `LazyOwnInfiniteStorage.decode` (method) `lazyown_infinitestorage.py:550` `def decode(self, input_path, output_path, block_size, protocol_version)` -- Decodes a video back into the original file using the specified protocol.
- `CLIRunner.__init__` (method) `lazyown_infinitestorage.py:634` `def __init__(self, storage)`
- `CLIRunner.run` (method) `lazyown_infinitestorage.py:637` `def run(self)`
- `Worker.__init__` (method) `lazyown_infinitestorage.py:687` `def __init__(self, func)`
- `Worker.run` (method) `lazyown_infinitestorage.py:693` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:703` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:831` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:839` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:842` `def run(self)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:850` `def __init__(self, storage)`
- `WebRunner.run_setup` (method) `lazyown_infinitestorage.py:861` `def run_setup(self)` -- Create directories and validate environment.
- `index` (function) `lazyown_infinitestorage.py:890` `def index()`
- `download` (function) `lazyown_infinitestorage.py:935` `def download(filename)`
- `add_security_headers` (function) `lazyown_infinitestorage.py:943` `def add_security_headers(response)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:955` `def run(self, host, port)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:963` `def __init__(self, storage)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:966` `def run(self, host, port)`
- `run_tests` (function) `lazyown_infinitestorage.py:970` `def run_tests()` -- Executes built-in round-trip tests for both protocols.
- `main` (function) `lazyown_infinitestorage.py:1018` `def main()` -- Entry point for LazyOwnInfiniteStorage.

## skill_lazyown_infinitestorage/tools.py
Depends on: `lazyown_infinitestorage.py`
- `lazyown_infinitestorage_encode` (function) `skill_lazyown_infinitestorage/tools.py:34` `def lazyown_infinitestorage_encode(params)` -- Encode a file into a video using LazyOwnInfiniteStorage.
- `lazyown_infinitestorage_decode` (function) `skill_lazyown_infinitestorage/tools.py:101` `def lazyown_infinitestorage_decode(params)` -- Decode a video back into the original file using LazyOwnInfiniteStorage.
- `lazyown_infinitestorage_upload_to_youtube` (function) `skill_lazyown_infinitestorage/tools.py:152` `def lazyown_infinitestorage_upload_to_youtube(params)` -- Upload a video to YouTube using browser automation.
- `get_tool` (function) `skill_lazyown_infinitestorage/tools.py:302` `def get_tool(name)` -- Get a tool by name.
- `list_tools` (function) `skill_lazyown_infinitestorage/tools.py:306` `def list_tools()` -- List all available tools.

## wsgi_app.py
Depends on: `lazyown_infinitestorage.py`
- `get_wsgi_app` (function) `wsgi_app.py:7` `def get_wsgi_app()` -- Factory function returning a gunicorn-compatible Flask application.
