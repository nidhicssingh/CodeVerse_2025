import tkinter as tk
from tkinter import ttk

memory = 0

def standard_calculator_menu(parent):
    def calculate(op):
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            if op == '+':
                result.set(a + b)
            elif op == '-':
                result.set(a - b)
            elif op == '*':
                result.set(a * b)
            elif op == '/':
                result.set("Error" if b == 0 else a / b)
        except:
            result.set("Invalid input")

    def memory_store():
        global memory
        memory = float(result.get())

    def memory_recall():
        result.set(memory)

    win = tk.Toplevel(parent)
    win.title("Standard Calculator")
    win.geometry("400x300")

    tk.Label(win, text="Number 1:").pack()
    entry1 = tk.Entry(win, font=("Arial", 14))
    entry1.pack()

    tk.Label(win, text="Number 2:").pack()
    entry2 = tk.Entry(win, font=("Arial", 14))
    entry2.pack()

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    for op in ['+', '-', '*', '/']:
        ttk.Button(btn_frame, text=op, command=lambda o=op: calculate(o)).pack(side='left', padx=5)

    result = tk.StringVar()
    tk.Label(win, textvariable=result, font=("Arial", 16)).pack(pady=10)

    ttk.Button(win, text="Memory Store", command=memory_store).pack()
    ttk.Button(win, text="Memory Recall", command=memory_recall).pack()
