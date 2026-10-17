```mermaid
graph LR
    root["root"]
    click root href "./root.md" "Details"
```

## Details

Static architecture map of 9 files (py, sh) in 1 components: root. Structure is extracted statically without LLM calls; component prose may be enriched locally.

### root (1)

root groups 8 files (py) around LazyOwnConfig, SecurityValidator, __init__, validate_file_path, validate_size. LazyOwnInfiniteStorage - Production-grade file-to-video encoder/decoder.

**Related Classes/Methods**:

- <a href="../lazyown_infinitestorage.py#L71-L147">lazyown_infinitestorage.py::LazyOwnConfig</a>
- <a href="../lazyown_infinitestorage.py#L148-L150">lazyown_infinitestorage.py::SecurityValidator</a>
- <a href="../lazyown_infinitestorage.py#L151-L153">lazyown_infinitestorage.py::__init__</a>
- <a href="../lazyown_infinitestorage.py#L154-L163">lazyown_infinitestorage.py::validate_file_path</a>
- <a href="../lazyown_infinitestorage.py#L164-L168">lazyown_infinitestorage.py::validate_size</a>
- <a href="../lazyown_infinitestorage.py#L169-L176">lazyown_infinitestorage.py::sanitize_filename</a>
- <a href="../lazyown_infinitestorage.py#L177-L183">lazyown_infinitestorage.py::validate_extension</a>
- <a href="../lazyown_infinitestorage.py#L184-L186">lazyown_infinitestorage.py::ErrorCorrector</a>
