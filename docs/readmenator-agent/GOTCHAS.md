# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `lazyown_infinitestorage.py` (score: 21.80, imported by 7 files)
- `skill_lazyown_infinitestorage/tools.py` (score: 2.50)
- `wsgi_app.py` (score: 2.10)
- `install.sh` (score: 0.00)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `lazyown_infinitestorage.py` -- 7 direct, 7 total dependents

## Hotspots (complexity + centrality)

- `lazyown_infinitestorage.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0
- `skill_lazyown_infinitestorage/tools.py` -- complexity: 0.1, centrality: 0.5, combined: 0.3
- `wsgi_app.py` -- complexity: 0.0, centrality: 0.1, combined: 0.1
- `install.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0

## Layer Violations

- `tests/test_error_correction.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_frames.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_integration.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_protocols.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
- `tests/test_security.py` (testing) -> `lazyown_infinitestorage.py` (presentation): testing must not import presentation
