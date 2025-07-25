import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# ------------------------------
# Functions
# ------------------------------
def add_task():
    task = entry.get().strip()
    priority = priority_var.get()
    if task:
        full_task = f"[{priority}] {task}"
        listbox.insert(tk.END, full_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        if not task.startswith("✅"):
            listbox.delete(index)
            listbox.insert(index, "✅ " + task)
    else:
        messagebox.showwarning("Selection Error", "Select a task to mark as done.")

def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        all_tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("📋 Your Tasks", all_tasks)
    else:
        messagebox.showinfo("📭 No Tasks", "Your to-do list is empty.")

def search_task():
    query = simpledialog.askstring("Search Task 🔍", "Enter task keyword:")
    if query:
        results = [task for task in listbox.get(0, tk.END) if query.lower() in task.lower()]
        if results:
            messagebox.showinfo("🔎 Search Results", "\n".join(results))
        else:
            messagebox.showinfo("No Match", "No task matched your search.")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully.")
    else:
        messagebox.showwarning("Nothing to Save", "Add tasks first.")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        listbox.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())

def toggle_theme():
    if root["bg"] == "#f5f5f5":
        root.configure(bg="#2c2c2c")
        listbox.configure(bg="#3e3e3e", fg="white", selectbackground="#606060")
        footer.configure(bg="#2c2c2c", fg="#bbb")
        label.configure(bg="#2c2c2c", fg="#ffccff")
        button_frame.configure(bg="#2c2c2c")
    else:
        root.configure(bg="#f5f5f5")
        listbox.configure(bg="white", fg="black", selectbackground="#ddd")
        footer.configure(bg="#f5f5f5", fg="#888")
        label.configure(bg="#f5f5f5", fg="#333")
        button_frame.configure(bg="#f5f5f5")

# ------------------------------
# GUI Setup
# ------------------------------
root = tk.Tk()
root.title("✨ Advanced To-Do List")
root.geometry("460x600")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

label = tk.Label(root, text="My Creative To-Do List 🌟", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
label.pack(pady=20)

# Entry and Priority
entry_frame = tk.Frame(root, bg="#f5f5f5")
entry_frame.pack()

entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=24, bd=2, relief="solid", justify="center")
entry.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(entry_frame, priority_var, "High", "Medium", "Low")
priority_menu.config(font=("Helvetica", 10))
priority_menu.grid(row=0, column=1)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

btn_style = {
    "font": ("Helvetica", 10, "bold"),
    "bd": 0,
    "width": 10,
    "padx": 5,
    "pady": 5,
    "activebackground": "#e0e0e0"
}

tk.Button(button_frame, text="➕ Add", command=add_task, bg="#4CAF50", fg="white", **btn_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="🗑️ Delete", command=delete_task, bg="#F44336", fg="white", **btn_style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✅ Done", command=mark_completed, bg="#9C27B0", fg="white", **btn_style).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="🔍 Search", command=search_task, bg="#3F51B5", fg="white", **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="💾 Save", command=save_tasks, bg="#009688", fg="white", **btn_style).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="📂 Load", command=load_tasks, bg="#795548", fg="white", **btn_style).grid(row=1, column=2, padx=5, pady=5)

# Task Listbox
listbox_frame = tk.Frame(root)
listbox_frame.pack(padx=20, pady=20)

listbox = tk.Listbox(listbox_frame, width=45, height=15, font=("Helvetica", 12), bd=2, relief="groove", selectbackground="#ddd")
listbox.pack()

# Bottom Controls
tk.Button(root, text="👁️ View All Tasks", command=view_tasks, bg="#607D8B", fg="white", **btn_style).pack(pady=5)
tk.Button(root, text="🌓 Toggle Theme", command=toggle_theme, bg="#E91E63", fg="white", **btn_style).pack()

# Footer
footer = tk.Label(root, text="Made with 💙 using Tkinter", font=("Arial", 10), bg="#f5f5f5", fg="#888")
footer.pack(pady=10)

root.mainloop()
