# LazyOwnInfiniteStorage -- Engineering Contract

This document serves as the authoritative engineering contract for the LazyOwnInfiniteStorage project. It records architectural decisions, coding standards, security requirements, and the SDD/TDD/BDD methodology applied during development.

## Methodology

### SDD (Specification-Driven Development)

Every component has a formal specification captured in docstrings and enforced through type hints. The specification states the contract of each class and method: inputs, outputs, invariants, and failure modes.

### TDD (Test-Driven Development)

All functionality is covered by pytest tests written before or alongside the code. The test suite runs in CI and must pass at 100% before any merge.

### BDD (Behavior-Driven Development)

Test names follow the pattern `test_<behavior>_<condition>` and are grouped into specification classes. Each test class documents the expected behavior of the system under test.

### Boy Scout Mode

All technical debt and security issues discovered during development were fixed immediately, regardless of scope. This includes:
- Removing broken duplicate files (`app.py`, `gui.py`)
- Fixing path traversal vulnerability in `SecurityValidator.validate_file_path`
- Fixing filename sanitization regex missing digit `9`
- Removing third-party tracking scripts (Google Analytics, Ko-fi widgets)
- Replacing deprecated `Flask-Bootstrap` with vanilla Bootstrap CDN
- Adding explicit template and static folder paths to Flask

## Architecture

### Single File Per Contract

- `lazyown_infinitestorage.py` -- Core library contract. Contains all business logic: config, security, error correction, frame encoding/decoding, FFmpeg pipeline, protocol handlers, and the main orchestrator. Also embeds CLI, WebRunner, and GUIRunner for self-contained deployment.
- `wsgi_app.py` -- WSGI contract. Thin factory that creates a Flask application from the core library for gunicorn.
- `tests/*.py` -- Test contracts. Each test file covers one domain: security, error correction, frames, protocols, integration.

### Configuration Centralization

All constants are centralized in `LazyOwnConfig`. No magic numbers exist in the code. All bounds, sizes, offsets, and choices are declared as class attributes. The config class is immutable by convention (no setters).

### Security Model

- `SecurityValidator` is the single source of truth for all security checks
- Path traversal: checked before `abspath` resolution
- Filename sanitization: allowlist regex `[^a-zA-Z0-9_\-\.]`
- Size limits: checked at config, validator, and web layers
- Extension validation: checked before any file operation
- Web upload isolation: all uploads processed in temporary directories

### Error Correction

- `ErrorCorrector` implements Hamming(8,4) extended code
- Single-bit error correction per nibble
- All header and payload bytes are doubled in size for protection
- CRC32 is applied to both header and payload independently

## Coding Standards

- English language throughout codebase and documentation
- No emojis in code or documentation
- Docstrings on every class and public method
- Type hints on all method signatures
- DRY principle: shared logic extracted into private methods
- SOLID principles: single responsibility per class, dependency injection via config
- No placeholders, no TODOs, no FIXMEs in production code
- No hardcoded paths; all paths derived from config or environment variables
- No absolute system paths; everything is relative to project root or temp directories

## Security Checklist

- Path traversal prevention: validated and tested
- Filename sanitization: allowlist regex, validated and tested
- File size limits: enforced at multiple layers, tested
- File extension validation: enforced on encode and decode, tested
- Secret key: sourced from environment variable with cryptographically secure fallback
- Security headers: HSTS, X-Frame-Options, X-Content-Type-Options, XSS protection, cache disable
- Upload isolation: tempfile-based processing with automatic cleanup
- No third-party tracking or external widgets in web interface

## Test Coverage

- 73 tests covering all major components
- Unit tests for config, security, error correction, frames, protocols
- Integration tests for full encode/decode roundtrip including resize scenarios
- Web interface tests for routes, uploads, downloads, and security headers
- All tests pass in under 5 seconds on standard hardware

## Deployment Contract

- `render.yaml` specifies the Render.com deployment
- `wsgi_app.py` provides a gunicorn-compatible Flask application
- `requirements.txt` lists all dependencies with minimum versions
- No system-specific installation scripts; environment setup is documented in README.md

## Maintenance

- All changes must pass the full test suite
- Security issues are always in scope and must be fixed immediately
- Technical debt discovered during any change must be resolved as part of that change
- Documentation (README.md, CLAUDE.md) must be updated with any architectural change
- This contract is version-controlled and changes require review
