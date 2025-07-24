import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("ToDo App - Sanjana")
root.geometry("400x450")
root.config(bg="#e6f2ff")  # Light blue background
title = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#e6f2ff")
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
task_entry.pack(pady=5)
task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12), selectbackground="skyblue")
task_listbox.pack(pady=10)
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, "✔️ " + task)
    except:
        messagebox.showwarning("Warning", "Please select a task to mark done!")
button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#b3e0ff")
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="#ff9999")
del_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", width=12, command=mark_done, bg="#b3ffb3")
done_btn.grid(row=0, column=2, padx=5)
root.mainloop()
