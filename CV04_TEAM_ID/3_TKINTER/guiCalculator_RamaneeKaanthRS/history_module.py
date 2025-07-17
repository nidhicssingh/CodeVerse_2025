import tkinter as tttk
from tkinter import ttk, messagebox

class HistoryPanel:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.history = app.history if hasattr(app, "history") else []
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.app.root, text="Calculation History", font=("Segoe UI", 16)).pack(pady=10)

        history_box = ttk.Frame(self.app.root)
        history_box.pack(padx=10, pady=10, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(history_box)
        scrollbar.pack(side="right", fill="y")

        listbox = ttk.Listbox(history_box, yscrollcommand=scrollbar.set, font=("Segoe UI", 12))
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)

        for item in self.history[-10:]:
            listbox.insert("end", item)

        ttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=10)
