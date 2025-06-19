
Reference:
https://x.com/salmanvsf/status/1935590497088852093

Infection Flow :
js -> powershell ->download jpg -> extract bmp -> load dll in memory

2f32e9e485b127c1bdcaf7984cc7485a - PO_N0_JKPO25040107.js
https://www.virustotal.com/gui/file/fda1d464861ac16072605f2a390e710b18353cae798fd0ff41b67a9556fe24e2

Downloads a JPG with a hidden BMP embedded.
Extracts the BMP.
Extracts pixel RGBs to get a hidden DLL payload.
Loads this DLL in-memory.
Calls a method inside it with a C2 URL ($pleated) and some junk args.
Effectively runs hidden code from the image.

# Extract Embedded DLL from Steganographic Image

This simple forensic script extracts a hidden DLL payload embedded inside a normal-looking JPG file.  
It is useful for analyzing suspicious images that hide malware using pixel RGB data.

## 📂 Files

- `extract_embedded_dll.py` — Python 3 script for Linux/REMnux. https://github.com/salmanvss/Scripts/blob/main/extract_embedded_dll.py
- `sample.jpg` — (Optional). https://www.virustotal.com/gui/file/6fd22b60afbd013a480c096ecc4da6cc89f7e805d44fc68ec18a4be8464259b0

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
