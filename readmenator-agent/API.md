# API

## lazyown_infinitestorage.py

### run_tests `def run_tests()`
- Defined: `lazyown_infinitestorage.py:943`
- Doc: Executes built-in round-trip tests for both protocols.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### main `def main()`
- Defined: `lazyown_infinitestorage.py:991`
- Doc: Entry point for LazyOwnInfiniteStorage.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:146`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### validate_file_path `def validate_file_path(self, file_path, must_exist)`
- Defined: `lazyown_infinitestorage.py:149`
- Doc: Resolves and validates an absolute file path.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### validate_size `def validate_size(self, size)`
- Defined: `lazyown_infinitestorage.py:159`
- Doc: Ensures the file size is within acceptable limits.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### sanitize_filename `def sanitize_filename(self, filename)`
- Defined: `lazyown_infinitestorage.py:164`
- Doc: Sanitizes a filename to remove unsafe characters.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### validate_extension `def validate_extension(self, file_path, allowed_extensions)`
- Defined: `lazyown_infinitestorage.py:172`
- Doc: Ensures the file extension is in the allowed set.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:182`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### encode_data `def encode_data(self, data)`
- Defined: `lazyown_infinitestorage.py:185`
- Doc: Encodes a byte sequence using Hamming(8,4) correction.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### decode_data `def decode_data(self, data)`
- Defined: `lazyown_infinitestorage.py:195`
- Doc: Decodes a Hamming(8,4) encoded byte sequence with single-bit error correction.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _encode_nibble `def _encode_nibble(self, nibble)`
- Defined: `lazyown_infinitestorage.py:206`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _decode_nibble `def _decode_nibble(self, byte_val)`
- Defined: `lazyown_infinitestorage.py:217`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:240`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### bits_to_frames `def bits_to_frames(self, bit_string, frame_width, frame_height, block_size)`
- Defined: `lazyown_infinitestorage.py:243`
- Doc: Yields grayscale frames from a bit string.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _create_frame `def _create_frame(self, bits, width, height, block_size, blocks_per_row)`
- Defined: `lazyown_infinitestorage.py:258`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:271`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### extract_bits_from_raw_frames `def extract_bits_from_raw_frames(self, raw_bytes, width, height, block_size, expected_bits)`
- Defined: `lazyown_infinitestorage.py:274`
- Doc: Extracts a bit string from rawvideo grayscale bytes.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:303`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### get_video_info `def get_video_info(self, input_path)`
- Defined: `lazyown_infinitestorage.py:306`
- Doc: Retrieves native resolution and metadata from a video file.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### get_metadata `def get_metadata(self, input_path)`
- Defined: `lazyown_infinitestorage.py:320`
- Doc: Extracts custom lazyown metadata from a video file using ffprobe.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### encode_video `def encode_video(self, frame_generator, output_path, frame_width, frame_height, fps)`
- Defined: `lazyown_infinitestorage.py:339`
- Doc: Encodes a generator of frames into a video file via FFmpeg stdin.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### extract_raw_frames `def extract_raw_frames(self, input_path, target_width, target_height, max_frames)`
- Defined: `lazyown_infinitestorage.py:366`
- Doc: Extracts raw grayscale frames from a video file via FFmpeg stdout.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### pack `def pack(self, data, frame_width, frame_height, block_size, fps)`
- Defined: `lazyown_infinitestorage.py:393`
- Doc: Packs raw data into a bit string.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### unpack `def unpack(self, bit_string, block_size)`
- Defined: `lazyown_infinitestorage.py:397`
- Doc: Unpacks a bit string into raw data.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:405`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### pack `def pack(self, data, frame_width, frame_height, block_size, fps)`
- Defined: `lazyown_infinitestorage.py:408`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### unpack `def unpack(self, bit_string, block_size)`
- Defined: `lazyown_infinitestorage.py:413`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config, corrector)`
- Defined: `lazyown_infinitestorage.py:430`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### pack `def pack(self, data, frame_width, frame_height, block_size, fps)`
- Defined: `lazyown_infinitestorage.py:434`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### unpack `def unpack(self, bit_string, block_size)`
- Defined: `lazyown_infinitestorage.py:453`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, config)`
- Defined: `lazyown_infinitestorage.py:484`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### create_web_runner `def create_web_runner(self)`
- Defined: `lazyown_infinitestorage.py:494`
- Doc: Return a WebRunner for WSGI or local web server use.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### encode `def encode(self, input_path, output_path, frame_width, frame_height, fps, block_size, protocol_version)`
- Defined: `lazyown_infinitestorage.py:498`
- Doc: Encodes a file into a video using the specified protocol.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### decode `def decode(self, input_path, output_path, block_size, protocol_version)`
- Defined: `lazyown_infinitestorage.py:523`
- Doc: Decodes a video back into the original file using the specified protocol.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _validate_encoding_parameters `def _validate_encoding_parameters(self, frame_width, frame_height, fps, block_size)`
- Defined: `lazyown_infinitestorage.py:534`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _detect_protocol `def _detect_protocol(self, input_path, block_size)`
- Defined: `lazyown_infinitestorage.py:544`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _decode_legacy `def _decode_legacy(self, input_path, output_path, block_size)`
- Defined: `lazyown_infinitestorage.py:577`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _decode_secure `def _decode_secure(self, input_path, output_path, block_size)`
- Defined: `lazyown_infinitestorage.py:590`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, storage)`
- Defined: `lazyown_infinitestorage.py:607`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self)`
- Defined: `lazyown_infinitestorage.py:610`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, func)`
- Defined: `lazyown_infinitestorage.py:660`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self)`
- Defined: `lazyown_infinitestorage.py:666`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, storage)`
- Defined: `lazyown_infinitestorage.py:676`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _init_ui `def _init_ui(self)`
- Defined: `lazyown_infinitestorage.py:682`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _change_mode `def _change_mode(self)`
- Defined: `lazyown_infinitestorage.py:750`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _browse_input `def _browse_input(self)`
- Defined: `lazyown_infinitestorage.py:761`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _start `def _start(self)`
- Defined: `lazyown_infinitestorage.py:771`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _on_finished `def _on_finished(self, message)`
- Defined: `lazyown_infinitestorage.py:794`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _on_error `def _on_error(self, message)`
- Defined: `lazyown_infinitestorage.py:799`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self)`
- Defined: `lazyown_infinitestorage.py:804`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, storage)`
- Defined: `lazyown_infinitestorage.py:812`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self)`
- Defined: `lazyown_infinitestorage.py:815`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, storage)`
- Defined: `lazyown_infinitestorage.py:823`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run_setup `def run_setup(self)`
- Defined: `lazyown_infinitestorage.py:834`
- Doc: Create directories and validate environment.
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _setup_routes `def _setup_routes(self)`
- Defined: `lazyown_infinitestorage.py:840`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self, host, port)`
- Defined: `lazyown_infinitestorage.py:928`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### __init__ `def __init__(self, storage)`
- Defined: `lazyown_infinitestorage.py:936`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### run `def run(self, host, port)`
- Defined: `lazyown_infinitestorage.py:939`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### _validate_upload `def _validate_upload(input_file, action)`
- Defined: `lazyown_infinitestorage.py:845`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### index `def index()`
- Defined: `lazyown_infinitestorage.py:863`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### download `def download(filename)`
- Defined: `lazyown_infinitestorage.py:908`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

