# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `lazyown_infinitestorage.py` (score: 21.80)
- `tests/test_security.py` (score: 3.80)
- `tests/test_integration.py` (score: 3.60)
- `tests/test_frames.py` (score: 3.30)
- `tests/test_protocols.py` (score: 3.20)
- `tests/test_error_correction.py` (score: 3.00)
- `skill_lazyown_infinitestorage/tools.py` (score: 2.50)
- `wsgi_app.py` (score: 2.10)
- `install.sh` (score: 0.00)

## Hotspots (complexity + centrality)

- `lazyown_infinitestorage.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0
- `tests/test_integration.py` -- complexity: 0.2, centrality: 0.4, combined: 0.3
- `skill_lazyown_infinitestorage/tools.py` -- complexity: 0.1, centrality: 0.5, combined: 0.3
- `tests/test_security.py` -- complexity: 0.2, centrality: 0.2, combined: 0.2
- `tests/test_frames.py` -- complexity: 0.2, centrality: 0.2, combined: 0.2
- `tests/test_protocols.py` -- complexity: 0.2, centrality: 0.1, combined: 0.1
- `tests/test_error_correction.py` -- complexity: 0.1, centrality: 0.1, combined: 0.1
- `wsgi_app.py` -- complexity: 0.0, centrality: 0.1, combined: 0.1
- `install.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0

## Layer Violations

- `tests/test_error_correction.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_frames.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_integration.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_protocols.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_security.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
