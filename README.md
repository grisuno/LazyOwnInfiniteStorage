# LazyOwnInfiniteStorage

Production-grade tool for encoding any file into a video and decoding it back with full data recovery, even after video resolution changes.

Inspired by the concept of DvorakDwarf's Infinite-Storage-Glitch, this implementation provides a hardened, tested, and self-contained Python utility with CLI, optional GUI, and optional web interfaces.

## Architecture

The project follows a strict single-file-per-contract pattern:

- `lazyown_infinitestorage.py` -- Core library, CLI runner, WebRunner, GUIRunner (self-contained)
- `wsgi_app.py` -- WSGI entry point for gunicorn and production web servers
- `tests/` -- Comprehensive BDD/TDD pytest suite
- `templates/index.html` -- Web interface template
- `static/css/` -- Theme stylesheets
- `render.yaml` -- Render.com deployment configuration

## Features

- Dual protocol support:
  - Legacy v1: end-of-file marker with filename-based resolution recovery
  - Secure v2: structured binary header with CRC32 integrity checks and Hamming(8,4) single-bit error correction
- Encode any file into a video using configurable pixel blocks
- Decode files from videos even after resolution changes
- Vectorized NumPy frame processing for performance
- Direct FFmpeg stdin/stdout piping without intermediate frame files
- Centralized configuration via `LazyOwnConfig`
- Security-hardened input validation and path sanitization
- Flask web server with security headers, CSRF protection, file extension validation, and size limits
- PyQt5 graphical user interface with background worker threads

## Requirements

- Python 3.8+
- FFmpeg
- NumPy
- OpenCV (opencv-python or opencv-python-headless)
- Flask (optional, for web interface)
- PyQt5 (optional, for GUI)
- gunicorn (optional, for production web server)

Install core dependencies:

```bash
pip install numpy opencv-python-headless
```

Install optional dependencies:

```bash
pip install flask werkzeug pyqt5 gunicorn
```

## Usage

### Command Line

Encode a file using the secure protocol:

```bash
python lazyown_infinitestorage.py --mode encode --input file.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4 --protocol secure
```

Decode a file from a video:

```bash
python lazyown_infinitestorage.py --mode decode --input video_640x480.mp4 --output recovered.zip --block_size 4 --protocol secure
```

Run the built-in test suite:

```bash
python lazyown_infinitestorage.py --mode test
```

Launch the GUI (does not require --mode):

```bash
python lazyown_infinitestorage.py --gui
```

Launch the web server (does not require --mode):

```bash
python lazyown_infinitestorage.py --serve --host 0.0.0.0 --port 5000
```

### Web Server (Production)

For production deployment with gunicorn:

```bash
gunicorn wsgi_app:app
```

## Protocols

### Legacy v1

- Uses an end-of-file marker (`0x80`) to determine payload boundaries
- Stores the original frame resolution in the output filename
- Compatible with the original Infinite-Storage-Glitch workflow

### Secure v2

- Binary header (`LAZY` magic, version, original file size, width, height, block size, FPS)
- Header and payload protected by CRC32 checksums
- Full payload protected by Hamming(8,4) extended error correction, capable of correcting single-bit errors per byte
- Resolution is recovered from the filename or video metadata

## Security

- Path traversal prevention on all file operations via `SecurityValidator`
- Filename sanitization using an allowlist regex (`[^a-zA-Z0-9_\-\.]`)
- Maximum file size limits enforced at config, validator, and web layers
- Web mode includes security headers (HSTS, X-Frame-Options, X-Content-Type-Options, XSS protection)
- `MAX_CONTENT_LENGTH` enforced on web uploads
- File extension validation on encode and decode operations
- Upload directory isolation with tempfile-based processing

## Testing

Run the full test suite with pytest:

```bash
pytest tests/ -v
```

The test suite covers:
- Configuration validation
- Security validator (path traversal, sanitization, size limits, extension checks)
- Hamming(8,4) error correction (encode/decode, single-bit error correction)
- Frame encoding and decoding
- Protocol handlers (Legacy and Secure)
- Full encode/decode roundtrip including resize scenarios
- Flask web interface routes, uploads, downloads, and security headers

## Deployment

The project includes a `render.yaml` for Render.com deployment:

```yaml
services:
  - type: web
    name: lazyowninfinitestorage
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn wsgi_app:app"
```

## License

GNU General Public License v3.0

## Acknowledgments

Inspired by DvorakDwarf's Infinite-Storage-Glitch concept. Credited in the code and documentation as the original idea source.

## Contributing

See CONTRIBUTING.md for guidelines.


---
### Grisuno Offensive Security Ecosystem
This tool is part of a broader, synergistic RedTeam workflow:
- [LazyOwn](https://github.com/grisuno/LazyOwn): RedTeam/APT framework with AI-powered C&C, rootkits and malleable implants (Windows/Linux/Mac).
- [LazyOwnBT](https://github.com/grisuno/LazyOwnBT): Advanced complementary toolkit for BlueTeam professionals.
- [Lazymapd](https://github.com/grisuno/Lazymapd): Fast, customizable port scanner for firewall evasion.

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity

AI agents: Read `readmenator-agent/INDEX.md` for fast project context.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