### add_security_headers `def add_security_headers(response)`
- Defined: `lazyown_infinitestorage.py:916`
- Imported by: `skill_lazyown_infinitestorage/tools.py`, `tests/test_error_correction.py`, `tests/test_frames.py`, `tests/test_integration.py`, `tests/test_protocols.py`, `tests/test_security.py`, `wsgi_app.py`

## skill_lazyown_infinitestorage/tools.py

### lazyown_infinitestorage_encode `def lazyown_infinitestorage_encode(params)`
- Defined: `skill_lazyown_infinitestorage/tools.py:34`
- Doc: Encode a file into a video using LazyOwnInfiniteStorage.
- Depends on: `lazyown_infinitestorage.py`

### lazyown_infinitestorage_decode `def lazyown_infinitestorage_decode(params)`
- Defined: `skill_lazyown_infinitestorage/tools.py:101`
- Doc: Decode a video back into the original file using LazyOwnInfiniteStorage.
- Depends on: `lazyown_infinitestorage.py`

### lazyown_infinitestorage_upload_to_youtube `def lazyown_infinitestorage_upload_to_youtube(params)`
- Defined: `skill_lazyown_infinitestorage/tools.py:152`
- Doc: Upload a video to YouTube using browser automation.
- Depends on: `lazyown_infinitestorage.py`

