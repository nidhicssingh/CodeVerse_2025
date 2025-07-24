import tkinter as tk
from tkinter import messagebox

# --------- Functions ---------
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, f"🔲 {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showinfo("Info", "Please select a task to delete.")

def mark_complete():
    selected = task_listbox.curselection()
    if selected:
        current = task_listbox.get(selected)
        if current.startswith("🔲"):
            task_listbox.delete(selected)
            task_listbox.insert(selected, current.replace("🔲", "✅"))
        elif current.startswith("✅"):
            task_listbox.delete(selected)
            task_listbox.insert(selected, current.replace("✅", "🔲"))

def clear_all():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)

# --------- GUI Setup ---------
root = tk.Tk()
root.title("To-Do App")
root.geometry("500x600")
root.configure(bg="#f0f8ff")

title = tk.Label(root, text="📝 My To-Do List", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=25, bd=3)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(input_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
add_button.pack(side=tk.LEFT)

# Task list
task_frame = tk.Frame(root, bg="#f0f8ff")
task_frame.pack(pady=20)

task_listbox = tk.Listbox(task_frame, width=40, height=12, font=("Helvetica", 14), bd=3, selectbackground="#90ee90")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#f0f8ff")
buttons_frame.pack(pady=20)

complete_btn = tk.Button(buttons_frame, text="Mark Completed", command=mark_complete, bg="#2196F3", fg="white", width=15)
complete_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(buttons_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", width=15)
delete_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(root, text="Clear All Tasks", command=clear_all, bg="#FF9800", fg="white", font=("Helvetica", 12, "bold"), width=20)
clear_btn.pack(pady=10)

footer = tk.Label(root, text="✨ Stay Organized!", font=("Helvetica", 10), bg="#f0f8ff", fg="gray")
footer.pack(pady=5)

root.mainloop()
