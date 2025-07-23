import tkinter as tk
import math
from tkinter import messagebox

history = []

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            history.append(entry.get() + " = " + result)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "H":
        history_text = "\n".join(history[-5:])
        messagebox.showinfo("History", history_text)
    else:
        entry.insert(tk.END, text)

def scientific_mode():
    def calculate():
        try:
            val = float(scientific_entry.get())
            choice = operation.get()
            if choice == "sin":
                result = math.sin(math.radians(val))
            elif choice == "cos":
                result = math.cos(math.radians(val))
            elif choice == "tan":
                result = math.tan(math.radians(val))
            elif choice == "sqrt":
                result = math.sqrt(val)
            output_label.config(text="Result: " + str(result))
        except:
            output_label.config(text="Error")

    win = tk.Toplevel(root)
    win.title("Scientific Mode")
    scientific_entry = tk.Entry(win, font="Arial 16")
    scientific_entry.pack(pady=10, padx=10)
    operation = tk.StringVar(value="sin")
    tk.OptionMenu(win, operation, "sin", "cos", "tan", "sqrt").pack(pady=5)
    tk.Button(win, text="Calculate", command=calculate).pack(pady=5)
    output_label = tk.Label(win, text="", font="Arial 14")
    output_label.pack(pady=10)

root = tk.Tk()
root.geometry("350x500")
root.title("Meghana's GUI Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["H", "(", ")", "."]
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack()
    for b in row:
        btn = tk.Button(row_frame, text=b, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=3, pady=3)
        btn.bind("<Button-1>", click)

tk.Button(root, text="Scientific Mode", font="Arial 14", command=scientific_mode).pack(pady=10)

root.mainloop()