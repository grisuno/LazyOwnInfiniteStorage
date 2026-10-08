# Second Brain

*Last synthesized: 2026-10-07 | 9 files | 2 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `lazyown_infinitestorage.py`, `test_security.py`, `test_integration.py`. Architecturally it is 3 layers, dominant testing (5 files) across 2 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Communities are self-contained in the resolved import graph; no cross-boundary bridges were recorded.

Open work clusters around documentation (100% file coverage), 0 security findings, 5 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 9 |
| Symbols | 153 |
| Resolved imports | 7 |
| Languages | py, sh |
| Communities | 2 |
| Doc coverage | 100% (9/9 files) |
| Security findings | 0 |
| Estimated read cost | ~2182 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_LazyOwnInfiniteStorage__2kif1pi
```

## Concept Wiki

- [root (8 files, cohesion 1.00)](./community_0_root.md)
- [orphans (1 files, cohesion 0.00)](./community_1_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `lazyown_infinitestorage.py` | 21.8 |
| `tests/test_security.py` | 3.8 |
| `tests/test_integration.py` | 3.6 |
| `tests/test_frames.py` | 3.3 |
| `tests/test_protocols.py` | 3.2 |

## Strongest Connections

- No cross-community connections recorded.

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
