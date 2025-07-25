import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete")

def clear_all():
    listbox.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=10, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

# Task list display
listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
