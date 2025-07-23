import tkinter as tk
from tkinter import messagebox

# -------------------------
# Subject-wise Quiz Data
# -------------------------
quiz_data = {
    "Python": [
        ("What keyword is used to define a function?", ["func", "def", "define", "lambda"], "def"),
        ("Which datatype is immutable in Python?", ["list", "set", "dictionary", "tuple"], "tuple"),
    ],
    "JavaScript": [
        ("Which method is used to output text in JS?", ["console.log()", "echo()", "print()", "write()"], "console.log()"),
        ("What is the datatype of NaN?", ["string", "undefined", "number", "object"], "number"),
    ],
    "Django": [
        ("Which command is used to start a new Django project?", ["django-admin startproject", "start django", "create-project", "manage.py runserver"], "django-admin startproject"),
        ("Which file contains the settings for a Django project?", ["urls.py", "views.py", "models.py", "settings.py"], "settings.py"),
    ]
}

# -------------------------
# Quiz Application
# -------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App - Python | JavaScript | Django")
        self.root.geometry("600x400")
        self.root.config(bg="#f2f2f2")

        self.subject = None
        self.questions = []
        self.current_q = 0
        self.score = 0

        self.build_subject_menu()

    def build_subject_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🧠 Choose a Subject", font=("Arial", 22, "bold"), bg="#f2f2f2").pack(pady=40)

        for subject in quiz_data.keys():
            tk.Button(self.root, text=subject, font=("Arial", 16), width=25,
                      command=lambda sub=subject: self.start_quiz(sub), bg="#4CAF50", fg="white").pack(pady=10)

    def start_quiz(self, subject):
        self.subject = subject
        self.questions = quiz_data[subject]
        self.current_q = 0
        self.score = 0
        self.display_question()

    def display_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        q, options, _ = self.questions[self.current_q]
        tk.Label(self.root, text=f"{self.subject} Quiz", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)
        tk.Label(self.root, text=f"Q{self.current_q + 1}: {q}", font=("Arial", 14), bg="#f2f2f2", wraplength=500).pack(pady=15)

        self.var = tk.StringVar()
        for opt in options:
            tk.Radiobutton(self.root, text=opt, variable=self.var, value=opt,
                           font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=100)

        tk.Button(self.root, text="Submit", command=self.check_answer,
                  font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=20)

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Select an Option", "Please select an answer before submitting.")
            return

        correct = self.questions[self.current_q][2]
        if selected == correct:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🎉 Quiz Completed!", font=("Arial", 22, "bold"), bg="#f2f2f2").pack(pady=40)
        tk.Label(self.root, text=f"Your Score: {self.score} / {len(self.questions)}",
                 font=("Arial", 18), bg="#f2f2f2").pack(pady=10)

        tk.Button(self.root, text="Take Another Quiz", command=self.build_subject_menu,
                  font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit,
                  font=("Arial", 14), bg="#f44336", fg="white").pack(pady=5)

# -------------------------
# Run the App
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()