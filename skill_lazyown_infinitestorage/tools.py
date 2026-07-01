"""MCP tools for LazyOwnInfiniteStorage integration."""

import os
import sys
import subprocess
import time
from typing import Dict, Any

# Add the current directory to Python path to import lazyown_infinitestorage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from lazyown_infinitestorage import (
        encode_file as lazyown_encode,
        decode_file as lazyown_decode,
        get_available_protocols
    )
    LAZYOWN_AVAILABLE = True
except ImportError as e:
    LAZYOWN_AVAILABLE = False
    LAZYOWN_IMPORT_ERROR = str(e)

# For YouTube upload, we'll use Selenium if available
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

def lazyown_infinitestorage_encode(params: Dict[str, Any]) -> Dict[str, Any]:
    """Encode a file into a video using LazyOwnInfiniteStorage."""
    if not LAZYOWN_AVAILABLE:
        return {
            "error": f"LazyOwnInfiniteStorage not available: {LAZYOWN_IMPORT_ERROR}",
            "success": False
        }
    
    try:
        input_file = params.get("input_file")
        output_file = params.get("output_file")
        frame_size_str = params.get("frame_size", "640 480")
        fps = int(params.get("fps", 30))
        block_size = int(params.get("block_size", 4))
        protocol = params.get("protocol", "secure")
        
        if not input_file or not output_file:
            return {
                "error": "input_file and output_file are required",
                "success": False
            }
        
        # Parse frame size
        try:
            width, height = map(int, frame_size_str.split())
            frame_size = (width, height)
        except ValueError:
            return {
                "error": "frame_size must be in format 'width height' (e.g., '640 480')",
                "success": False
            }
        
        # Validate inputs
        if not os.path.exists(input_file):
            return {
                "error": f"Input file not found: {input_file}",
                "success": False
            }
        
        # Call the encoding function
        lazyown_encode(
            input_path=input_file,
            output_path=output_file,
            frame_size=frame_size,
            fps=fps,
            block_size=block_size,
            protocol=protocol
        )
        
        return {
            "success": True,
            "message": f"Successfully encoded {input_file} to {output_file}",
            "output_file": output_file,
            "parameters": {
                "frame_size": frame_size,
                "fps": fps,
                "block_size": block_size,
                "protocol": protocol
            }
        }
        
    except Exception as e:
        return {
            "error": f"Encoding failed: {str(e)}",
            "success": False
        }

def lazyown_infinitestorage_decode(params: Dict[str, Any]) -> Dict[str, Any]:
    """Decode a video back into the original file using LazyOwnInfiniteStorage."""
    if not LAZYOWN_AVAILABLE:
        return {
            "error": f"LazyOwnInfiniteStorage not available: {LAZYOWN_IMPORT_ERROR}",
            "success": False
        }
    
    try:
        input_file = params.get("input_file")
        output_file = params.get("output_file")
        block_size = int(params.get("block_size", 4))
        protocol = params.get("protocol", "secure")
        
        if not input_file or not output_file:
            return {
                "error": "input_file and output_file are required",
                "success": False
            }
        
        # Validate inputs
        if not os.path.exists(input_file):
            return {
                "error": f"Input video not found: {input_file}",
                "success": False
            }
        
        # Call the decoding function
        lazyown_decode(
            input_path=input_file,
            output_path=output_file,
            block_size=block_size,
            protocol=protocol
        )
        
        return {
            "success": True,
            "message": f"Successfully decoded {input_file} to {output_file}",
            "output_file": output_file,
            "parameters": {
                "block_size": block_size,
                "protocol": protocol
            }
        }
        
    except Exception as e:
        return {
            "error": f"Decoding failed: {str(e)}",
            "success": False
        }

