
import tkinter as tk
from tkinter import messagebox

# ------------------ Quiz Data ------------------
questions = [
    "Which language is used for web development?",
    "Who developed Python language?",
    "Which planet is known as the Red Planet?",
    "Which keyword is used to define a function in Python?"
]

options = [
    ["Python", "Java", "HTML", "C++"],
    ["Guido van Rossum", "Elon Musk", "James Gosling", "Mark Zuckerberg"],
    ["Earth", "Venus", "Mars", "Jupiter"],
    ["func", "def", "function", "define"]
]

answers = [0, 2, 0, 2, 1]  # Indexes of correct answers

# ------------------ GUI Setup ------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        self.q_no = 0
        self.score = 0
        self.selected = tk.IntVar()
        
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Quiz Time!", font=("Arial", 20, "bold"), fg="violet")
        self.title.pack(pady=20)

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.selected, value=i, font=("Arial", 12))
            btn.pack(anchor="w", padx=100)
            self.radio_buttons.append(btn)

        self.next_btn = tk.Button(self.root, text="Next", command=self.next_question, bg="green", fg="white", font=("Arial", 12, "bold"))
        self.next_btn.pack(pady=20)

    def display_question(self):
        self.selected.set(-1)
        self.question_label.config(text=questions[self.q_no])
        for i in range(4):
            self.radio_buttons[i].config(text=options[self.q_no][i])

    def next_question(self):
        selected_ans = self.selected.get()
        if selected_ans == -1:
            messagebox.showwarning("Select an answer", "Please select an option before continuing.")
            return

        if selected_ans == answers[self.q_no]:
            self.score += 1

        self.q_no += 1
        if self.q_no >= len(questions):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        result = f"Your Score: {self.score} / {len(questions)}"
        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 20, "bold"), fg="purple").pack(pady=20)
        tk.Label(self.root, text=result, font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.destroy, bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# ------------------ Run App ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
