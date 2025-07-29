import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Functions
# ------------------------------
def add_task(event=None):
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("📝 Task Missing", "Please enter a task before adding!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected[0])
        confirm = messagebox.askyesno("🗑️ Delete Task", f"Delete this task?\n\n• {task}")
        if confirm:
            listbox.delete(selected[0])
    else:
        messagebox.showwarning("⚠️ No Task Selected", "Please choose a task to delete.")

def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        all_tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("📋 All Tasks", all_tasks)
    else:
        messagebox.showinfo("📭 Empty", "No tasks in your list.")

# ------------------------------
# GUI Setup
# ------------------------------
root = tk.Tk()
root.title("🌟 Glow To-Do List")
root.geometry("500x600")
root.configure(bg="#d0f4ff")  # Light sky theme
root.resizable(False, False)

# ------------------------------
# Heading
# ------------------------------
header = tk.Label(
    root, text="🚀 Task Tracker Pro", 
    font=("Segoe UI Black", 26, "bold"),
    bg="#d0f4ff", fg="#023e8a", pady=20
)
header.pack()

# ------------------------------
# Entry Box
# ------------------------------
entry = tk.Entry(
    root, font=("Segoe UI", 14), width=32,
    bd=0, relief="flat", bg="#ffffff", fg="#333",
    highlightthickness=2, highlightbackground="#90e0ef",
    justify="center"
)
entry.pack(pady=12)
entry.bind("<Return>", add_task)

# ------------------------------
# Buttons Frame
# ------------------------------
button_frame = tk.Frame(root, bg="#d0f4ff")
button_frame.pack(pady=10)

def glow_button(text, bg_color, cmd):
    return tk.Button(
        button_frame, text=text, command=cmd,
        font=("Segoe UI", 11, "bold"),
        bg=bg_color, fg="white", activebackground="#caf0f8",
        relief="flat", width=12, pady=6, bd=0, cursor="hand2"
    )

add_btn = glow_button("➕ Add", "#48cae4", add_task)
delete_btn = glow_button("🗑️ Delete", "#ff6b6b", delete_task)
view_btn = glow_button("👁️ View", "#5e60ce", view_tasks)

add_btn.grid(row=0, column=0, padx=8)
delete_btn.grid(row=0, column=1, padx=8)
view_btn.grid(row=0, column=2, padx=8)

# ------------------------------
# Listbox with Scrollbar
# ------------------------------
list_frame = tk.Frame(root, bg="#d0f4ff")
list_frame.pack(pady=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    list_frame, font=("Segoe UI", 12), width=45, height=14,
    bd=0, bg="#ffffff", fg="#222", selectbackground="#90e0ef",
    highlightthickness=1, relief="flat", yscrollcommand=scrollbar.set
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# ------------------------------
# Footer
# ------------------------------
footer = tk.Label(
    root, text="Made with 💙 using Tkinter", 
    font=("Segoe UI", 10), fg="#666", bg="#d0f4ff", pady=15
)
footer.pack()

# ------------------------------
# Launch App
# ------------------------------
root.mainloop()
