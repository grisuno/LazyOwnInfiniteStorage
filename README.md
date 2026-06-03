```sh
 ▄█          ▄████████  ▄███████▄  ▄██   ▄    ▄██████▄   ▄█     █▄  ███▄▄▄▄             
 ███         ███    ███ ██▀     ▄██ ███   ██▄ ███    ███ ███     ███ ███▀▀▀██▄           
 ███         ███    ███       ▄███▀ ███▄▄▄███ ███    ███ ███     ███ ███   ███           
 ███         ███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███ ███    ███ ███     ███ ███   ███           
 ███       ▀███████████   ▄███▀   ▀ ▄██   ███ ███    ███ ███     ███ ███   ███           
 ███         ███    ███ ▄███▀       ███   ███ ███    ███ ███     ███ ███   ███           
 ███▌    ▄   ███    ███ ███▄     ▄█ ███   ███ ███    ███ ███ ▄█▄ ███ ███   ███           
 █████▄▄██   ███    █▀   ▀████████▀  ▀█████▀   ▀██████▀   ▀███▀███▀   ▀█   █▀            
 ▀                                                                                        
  ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█      ███        ▄████████                
 ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███  ▀█████████▄   ███    ███                
 ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌    ▀███▀▀██   ███    █▀                 
 ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌     ███   ▀  ▄███▄▄▄                    
 ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌     ███     ▀▀███▀▀▀                    
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    █▄                 
 ███  ███   ███   ███        ███  ███   ███ ███      ███       ███    ███                
 █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀      ▄████▀     ██████████                
                                                                                          
    ▄████████     ███      ▄██████▄     ▄████████    ▄████████    ▄██████▄     ▄████████ 
   ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
   ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███   ███    █▀    ███    █▀  
   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███  ▄███         ▄███▄▄▄     
 ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀     
          ███     ███     ███    ███ ▀███████████   ███    ███   ███    ███   ███    █▄  
    ▄█    ███     ███     ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ▄████████▀     ▄████▀    ▀██████▀    ███    ███   ███    █▀    ████████▀    ██████████ 
                                       ███    ███                                         
```

# LazyOwnInfiniteStorage

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

LazyOwnInfiniteStorage is a tool for encoding and decoding files into videos. This project allows you to store data in videos by creating frames that represent data bits, making it easy to recover the original information even after the video has been modified (for example, by changing its resolution).

Resulting in a video like this:

![image](https://github.com/grisuno/LazyOwnInfiniteStorage/assets/1097185/39044629-7e0c-4806-806a-9bbc5a847d88)

## Features

- Encode files into videos using pixel blocks.
- Decode files from videos, even if the video resolution has been changed.
- Use filenames to store information about the original resolution.

## Requirements

- Python 3.6+
- OpenCV
- FFmpeg

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/grisuno/LazyOwnInfiniteStorage.git
    cd LazyOwnInfiniteStorage
    ```

2. Install the dependencies:

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

## Usage

### Encoding

To encode a file into a video:

```sh
python lazyown_infinitestorage.py --mode encode --input file.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4
```

### Decoding
To decode a file from a video:

```sh
python lazyown_infinitestorage.py --mode decode --input video_640x480.mp4 --output recoveredfile.zip --block_size 4
```

# Using the GUI

![image](https://github.com/grisuno/LazyOwnInfiniteStorage/assets/1097185/2e9085ce-0a4f-42b9-bc08-d13e44deb777)


## Mode Selection:

```sh
python gui
```

### Mode Selection:

Choose between Encode and Decode modes using the dropdown menu.
Encode Mode:

Select ZIP File: Click Browse to choose the ZIP file you want to encode.
Video Name: Enter the desired name for the output video file.
Frame Size: Adjust the width and height of the frames (in pixels).
Block Size: Define the size of the blocks used for encoding (in pixels).
Frames per Second: Specify the frame rate for the output video.
Click Start to begin the encoding process.
Decode Mode:

- Select Video File: Click Browse to choose the video file you want to decode.
- Recovered ZIP File Name: Enter the name for the recovered ZIP file.
- Block Size: Define the size of the blocks used for decoding (must match the block size used during encoding).
- Click Start to begin the decoding process.


#### Messages:

When finished or in case of an error, a message window will appear indicating the status of the process.

# Contributions
Contributions are welcome! If you find any issues or have any improvements, feel free to open an issue or a pull request.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)

# Acknowledgments
This project is inspired by the work of DvorakDwarf on Infinite-Storage-Glitch. Any code criticism to help improve is appreciated.

Do whatever you want with the code, but credit would be appreciated. If you have any issues with LazyOwnInfiniteStorage, please contact me on Discord.

## Created by grisuno
