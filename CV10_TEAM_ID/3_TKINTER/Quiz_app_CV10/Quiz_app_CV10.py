import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Quiz App")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")

        self.subjects = {
            "Math": [
                ("5 + 3 =", "8"),
                ("10 - 6 =", "4"),
                ("6 x 2 =", "12"),
                ("12 / 3 =", "4")
            ],
            "Geography": [
                ("Capital of India?", "New Delhi"),
                ("Largest ocean?", "Pacific"),
                ("Mount Everest is in?", "Nepal"),
                ("Sahara is a?", "Desert")
            ],
            "Computer Science": [
                ("What does CPU stand for?", "Central Processing Unit"),
                ("Python is a?", "Programming Language"),
                ("HTML is used for?", "Web Design"),
                ("Binary of 2?", "10")
            ],
            "Science": [
                ("H2O is?", "Water"),
                ("Planet with rings?", "Saturn"),
                ("Organ that pumps blood?", "Heart"),
                ("Sun is a?", "Star")
            ],
            "Art & Culture": [
                ("Mona Lisa painted by?", "Leonardo da Vinci"),
                ("Bharatanatyam is from?", "Tamil Nadu"),
                ("Famous Indian festival of lights?", "Diwali"),
                ("Taj Mahal built by?", "Shah Jahan")
            ]
        }

        self.selected_subject = None
        self.questions = []
        self.q_index = 0
        self.score = 0

        self.build_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_main_menu(self):
        self.clear_window()

        canvas = tk.Canvas(self.root, width=600, height=100, bg="#4a90e2", highlightthickness=0)
        canvas.pack()
        canvas.create_text(300, 50, text="🎓 Welcome to the Quiz App", font=("Helvetica", 20, "bold"), fill="white")

        tk.Label(self.root, text="Choose a Subject", font=("Arial", 14), bg="#f0f8ff").pack(pady=20)

        for subject in self.subjects.keys():
            tk.Button(self.root, text=subject, font=("Arial", 12, "bold"), width=20, bg="#dcdcdc",
                      command=lambda s=subject: self.start_quiz(s)).pack(pady=5)

    def start_quiz(self, subject):
        self.selected_subject = subject
        self.questions = self.subjects[subject]
        self.q_index = 0
        self.score = 0
        self.build_quiz_screen()

    def build_quiz_screen(self):
        self.clear_window()
        self.root.configure(bg="#fffaf0")

        tk.Label(self.root, text=f"{self.selected_subject} Quiz", font=("Helvetica", 18, "bold"),
                 fg="#4a4a4a", bg="#fffaf0").pack(pady=20)

        question, _ = self.questions[self.q_index]
        self.question_label = tk.Label(self.root, text=f"Q{self.q_index+1}: {question}", font=("Arial", 14),
                                       bg="#fffaf0")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 12), width=30, justify="center")
        self.answer_entry.pack(pady=10)

        tk.Button(self.root, text="Submit", font=("Arial", 12), bg="#e6e6fa", command=self.check_answer).pack(pady=10)

    def check_answer(self):
        user_ans = self.answer_entry.get().strip().lower()
        correct_ans = self.questions[self.q_index][1].strip().lower()

        if user_ans == correct_ans:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.build_quiz_screen()
        else:
            self.show_result()

    def show_result(self):
        self.clear_window()

        result_text = f"🎉 You scored {self.score} out of {len(self.questions)}"
        tk.Label(self.root, text="Quiz Completed!", font=("Helvetica", 20, "bold"), fg="#008000").pack(pady=30)
        tk.Label(self.root, text=result_text, font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="🏠 Back to Menu", font=("Arial", 12), bg="#dcdcdc",
                  command=self.build_main_menu).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