### get_tool `def get_tool(name)`
- Defined: `skill_lazyown_infinitestorage/tools.py:302`
- Doc: Get a tool by name.
- Depends on: `lazyown_infinitestorage.py`

### list_tools `def list_tools()`
- Defined: `skill_lazyown_infinitestorage/tools.py:306`
- Doc: List all available tools.
- Depends on: `lazyown_infinitestorage.py`

## tests/test_error_correction.py

### setup `def setup(self)`
- Defined: `tests/test_error_correction.py:11`
- Depends on: `lazyown_infinitestorage.py`

### test_encode_data_doubles_length `def test_encode_data_doubles_length(self)`
- Defined: `tests/test_error_correction.py:15`
- Depends on: `lazyown_infinitestorage.py`

### test_decode_data_reverses_encoding `def test_decode_data_reverses_encoding(self)`
- Defined: `tests/test_error_correction.py:20`
- Depends on: `lazyown_infinitestorage.py`

### test_decode_data_with_single_bit_error `def test_decode_data_with_single_bit_error(self)`
- Defined: `tests/test_error_correction.py:26`
- Depends on: `lazyown_infinitestorage.py`

### test_decode_data_rejects_odd_length `def test_decode_data_rejects_odd_length(self)`
- Defined: `tests/test_error_correction.py:33`
- Depends on: `lazyown_infinitestorage.py`

### test_encode_nibble_all_values `def test_encode_nibble_all_values(self)`
- Defined: `tests/test_error_correction.py:37`
- Depends on: `lazyown_infinitestorage.py`

### test_decode_nibble_all_values `def test_decode_nibble_all_values(self)`
- Defined: `tests/test_error_correction.py:42`
- Depends on: `lazyown_infinitestorage.py`

### test_roundtrip_various_inputs `def test_roundtrip_various_inputs(self, data)`
- Defined: `tests/test_error_correction.py:49`
- Depends on: `lazyown_infinitestorage.py`

### test_single_bit_error_per_nibble `def test_single_bit_error_per_nibble(self, nibble)`
- Defined: `tests/test_error_correction.py:55`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_frames.py

### setup `def setup(self)`
- Defined: `tests/test_frames.py:12`
- Depends on: `lazyown_infinitestorage.py`

### test_bits_to_frames_yields_correct_number_of_frames `def test_bits_to_frames_yields_correct_number_of_frames(self)`
- Defined: `tests/test_frames.py:16`
- Depends on: `lazyown_infinitestorage.py`

### test_each_frame_has_correct_dimensions `def test_each_frame_has_correct_dimensions(self)`
- Defined: `tests/test_frames.py:28`
- Depends on: `lazyown_infinitestorage.py`

### test_bit_one_produces_white_block `def test_bit_one_produces_white_block(self)`
- Defined: `tests/test_frames.py:33`
- Depends on: `lazyown_infinitestorage.py`

### test_bit_zero_produces_black_block `def test_bit_zero_produces_black_block(self)`
- Defined: `tests/test_frames.py:38`
- Depends on: `lazyown_infinitestorage.py`

### test_padding_zeros_fill_incomplete_frame `def test_padding_zeros_fill_incomplete_frame(self)`
- Defined: `tests/test_frames.py:43`
- Depends on: `lazyown_infinitestorage.py`

