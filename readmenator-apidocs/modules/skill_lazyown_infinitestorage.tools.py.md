# `skill_lazyown_infinitestorage.tools`

> Source: [skill_lazyown_infinitestorage/tools.py:1](../../skill_lazyown_infinitestorage/tools.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

MCP tools for LazyOwnInfiniteStorage integration.

## Contents

- **Functions:** [`lazyown_infinitestorage_encode`](#lazyown_infinitestorage_encode), [`lazyown_infinitestorage_decode`](#lazyown_infinitestorage_decode), [`lazyown_zip_to_video`](#lazyown_zip_to_video), [`lazyown_video_to_zip`](#lazyown_video_to_zip), [`lazyown_create_zip`](#lazyown_create_zip), [`lazyown_extract_zip`](#lazyown_extract_zip), [`lazyown_infinitestorage_upload_to_youtube`](#lazyown_infinitestorage_upload_to_youtube), [`get_tool`](#get_tool), [`list_tools`](#list_tools)
- **Constants:** [`TOOLS`](#tools)

## Functions

<a id="lazyown_infinitestorage_encode"></a>

### `lazyown_infinitestorage_encode`

`function` | [skill_lazyown_infinitestorage/tools.py:52](../../skill_lazyown_infinitestorage/tools.py#L52)

```python
def lazyown_infinitestorage_encode(params: Dict[str, Any]) -> Dict[str, Any]
```

Encode a file into a video using LazyOwnInfiniteStorage.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_infinitestorage_decode"></a>

### `lazyown_infinitestorage_decode`

`function` | [skill_lazyown_infinitestorage/tools.py:105](../../skill_lazyown_infinitestorage/tools.py#L105)

```python
def lazyown_infinitestorage_decode(params: Dict[str, Any]) -> Dict[str, Any]
```

Decode a video back into the original file using LazyOwnInfiniteStorage.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_zip_to_video"></a>

### `lazyown_zip_to_video`

`function` | [skill_lazyown_infinitestorage/tools.py:149](../../skill_lazyown_infinitestorage/tools.py#L149)

```python
def lazyown_zip_to_video(params: Dict[str, Any]) -> Dict[str, Any]
```

Zip a file or directory then encode the archive into a video (zip -> video).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_video_to_zip"></a>

### `lazyown_video_to_zip`

`function` | [skill_lazyown_infinitestorage/tools.py:195](../../skill_lazyown_infinitestorage/tools.py#L195)

```python
def lazyown_video_to_zip(params: Dict[str, Any]) -> Dict[str, Any]
```

Decode a video into a zip archive then extract it (video -> zip -> files).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_create_zip"></a>

### `lazyown_create_zip`

`function` | [skill_lazyown_infinitestorage/tools.py:236](../../skill_lazyown_infinitestorage/tools.py#L236)

```python
def lazyown_create_zip(params: Dict[str, Any]) -> Dict[str, Any]
```

Create a zip archive from a file or directory.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_extract_zip"></a>

### `lazyown_extract_zip`

`function` | [skill_lazyown_infinitestorage/tools.py:268](../../skill_lazyown_infinitestorage/tools.py#L268)

```python
def lazyown_extract_zip(params: Dict[str, Any]) -> Dict[str, Any]
```

Safely extract a zip archive into a directory (blocks zip slip).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="lazyown_infinitestorage_upload_to_youtube"></a>

### `lazyown_infinitestorage_upload_to_youtube`

`function` | [skill_lazyown_infinitestorage/tools.py:299](../../skill_lazyown_infinitestorage/tools.py#L299)

```python
def lazyown_infinitestorage_upload_to_youtube(params: Dict[str, Any]) -> Dict[str, Any]
```

Upload a video to YouTube using browser automation.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `params` | `Dict[str, Any]` |  |  |

**Returns:** `Dict[str, Any]`

---

<a id="get_tool"></a>

### `get_tool`

`function` | [skill_lazyown_infinitestorage/tools.py:453](../../skill_lazyown_infinitestorage/tools.py#L453)

```python
def get_tool(name: str)
```

Get a tool by name.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `name` | `str` |  |  |

---

<a id="list_tools"></a>

### `list_tools`

`function` | [skill_lazyown_infinitestorage/tools.py:457](../../skill_lazyown_infinitestorage/tools.py#L457)

```python
def list_tools()
```

List all available tools.

---

## Constants

<a id="tools"></a>

### `TOOLS`

`constant` | [skill_lazyown_infinitestorage/tools.py:443](../../skill_lazyown_infinitestorage/tools.py#L443)

```python
TOOLS
```

---
