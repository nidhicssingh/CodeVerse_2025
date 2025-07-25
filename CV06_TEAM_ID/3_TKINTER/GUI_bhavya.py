import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Scientific Calculator with Unit Converter")
        self.root.geometry("500x650")
        self.expression = ""
        self.theme = "dark"

        self.create_widgets()
        self.bind_shortcuts()
        self.apply_theme()

    def create_widgets(self):
        # Entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 22), bd=5, relief="sunken", justify='right')
        self.entry.pack(fill="x", padx=10, pady=10, ipady=10)

        # Scientific buttons
        sci_frame = tk.Frame(self.root)
        sci_frame.pack(padx=10, pady=5)
        sci_buttons = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'x²', '1/x', 'π', 'e']
        for i, btn in enumerate(sci_buttons):
            tk.Button(sci_frame, text=btn, width=6, height=2, command=lambda b=btn: self.scientific_func(b)).grid(row=0, column=i, padx=2, pady=2)

        # Calculator buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(padx=10, pady=10)
        btns = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '⌫'],
            ['1', '2', '3', '-', '%'],
            ['0', '.', '=', '+', 'Theme']
        ]

        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                b = tk.Button(btn_frame, text=char, width=6, height=2, font=("Arial", 14), command=lambda ch=char: self.on_click(ch))
                b.grid(row=r, column=c, padx=5, pady=5)

        # Unit Converter
        convert_frame = tk.LabelFrame(self.root, text="🔁 Unit Converter", font=("Arial", 12))
        convert_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(convert_frame, text="Value:").grid(row=0, column=0, padx=5)
        self.unit_val = tk.Entry(convert_frame, width=10)
        self.unit_val.grid(row=0, column=1, padx=5)

        tk.Label(convert_frame, text="From:").grid(row=0, column=2)
        self.from_unit = ttk.Combobox(convert_frame, values=["cm", "m", "km", "g", "kg"], width=5, state="readonly")
        self.from_unit.set("cm")
        self.from_unit.grid(row=0, column=3)

        tk.Label(convert_frame, text="To:").grid(row=0, column=4)
        self.to_unit = ttk.Combobox(convert_frame, values=["cm", "m", "km", "g", "kg"], width=5, state="readonly")
        self.to_unit.set("m")
        self.to_unit.grid(row=0, column=5)

        tk.Button(convert_frame, text="Convert", command=self.convert_units).grid(row=0, column=6, padx=5)
        self.convert_result = tk.Label(convert_frame, text="", font=("Arial", 11, "italic"))
        self.convert_result.grid(row=1, column=0, columnspan=7)

    def on_click(self, ch):
        if ch == "C":
            self.expression = ""
        elif ch == "⌫":
            self.expression = self.expression[:-1]
        elif ch == "=":
            self.evaluate()
            return
        elif ch == "Theme":
            self.toggle_theme()
            return
        else:
            self.expression += str(ch)
        self.entry_var.set(self.expression)

    def scientific_func(self, func):
        try:
            value = float(self.entry_var.get())
            result = {
                "sin": math.sin(math.radians(value)),
                "cos": math.cos(math.radians(value)),
                "tan": math.tan(math.radians(value)),
                "log": math.log10(value),
                "exp": math.exp(value),
                "sqrt": math.sqrt(value),
                "x²": value ** 2,
                "1/x": 1 / value,
                "π": math.pi,
                "e": math.e
            }.get(func, value)
            self.expression = str(result)
            self.entry_var.set(self.expression)
        except Exception as e:
            self.entry_var.set("Error")

    def evaluate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.entry_var.set(self.expression)
        except ZeroDivisionError:
            self.entry_var.set("Cannot divide by zero")
        except Exception:
            self.entry_var.set("Error")

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.apply_theme()

    def apply_theme(self):
        dark = {"bg": "#2c2c2c", "fg": "#ffffff", "btn": "#444", "entry": "#3e3e3e"}
        light = {"bg": "#f9f9f9", "fg": "#000000", "btn": "#ddd", "entry": "#ffffff"}
        th = dark if self.theme == "dark" else light

        self.root.configure(bg=th["bg"])
        self.entry.configure(bg=th["entry"], fg=th["fg"])

        for widget in self.root.winfo_children():
            self.set_colors(widget, th)

    def set_colors(self, widget, theme):
        try:
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Entry) or isinstance(widget, tk.Label):
                widget.configure(bg=theme["btn"], fg=theme["fg"])
            if isinstance(widget, tk.LabelFrame) or isinstance(widget, tk.Frame):
                widget.configure(bg=theme["bg"])
            for child in widget.winfo_children():
                self.set_colors(child, theme)
        except:
            pass

    def convert_units(self):
        try:
            val = float(self.unit_val.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            # Conversion in meters or kg
            factor = {
                "cm": 0.01, "m": 1, "km": 1000,
                "g": 0.001, "kg": 1
            }

            if from_u in factor and to_u in factor:
                base = val * factor[from_u]
                result = base / factor[to_u]
                self.convert_result.config(text=f"{val} {from_u} = {round(result, 4)} {to_u}")
            else:
                self.convert_result.config(text="Invalid unit")
        except:
            self.convert_result.config(text="Error in conversion")

    def bind_shortcuts(self):
        self.root.bind('<Return>', lambda e: self.evaluate())
        self.root.bind('<Escape>', lambda e: self.clear())
        self.root.bind('<BackSpace>', lambda e: self.backspace())

    def clear(self):
        self.expression = ""
        self.entry_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry_var.set(self.expression)

# Run app
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
