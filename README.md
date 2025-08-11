# SUBI Unlock v1.0.5

**SUBI Unlock** is a lightweight, portable, offline tool to remove editing/printing/copying restrictions from your own PDFs—no installation required.  
Drop one PDF onto the app window and it creates an unlocked copy.

---

## 🧭 Purpose

This tool is designed for **your personal documents** where:

- You previously set edit/print restrictions
- You’ve **forgotten the permission password**
- The PDF is **viewable** (you can open it)

Do **not** use this on PDFs you don’t own or don’t have the legal right to modify.

---

## ✅ What’s new in 1.0.5

- Faster processing
- Unlocks some PDFs that previously failed
- Better effort to preserve original quality
- Automatically opens the resulting PDF
- You can also **choose a file via button** (not only Drag & Drop)

---

## ⭐ Features

- 🖱️ **Drag & Drop**: drop **one** PDF onto the app window
- 🔓 Removes edit/print/copy restrictions
- 🖥️ **Fully offline**: everything runs locally (no uploads)
- 🚫 **Portable**: unzip and run the `.exe`
- 📄 Original is preserved; result is saved as `name_SUBI_unlocked.pdf` in the same folder
- 👀 The unlocked PDF opens automatically when done

---

## ⚠️ Limitations

- ❌ Cannot open PDFs that **require a password just to view**
- ❌ Does **not** remove DRM (Digital Rights Management)
- ✅ Works only on PDFs you can already open, removing permission restrictions

---

## 🚀 How to Use

1. **Extract** the ZIP completely (don’t run from the compressed folder).  
2. Run `SUBI_unlock_v1.0.5.exe`.  
3. Drag **one** PDF onto the app window *(or click the button to choose a file)*.  
4. The unlocked file `*_SUBI_unlocked.pdf` is created in the same folder and opens automatically.  
5. A success popup appears: it opens the developer blog **after 5 seconds**, or **immediately** when you click “Confirm,” then the program exits.

---

## 🧩 How it Works

- Uses **qpdf** internally: `unlockpdf/bin/qpdf.exe`  
- No internet connection is required; all processing happens on **your PC**  
- The result opens with your system’s default PDF viewer (e.g., Edge, Acrobat)

---

## 🗂️ Folder Structure


---

## 🛠️ Troubleshooting

- **“Could not find qpdf”** → Verify `unlockpdf/bin/qpdf.exe` exists and you extracted the ZIP before running.  
- **Result doesn’t open** → Ensure a default PDF viewer is set in Windows.  
- **Unlock failed** → If the file can’t be opened without a password, it cannot be unlocked by this tool.

---

## 📜 License

- **App (SUBI Unlock)**: Proprietary EULA (no redistribution/modification/reverse engineering). See `LICENSE.txt`.  
- **Third-party**: qpdf is licensed under **Apache License 2.0**. See `THIRD_PARTY_LICENSES/qpdf-LICENSE.txt`.

> Starting with v1.0.5, **Ghostscript is not used**. GS-related notices have been removed.

---

## 👨‍💻 Author

Made by **SUBI (슈퍼브레인)**  
🔗 Blog: <https://superbrainsb.tistory.com/85>
