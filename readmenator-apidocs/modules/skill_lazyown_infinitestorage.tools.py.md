# `skill_lazyown_infinitestorage.tools`

> Source: [skill_lazyown_infinitestorage/tools.py:1](../../skill_lazyown_infinitestorage/tools.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

MCP tools for LazyOwnInfiniteStorage integration.

## Contents

- **Functions:** [`lazyown_infinitestorage_encode`](#lazyown_infinitestorage_encode), [`lazyown_infinitestorage_decode`](#lazyown_infinitestorage_decode), [`lazyown_infinitestorage_upload_to_youtube`](#lazyown_infinitestorage_upload_to_youtube), [`get_tool`](#get_tool), [`list_tools`](#list_tools)
- **Constants:** [`TOOLS`](#tools)

## Functions

<a id="lazyown_infinitestorage_encode"></a>

### `lazyown_infinitestorage_encode`

`function` | [skill_lazyown_infinitestorage/tools.py:34](../../skill_lazyown_infinitestorage/tools.py#L34)

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

`function` | [skill_lazyown_infinitestorage/tools.py:101](../../skill_lazyown_infinitestorage/tools.py#L101)

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

<a id="lazyown_infinitestorage_upload_to_youtube"></a>

### `lazyown_infinitestorage_upload_to_youtube`

`function` | [skill_lazyown_infinitestorage/tools.py:152](../../skill_lazyown_infinitestorage/tools.py#L152)

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

`function` | [skill_lazyown_infinitestorage/tools.py:302](../../skill_lazyown_infinitestorage/tools.py#L302)

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

`function` | [skill_lazyown_infinitestorage/tools.py:306](../../skill_lazyown_infinitestorage/tools.py#L306)

```python
def list_tools()
```

List all available tools.

---

## Constants

<a id="tools"></a>

### `TOOLS`

`constant` | [skill_lazyown_infinitestorage/tools.py:296](../../skill_lazyown_infinitestorage/tools.py#L296)

```python
TOOLS
```

---
