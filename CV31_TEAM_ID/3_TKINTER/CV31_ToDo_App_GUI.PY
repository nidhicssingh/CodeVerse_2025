import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Functions
# ------------------------------
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        all_tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("📋 Your Tasks", all_tasks)
    else:
        messagebox.showinfo("📭 No Tasks", "Your to-do list is empty.")

# ------------------------------
# GUI Setup
# ------------------------------
root = tk.Tk()
root.title("📝 Fancy To-Do List")
root.geometry("400x500")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# Heading
label = tk.Label(root, text="My To-Do List 🗂️", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
label.pack(pady=20)

# Task Entry
entry = tk.Entry(root, font=("Helvetica", 14), width=28, bd=2, relief="solid", justify="center")
entry.pack(pady=10)

# Buttons Frame
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

add_btn = tk.Button(button_frame, text="➕ Add", command=add_task, bg="#4CAF50", fg="white", **btn_style)
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(button_frame, text="🗑️ Delete", command=delete_task, bg="#F44336", fg="white", **btn_style)
delete_btn.pack(side=tk.LEFT, padx=5)

view_btn = tk.Button(button_frame, text="👁️ View", command=view_tasks, bg="#2196F3", fg="white", **btn_style)
view_btn.pack(side=tk.LEFT, padx=5)

# Task Listbox
listbox_frame = tk.Frame(root)
listbox_frame.pack(padx=40,pady=20)

listbox = tk.Listbox(listbox_frame, width=40, height=15, font=("Helvetica", 12), bd=2, relief="groove", selectbackground="#ddd")
listbox.pack()

# Footer
footer = tk.Label(root, text="Created with ❤️ in Python", font=("Arial", 10), bg="#f5f5f5", fg="#888")
footer.pack(pady=10)

# Run the app
root.mainloop()