"""
SUBI Unlock v1.0.4
PDF Permission Unlocker Tool (Offline)

Author: SUBI (SuperBrain, Sangbok Lee)
Email: contact.subi@gmail.com
Blog: https://superbrainsb.tistory.com/85
GitHub: https://github.com/SUBI-Tools/subi-unlock

License: CC BY-NC-ND 4.0 + custom restrictions
See LICENSE_CC_BY-NC-ND_WITH_CUSTOM.txt for details

Purpose:
This script is intended to remove editing and printing restrictions 
from PDF files that the user has legal access to but has forgotten the permission password.
It does NOT bypass viewing passwords or DRM protection.

Created: 2025-08-09
"""


import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import PyPDF2
import webbrowser

BLOG_LINK = "https://superbrainsb.tistory.com/85"
GS_EXECUTABLE = os.path.join(os.getcwd(), "ghostscript", "gswin64c.exe")

def validate_pdf(path):
    if not path.lower().endswith('.pdf'):
        return False, "PDF 파일만 가능합니다."
    try:
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            if reader.is_encrypted:
                try:
                    reader.decrypt('')
                except:
                    return False, "비밀번호 없이 못여는 PDF는 변환할 수 없습니다."
    except Exception:
        return False, "PDF 파일을 열 수 없습니다. 손상되었거나 DRM이 적용된 파일일 수 있습니다."
    return True, ""

def unlock_pdf(input_pdf):
    filename = os.path.basename(input_pdf)
    base, _ = os.path.splitext(filename)
    output_pdf = os.path.join(os.path.dirname(input_pdf), f"{base}_SUBI_unlocked.pdf")

    cmd = [
        GS_EXECUTABLE,
        "-sDEVICE=pdfwrite",
        "-dNOPAUSE",
        "-dBATCH",
        "-dSAFER",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return False, "Ghostscript 오류: DRM이 적용되었거나 변환에 실패했습니다."
    except FileNotFoundError:
        return False, "Ghostscript 실행 파일을 찾을 수 없습니다."

    return True, output_pdf

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

def show_done_popup():
    done_popup = tk.Toplevel(root)
    done_popup.title("완료")
    done_popup.resizable(False, False)
    done_popup.attributes('-topmost', True)
    done_popup.overrideredirect(True)  # 창 상단 최소/최대/닫기 버튼 제거
    center_window(done_popup, 400, 120)

    tk.Label(done_popup, text="PDF 변환이 완료되었습니다!\n5초 후 블로그 페이지로 이동합니다.").pack(padx=20, pady=10)

    def go_blog_and_exit():
        webbrowser.open(BLOG_LINK)
        done_popup.destroy()
        root.destroy()

    ok_btn = tk.Button(done_popup, text="확인", command=go_blog_and_exit)
    ok_btn.pack(pady=(0, 15))

    done_popup.after(5000, go_blog_and_exit)

def handle_drop(event):
    files = root.tk.splitlist(event.data)
    if len(files) != 1:
        messagebox.showerror("오류", "한 번에 한 개의 파일만 변환 가능합니다.")
        return

    filepath = files[0]

    valid, message = validate_pdf(filepath)
    if not valid:
        messagebox.showerror("오류", message)
        return

    converting = tk.Toplevel(root)
    converting.title("PDF 변환 중")
    label = tk.Label(converting, text="파일 변환이 진행중입니다.\n시간이 몇 분 정도로 오래 걸릴 수 있습니다.")
    label.pack(padx=20, pady=20)
    converting.attributes('-topmost', True)
    center_window(converting, 400, 100)
    converting.update()

    success, result = unlock_pdf(filepath)
    converting.destroy()

    if success:
        show_done_popup()
    else:
        messagebox.showerror("오류", result)

def show_dragdrop_ui():
    global root

    for widget in root.winfo_children():
        widget.destroy()

    try:
        from tkinterdnd2 import DND_FILES, TkinterDnD
        root.destroy()
        root = TkinterDnD.Tk()
        configure_window(root)
    except ImportError:
        pass

    label = tk.Label(root, text="🔓 여기에 PDF 파일을 가져다 놓으세요.", bg="lavender")
    label.pack(expand=True)

    try:
        root.drop_target_register('DND_Files')
        root.dnd_bind('<<Drop>>', handle_drop)
    except Exception:
        pass

def show_agreement_ui():
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="lavender")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = tk.Label(
        frame,
        text=(
            "이 프로그램은 편집 권한이 있는 PDF의 제한을 해제하기 위한 도구입니다.\n"
            "저작권 침해를 위한 용도로 사용할 수 없습니다.\n\n"
            "이 파일을 잠금해제하여 편집할 수 있는 권한이 있는 사람입니까?"
        ),
        bg="lavender",
        wraplength=win_width - 40,
        justify="center"
    )
    label.pack(pady=(10, 20))

    btn_frame = tk.Frame(frame, bg="lavender")
    btn_frame.pack()

    agree_btn = tk.Button(btn_frame, text="✅ 동의함", width=12, command=show_dragdrop_ui)
    disagree_btn = tk.Button(btn_frame, text="❌ 동의하지 않음", width=12, command=root.destroy)

    agree_btn.grid(row=0, column=0, padx=10)
    disagree_btn.grid(row=0, column=1, padx=10)

def configure_window(root_window):
    root_window.title("SUBI Unlock")
    root_window.configure(bg="lavender")
    screen_width = root_window.winfo_screenwidth()
    screen_height = root_window.winfo_screenheight()
    global win_width, win_height
    win_width = int(screen_width * 0.22)
    win_height = int(screen_height * 0.38)
    center_window(root_window, win_width, win_height)
    root_window.resizable(False, False)

root = tk.Tk()
configure_window(root)
show_agreement_ui()
root.mainloop()