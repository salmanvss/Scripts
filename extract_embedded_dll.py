#!/usr/bin/env python3

import sys
from PIL import Image

def find_bmp_header(data, header=b'\x42\x4D\x32\x55\x36\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00'):
    for i in range(len(data) - len(header)):
        if data[i:i+len(header)] == header:
            return i
    return -1

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <image.jpg>")
        sys.exit(1)

    jpg_path = sys.argv[1]

    # Read JPG bytes
    with open(jpg_path, 'rb') as f:
        data = f.read()

    offset = find_bmp_header(data)
    if offset == -1:
        print("[-] No embedded BMP found.")
        sys.exit(1)

    bmp_data = data[offset:]

    # Write temp BMP
    with open('temp_extracted.bmp', 'wb') as f:
        f.write(bmp_data)

    # Open BMP and extract RGB bytes
    img = Image.open('temp_extracted.bmp')
    rgb_data = []
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))[:3]
            rgb_data.extend([r, g, b])

    # First 4 bytes = payload length
    length_bytes = bytes(rgb_data[:4])
    payload_len = int.from_bytes(length_bytes, byteorder='little')
    payload = bytes(rgb_data[4:4+payload_len])

    # Write DLL
    with open('extracted_payload.dll', 'wb') as f:
        f.write(payload)

    print("[+] Extraction complete: extracted_payload.dll")

if __name__ == '__main__':
    main()
