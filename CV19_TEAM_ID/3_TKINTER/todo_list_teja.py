import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)

# List to store tasks
tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        listbox.delete(task_index)
        tasks.pop(task_index)
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        task = tasks[task_index]
        if not task.startswith("✔ "):
            tasks[task_index] = "✔ " + task
        else:
            tasks[task_index] = task.replace("✔ ", "")
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Select a task to mark done.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# UI Components
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=45, height=15, selectbackground="lightblue")
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=0, padx=10)

done_btn = tk.Button(btn_frame, text="Mark Done", command=mark_done)
done_btn.grid(row=0, column=1, padx=10)

# Start the app
root.mainloop()
