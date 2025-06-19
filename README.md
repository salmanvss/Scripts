# Extract Embedded DLL from Steganographic Image

This simple forensic script extracts a hidden DLL payload embedded inside a normal-looking JPG file.  
It is useful for analyzing suspicious images that hide malware using pixel RGB data.

## 📂 Files

- `extract_embedded_dll.py` — Python 3 script for Linux/REMnux. https://github.com/salmanvss/Scripts/blob/main/extract_embedded_dll.py
- `sample.jpg` — (Optional) Example stego image for testing (add your own or use a threat sample). https://www.virustotal.com/gui/file/6fd22b60afbd013a480c096ecc4da6cc89f7e805d44fc68ec18a4be8464259b0

## ⚙️ Requirements

- Python 3
- Pillow library (`pip install pillow`)

Tested on [REMnux](https://remnux.org/), but works on any Linux/macOS/Python environment.

## 🚀 Usage

1️⃣ Make it executable:

```bash
chmod +x extract_embedded_dll.py

2️⃣ Run it:

./extract_embedded_dll.py suspicious_image.jpg

3️⃣ Output:

The script saves the extracted payload as extracted_payload.dll in the same folder.
