# API

## lazyown_infinitestorage.py
Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`
- `SecurityValidator.__init__` (method) `lazyown_infinitestorage.py:146` `def __init__(self, config)`
- `SecurityValidator.validate_file_path` (method) `lazyown_infinitestorage.py:149` `def validate_file_path(self, file_path, must_exist)` -- Resolves and validates an absolute file path.
- `SecurityValidator.validate_size` (method) `lazyown_infinitestorage.py:159` `def validate_size(self, size)` -- Ensures the file size is within acceptable limits.
- `SecurityValidator.sanitize_filename` (method) `lazyown_infinitestorage.py:164` `def sanitize_filename(self, filename)` -- Sanitizes a filename to remove unsafe characters.
- `SecurityValidator.validate_extension` (method) `lazyown_infinitestorage.py:172` `def validate_extension(self, file_path, allowed_extensions)` -- Ensures the file extension is in the allowed set.
- `ErrorCorrector.__init__` (method) `lazyown_infinitestorage.py:182` `def __init__(self, config)`
- `ErrorCorrector.encode_data` (method) `lazyown_infinitestorage.py:185` `def encode_data(self, data)` -- Encodes a byte sequence using Hamming(8,4) correction.
- `ErrorCorrector.decode_data` (method) `lazyown_infinitestorage.py:195` `def decode_data(self, data)` -- Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.
- `FrameEncoder.__init__` (method) `lazyown_infinitestorage.py:240` `def __init__(self, config)`
- `FrameEncoder.bits_to_frames` (method) `lazyown_infinitestorage.py:243` `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` -- Yields grayscale frames from a bit string.
- `FrameDecoder.__init__` (method) `lazyown_infinitestorage.py:271` `def __init__(self, config)`
- `FrameDecoder.extract_bits_from_raw_frames` (method) `lazyown_infinitestorage.py:274` `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)` -- Extracts a bit string from rawvideo grayscale bytes.
- `FFmpegPipeline.__init__` (method) `lazyown_infinitestorage.py:303` `def __init__(self, config)`
- `FFmpegPipeline.get_video_info` (method) `lazyown_infinitestorage.py:306` `def get_video_info(self, input_path)` -- Retrieves native resolution and metadata from a video file.
- `FFmpegPipeline.get_metadata` (method) `lazyown_infinitestorage.py:320` `def get_metadata(self, input_path)` -- Extracts custom lazyown metadata from a video file using ffprobe.
- `FFmpegPipeline.encode_video` (method) `lazyown_infinitestorage.py:339` `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)` -- Encodes a generator of frames into a video file via FFmpeg stdin.
- `FFmpegPipeline.extract_raw_frames` (method) `lazyown_infinitestorage.py:366` `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)` -- Extracts raw grayscale frames from a video file via FFmpeg stdout.
- `ProtocolHandler.pack` (method) `lazyown_infinitestorage.py:393` `def pack(self, data, frame_width, frame_height, block_size, fps)` -- Packs raw data into a bit string.
- `ProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:397` `def unpack(self, bit_string, block_size)` -- Unpacks a bit string into raw data.
- `LegacyProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:405` `def __init__(self, config)`
- `LegacyProtocolHandler.pack` (method) `lazyown_infinitestorage.py:408` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `LegacyProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:413` `def unpack(self, bit_string, block_size)`
- `SecureProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:430` `def __init__(self, config, corrector)`
- `SecureProtocolHandler.pack` (method) `lazyown_infinitestorage.py:434` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `SecureProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:453` `def unpack(self, bit_string, block_size)`
- `LazyOwnInfiniteStorage.__init__` (method) `lazyown_infinitestorage.py:484` `def __init__(self, config)`
- `LazyOwnInfiniteStorage.create_web_runner` (method) `lazyown_infinitestorage.py:494` `def create_web_runner(self)` -- Return a WebRunner for WSGI or local web server use.
- `LazyOwnInfiniteStorage.encode` (method) `lazyown_infinitestorage.py:498` `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)` -- Encodes a file into a video using the specified protocol.
- `LazyOwnInfiniteStorage.decode` (method) `lazyown_infinitestorage.py:523` `def decode(self, input_path, output_path, block_size, protocol_version)` -- Decodes a video back into the original file using the specified protocol.
- `CLIRunner.__init__` (method) `lazyown_infinitestorage.py:607` `def __init__(self, storage)`
- `CLIRunner.run` (method) `lazyown_infinitestorage.py:610` `def run(self)`
- `Worker.__init__` (method) `lazyown_infinitestorage.py:660` `def __init__(self, func)`
- `Worker.run` (method) `lazyown_infinitestorage.py:666` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:676` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:804` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:812` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:815` `def run(self)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:823` `def __init__(self, storage)`
- `WebRunner.run_setup` (method) `lazyown_infinitestorage.py:834` `def run_setup(self)` -- Create directories and validate environment.
- `WebRunner.index` (method) `lazyown_infinitestorage.py:863` `def index()`
- `WebRunner.download` (method) `lazyown_infinitestorage.py:908` `def download(filename)`
- `WebRunner.add_security_headers` (method) `lazyown_infinitestorage.py:916` `def add_security_headers(response)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:928` `def run(self, host, port)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:936` `def __init__(self, storage)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:939` `def run(self, host, port)`
- `WebRunner.run_tests` (method) `lazyown_infinitestorage.py:943` `def run_tests()` -- Executes built-in round-trip tests for both protocols.
- `WebRunner.main` (method) `lazyown_infinitestorage.py:991` `def main()` -- Entry point for LazyOwnInfiniteStorage.

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
