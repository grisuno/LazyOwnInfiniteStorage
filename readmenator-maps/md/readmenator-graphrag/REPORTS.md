# GraphRAG Community Reports

Entities: 240 | Relationships: 590 | Communities: 2 | Themes: 0 | Text units: 163

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

9 files in 2 communities. Highest-impact communities: root (7.0), unassigned files (0.5). God nodes: lazyown_infinitestorage.py, tests/test_security.py, tests/test_integration.py, tests/test_frames.py, tests/test_protocols.py.

- [root] rating 7.0: `lazyown_infinitestorage.py` ranks 1 by PageRank, 7 importers, 79 symbols: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.
- [unassigned files] rating 0.5: `install.sh` ranks 1 by PageRank, 0 importers, 0 symbols: Verificar si Python está instalado
- Key entities: file:lazyown_infinitestorage.py, file:tests/test_integration.py, file:install.sh
- Children: c0, c1
- Root rating = highest community rating.

## root (`c0`, community, rating 7.0)

8 files under tests (py 8), mostly testing. Core file lazyown_infinitestorage.py (PageRank 0.4649, imported by 7 files): LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder. Key abstractions: LazyOwnConfig, SecurityValidator, ErrorCorrector, FrameEncoder, FrameDecoder, FFmpegPipeline.

- `lazyown_infinitestorage.py` ranks 1 by PageRank, 7 importers, 79 symbols: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.
- `skill_lazyown_infinitestorage/tools.py` ranks 2 by PageRank, 0 importers, 5 symbols: MCP tools for LazyOwnInfiniteStorage integration.
- `tests/test_error_correction.py` ranks 3 by PageRank, 0 importers, 10 symbols: Unit tests for ErrorCorrector Hamming(8,4) implementation.
- Hotspot `lazyown_infinitestorage.py`: 79 symbols, 26 connections (score 1.00).
- Hotspot `tests/test_integration.py`: 16 symbols, 10 connections (score 0.31).
- 5 layer violations, e.g. test_error_correction.py (testing) -> lazyown_infinitestorage.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Key entities: file:lazyown_infinitestorage.py, file:tests/test_integration.py, file:tests/test_security.py, file:skill_lazyown_infinitestorage/tools.py, file:tests/test_protocols.py, file:tests/test_frames.py, file:tests/test_error_correction.py, sym:lazyown_infinitestorage.py::encode@525
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 7.

## unassigned files (`c1`, community, rating 0.5)

1 files under root (sh 1), mostly utility. Core file install.sh (PageRank 0.0669, imported by 0 files): Verificar si Python está instalado

- `install.sh` ranks 1 by PageRank, 0 importers, 0 symbols: Verificar si Python está instalado
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:install.sh
- Rating 0.5/10 = 7 x PageRank share 0.07 + 3 x risk 0.00. Internal imports: 0.
