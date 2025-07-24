import tkinter as tttk
from tkinter import ttk, messagebox

class StandardCalculator:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        tttk.Label(self.app.root, text="Standard Calculator", font=("Segoe UI", 16)).pack(pady=5, padx=10, fill="x", expand=True)

        self.entry = tttk.Entry(self.app.root, font=("Segoe UI", 14))
        self.entry.pack(pady=5, padx=10, fill="x", expand=True)
        self.result_label = tttk.Label(self.app.root, text="Standard Result:", font=("Segoe UI", 12))
        self.result_label.pack(pady=5, padx=10, fill="x", expand=True)

        btns_frame = tttk.Frame(self.app.root)
        btns_frame.pack(pady=5, padx=10, fill="x", expand=True)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                tttk.Button(
                    btns_frame, text=char, width=5,
                    command=lambda c=char: self.on_button_click(c)
                ).grid(row=r, column=c, padx=5, pady=5)

        tttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=5, padx=10, fill="x", expand=True)
        self.app.root.bind('<Key>', self.on_key_press)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, 'end')
            self.result_label.config(text="Standard Result:")
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.result_label.config(text=f"Result: {result}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert('end', char)

    def on_key_press(self, event):
        if event.char in '0123456789+-*/.=':
            self.on_button_click(event.char)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':
            current = self.entry.get()
            self.entry.delete(0, 'end')
            self.entry.insert(0, current[:-1])

