import tkinter as tk
import math

def click(event):
    global expression
    expression += event.widget.cget("text")
    screen_var.set(expression)

def clear():
    global expression
    expression = ""
    screen_var.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        screen_var.set(result)
        expression = result
    except Exception as e:
        screen_var.set("Error")
        expression = ""

def square_root():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        screen_var.set(result)
        expression = result
    except:
        screen_var.set("Error")
        expression = ""

def power():
    global expression
    expression += "**"
    screen_var.set(expression)

def toggle_theme():
    global dark
    dark = not dark
    bg = "#1c1c1c" if dark else "#f0f0f0"
    fg = "#ffffff" if dark else "#000000"
    root.config(bg=bg)
    screen.config(bg=bg, fg=fg)
    for btn in buttons:
        btn.config(bg=bg, fg=fg)

# GUI setup
root = tk.Tk()
root.geometry("400x550")
root.title("Tkinter Calculator")
expression = ""
dark = False

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 24", bd=10, relief="ridge", justify="right")
screen.pack(fill="both", ipadx=8, ipady=15, pady=20)

frame = tk.Frame(root)
frame.pack()

buttons = []
btn_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["√", "^", "Theme"]
]

for row in btn_texts:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for item in row:
        if item == "=":
            b = tk.Button(row_frame, text=item, font="Arial 18", width=6, command=calculate)
        elif item == "C":
            b = tk.Button(row_frame, text=item, font="Arial 18", width=6, command=clear)
        elif item == "√":
            b = tk.Button(row_frame, text=item, font="Arial 18", width=6, command=square_root)
        elif item == "^":
            b = tk.Button(row_frame, text=item, font="Arial 18", width=6, command=power)
        elif item == "Theme":
            b = tk.Button(row_frame, text=item, font="Arial 18", width=13, command=toggle_theme)
        else:
            b = tk.Button(row_frame, text=item, font="Arial 18", width=6)
            b.bind("<Button-1>", click)
        b.pack(side="left", padx=5, pady=5)
        buttons.append(b)

root.mainloop()