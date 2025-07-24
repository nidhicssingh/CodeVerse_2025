import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.tasks = []

        self.entry = tk.Entry(root, font="Arial 14")
        self.entry.pack(pady=10, fill="x", padx=10)

        self.add_btn = tk.Button(root, text="Add Task", font="Arial 12", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_frame = tk.Frame(root)
        self.task_frame.pack(fill="both", expand=True)

        self.refresh_tasks()

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.entry.delete(0, tk.END)
            self.refresh_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame, bd=1, relief=tk.SOLID, padx=10, pady=5)
            frame.pack(fill="x", pady=5, padx=10)

            task_label = tk.Label(frame, text=task, font="Arial 12", anchor="w")
            task_label.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑️", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
