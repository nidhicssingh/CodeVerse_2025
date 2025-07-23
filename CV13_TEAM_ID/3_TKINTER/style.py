import tkinter as tk

def apply_style(root):
    root.configure(bg="#1e1e2e")
    style = {
        "font": ("Segoe UI", 12),
        "bg": "#1e1e2e",
        "fg": "#ffffff",
        "padx": 10,
        "pady": 5
    }

    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Entry, tk.Button)):
            widget.configure(**style)
            widget.configure(relief=tk.RAISED, bd=2)
            if isinstance(widget, tk.Entry):
                widget.configure(insertbackground="white")
