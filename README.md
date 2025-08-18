SUBI Unlock v1.0.6
==================

SUBI Unlock is a lightweight, offline PDF restriction removal tool that runs without installation.
Drag and drop a single PDF file onto the window to remove editing, printing, and copying restrictions, then save as a new file.

Purpose
-------
This tool is designed for convenience with your own personal documents, for cases such as:
- You previously set editing/printing restrictions,
- You forgot the permission password,
- The file is viewable but restricted.

※ Do not use this tool to unlock PDFs belonging to others or files you are not legally authorized to modify.

What's New in 1.0.6 (2025.Aug.18)
---------------------------------
- Optimized program size
- Partially resolved Windows security false-positive issues
- English version separately released
- File-selection button disabled again

What's New in 1.0.5
-------------------
- Improved processing speed
- Unlock possible for certain files that previously failed
- Better preservation of original quality
- Automatically opens the unlocked PDF after processing
- Added file-selection button in addition to Drag & Drop

Features
--------
- Drag & Drop: simply drag one PDF file into the window.
- Remove restrictions on editing, printing, and copying.
- Fully offline: all processing is done locally (no uploads).
- No installation: just extract and run the EXE.
- Original file preserved; output file saved in the same folder as *_SUBI_unlocked.pdf.
- Automatically open the unlocked PDF upon completion.

Limitations
-----------
- Cannot open PDFs that require a password just to view.
- Does not remove DRM (Digital Rights Management).
- Works only on already viewable PDFs, removing editing/printing/copying restrictions.

How to Use
----------
1. Fully extract the ZIP file (do not run from inside a compressed folder).
2. Run SUBI_unlock_v1.0.6.exe.
3. Drag & drop a single PDF file onto the app window.
4. A new file named *_SUBI_unlocked.pdf will be created in the same folder and opened automatically.
5. A success popup will appear: after 5 seconds, it will automatically open the developer’s blog. Clicking “OK” will move immediately. The program then exits.

How it Works
------------
- Internally uses qpdf (unlockpdf/bin/qpdf.exe).
- No network connection required; all processing happens locally.
- The unlocked file opens with your system’s default PDF viewer (Edge, Acrobat, etc.).

Folder Structure
----------------
SUBI_unlock_v1.0.6/
├─ SUBI_unlock_v1.0.6.exe
├─ LICENSE.txt
├─ README.txt (or README.md)
└─ THIRD_PARTY_LICENSES/
   └─ qpdf-LICENSE.txt

Troubleshooting
---------------
- Result does not open → Ensure a default PDF viewer is set in Windows.
- Unlock fails → If the file cannot be opened without a password, it cannot be unlocked.

License
-------
- App (SUBI Unlock): Proprietary EULA (non-open license).
  Redistribution, modification, and reverse engineering are prohibited.
  See LICENSE.txt for details.

- Third-party software: qpdf is distributed under the Apache License 2.0.
  Full text is included in THIRD_PARTY_LICENSES/qpdf-LICENSE.txt.

- Note: From v1.0.5 onward, Ghostscript is no longer used. GS-related notices have been removed.

Author
------
Made by SUBI (Superbrain)
Blog: https://superbrainsb.tistory.com/86
