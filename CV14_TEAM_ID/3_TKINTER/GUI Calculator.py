import tkinter as tk
import math

# Function to update display
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# Function to evaluate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to square root
def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Tkinter Calculator")
root.configure(bg="#2c3e50")
root.geometry("350x450")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Button design
button_font = ("Arial", 18)
btn_color = "#ecf0f1"
btn_active = "#bdc3c7"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('CE', 5, 0), ('√', 5, 1)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'CE':
        action = clear
    elif text == '√':
        action = sqrt
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, font=button_font, width=5, height=2, bg=btn_color, activebackground=btn_active,
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Fill empty space in row 5
tk.Label(root, bg="#2c3e50").grid(row=5, column=2)
tk.Label(root, bg="#2c3e50").grid(row=5, column=3)

root.mainloop()