### setup `def setup(self)`
- Defined: `tests/test_frames.py:58`
- Depends on: `lazyown_infinitestorage.py`

### test_extract_bits_from_empty_raises `def test_extract_bits_from_empty_raises(self)`
- Defined: `tests/test_frames.py:62`
- Depends on: `lazyown_infinitestorage.py`

### test_extract_bits_from_raw_frames_basic `def test_extract_bits_from_raw_frames_basic(self)`
- Defined: `tests/test_frames.py:66`
- Depends on: `lazyown_infinitestorage.py`

### test_extract_bits_respects_expected_bits `def test_extract_bits_respects_expected_bits(self)`
- Defined: `tests/test_frames.py:74`
- Depends on: `lazyown_infinitestorage.py`

### test_extract_bits_from_resized_frame `def test_extract_bits_from_resized_frame(self)`
- Defined: `tests/test_frames.py:82`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_integration.py

### setup `def setup(self)`
- Defined: `tests/test_integration.py:22`
- Depends on: `lazyown_infinitestorage.py`

### test_secure_protocol_roundtrip `def test_secure_protocol_roundtrip(self)`
- Defined: `tests/test_integration.py:26`
- Depends on: `lazyown_infinitestorage.py`

### test_legacy_protocol_roundtrip `def test_legacy_protocol_roundtrip(self)`
- Defined: `tests/test_integration.py:44`
- Depends on: `lazyown_infinitestorage.py`

### test_secure_protocol_resilient_to_resolution_change `def test_secure_protocol_resilient_to_resolution_change(self)`
- Defined: `tests/test_integration.py:62`
- Depends on: `lazyown_infinitestorage.py`

### test_protocol_auto_detection_prefers_secure `def test_protocol_auto_detection_prefers_secure(self)`
- Defined: `tests/test_integration.py:83`
- Depends on: `lazyown_infinitestorage.py`

### test_empty_file_roundtrip `def test_empty_file_roundtrip(self)`
- Defined: `tests/test_integration.py:96`
- Depends on: `lazyown_infinitestorage.py`

### test_large_file_roundtrip `def test_large_file_roundtrip(self)`
- Defined: `tests/test_integration.py:110`
- Depends on: `lazyown_infinitestorage.py`

### setup `def setup(self)`
- Defined: `tests/test_integration.py:135`
- Depends on: `lazyown_infinitestorage.py`

### test_index_get `def test_index_get(self)`
- Defined: `tests/test_integration.py:142`
- Depends on: `lazyown_infinitestorage.py`

### test_encode_upload `def test_encode_upload(self)`
- Defined: `tests/test_integration.py:147`
- Depends on: `lazyown_infinitestorage.py`

### test_decode_upload `def test_decode_upload(self)`
- Defined: `tests/test_integration.py:167`
- Depends on: `lazyown_infinitestorage.py`

### test_security_headers_present `def test_security_headers_present(self)`
- Defined: `tests/test_integration.py:193`
- Depends on: `lazyown_infinitestorage.py`

### test_download_not_found `def test_download_not_found(self)`
- Defined: `tests/test_integration.py:199`
- Depends on: `lazyown_infinitestorage.py`

### test_missing_file_error `def test_missing_file_error(self)`
- Defined: `tests/test_integration.py:203`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_protocols.py

### setup `def setup(self)`
- Defined: `tests/test_protocols.py:11`
- Depends on: `lazyown_infinitestorage.py`

### test_pack_includes_end_marker `def test_pack_includes_end_marker(self)`
- Defined: `tests/test_protocols.py:15`
- Depends on: `lazyown_infinitestorage.py`

### test_unpack_strips_end_marker `def test_unpack_strips_end_marker(self)`
- Defined: `tests/test_protocols.py:21`
- Depends on: `lazyown_infinitestorage.py`

### test_unpack_with_trailing_zeros `def test_unpack_with_trailing_zeros(self)`
- Defined: `tests/test_protocols.py:27`
- Depends on: `lazyown_infinitestorage.py`

