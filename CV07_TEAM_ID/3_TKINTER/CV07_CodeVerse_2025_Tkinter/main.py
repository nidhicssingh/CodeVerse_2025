import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DATA_FILE = "tasks.json"
PRIORITY_COLORS = {
    "High": "#e74c3c",
    "Medium": "#f39c12",
    "Low": "#2ecc71"
}


class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, text, priority):
        self.tasks.append({"text": text, "priority": priority, "completed": False})
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def toggle_completion(self, index, is_done):
        self.tasks[index]["completed"] = is_done
        self.save_tasks()


class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ToDo App - Tkinter Edition ✅")
        self.geometry("600x500")
        self.config(bg="#f7f7f7")

        self.task_manager = TaskManager(DATA_FILE)

        self.setup_ui()
        self.render_tasks()

    def setup_ui(self):
        tk.Label(self, text="📝 My Task List", font=("Helvetica", 20, "bold"), bg="#f7f7f7").pack(pady=10)

        input_frame = tk.Frame(self, bg="#f7f7f7")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.task_entry.grid(row=0, column=0, padx=10)

        self.priority_combo = ttk.Combobox(input_frame, values=["High", "Medium", "Low"], width=10, state="readonly")
        self.priority_combo.set("Medium")
        self.priority_combo.grid(row=0, column=1, padx=5)

        tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#3498db", fg="white", width=10).grid(row=0, column=2, padx=10)

        self.task_container = tk.Frame(self, bg="#f7f7f7")
        self.task_container.pack(fill="both", expand=True, pady=5)

        self.canvas = tk.Canvas(self.task_container, bg="#f7f7f7", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.task_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f7f7f7")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        priority = self.priority_combo.get()

        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return

        self.task_manager.add_task(task_text, priority)
        self.task_entry.delete(0, tk.END)
        self.render_tasks()

    def render_tasks(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.task_manager.tasks):
            self.create_task_widget(index, task)

    def create_task_widget(self, index, task):
        frame = tk.Frame(self.scrollable_frame, bg="#ffffff", pady=6)
        frame.pack(fill="x", padx=10, pady=4)

        var = tk.BooleanVar(value=task["completed"])

        def toggle():
            self.task_manager.toggle_completion(index, var.get())
            self.render_tasks()

        checkbox = tk.Checkbutton(frame, variable=var, command=toggle, bg="#ffffff")
        checkbox.pack(side="left", padx=5)

        style = ("Arial", 12, "italic") if task["completed"] else ("Arial", 12, "normal")
        color = "#95a5a6" if task["completed"] else "#2c3e50"

        label = tk.Label(frame, text=task["text"], font=style, fg=color, bg="#ffffff")
        label.pack(side="left", padx=10)

        prio_color = PRIORITY_COLORS[task["priority"]]
        prio_label = tk.Label(frame, text=task["priority"], font=("Arial", 10, "bold"),
                              bg=prio_color, fg="white", padx=8, pady=2)
        prio_label.pack(side="right", padx=10)

        delete_btn = tk.Button(frame, text="🗑", bg="#e74c3c", fg="white", width=3,
                               command=lambda: self.delete_task(index))
        delete_btn.pack(side="right", padx=5)

    def delete_task(self, index):
        self.task_manager.delete_task(index)
        self.render_tasks()


if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
