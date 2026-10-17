"""Model Context Protocol server for LazyOwnInfiniteStorage.

Exposes stdio tools so an agent can run the full zip -> video pipeline and the
inverse video -> zip pipeline with easy to remember English commands.
"""

import asyncio
import os
import sys
from typing import Any, Dict

# Make the core library importable when run from any working directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lazyown_infinitestorage import (
    LazyOwnConfig,
    LazyOwnInfiniteStorage,
)

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
    HAS_MCP = True
except ImportError as exc:  # pragma: no cover - dependency missing at runtime
    HAS_MCP = False
    MCP_IMPORT_ERROR = str(exc)

_CONFIG = LazyOwnConfig()
_STORAGE = LazyOwnInfiniteStorage(_CONFIG)

TOOL_DESCRIPTIONS = {
    "lazyown_zip_to_video": (
        "Zip a file or directory then encode the archive into a video. "
        "Full pipeline: source -> zip -> video. Parameters: source_path, "
        "output_video, frame_size (\"W H\"), fps, block_size, protocol."
    ),
    "lazyown_video_to_zip": (
        "Decode a video into a zip archive then extract it into a directory. "
        "Inverse pipeline: video -> zip -> extracted files. Parameters: "
        "input_video, output_dir, block_size, protocol."
    ),
    "lazyown_encode": (
        "Encode a single file into a video. Parameters: input_file, output_file, "
        "frame_size (\"W H\"), fps, block_size, protocol."
    ),
    "lazyown_decode": (
        "Decode a video back into the original file. Parameters: input_file, "
        "output_file, block_size, protocol."
    ),
    "lazyown_create_zip": (
        "Create a zip archive from a file or directory. Parameters: source_path, "
        "output_zip."
    ),
    "lazyown_extract_zip": (
        "Safely extract a zip archive into a directory (blocks zip slip). "
        "Parameters: zip_path, output_dir."
    ),
}


def _parse_frame_size(value: Any) -> tuple:
    if isinstance(value, (list, tuple)) and len(value) == 2:
        return int(value[0]), int(value[1])
    width, height = map(int, str(value).split())
    return width, height


def _protocol_value(protocol: Any) -> int:
    if protocol is None:
        return _CONFIG.PROTOCOL_VERSION_SECURE
    return (
        _CONFIG.PROTOCOL_VERSION_LEGACY
        if str(protocol).lower() == "legacy"
        else _CONFIG.PROTOCOL_VERSION_SECURE
    )


def _tool_zip_to_video(arguments: Dict[str, Any]) -> Dict[str, Any]:
    source_path = arguments.get("source_path")
    output_video = arguments.get("output_video")
    if not source_path or not output_video:
        return {"success": False, "error": "source_path and output_video are required"}
    frame_width, frame_height = _parse_frame_size(arguments.get("frame_size", "640 480"))
    fps = int(arguments.get("fps", _CONFIG.DEFAULT_FPS))
    block_size = int(arguments.get("block_size", _CONFIG.DEFAULT_BLOCK_SIZE))
    protocol_version = _protocol_value(arguments.get("protocol", "secure"))
    try:
        video_path = _STORAGE.zip_to_video(
            source_path, output_video, frame_width, frame_height, fps, block_size, protocol_version
        )
        return {
            "success": True,
            "message": f"Zipped {source_path} and encoded to video {video_path}",
            "video_path": video_path,
            "parameters": {
                "frame_size": [frame_width, frame_height],
                "fps": fps,
                "block_size": block_size,
                "protocol": "legacy" if protocol_version == _CONFIG.PROTOCOL_VERSION_LEGACY else "secure",
            },
        }
    except Exception as exc:
        return {"success": False, "error": f"zip_to_video failed: {exc}"}


