import cv2
import numpy as np
import argparse
import os
import subprocess
import tempfile

BANNER = """
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
"""

def encode_file_to_images(input_file, temp_dir, frame_size, block_size=4):
    with open(input_file, 'rb') as f:
        data = f.read()

    bit_data = ''.join(format(byte, '08b') for byte in data)
    bit_data += '1' + '0' * ((8 - len(bit_data) % 8) % 8)

    width, height = frame_size
    bits_per_frame = (width // block_size) * (height // block_size)
    frame_count = (len(bit_data) + bits_per_frame - 1) // bits_per_frame

    for i in range(frame_count):
        frame_bits = bit_data[i * bits_per_frame : (i + 1) * bits_per_frame]
        frame_bits = frame_bits.ljust(bits_per_frame, '0')
        frame = np.zeros((height, width), dtype=np.uint8)
        for idx, bit in enumerate(frame_bits):
            x = (idx % (width // block_size)) * block_size
            y = (idx // (width // block_size)) * block_size
            color = 255 if bit == '1' else 0
            frame[y:y+block_size, x:x+block_size] = color
        frame_path = os.path.join(temp_dir, f'frame_{i:05d}.png')
        cv2.imwrite(frame_path, frame)

def encode_file_to_video(input_file, output_file, frame_size, fps, block_size=4):
    with tempfile.TemporaryDirectory() as temp_dir:
        encode_file_to_images(input_file, temp_dir, frame_size, block_size)
        width, height = frame_size
        resolution = f"{width}x{height}"
        output_file_with_resolution = f"{os.path.splitext(output_file)[0]}_{resolution}.mp4"
        subprocess.run([
            'ffmpeg', '-y', '-framerate', str(fps), '-i', os.path.join(temp_dir, 'frame_%05d.png'),
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', 'faststart', output_file_with_resolution
        ])

def decode_video_to_file(input_file, output_file, block_size=4):
    cap = cv2.VideoCapture(input_file)
    
    # Extract original resolution from file name
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    resolution_str = file_name.split('_')[-1]
    width, height = map(int, resolution_str.split('x'))
    
    bit_data = ''
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, (width, height), interpolation=cv2.INTER_AREA)
        for y in range(0, height, block_size):
            for x in range(0, width, block_size):
                if y + block_size > resized_frame.shape[0] or x + block_size > resized_frame.shape[1]:
                    bit = '0'
                else:
                    bit = '1' if np.mean(resized_frame[y:y+block_size, x:x+block_size]) > 127 else '0'
                bit_data += bit

    cap.release()

    print(f"Extracted bit data length: {len(bit_data)}")
    print(f"Extracted bit data (first 512 bits): {bit_data[:512]}")

    byte_data = bytearray()
    for i in range(0, len(bit_data), 8):
        byte_data.append(int(bit_data[i:i+8], 2))

    end_marker = b'\x80'
    end = byte_data.rfind(end_marker)
    if end != -1:
        byte_data = byte_data[:end]

    with open(output_file, 'wb') as f:
        f.write(byte_data)

    print(f"Recovered byte data length: {len(byte_data)}")
    print(f"Recovered byte data (first 64 bytes): {byte_data[:64]}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description='Encode and decode files to and from video')
    parser.add_argument('--mode', choices=['encode', 'decode'], required=True, help='Operation mode: encode or decode')
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='Output file')
    parser.add_argument('--frame_size', type=int, nargs=2, required=True, help='Frame size (width height)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second for video encoding (default: 30)')
    parser.add_argument('--block_size', type=int, default=4, help='Size of the blocks representing bits (default: 4)')

    args = parser.parse_args()

    if args.mode == 'encode':
        encode_file_to_video(args.input, args.output, tuple(args.frame_size), args.fps, args.block_size)
    elif args.mode == 'decode':
        decode_video_to_file(args.input, args.output, args.block_size)

if __name__ == '__main__':
    main()