### setup `def setup(self)`
- Defined: `tests/test_protocols.py:39`
- Depends on: `lazyown_infinitestorage.py`

### test_pack_produces_bit_string `def test_pack_produces_bit_string(self)`
- Defined: `tests/test_protocols.py:44`
- Depends on: `lazyown_infinitestorage.py`

### test_unpack_recovers_original_data `def test_unpack_recovers_original_data(self)`
- Defined: `tests/test_protocols.py:49`
- Depends on: `lazyown_infinitestorage.py`

### test_unpack_detects_corrupted_header `def test_unpack_detects_corrupted_header(self)`
- Defined: `tests/test_protocols.py:55`
- Depends on: `lazyown_infinitestorage.py`

### test_unpack_detects_corrupted_payload `def test_unpack_detects_corrupted_payload(self)`
- Defined: `tests/test_protocols.py:66`
- Depends on: `lazyown_infinitestorage.py`

### test_roundtrip_various_sizes `def test_roundtrip_various_sizes(self, size)`
- Defined: `tests/test_protocols.py:80`
- Depends on: `lazyown_infinitestorage.py`

## tests/test_security.py

### test_magic_bytes_are_valid `def test_magic_bytes_are_valid(self)`
- Defined: `tests/test_security.py:12`
- Depends on: `lazyown_infinitestorage.py`

### test_protocol_versions_are_distinct `def test_protocol_versions_are_distinct(self)`
- Defined: `tests/test_security.py:15`
- Depends on: `lazyown_infinitestorage.py`

### test_default_values_within_bounds `def test_default_values_within_bounds(self)`
- Defined: `tests/test_security.py:18`
- Depends on: `lazyown_infinitestorage.py`

### test_header_offsets_are_consistent `def test_header_offsets_are_consistent(self)`
- Defined: `tests/test_security.py:24`
- Depends on: `lazyown_infinitestorage.py`

### test_max_file_size_is_reasonable `def test_max_file_size_is_reasonable(self)`
- Defined: `tests/test_security.py:31`
- Depends on: `lazyown_infinitestorage.py`

### setup `def setup(self)`
- Defined: `tests/test_security.py:41`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_file_path_resolves_absolute `def test_validate_file_path_resolves_absolute(self)`
- Defined: `tests/test_security.py:45`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_file_path_rejects_traversal `def test_validate_file_path_rejects_traversal(self)`
- Defined: `tests/test_security.py:50`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_file_path_must_exist_when_required `def test_validate_file_path_must_exist_when_required(self)`
- Defined: `tests/test_security.py:54`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_size_rejects_oversized_files `def test_validate_size_rejects_oversized_files(self)`
- Defined: `tests/test_security.py:58`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_size_accepts_maximum `def test_validate_size_accepts_maximum(self)`
- Defined: `tests/test_security.py:62`
- Depends on: `lazyown_infinitestorage.py`

### test_sanitize_filename_strips_unsafe_characters `def test_sanitize_filename_strips_unsafe_characters(self)`
- Defined: `tests/test_security.py:65`
- Depends on: `lazyown_infinitestorage.py`

### test_sanitize_filename_preserves_safe_characters `def test_sanitize_filename_preserves_safe_characters(self)`
- Defined: `tests/test_security.py:70`
- Depends on: `lazyown_infinitestorage.py`

### test_sanitize_filename_fallback `def test_sanitize_filename_fallback(self)`
- Defined: `tests/test_security.py:74`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_extension_accepts_allowed `def test_validate_extension_accepts_allowed(self)`
- Defined: `tests/test_security.py:77`
- Depends on: `lazyown_infinitestorage.py`

### test_validate_extension_rejects_disallowed `def test_validate_extension_rejects_disallowed(self)`
- Defined: `tests/test_security.py:81`
- Depends on: `lazyown_infinitestorage.py`

## wsgi_app.py

### get_wsgi_app `def get_wsgi_app()`
- Defined: `wsgi_app.py:7`
- Doc: Factory function returning a gunicorn-compatible Flask application.
- Depends on: `lazyown_infinitestorage.py`
