```sh
 ▄█          ▄████████  ▄███████▄  ▄██   ▄    ▄██████▄   ▄█     █▄  ███▄▄▄▄
 ███         ███    ███ ██▀     ▄██ ███   ██▄ ███    ███ ███     ███ ███▀▀▀██▄
 ███         ███    ███       ▄███▀ ███▄▄▄███ ███    ███ ███     ███ ███   ███
 ███         ███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███ ███    ███ ███     ███ ███   ███
 ███       ▀███████████   ▄███▀   ▀ ▄██   ███ ███    ███ ███     ███ ███   ███
 ███         ███    ███ ▄███▀       ███   ███ ███    ███ ███     ███ ███   ███
 ███▌    ▄   ███    ███ ███▄     ▄█ ███   ███ ███    ███ ███ ▄█▄ ███ ███   ███
 █████▄▄██   ███    █▀   ▀████████▀  ▀█████▀   ▀██████▀   ▀███▀███▀   ▀█   █▀
  ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█      ███        ▄████████
 ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███  ▀█████████▄   ███    ███
 ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌    ▀███▀▀██   ███    █▀
 ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌     ███   ▀  ▄███▄▄▄
 ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌     ███     ▀▀███▀▀▀
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    █▄
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    ███
 █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀      ▄████▀     ██████████
    ▄████████     ███      ▄██████▄     ▄████████    ▄████████    ▄██████▄     ▄████████
   ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
   ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███   ███    █▀    ███    █▀
   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███  ▄███         ▄███▄▄▄
 ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀
          ███     ███     ███    ███ ▀███████████   ███    ███   ███    ███   ███    █▄
    ▄█    ███     ███     ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
  ▄████████▀     ▄████▀    ▀██████▀    ███    ███   ███    █▀    ████████▀    ██████████
```

# LazyOwnInfiniteStorage

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

LazyOwnInfiniteStorage is a production-grade tool for encoding and decoding files into videos. This project stores data in videos by creating grayscale frames that represent data bits, enabling recovery of the original information even after the video resolution has been modified.

Resulting in a video like this:

![image](https://github.com/grisuno/LazyOwnInfiniteStorage/assets/1097185/39044629-7e0c-4806-806a-9bbc5a847d88)

## Features

- **Dual Protocol Support:**
  - **Legacy (v1):** Original encoding with end-marker and filename-based resolution recovery.
  - **Secure (v2):** Structured binary header with CRC32 integrity checks and Hamming(8,4) error correction for robust decoding.
- Encode any file into a video using configurable pixel blocks.
- Decode files from videos even after resolution changes.
- Single-file, self-contained Python script with CLI, GUI, and Web interfaces.
- Vectorized NumPy frame processing for performance.
- Direct FFmpeg stdin/stdout piping without intermediate frame files.
- Security-hardened input validation and path sanitization.

## Requirements

- Python 3.8+
- OpenCV (opencv-python)
- NumPy
- FFmpeg

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/grisuno/LazyOwnInfiniteStorage.git
    cd LazyOwnInfiniteStorage
    ```

2. Create a virtual environment and install dependencies:

    ```sh
    python3 -m venv env
    source env/bin/activate
    pip install opencv-python numpy
    ```

3. Ensure FFmpeg is installed on your system.

## Usage

LazyOwnInfiniteStorage is provided as a single autocontained script.

### Command Line Interface (CLI)

#### Encoding

To encode a file into a video using the secure protocol (recommended):

```sh
python lazyown_infinitestorage.py --mode encode --input file.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4 --protocol secure
```

To use the legacy protocol:

```sh
python lazyown_infinitestorage.py --mode encode --input file.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4 --protocol legacy
```

#### Decoding

To decode a file from a video:

```sh
python lazyown_infinitestorage.py --mode decode --input video_640x480.mp4 --output recoveredfile.zip --block_size 4 --protocol secure
```

#### Built-in Tests

Run the integrated test suite to verify both protocols including resize scenarios:

```sh
python lazyown_infinitestorage.py --mode test
```

### Graphical User Interface (GUI)

Launch the PyQt5-based GUI:

```sh
python lazyown_infinitestorage.py --gui
```

Requires PyQt5 to be installed:

```sh
pip install PyQt5
```

### Web Interface

Start the Flask web server:

```sh
python lazyown_infinitestorage.py --serve --host 0.0.0.0 --port 5000
```

Requires Flask to be installed:

```sh
pip install Flask
```

## Protocols

### Legacy Protocol (v1)

- Uses an end-of-file marker (`0x80`) to determine payload boundaries.
- Stores the original frame resolution in the output filename.
- Compatible with the original LazyOwnInfiniteStorage workflow.

### Secure Protocol (v2)

- Binary header (`LAZY` magic, version, original file size, width, height, block size, FPS).
- Header and payload protected by CRC32 checksums.
- Full payload protected by Hamming(8,4) extended error correction, capable of correcting single-bit errors per byte.
- Resolution is recovered from the filename or video metadata.

## Security

- Path traversal prevention on all file operations.
- Filename sanitization to remove unsafe characters.
- Maximum file size limits to prevent abuse.
- Web mode includes security headers (HSTS, X-Frame-Options, X-Content-Type-Options, XSS protection).
- `MAX_CONTENT_LENGTH` enforced on web uploads.

## Contributions

Contributions are welcome. If you find any issues or have improvements, feel free to open an issue or a pull request.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)

## Acknowledgments

This project is inspired by the work of DvorakDwarf on Infinite-Storage-Glitch. Any code criticism to help improve is appreciated.

Do whatever you want with the code, but credit would be appreciated. If you have any issues with LazyOwnInfiniteStorage, please contact me on Discord.

## Created by grisuno
