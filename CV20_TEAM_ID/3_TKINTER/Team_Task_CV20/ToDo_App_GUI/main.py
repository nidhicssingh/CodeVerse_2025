import tkinter as tk
from tkinter import messagebox, ttk
import os

tasks_file = "tasks.txt"

def save_tasks():
    with open(tasks_file, "w") as f:
        for task in listbox.get(0, tk.END):
            f.write(task + "\n")

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

def add_task():
    task = entry.get().strip()
    category = category_var.get()
    if task:
        task_full = f"[{category}] {task}"
        listbox.insert(tk.END, task_full)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        all_tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("📋 Your Tasks", all_tasks)
    else:
        messagebox.showinfo("📭 No Tasks", "Your to-do list is empty.")

def toggle_theme():
    global is_dark
    is_dark = not is_dark
    bg = "#2c2c2c" if is_dark else "#f5f5f5"
    fg = "#ffffff" if is_dark else "#333"
    root.configure(bg=bg)
    label.config(bg=bg, fg=fg)
    button_frame.config(bg=bg)
    footer.config(bg=bg, fg="#888")
    entry.config(bg="#fff" if not is_dark else "#555", fg=fg)
    listbox.config(bg="#fff" if not is_dark else "#444", fg=fg)

# GUI Setup
root = tk.Tk()
root.title("📝 Enhanced To-Do List")
root.geometry("450x550")
root.configure(bg="#f5f5f5")
root.resizable(False, False)
is_dark = False

label = tk.Label(root, text="To-Do List 🗂️", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=30, bd=2, relief="solid", justify="center")
entry.pack(pady=5)

category_var = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=category_var, values=["Work", "Personal", "Urgent", "Other"])
category_menu.set("Work")
category_menu.pack(pady=5)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

btn_style = {
    "font": ("Helvetica", 12, "bold"),
    "bd": 0,
    "width": 12,
    "padx": 5,
    "pady": 5,
    "activebackground": "#e0e0e0"
}

tk.Button(button_frame, text="➕ Add", command=add_task, bg="#4CAF50", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="🗑️ Delete", command=delete_task, bg="#F44336", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="👁️ View", command=view_tasks, bg="#2196F3", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=15)
listbox = tk.Listbox(listbox_frame, width=45, height=12, font=("Helvetica", 12), bd=2, relief="groove", selectbackground="#ddd")
listbox.pack()

toggle_btn = tk.Button(root, text="🌗 Toggle Theme", command=toggle_theme, bg="#888", fg="white", **btn_style)
toggle_btn.pack(pady=10)

footer = tk.Label(root, text="Created with ❤️ in Python", font=("Arial", 10), bg="#f5f5f5", fg="#888")
footer.pack(pady=10)

load_tasks()
root.mainloop()
