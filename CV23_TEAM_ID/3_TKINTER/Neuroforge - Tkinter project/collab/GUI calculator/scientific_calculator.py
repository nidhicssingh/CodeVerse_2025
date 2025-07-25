import tkinter as tk
from tkinter import ttk, messagebox
import math

def scientific_calculator_menu(parent):
    def calculate():
        try:
            val1 = float(entry1.get())
            val2 = float(entry2.get()) if entry2.winfo_ismapped() else None
            op = operation.get()

            if op == "Power":
                result.set(math.pow(val1, val2))
            elif op == "Square Root":
                result.set(math.sqrt(val1))
            elif op == "Logarithm":
                result.set(math.log(val1, 10))
            elif op == "Sine":
                result.set(math.sin(math.radians(val1)))
            elif op == "Cosine":
                result.set(math.cos(math.radians(val1)))
            elif op == "Tangent":
                result.set(math.tan(math.radians(val1)))
            elif op == "Factorial":
                result.set(math.factorial(int(val1)))
            elif op == "Absolute":
                result.set(abs(val1))
            elif op == "Modulus":
                result.set(val1 % val2)
            elif op == "Exponential":
                result.set(math.exp(val1))
            else:
                result.set("Invalid operation")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def toggle_entry2(*args):
        op = operation.get()
        if op in ["Power", "Modulus"]:
            entry2.pack(pady=5)
            lbl2.pack(pady=2)
        else:
            entry2.pack_forget()
            lbl2.pack_forget()

    win = tk.Toplevel(parent)
    win.title("Scientific Calculator")
    win.geometry("400x400")

    tk.Label(win, text="Select Operation:", font=("Helvetica", 12)).pack(pady=5)
    operation = ttk.Combobox(win, values=[
        "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent",
        "Factorial", "Absolute", "Modulus", "Exponential"
    ])
    operation.set("Sine")
    operation.pack()
    operation.bind("<<ComboboxSelected>>", toggle_entry2)

    tk.Label(win, text="Value 1:", font=("Helvetica", 12)).pack()
    entry1 = tk.Entry(win, font=("Helvetica", 12))
    entry1.pack(pady=5)

    lbl2 = tk.Label(win, text="Value 2:", font=("Helvetica", 12))
    entry2 = tk.Entry(win, font=("Helvetica", 12))

    result = tk.StringVar()
    ttk.Button(win, text="Calculate", command=calculate).pack(pady=10)
    tk.Label(win, textvariable=result, font=("Helvetica", 14), fg="green").pack(pady=10)

    toggle_entry2()  # Initial call
