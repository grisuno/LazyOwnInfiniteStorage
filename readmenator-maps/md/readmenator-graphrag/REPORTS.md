# GraphRAG Community Reports

Entities: 287 | Relationships: 748 | Communities: 2 | Themes: 0 | Text units: 205

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

11 files in 2 communities. Highest-impact communities: root (7.0), unassigned files (0.4). God nodes: lazyown_infinitestorage.py, tests/test_security.py, tests/test_integration.py, tests/test_zip.py, mcp_server.py.

- [root] rating 7.0: `lazyown_infinitestorage.py` ranks 1 by PageRank, 9 importers, 84 symbols: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.
- [unassigned files] rating 0.4: `install.sh` ranks 1 by PageRank, 0 importers, 0 symbols: Verificar si Python está instalado
- Key entities: file:lazyown_infinitestorage.py, file:tests/test_integration.py, file:install.sh
- Children: c0, c1
- Root rating = highest community rating.

## root (`c0`, community, rating 7.0)

10 files under tests (py 10), mostly testing. Core file lazyown_infinitestorage.py (PageRank 0.4638, imported by 9 files): LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder. Key abstractions: LazyOwnConfig, SecurityValidator, ErrorCorrector, FrameEncoder, FrameDecoder, FFmpegPipeline.

- `lazyown_infinitestorage.py` ranks 1 by PageRank, 9 importers, 84 symbols: LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.
- `mcp_server.py` ranks 2 by PageRank, 0 importers, 13 symbols: Model Context Protocol server for LazyOwnInfiniteStorage.
- `skill_lazyown_infinitestorage/tools.py` ranks 3 by PageRank, 0 importers, 11 symbols: MCP tools for LazyOwnInfiniteStorage integration.
- Hotspot `lazyown_infinitestorage.py`: 84 symbols, 29 connections (score 1.00).
- Hotspot `skill_lazyown_infinitestorage/tools.py`: 11 symbols, 12 connections (score 0.30).
- 6 layer violations, e.g. test_error_correction.py (testing) -> lazyown_infinitestorage.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Key entities: file:lazyown_infinitestorage.py, file:tests/test_integration.py, file:tests/test_zip.py, file:skill_lazyown_infinitestorage/tools.py, file:tests/test_security.py, file:mcp_server.py, file:tests/test_protocols.py, sym:lazyown_infinitestorage.py::encode@544
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 9.

## unassigned files (`c1`, community, rating 0.4)

1 files under root (sh 1), mostly utility. Core file install.sh (PageRank 0.0536, imported by 0 files): Verificar si Python está instalado

- `install.sh` ranks 1 by PageRank, 0 importers, 0 symbols: Verificar si Python está instalado
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:install.sh
- Rating 0.4/10 = 7 x PageRank share 0.06 + 3 x risk 0.00. Internal imports: 0.
