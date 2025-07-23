import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Warning", "Please enter a task.")

def remove_task():
    index = lb.curselection()
    if index:
        removed = tasks.pop(index[0])
        update_listbox()
        messagebox.showinfo("✅ Removed", f"Removed: {removed}")
    else:
        messagebox.showwarning("⚠️ Warning", "Please select a task to remove.")

def update_listbox():
    lb.delete(0, tk.END)
    for t in tasks:
        lb.insert(tk.END, t)

# ——— GUI Setup ———
root = tk.Tk()
root.title("📋 TO‑DO LIST — Meghana")  # Added your name here
root.geometry("400x500")

tk.Label(root, text="My To‑Do List", font=("Arial", 18, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5, padx=20, fill="x")
entry.focus()

add_btn = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_btn.pack(pady=5)

remove_btn = tk.Button(root, text="Remove Task", font=("Arial", 14), command=remove_task)
remove_btn.pack(pady=5)

lb = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
lb.pack(pady=10, padx=20, fill="both", expand=True)

root.mainloop()
