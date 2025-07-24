import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x550")
        self.root.configure(bg="lavender")

        self.tasks = []

        # Heading
        heading = tk.Label(root, text="My Tasks", font=("Arial", 20, "bold"), bg="#aa88c7", fg="#2c1c37")
        heading.pack(pady=15)

        # Entry box (styled)
        self.entry = tk.Entry(root, font=("Arial", 14), bd=0, relief="flat", justify="left",
                              bg="white", fg="#2c3e50", insertbackground="#2c3e50")
        self.entry.pack(pady=10, padx=20, fill="x", ipady=10)
        self.entry.configure(highlightbackground="#ccc", highlightthickness=1)

        # Button Frame
        button_frame = tk.Frame(root, bg="#e5e081")
        button_frame.pack(pady=10)

        self.add_btn = tk.Button(button_frame, text=" Add", font=("Helvetica", 12, "bold"),
                                 bg="#27ae60", fg="white", width=10, bd=0, command=self.add_task,
                                 activebackground="#2ecc71")
        self.add_btn.pack(side="left", padx=5)

        self.view_btn = tk.Button(button_frame, text=" View", font=("Helvetica", 12, "bold"),
                                  bg="#2980b9", fg="white", width=10, bd=0, command=self.view_tasks,
                                  activebackground="#3498db")
        self.view_btn.pack(side="left", padx=5)

        # Task frame
        self.task_frame = tk.Frame(root, bg="#1a446d")
        self.task_frame.pack(fill="both", expand=True, pady=10)

        # Footer
        footer = tk.Label(root, text="Made with ❤️ in Python", font=("Helvetica", 10),
                          bg="#cb62cb", fg="#95a5a6")
        footer.pack(pady=5)

        self.refresh_tasks()

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({'text': task_text, 'done': False})
            self.entry.delete(0, tk.END)
            self.refresh_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.refresh_tasks()

    def mark_done(self, index):
        self.tasks[index]['done'] = not self.tasks[index]['done']
        self.refresh_tasks()

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("📭 No Tasks", "Your to-do list is empty.")
        else:
            task_list = ""
            for i, task in enumerate(self.tasks):
                status = "✔" if task['done'] else "✖"
                task_list += f"{i + 1}. {status} {task['text']}\n"
            messagebox.showinfo("📋 Your Tasks", task_list)

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            card = tk.Frame(self.task_frame, bg="white", bd=0, relief="flat")
            card.pack(fill="x", padx=20, pady=6)

            display_text = f"✔ {task['text']}" if task['done'] else task['text']
            color = "#27ae60" if task['done'] else "#2c3e50"

            task_label = tk.Label(card, text=display_text, font=("Helvetica", 12), bg="white", fg=color, anchor="w")
            task_label.pack(side="left", fill="x", expand=True, padx=(10, 0), pady=5)

            done_btn = tk.Button(card, text="✅" if not task['done'] else "↩️", font=("Helvetica", 10),
                                 command=lambda i=i: self.mark_done(i),
                                 bg="#ecf0f1", fg="#34495e", width=3, bd=0, activebackground="#d0d3d4")
            done_btn.pack(side="right", padx=5)

            del_btn = tk.Button(card, text="🗑️", font=("Helvetica", 10),
                                command=lambda i=i: self.delete_task(i),
                                bg="#ecf0f1", fg="#c0392b", width=3, bd=0, activebackground="#e74c3c")
            del_btn.pack(side="right", padx=5)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
