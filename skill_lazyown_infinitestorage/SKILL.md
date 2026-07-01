---
name: lazyown_infinitestorage
description: Use when you need to encode files to videos, decode videos to files, or upload videos to YouTube using browser automation (assuming user is already logged in).
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [productivity, encoding, video, youtube]
    related_skills: [hermes-agent-skill-authoring]
---

# LazyOwnInfiniteStorage Skill

Provides MCP tools for encoding files to videos and decoding videos to files using LazyOwnInfiniteStorage, plus YouTube upload via browser automation.

## Overview

This skill integrates the LazyOwnInfiniteStorage tool with Hermes Agent, providing three main capabilities:
1. Encode files into videos using either legacy or secure protocols
2. Decode videos back into original files
3. Upload videos to YouTube using browser automation (requires user to be logged into YouTube)

The LazyOwnInfiniteStorage tool stores data in videos by creating grayscale frames that represent data bits, enabling recovery of original information even after video resolution changes.

## When to Use

- Use `lazyown_infinitestorage_encode` when you need to conceal data within a video file for storage or transmission
- Use `lazyown_infinitestorage_decode` when you need to extract data from a video that was encoded with LazyOwnInfiniteStorage
- Use `lazyown_infinitestorage_upload_to_youtube` when you want to upload an encoded video to YouTube without using the YouTube API (relies on browser automation with existing login)

Don't use for:
- Real-time video streaming applications
- Applications requiring direct YouTube API access (use the youtube-content skill instead)
- When Selenium/webdriver dependencies cannot be installed

## Tools

### lazyown_infinitestorage_encode
Encodes a file into a video using either the legacy or secure protocol.

**Parameters:**
- `input_file` (string): Path to the file to encode
- `output_file` (string): Path for the output video file
- `frame_size` (string, optional): Width and height of video frames (e.g., "640 480"). Default: "640 480"
- `fps` (integer, optional): Frames per second. Default: 30
- `block_size` (integer, optional): Size of pixel blocks. Default: 4
- `protocol` (string, optional): Either "legacy" or "secure". Default: "secure"

### lazyown_infinitestorage_decode
Decodes a video back into the original file.

**Parameters:**
- `input_file` (string): Path to the input video file
- `output_file` (string): Path for the output decoded file
- `block_size` (integer, optional): Size of pixel blocks used during encoding. Default: 4
- `protocol` (string, optional): Either "legacy" or "secure". Default: "secure"

### lazyown_infinitestorage_upload_to_youtube
Uploads a video to YouTube using browser automation. Assumes the user is already logged into YouTube in the browser.

**Parameters:**
- `video_file` (string): Path to the video file to upload
- `title` (string): Title for the YouTube video
- `description` (string, optional): Description for the YouTube video. Default: ""
- `tags` (string, optional): Comma-separated tags for the YouTube video. Default: ""
- `privacy` (string, optional): Privacy setting ("public", "unlisted", "private"). Default: "private"

## Dependencies

This skill requires the LazyOwnInfiniteStorage tool to be available. Additionally, the YouTube upload functionality requires Selenium and a compatible web driver.

Install Python dependencies for LazyOwnInfiniteStorage:
```bash
pip install opencv-python numpy
```

For YouTube upload functionality:
```bash
pip install selenium
```
And ensure a web driver (e.g., chromedriver) is available in the system's PATH.

## Usage Examples

Encode a file to video:
```
hermes tools lazyown_infinitestorage_encode --input_file /path/to/document.pdf --output_file /path/to/video.mp4 --frame_size "640 480" --fps 30 --block_size 4 --protocol secure
```

Decode a video to file:
```
hermes tools lazyown_infinitestorage_decode --input_file /path/to/video.mp4 --output_file /path/to/recovered.pdf --block_size 4 --protocol secure
```

Upload video to YouTube:
```
hermes tools lazyown_infinitestorage_upload_to_youtube --video_file /path/to/video.mp4 --title "My Encoded Video" --description "This video contains encoded data" --tags "data,storage,encoding" --privacy "unlisted"
```

## Implementation Notes

The YouTube upload tool uses Selenium to automate the YouTube web interface. It assumes:
1. The user is already logged into YouTube in the browser session
2. Chrome browser is available (can be modified to use other browsers)
3. The YouTube interface structure matches the XPath selectors used

If YouTube changes its UI, the XPath selectors in the upload tool may need to be updated.

## Common Pitfalls

1. **YouTube login requirement**: The upload tool requires the user to be already logged into YouTube. It does not handle login credentials for security reasons.

2. **Browser compatibility**: The tool is configured for Chrome. To use a different browser, modify the webdriver initialization in the upload_to_youtube function.

3. **YouTube UI changes**: YouTube frequently updates its interface, which may break the XPath selectors used in the upload automation.

4. **File size limitations**: Very large files may result in extremely large videos or encoding timeouts. Consider file size limitations based on your needs.

5. **Protocol selection**: The secure protocol includes error correction (Hamming(8,4)) and CRC32 checks, making it more robust but potentially larger than the legacy protocol.

## Verification Checklist

- [ ] Skill is located at `skills/productivity/lazyown_infinitestorage/SKILL.md`
- [ ] Frontmatter starts with `---` and ends with `---`
- [ ] Required fields present: name, description, version, author, license, metadata
- [ ] Description starts with "Use when ..." and is under 1024 characters
- [ ] Total file size is reasonable (aim for 8-15k characters)
- [ ] Structure follows: Title → Overview → When to Use → Tools → Dependencies → Usage Examples → Implementation Notes → Common Pitfalls → Verification Checklist
- [ ] Each tool section includes clear parameter descriptions and usage examples
- [ ] No duplicated content or unnecessary prose