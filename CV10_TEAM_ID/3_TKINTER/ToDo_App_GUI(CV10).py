import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

tasks = [] 
def refresh_list():
    listbox.delete(0, tk.END)
    for i, (task, done, due) in enumerate(tasks):
        status = "✅" if done else "❌"
        due_text = f"(Due: {due})" if due else ""
        listbox.insert(tk.END, f"{i+1}. {status} {task} {due_text}")

def add_task():
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    due_date = simpledialog.askstring("Due Date", "Optional: Enter due date (e.g., 2025-08-01)")
    tasks.append((task, False, due_date))
    entry.delete(0, tk.END)
    refresh_list()

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        refresh_list()
    else:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def toggle_done():
    selected = listbox.curselection()
    if selected:
        i = selected[0]
        task, done, due = tasks[i]
        tasks[i] = (task, not done, due)
        refresh_list()
    else:
        messagebox.showwarning("Selection Error", "Select a task to mark done/undone.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task, done, due in tasks:
            f.write(f"{task}|{done}|{due}\n")
    messagebox.showinfo("Saved", "Tasks saved successfully.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks.clear()
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    task, done, due = parts
                    tasks.append((task, done == 'True', due if due != 'None' else None))
        refresh_list()
        messagebox.showinfo("Loaded", "Tasks loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved task file found.")

def search_task():
    keyword = simpledialog.askstring("Search Task", "Enter keyword to search:")
    if not keyword:
        return
    filtered = [f"{i+1}. {'✅' if done else '❌'} {task} (Due: {due})"
                for i, (task, done, due) in enumerate(tasks)
                if keyword.lower() in task.lower()]
    result = "\n".join(filtered) if filtered else "No matching tasks found."
    messagebox.showinfo("Search Results", result)

root = tk.Tk()
root.title("🌟 Advanced To-Do List")
root.geometry("500x600")
root.configure(bg="#fffbe7")

tk.Label(root, text="My To-Do List ✅", font=("Helvetica", 20, "bold"), bg="#fffbe7", fg="#3e3e3e").pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 14), width=35, bd=2, relief="groove")
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#fffbe7")
button_frame.pack(pady=10)

btn_style = {"font": ("Arial", 11), "padx": 8, "pady": 4, "bd": 0}

tk.Button(button_frame, text="➕ Add", bg="#4CAF50", fg="white", command=add_task, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="🗑️ Delete", bg="#f44336", fg="white", command=delete_task, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✔️ Done", bg="#2196F3", fg="white", command=toggle_done, **btn_style).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="💾 Save", bg="#607d8b", fg="white", command=save_tasks, **btn_style).grid(row=1, column=0, pady=5)
tk.Button(button_frame, text="📂 Load", bg="#795548", fg="white", command=load_tasks, **btn_style).grid(row=1, column=1, pady=5)
tk.Button(button_frame, text="🔍 Search", bg="#9c27b0", fg="white", command=search_task, **btn_style).grid(row=1, column=2, pady=5)

listbox = tk.Listbox(root, width=50, height=15, font=("Courier New", 12), bd=2, relief="ridge", selectbackground="#cce7e8")
listbox.pack(pady=20)

tk.Label(root, text="💡 Tip: Double-click task to mark as done!", bg="#fffbe7", fg="#888", font=("Arial", 10)).pack()
tk.Label(root, text="Made with ❤️ in Python", font=("Arial", 9), bg="#fffbe7", fg="#aaa").pack(pady=5)

def on_double_click(event):
    toggle_done()
listbox.bind("<Double-1>", on_double_click)

root.mainloop()
