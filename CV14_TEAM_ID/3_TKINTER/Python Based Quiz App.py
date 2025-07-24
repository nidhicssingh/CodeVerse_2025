import tkinter as tk
from tkinter import messagebox

# --------------- QUIZ DATA (5 Subjects) ---------------
quiz_data = {
    "Math": [
        ("What is 5 + 7?", "12", ["10", "11", "12", "13"]),
        ("Square root of 64?", "8", ["6", "7", "8", "9"]),
    ],
    "Science": [
        ("What planet is known as the Red Planet?", "Mars", ["Earth", "Venus", "Mars", "Jupiter"]),
        ("What gas do plants breathe in?", "Carbon Dioxide", ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"]),
    ],
    "GK": [
        ("Capital of India?", "New Delhi", ["Mumbai", "Chennai", "New Delhi", "Bangalore"]),
        ("Who is the father of the nation?", "Mahatma Gandhi", ["Nehru", "Mahatma Gandhi", "Subhas Bose", "Ambedkar"]),
    ],
    "Computer": [
        ("CPU stands for?", "Central Processing Unit", ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Control Processing Unit"]),
        ("Shortcut for copy?", "Ctrl+C", ["Ctrl+V", "Ctrl+X", "Ctrl+C", "Ctrl+Z"]),
    ],
    "History": [
        ("Who discovered America?", "Christopher Columbus", ["Vasco da Gama", "Columbus", "Magellan", "Cook"]),
        ("Taj Mahal was built by?", "Shah Jahan", ["Akbar", "Aurangzeb", "Shah Jahan", "Babur"]),
    ],
}

# ------------------- GUI SETUP ---------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.configure(bg="#f4f6f7")
        self.subject = None
        self.q_index = 0
        self.score = 0

        self.title_label = tk.Label(root, text="🧠 Welcome to the Quiz App!", font=("Arial", 20, "bold"), bg="#f4f6f7")
        self.title_label.pack(pady=20)

        self.subject_frame = tk.Frame(root, bg="#f4f6f7")
        self.subject_frame.pack()

        tk.Label(self.subject_frame, text="Choose a subject:", font=("Arial", 14), bg="#f4f6f7").pack(pady=5)

        for sub in quiz_data.keys():
            tk.Button(self.subject_frame, text=sub, font=("Arial", 12), width=20, command=lambda s=sub: self.start_quiz(s),
                      bg="#3498db", fg="white").pack(pady=4)

        self.quiz_frame = tk.Frame(root, bg="#f4f6f7")

    def start_quiz(self, subject):
        self.subject = subject
        self.questions = quiz_data[subject]
        self.q_index = 0
        self.score = 0
        self.subject_frame.pack_forget()
        self.title_label.config(text=f"{subject} Quiz")
        self.quiz_frame.pack(pady=10)
        self.show_question()

    def show_question(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        question, correct_ans, options = self.questions[self.q_index]

        tk.Label(self.quiz_frame, text=f"Q{self.q_index + 1}: {question}", font=("Arial", 14), bg="#f4f6f7", wraplength=500, justify="left").pack(pady=10)

        self.selected = tk.StringVar()

        for opt in options:
            tk.Radiobutton(self.quiz_frame, text=opt, variable=self.selected, value=opt, font=("Arial", 12),
                           bg="#f4f6f7", anchor="w").pack(anchor="w", padx=20)

        tk.Button(self.quiz_frame, text="Next", font=("Arial", 12), command=self.check_answer, bg="#2ecc71", fg="white").pack(pady=10)

    def check_answer(self):
        selected = self.selected.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        correct = self.questions[self.q_index][1]
        if selected == correct:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.quiz_frame.pack_forget()
        self.title_label.config(text="Quiz Completed ✅")

        result_frame = tk.Frame(self.root, bg="#f4f6f7")
        result_frame.pack(pady=30)

        tk.Label(result_frame, text=f"Subject: {self.subject}", font=("Arial", 14), bg="#f4f6f7").pack(pady=5)
        tk.Label(result_frame, text=f"Your Score: {self.score}/{len(self.questions)}", font=("Arial", 16, "bold"), bg="#f4f6f7", fg="#27ae60").pack(pady=10)

        tk.Button(result_frame, text="Play Again", command=lambda: self.restart(result_frame), font=("Arial", 12), bg="#f39c12", fg="white").pack(pady=5)
        tk.Button(result_frame, text="Exit", command=self.root.destroy, font=("Arial", 12), bg="#e74c3c", fg="white").pack()

    def restart(self, frame):
        frame.destroy()
        self.title_label.config(text="🧠 Welcome to the Quiz App!")
        self.subject_frame.pack()

# ------------------- RUN APP ---------------------
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
