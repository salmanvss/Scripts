
Reference:
https://x.com/salmanvsf/status/1935590497088852093

Infection Flow :
js -> powershell ->download jpg -> extract bmp -> load dll in memory (Katz Stealer)

2f32e9e485b127c1bdcaf7984cc7485a - PO_N0_JKPO25040107.js
https://www.virustotal.com/gui/file/fda1d464861ac16072605f2a390e710b18353cae798fd0ff41b67a9556fe24e2

1. Downloads a JPG with a hidden BMP embedded.
2. Extracts the BMP.
3. Extracts pixel RGBs to get a hidden DLL payload.
4. Loads this DLL in-memory.
5. Calls a method inside it with a C2 URL ($pleated) and some junk args.
6. Runs hidden dll from the image.

# Extract Embedded DLL from Steganographic Image

This script extracts a hidden binary payload that is embedded inside a seemingly normal JPG image using a simple steganographic trick: it hides a valid BMP file starting somewhere inside the JPG’s raw bytes.

⚙️ Step 1 — Scan for the BMP header
A standard BMP file starts with a specific byte signature:
42 4D 32 55 36 00 00 00 00 00 36 00 00 00 28 00
: 42 4D is 'BM' in ASCII — the standard BMP magic number.
The script reads the entire JPG file byte by byte and searches for this exact BMP header pattern.

⚙️ Step 2 — Extract the BMP data
Once it finds the header, it assumes everything from that offset onward is a valid BMP file.
It slices the JPG’s raw bytes from the found header offset to the end.
This gives the hidden BMP image, which can be processed like a normal BMP.

⚙️ Step 3 — Decode the hidden payload
The extracted BMP is opened using an image library.
It loops through every pixel’s RGB values and collects them in order.
The first 4 RGB bytes give the length of the hidden payload.
The next bytes are the actual binary data — usually a compiled .NET DLL.




## 📂 Files

- `extract_embedded_dll.py` — Python 3 script for Linux/REMnux. https://github.com/salmanvss/Scripts/blob/main/extract_embedded_dll.py
- `suspicious_image.jpg` — Live sample. https://www.virustotal.com/gui/file/6fd22b60afbd013a480c096ecc4da6cc89f7e805d44fc68ec18a4be8464259b0

## ⚙️ Requirements

- Python 3
Tested on [REMnux](https://remnux.org/), but works on any Linux/macOS/Python environment.

## 🚀 Usage

1️⃣ Make it executable:

```bash
chmod +x extract_embedded_dll.py

2️⃣ Run it:

./extract_embedded_dll.py suspicious_image.jpg

3️⃣ Output:

The script saves the extracted payload as extracted_payload.dll in the same folder.