def lazyown_infinitestorage_upload_to_youtube(params: Dict[str, Any]) -> Dict[str, Any]:
    """Upload a video to YouTube using browser automation."""
    if not SELENIUM_AVAILABLE:
        return {
            "error": "Selenium not available. Install with: pip install selenium",
            "success": False
        }
    
    try:
        video_file = params.get("video_file")
        title = params.get("title", "")
        description = params.get("description", "")
        tags = params.get("tags", "")
        privacy = params.get("privacy", "private")
        
        if not video_file:
            return {
                "error": "video_file is required",
                "success": False
            }
        
        if not os.path.exists(video_file):
            return {
                "error": f"Video file not found: {video_file}",
                "success": False
            }
        
        # Set up Chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # Uncomment the next line if you want to run headless
        # options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 20)
        
        try:
            # Navigate to YouTube
            driver.get("https://www.youtube.com")
            time.sleep(2)
            
            # Click on the upload button (camera icon)
            upload_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//ytd-topbar-menu-button-renderer[@id='upload-button']"))
            )
            upload_button.click()
            time.sleep(2)
            
            # Click on the upload video option
            upload_video_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-item[@id='text-item-0']"))
            )
            upload_video_option.click()
            time.sleep(2)
            
            # Find the file input element and send the video file path
            file_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            file_input.send_keys(os.path.abspath(video_file))
            time.sleep(3)  # Wait for upload to start
            
            # Fill in the title
            title_box = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='textbox' and @contenteditable='true']"))
            )
            title_box.clear()
            title_box.send_keys(title)
            time.sleep(1)
            
            # Fill in the description
            description_box = driver.find_element(By.XPATH, "//div[@id='description-textarea' and @contenteditable='true']")
            description_box.clear()
            description_box.send_keys(description)
            time.sleep(1)
            
            # Handle tags if provided
            if tags:
                # Click to show more options
                show_more = driver.find_element(By.XPATH, "//ytcp-button[@id='toggle-button']")
                show_more.click()
                time.sleep(1)
                
                # Find tags input
                tags_input = driver.find_element(By.XPATH, "//input[@id='text-input' and @placeholder='Add a tag (e.g., gaming, vlog, music)']")
                for tag in tags.split(','):
                    tag = tag.strip()
                    if tag:
                        tags_input.send_keys(tag)
                        tags_input.send_keys('\n')  # Press Enter to add the tag
                        time.sleep(0.5)
            
            # Set privacy
            privacy_radio = driver.find_element(By.XPATH, f"//tp-yt-paper-radio-button[@name='{privacy}']")
            privacy_radio.click()
            time.sleep(1)
            
            # Click next buttons (usually 3 times)
            for _ in range(3):
                next_button = driver.find_element(By.XPATH, "//ytcp-button[@id='next-button']")
                next_button.click()
                time.sleep(2)
            
            # Click done/publish button
            done_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//ytcp-button[@id='done-button']"))
            )
            done_button.click()
            time.sleep(3)
            
            # Get the video URL (optional)
            video_url = ""
            try:
                video_url_element = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//ytcp-video-info[@id='info']//a[@id='video-url']"))
                )
                video_url = video_url_element.get_attribute("href")
            except:
                pass  # Video URL extraction is optional
            
            return {
                "success": True,
                "message": f"Successfully uploaded {video_file} to YouTube",
                "video_url": video_url,
                "parameters": {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "privacy": privacy
                }
            }
            
        finally:
            # Keep browser open for a moment so user can see result, then close
            time.sleep(5)
            driver.quit()
    
    except Exception as e:
        return {
            "error": f"YouTube upload failed: {str(e)}",
            "success": False
        }

# Tool registry for MCP
TOOLS = {
    "lazyown_infinitestorage_encode": lazyown_infinitestorage_encode,
    "lazyown_infinitestorage_decode": lazyown_infinitestorage_decode,
    "lazyown_infinitestorage_upload_to_youtube": lazyown_infinitestorage_upload_to_youtube
}

def get_tool(name: str):
    """Get a tool by name."""
    return TOOLS.get(name)

def list_tools():
    """List all available tools."""
    return list(TOOLS.keys())