---
name: lazyown_infinitestorage
description: Use when you need to zip files and encode them into videos, decode videos back into zips, or encode/decode single files using LazyOwnInfiniteStorage.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [productivity, encoding, video, zip, storage]
    related_skills: [hermes-agent-skill-authoring]
---

# LazyOwnInfiniteStorage Skill

Provides MCP tools for zipping files and encoding them into videos, decoding videos back into zips, and encoding or decoding single files using LazyOwnInfiniteStorage. The tool stores data in videos by creating grayscale frames that represent data bits, enabling recovery of original information even after video resolution changes.

## Overview

This skill integrates the LazyOwnInfiniteStorage tool with Hermes Agent, providing these capabilities:

1. Zip a file or directory and encode the archive into a video (`lazyown_zip_to_video`)
2. Decode a video into a zip archive and extract it (`lazyown_video_to_zip`)
3. Encode a single file into a video (`lazyown_infinitestorage_encode`)
4. Decode a video back into the original file (`lazyown_infinitestorage_decode`)
5. Create a zip archive (`lazyown_create_zip`)
6. Safely extract a zip archive (`lazyown_extract_zip`)
7. Upload a video to YouTube using browser automation (`lazyown_infinitestorage_upload_to_youtube`, requires Selenium and a logged-in browser)

## Quick commands (easy to remember)

Zip a folder and encode to video:
```
hermes tools lazyown_zip_to_video --source_path ./my_folder --output_video ./archive.mp4 --frame_size "640 480" --fps 30 --block_size 4 --protocol secure
```

Restore a video back into extracted files:
```
hermes tools lazyown_video_to_zip --input_video ./archive_640x480.mp4 --output_dir ./restored --block_size 4 --protocol secure
```

Encode a single file:
```
hermes tools lazyown_infinitestorage_encode --input_file ./document.pdf --output_file ./video.mp4 --frame_size "640 480" --fps 30 --block_size 4 --protocol secure
```

Decode a video to file:
```
hermes tools lazyown_infinitestorage_decode --input_file ./video_640x480.mp4 --output_file ./document.pdf --block_size 4 --protocol secure
```

## When to Use

- Use `lazyown_zip_to_video` when you need to conceal a folder or multiple files within a video
- Use `lazyown_video_to_zip` when you need to recover the original files from an encoded video
- Use `lazyown_infinitestorage_encode` when you need to conceal a single file within a video
- Use `lazyown_infinitestorage_decode` when you need to extract a file from a video encoded with LazyOwnInfiniteStorage
- Use `lazyown_create_zip` / `lazyown_extract_zip` for standalone zip operations

Don't use for:
- Real-time video streaming applications
- Applications requiring direct YouTube API access
- When Selenium/webdriver dependencies cannot be installed (YouTube upload only)

## Tools

### lazyown_zip_to_video
Zip a file or directory then encode the archive into a video. Full pipeline: source -> zip -> video.

Parameters:
- `source_path` (string, required): File or directory to zip and encode
- `output_video` (string, required): Path for the output video file
- `frame_size` (string, optional): Width and height (e.g., "640 480"). Default: "640 480"
- `fps` (integer, optional): Frames per second. Default: 30
- `block_size` (integer, optional): Pixel block size. Default: 4
- `protocol` (string, optional): "legacy" or "secure". Default: "secure"

### lazyown_video_to_zip
Decode a video into a zip archive then extract it. Inverse pipeline: video -> zip -> files.

Parameters:
- `input_video` (string, required): Path to the encoded video
- `output_dir` (string, required): Directory to extract restored files into
- `block_size` (integer, optional): Pixel block size. Default: 4
- `protocol` (string, optional): "legacy" or "secure". Default: "secure"

### lazyown_infinitestorage_encode
Encode a single file into a video.

Parameters:
- `input_file` (string, required): Path to the file to encode
- `output_file` (string, required): Path for the output video file
- `frame_size` (string, optional): Width and height (e.g., "640 480"). Default: "640 480"
- `fps` (integer, optional): Frames per second. Default: 30
- `block_size` (integer, optional): Pixel block size. Default: 4
- `protocol` (string, optional): "legacy" or "secure". Default: "secure"

### lazyown_infinitestorage_decode
Decode a video back into the original file.

Parameters:
- `input_file` (string, required): Path to the input video
- `output_file` (string, required): Path for the output decoded file
- `block_size` (integer, optional): Pixel block size. Default: 4
- `protocol` (string, optional): "legacy" or "secure". Default: "secure"

### lazyown_create_zip
Create a zip archive from a file or directory.

Parameters:
- `source_path` (string, required): File or directory to zip
- `output_zip` (string, required): Path for the output zip file

### lazyown_extract_zip
Safely extract a zip archive into a directory (blocks zip slip path traversal).

Parameters:
- `zip_path` (string, required): Path to the zip archive
- `output_dir` (string, required): Directory to extract into

### lazyown_infinitestorage_upload_to_youtube
Upload a video to YouTube using browser automation. Assumes the user is already logged into YouTube.

Parameters:
- `video_file` (string, required): Path to the video file to upload
- `title` (string, required): Title for the YouTube video
- `description` (string, optional): Description. Default: ""
- `tags` (string, optional): Comma-separated tags. Default: ""
- `privacy` (string, optional): "public", "unlisted", or "private". Default: "private"

## Dependencies

Install Python dependencies:
```bash
pip install opencv-python numpy
```

For YouTube upload functionality:
```bash
pip install selenium
```
And ensure a web driver (e.g., chromedriver) is available in the system PATH.

## Security

- All file paths are validated before use to block path traversal.
- Zip extraction validates every member path so archives cannot write outside the target directory (zip slip protection).
- Zip bombs are limited by member count and total uncompressed size.
- Raw frame extraction is size-bounded to prevent memory exhaustion on large videos.
- File size limits are enforced at config, validator, and tool layers.

## Verification Checklist

- [ ] Skill is located at `skill_lazyown_infinitestorage/SKILL.md`
- [ ] Frontmatter starts with `---` and ends with `---`
- [ ] Required fields present: name, description, version, author, license, metadata
- [ ] Description starts with "Use when ..." and is under 1024 characters
- [ ] Tools section lists every tool in `TOOLS` registry with parameters
- [ ] Quick commands section provides easy to remember English examples
- [ ] Security section documents path traversal, zip slip, and size limits
- [ ] No emojis in code or documentation
