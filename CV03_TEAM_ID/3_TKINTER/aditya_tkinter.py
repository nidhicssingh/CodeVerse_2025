import tkinter as tk

def say_hello():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

label = tk.Label(root, text="Welcome!", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

root.mainloop()