def _tool_video_to_zip(arguments: Dict[str, Any]) -> Dict[str, Any]:
    input_video = arguments.get("input_video")
    output_dir = arguments.get("output_dir")
    if not input_video or not output_dir:
        return {"success": False, "error": "input_video and output_dir are required"}
    block_size = int(arguments.get("block_size", _CONFIG.DEFAULT_BLOCK_SIZE))
    protocol_version = _protocol_value(arguments.get("protocol", "secure"))
    try:
        restored_dir = _STORAGE.video_to_zip(
            input_video, output_dir, block_size, protocol_version
        )
        return {
            "success": True,
            "message": f"Decoded video {input_video} and extracted zip to {restored_dir}",
            "output_dir": restored_dir,
            "parameters": {
                "block_size": block_size,
                "protocol": "legacy" if protocol_version == _CONFIG.PROTOCOL_VERSION_LEGACY else "secure",
            },
        }
    except Exception as exc:
        return {"success": False, "error": f"video_to_zip failed: {exc}"}


def _tool_encode(arguments: Dict[str, Any]) -> Dict[str, Any]:
    input_file = arguments.get("input_file")
    output_file = arguments.get("output_file")
    if not input_file or not output_file:
        return {"success": False, "error": "input_file and output_file are required"}
    frame_width, frame_height = _parse_frame_size(arguments.get("frame_size", "640 480"))
    fps = int(arguments.get("fps", _CONFIG.DEFAULT_FPS))
    block_size = int(arguments.get("block_size", _CONFIG.DEFAULT_BLOCK_SIZE))
    protocol_version = _protocol_value(arguments.get("protocol", "secure"))
    try:
        _STORAGE.encode(input_file, output_file, frame_width, frame_height, fps, block_size, protocol_version)
        return {
            "success": True,
            "message": f"Encoded {input_file} to video {output_file}",
            "output_file": output_file,
            "parameters": {
                "frame_size": [frame_width, frame_height],
                "fps": fps,
                "block_size": block_size,
                "protocol": "legacy" if protocol_version == _CONFIG.PROTOCOL_VERSION_LEGACY else "secure",
            },
        }
    except Exception as exc:
        return {"success": False, "error": f"encode failed: {exc}"}


def _tool_decode(arguments: Dict[str, Any]) -> Dict[str, Any]:
    input_file = arguments.get("input_file")
    output_file = arguments.get("output_file")
    if not input_file or not output_file:
        return {"success": False, "error": "input_file and output_file are required"}
    block_size = int(arguments.get("block_size", _CONFIG.DEFAULT_BLOCK_SIZE))
    protocol_version = _protocol_value(arguments.get("protocol", "secure"))
    try:
        _STORAGE.decode(input_file, output_file, block_size, protocol_version)
        return {
            "success": True,
            "message": f"Decoded {input_file} to {output_file}",
            "output_file": output_file,
            "parameters": {
                "block_size": block_size,
                "protocol": "legacy" if protocol_version == _CONFIG.PROTOCOL_VERSION_LEGACY else "secure",
            },
        }
    except Exception as exc:
        return {"success": False, "error": f"decode failed: {exc}"}


def _tool_create_zip(arguments: Dict[str, Any]) -> Dict[str, Any]:
    source_path = arguments.get("source_path")
    output_zip = arguments.get("output_zip")
    if not source_path or not output_zip:
        return {"success": False, "error": "source_path and output_zip are required"}
    try:
        zip_path = _STORAGE.create_zip(source_path, output_zip)
        return {"success": True, "message": f"Created zip {zip_path}", "zip_path": zip_path}
    except Exception as exc:
        return {"success": False, "error": f"create_zip failed: {exc}"}


def _tool_extract_zip(arguments: Dict[str, Any]) -> Dict[str, Any]:
    zip_path = arguments.get("zip_path")
    output_dir = arguments.get("output_dir")
    if not zip_path or not output_dir:
        return {"success": False, "error": "zip_path and output_dir are required"}
    try:
        restored_dir = _STORAGE.extract_zip(zip_path, output_dir)
        return {"success": True, "message": f"Extracted {zip_path} to {restored_dir}", "output_dir": restored_dir}
    except Exception as exc:
        return {"success": False, "error": f"extract_zip failed: {exc}"}


TOOL_HANDLERS = {
    "lazyown_zip_to_video": _tool_zip_to_video,
    "lazyown_video_to_zip": _tool_video_to_zip,
    "lazyown_encode": _tool_encode,
    "lazyown_decode": _tool_decode,
    "lazyown_create_zip": _tool_create_zip,
    "lazyown_extract_zip": _tool_extract_zip,
}


