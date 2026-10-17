# API

## lazyown_infinitestorage.py
Imported by: `mcp_server.py`, `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `tests/test_zip.py`, `wsgi_app.py`
- `SecurityValidator.__init__` (method) `lazyown_infinitestorage.py:159` `def __init__(self, config)`
- `SecurityValidator.validate_file_path` (method) `lazyown_infinitestorage.py:162` `def validate_file_path(self, file_path, must_exist)` -- Resolves and validates an absolute file path.
- `SecurityValidator.validate_size` (method) `lazyown_infinitestorage.py:172` `def validate_size(self, size)` -- Ensures the file size is within acceptable limits.
- `SecurityValidator.sanitize_filename` (method) `lazyown_infinitestorage.py:177` `def sanitize_filename(self, filename)` -- Sanitizes a filename to remove unsafe characters.
- `SecurityValidator.validate_extension` (method) `lazyown_infinitestorage.py:185` `def validate_extension(self, file_path, allowed_extensions)` -- Ensures the file extension is in the allowed set.
- `ErrorCorrector.__init__` (method) `lazyown_infinitestorage.py:195` `def __init__(self, config)`
- `ErrorCorrector.encode_data` (method) `lazyown_infinitestorage.py:198` `def encode_data(self, data)` -- Encodes a byte sequence using Hamming(8,4) correction.
- `ErrorCorrector.decode_data` (method) `lazyown_infinitestorage.py:208` `def decode_data(self, data)` -- Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.
- `FrameEncoder.__init__` (method) `lazyown_infinitestorage.py:253` `def __init__(self, config)`
- `FrameEncoder.bits_to_frames` (method) `lazyown_infinitestorage.py:256` `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)` -- Yields grayscale frames from a bit string.
- `FrameDecoder.__init__` (method) `lazyown_infinitestorage.py:284` `def __init__(self, config)`
- `FrameDecoder.extract_bits_from_raw_frames` (method) `lazyown_infinitestorage.py:287` `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)` -- Extracts a bit string from rawvideo grayscale bytes.
- `FFmpegPipeline.__init__` (method) `lazyown_infinitestorage.py:316` `def __init__(self, config)`
- `FFmpegPipeline.get_video_info` (method) `lazyown_infinitestorage.py:319` `def get_video_info(self, input_path)` -- Retrieves native resolution and metadata from a video file.
- `FFmpegPipeline.get_metadata` (method) `lazyown_infinitestorage.py:355` `def get_metadata(self, input_path)` -- Extracts custom lazyown metadata from a video file using ffprobe.
- `FFmpegPipeline.encode_video` (method) `lazyown_infinitestorage.py:374` `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)` -- Encodes a generator of frames into a video file via FFmpeg stdin.
- `FFmpegPipeline.extract_raw_frames` (method) `lazyown_infinitestorage.py:401` `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)` -- Extracts raw grayscale frames from a video file via FFmpeg stdout.
- `ProtocolHandler.pack` (method) `lazyown_infinitestorage.py:439` `def pack(self, data, frame_width, frame_height, block_size, fps)` -- Packs raw data into a bit string.
- `ProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:443` `def unpack(self, bit_string, block_size)` -- Unpacks a bit string into raw data.
- `LegacyProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:451` `def __init__(self, config)`
- `LegacyProtocolHandler.pack` (method) `lazyown_infinitestorage.py:454` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `LegacyProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:459` `def unpack(self, bit_string, block_size)`
- `SecureProtocolHandler.__init__` (method) `lazyown_infinitestorage.py:476` `def __init__(self, config, corrector)`
- `SecureProtocolHandler.pack` (method) `lazyown_infinitestorage.py:480` `def pack(self, data, frame_width, frame_height, block_size, fps)`
- `SecureProtocolHandler.unpack` (method) `lazyown_infinitestorage.py:499` `def unpack(self, bit_string, block_size)`
- `LazyOwnInfiniteStorage.__init__` (method) `lazyown_infinitestorage.py:530` `def __init__(self, config)`
- `LazyOwnInfiniteStorage.create_web_runner` (method) `lazyown_infinitestorage.py:540` `def create_web_runner(self)` -- Return a WebRunner for WSGI or local web server use.
- `LazyOwnInfiniteStorage.encode` (method) `lazyown_infinitestorage.py:544` `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)` -- Encodes a file into a video using the specified protocol.
- `LazyOwnInfiniteStorage.decode` (method) `lazyown_infinitestorage.py:567` `def decode(self, input_path, output_path, block_size, protocol_version)` -- Decodes a video back into the original file using the specified protocol.
- `LazyOwnInfiniteStorage.create_zip` (method) `lazyown_infinitestorage.py:653` `def create_zip(self, source_path, output_zip)` -- Create a zip archive from a file or directory.
- `LazyOwnInfiniteStorage.extract_zip` (method) `lazyown_infinitestorage.py:672` `def extract_zip(self, zip_path, output_dir)` -- Safely extract a zip archive into output_dir (blocks zip slip).
- `LazyOwnInfiniteStorage.zip_to_video` (method) `lazyown_infinitestorage.py:693` `def zip_to_video(self, source_path, output_video, frame_width, frame_height, fps, block_size, protocol_version)` -- Zip a file or directory then encode the archive to video.
- `LazyOwnInfiniteStorage.video_to_zip` (method) `lazyown_infinitestorage.py:707` `def video_to_zip(self, input_video, output_dir, block_size, protocol_version)` -- Decode a video to a zip archive then extract it into output_dir.
- `CLIRunner.__init__` (method) `lazyown_infinitestorage.py:726` `def __init__(self, storage)`
- `CLIRunner.run` (method) `lazyown_infinitestorage.py:729` `def run(self)`
- `Worker.__init__` (method) `lazyown_infinitestorage.py:789` `def __init__(self, func)`
- `Worker.run` (method) `lazyown_infinitestorage.py:795` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:805` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:933` `def run(self)`
- `GUIRunner.__init__` (method) `lazyown_infinitestorage.py:941` `def __init__(self, storage)`
- `GUIRunner.run` (method) `lazyown_infinitestorage.py:944` `def run(self)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:952` `def __init__(self, storage)`
- `WebRunner.run_setup` (method) `lazyown_infinitestorage.py:963` `def run_setup(self)` -- Create directories and validate environment.
- `index` (function) `lazyown_infinitestorage.py:992` `def index()`
- `download` (function) `lazyown_infinitestorage.py:1037` `def download(filename)`
- `add_security_headers` (function) `lazyown_infinitestorage.py:1045` `def add_security_headers(response)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:1057` `def run(self, host, port)`
- `WebRunner.__init__` (method) `lazyown_infinitestorage.py:1065` `def __init__(self, storage)`
- `WebRunner.run` (method) `lazyown_infinitestorage.py:1068` `def run(self, host, port)`
- `run_tests` (function) `lazyown_infinitestorage.py:1072` `def run_tests()` -- Executes built-in round-trip tests for both protocols.
- `main` (function) `lazyown_infinitestorage.py:1120` `def main()` -- Entry point for LazyOwnInfiniteStorage.

## mcp_server.py
Depends on: `lazyown_infinitestorage.py`
- `list_tools` (function) `mcp_server.py:310` `def list_tools()`
- `call_tool` (function) `mcp_server.py:314` `def call_tool(name, arguments)`
- `main` (function) `mcp_server.py:330` `def main()` -- Entry point for the LazyOwnInfiniteStorage MCP stdio server.

## skill_lazyown_infinitestorage/tools.py
Depends on: `lazyown_infinitestorage.py`
- `lazyown_infinitestorage_encode` (function) `skill_lazyown_infinitestorage/tools.py:52` `def lazyown_infinitestorage_encode(params)` -- Encode a file into a video using LazyOwnInfiniteStorage.
- `lazyown_infinitestorage_decode` (function) `skill_lazyown_infinitestorage/tools.py:105` `def lazyown_infinitestorage_decode(params)` -- Decode a video back into the original file using LazyOwnInfiniteStorage.
- `lazyown_zip_to_video` (function) `skill_lazyown_infinitestorage/tools.py:149` `def lazyown_zip_to_video(params)` -- Zip a file or directory then encode the archive into a video (zip -> video).
- `lazyown_video_to_zip` (function) `skill_lazyown_infinitestorage/tools.py:195` `def lazyown_video_to_zip(params)` -- Decode a video into a zip archive then extract it (video -> zip -> files).
- `lazyown_create_zip` (function) `skill_lazyown_infinitestorage/tools.py:236` `def lazyown_create_zip(params)` -- Create a zip archive from a file or directory.
- `lazyown_extract_zip` (function) `skill_lazyown_infinitestorage/tools.py:268` `def lazyown_extract_zip(params)` -- Safely extract a zip archive into a directory (blocks zip slip).
- `lazyown_infinitestorage_upload_to_youtube` (function) `skill_lazyown_infinitestorage/tools.py:299` `def lazyown_infinitestorage_upload_to_youtube(params)` -- Upload a video to YouTube using browser automation.
- `get_tool` (function) `skill_lazyown_infinitestorage/tools.py:453` `def get_tool(name)` -- Get a tool by name.
- `list_tools` (function) `skill_lazyown_infinitestorage/tools.py:457` `def list_tools()` -- List all available tools.

## wsgi_app.py
Depends on: `lazyown_infinitestorage.py`
- `get_wsgi_app` (function) `wsgi_app.py:7` `def get_wsgi_app()` -- Factory function returning a gunicorn-compatible Flask application.
