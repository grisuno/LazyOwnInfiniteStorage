# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 11 files at commit `d4b6ed81f514`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: Production-grade tool for encoding any file into a video and decoding it back with full data recovery, even after video resolution changes. (`README.md:3`)
- Domain vocabulary (term, files): `setup` (7), `protocol` (6), `bit` (6), `lazy` (6), `own` (6), `encode` (6), `specification` (6), `video` (5), `decode` (5), `extract` (5), `infinite` (5), `storage` (5), `files` (5), `zip` (4), `file` (4)
- Subsystem `root`: 10 files, core `lazyown_infinitestorage.py`: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.
- Business rules that the code cannot show live in section 7: record them there.

## 2. Workflow

Detected commands:
- `python -m pytest -q` (tests/ layout)

Session protocol:
1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).
2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask "<question>"` (local = entities + sources, `--global` = community reports).
3. Before editing a file: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md`.
4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.
5. End: record decisions, business rules, and gotchas with `readmenator . remember "<note>" --kind decision`.

## 3. Rules and constraints

Declared:
- Removing broken duplicate files (`app.py`, `gui.py`) (`CLAUDE.md:22`)
- Fixing path traversal vulnerability in `SecurityValidator.validate_file_path` (`CLAUDE.md:23`)
- Fixing filename sanitization regex missing digit `9` (`CLAUDE.md:24`)
- Removing third-party tracking scripts (Google Analytics, Ko-fi widgets) (`CLAUDE.md:25`)
- Replacing deprecated `Flask-Bootstrap` with vanilla Bootstrap CDN (`CLAUDE.md:26`)
- Adding explicit template and static folder paths to Flask (`CLAUDE.md:27`)
- `SecurityValidator` is the single source of truth for all security checks (`CLAUDE.md:43`)
- Path traversal: checked before `abspath` resolution (`CLAUDE.md:44`)
- Filename sanitization: allowlist regex `[^a-zA-Z0-9_\-\.]` (`CLAUDE.md:45`)
- Size limits: checked at config, validator, and web layers (`CLAUDE.md:46`)
- Extension validation: checked before any file operation (`CLAUDE.md:47`)
- Web upload isolation: all uploads processed in temporary directories (`CLAUDE.md:48`)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 0; layer violations: 6 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- Following the project's naming and style conventions. (`CONTRIBUTING.md:48`)
- Making sure your code is properly indented and formatted. (`CONTRIBUTING.md:49`)
- Adding comments where necessary to explain your code logic. (`CONTRIBUTING.md:50`)

Measured baseline:
- py: 10 files, 194 symbols; docstrings on 34% of symbols; functions snake_case (100%); types PascalCase (100%); median file 131 lines, max 1129.
- sh: 1 files, 0 symbols; median file 37 lines, max 37.
- Tests: 6 files under tests; follow the existing naming (e.g. `test_error_correction.py`).

## 5. Minimum deliverables

Declared:
- Path traversal prevention: validated and tested (`CLAUDE.md:71`)
- Filename sanitization: allowlist regex, validated and tested (`CLAUDE.md:72`)
- File size limits: enforced at multiple layers, tested (`CLAUDE.md:73`)
- File extension validation: enforced on encode and decode, tested (`CLAUDE.md:74`)
- Secret key: sourced from environment variable with cryptographically secure fallback (`CLAUDE.md:75`)
- Security headers: HSTS, X-Frame-Options, X-Content-Type-Options, XSS protection, cache disable (`CLAUDE.md:76`)
- Upload isolation: tempfile-based processing with automatic cleanup (`CLAUDE.md:77`)
- No third-party tracking or external widgets in web interface (`CLAUDE.md:78`)
- 73 tests covering all major components (`CLAUDE.md:82`)
- Unit tests for config, security, error correction, frames, protocols (`CLAUDE.md:83`)
- Integration tests for full encode/decode roundtrip including resize scenarios (`CLAUDE.md:84`)
- Web interface tests for routes, uploads, downloads, and security headers (`CLAUDE.md:85`)
- All tests pass in under 5 seconds on standard hardware (`CLAUDE.md:86`)
- **Fork the repository** and clone your fork locally. (`CONTRIBUTING.md:15`)
- **Create a branch for your contribution**. Use a descriptive name for your branch. (`CONTRIBUTING.md:22`)
- **Make your changes**. Make sure your code follows the project style and that you have added the necessary tests. (`CONTRIBUTING.md:28`)
- **Commit your changes**. Make sure to write a clear and descriptive commit message. (`CONTRIBUTING.md:30`)
- **Push your changes to your fork**. (`CONTRIBUTING.md:36`)
- **Open a pull request**. Go to the original repository on GitHub and open a pull request from your fork. Describe the changes you have made and why they are useful. (`CONTRIBUTING.md:42`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 34%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `lazyown_infinitestorage.py`, `tests/test_security.py`, `tests/test_integration.py`, `tests/test_zip.py`, `mcp_server.py`
- Hotspots (complex and central): `lazyown_infinitestorage.py`, `skill_lazyown_infinitestorage/tools.py`, `tests/test_integration.py`, `mcp_server.py`, `tests/test_zip.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