def _build_tools() -> list:
    return [
        Tool(
            name="lazyown_zip_to_video",
            description=TOOL_DESCRIPTIONS["lazyown_zip_to_video"],
            inputSchema={
                "type": "object",
                "properties": {
                    "source_path": {"type": "string", "description": "File or directory to zip and encode"},
                    "output_video": {"type": "string", "description": "Output video path"},
                    "frame_size": {"type": "string", "description": "\"W H\" (default 640 480)"},
                    "fps": {"type": "integer", "description": "Frames per second (default 30)"},
                    "block_size": {"type": "integer", "description": "Pixel block size (default 4)"},
                    "protocol": {"type": "string", "description": "legacy or secure (default secure)"},
                },
                "required": ["source_path", "output_video"],
            },
        ),
        Tool(
            name="lazyown_video_to_zip",
            description=TOOL_DESCRIPTIONS["lazyown_video_to_zip"],
            inputSchema={
                "type": "object",
                "properties": {
                    "input_video": {"type": "string", "description": "Encoded video path"},
                    "output_dir": {"type": "string", "description": "Directory to extract restored zip into"},
                    "block_size": {"type": "integer", "description": "Pixel block size (default 4)"},
                    "protocol": {"type": "string", "description": "legacy or secure (default secure)"},
                },
                "required": ["input_video", "output_dir"],
            },
        ),
        Tool(
            name="lazyown_encode",
            description=TOOL_DESCRIPTIONS["lazyown_encode"],
            inputSchema={
                "type": "object",
                "properties": {
                    "input_file": {"type": "string", "description": "File to encode"},
                    "output_file": {"type": "string", "description": "Output video path"},
                    "frame_size": {"type": "string", "description": "\"W H\" (default 640 480)"},
                    "fps": {"type": "integer", "description": "Frames per second (default 30)"},
                    "block_size": {"type": "integer", "description": "Pixel block size (default 4)"},
                    "protocol": {"type": "string", "description": "legacy or secure (default secure)"},
                },
                "required": ["input_file", "output_file"],
            },
        ),
        Tool(
            name="lazyown_decode",
            description=TOOL_DESCRIPTIONS["lazyown_decode"],
            inputSchema={
                "type": "object",
                "properties": {
                    "input_file": {"type": "string", "description": "Video to decode"},
                    "output_file": {"type": "string", "description": "Output file path"},
                    "block_size": {"type": "integer", "description": "Pixel block size (default 4)"},
                    "protocol": {"type": "string", "description": "legacy or secure (default secure)"},
                },
                "required": ["input_file", "output_file"],
            },
        ),
        Tool(
            name="lazyown_create_zip",
            description=TOOL_DESCRIPTIONS["lazyown_create_zip"],
            inputSchema={
                "type": "object",
                "properties": {
                    "source_path": {"type": "string", "description": "File or directory to zip"},
                    "output_zip": {"type": "string", "description": "Output zip path"},
                },
                "required": ["source_path", "output_zip"],
            },
        ),
        Tool(
            name="lazyown_extract_zip",
            description=TOOL_DESCRIPTIONS["lazyown_extract_zip"],
            inputSchema={
                "type": "object",
                "properties": {
                    "zip_path": {"type": "string", "description": "Zip archive to extract"},
                    "output_dir": {"type": "string", "description": "Directory to extract into"},
                },
                "required": ["zip_path", "output_dir"],
            },
        ),
    ]


async def _run() -> int:
    if not HAS_MCP:
        print(f"mcp package not available: {MCP_IMPORT_ERROR}", file=sys.stderr)
        return 1

    server = Server("lazyown_infinitestorage")

    @server.list_tools()
    async def list_tools() -> list:
        return _build_tools()

    @server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]) -> list:
        handler = TOOL_HANDLERS.get(name)
        if handler is None:
            raise ValueError(f"Unknown tool: {name}")
        result = handler(arguments)
        return [TextContent(type="text", text=str(result))]

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )
    return 0


def main() -> int:
    """Entry point for the LazyOwnInfiniteStorage MCP stdio server."""
    return asyncio.run(_run())


if __name__ == "__main__":
    sys.exit(main())
