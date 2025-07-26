import tkinter as tk
from tkinter import ttk
import math

# Main window
root = tk.Tk()
root.title("Enhanced GUI Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

expression = ""
history = []

# Display frame
display_var = tk.StringVar()
display = ttk.Entry(root, textvariable=display_var, font=("Arial", 24), justify="right")
display.pack(fill="x", padx=10, pady=10)

# History frame
history_frame = tk.Frame(root, bg="#e0e0e0")
history_frame.pack(fill="both", expand=True, padx=10, pady=5)
history_label = tk.Label(history_frame, text="History", bg="#e0e0e0", font=("Arial", 12))
history_label.pack()
history_listbox = tk.Listbox(history_frame, height=5)
history_listbox.pack(fill="both", expand=True)

# Button click handler
def press(key):
    global expression
    expression += str(key)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        history.append(expression + " = " + result)
        history_listbox.insert(tk.END, expression + " = " + result)
        expression = ""
    except:
        display_var.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        display_var.set(result)
        history.append("√" + expression + " = " + result)
        history_listbox.insert(tk.END, "√" + expression + " = " + result)
        expression = ""
    except:
        display_var.set("Error")
        expression = ""

def power():
    global expression
    expression += "**"

def pi():
    global expression
    expression += str(math.pi)
    display_var.set(expression)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', '√', '^', 'π']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: (
            calculate() if x == '=' else
            clear() if x == 'C' else
            sqrt() if x == '√' else
            power() if x == '^' else
            pi() if x == 'π' else
            press(x)
        )
        tk.Button(frame, text=btn, font=("Arial", 18), command=action).pack(side="left", expand=True, fill="both")

root.mainloop()