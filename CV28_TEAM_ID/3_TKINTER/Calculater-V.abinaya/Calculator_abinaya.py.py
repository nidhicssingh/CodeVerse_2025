import tkinter as tk
from tkinter import messagebox

# Quiz questions for each subject
quiz_data = {
    "Math": [
        ("What is 5 + 3?", "8", ["6", "7", "8", "9"]),
        ("What is 12 / 4?", "3", ["2", "3", "4", "5"])
    ],
    "Science": [
        ("What planet is known as the Red Planet?", "Mars", ["Earth", "Mars", "Venus", "Jupiter"]),
        ("What gas do plants absorb?", "Carbon Dioxide", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"])
    ],
    "History": [
        ("Who was the first President of the USA?", "George Washington", ["Lincoln", "Jefferson", "George Washington", "Adams"]),
        ("Which year did World War II end?", "1945", ["1939", "1942", "1945", "1950"])
    ],
    "Sports": [
        ("How many players in a football team?", "11", ["9", "10", "11", "12"]),
        ("Which sport uses a bat and ball?", "Cricket", ["Tennis", "Football", "Cricket", "Hockey"])
    ],
    "Movies": [
        ("Who is Iron Man?", "Tony Stark", ["Steve Rogers", "Tony Stark", "Bruce Wayne", "Peter Parker"]),
        ("Which movie has the character Elsa?", "Frozen", ["Moana", "Tangled", "Frozen", "Brave"])
    ]
}

# Main quiz app class
class QuizApp:
    def _init_(self, root):  # Correct constructor with 'root' as argument
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.configure(bg="#e6f2ff")

        self.subject = None
        self.question_index = 0
        self.score = 0

        self.start_screen()

    def start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select a Subject", font=("Arial", 20, "bold"), bg="#e6f2ff").pack(pady=30)

        for subject in quiz_data:
            tk.Button(self.root, text=subject, font=("Arial", 16), width=20, bg="#cce6ff",
                      command=lambda s=subject: self.start_quiz(s)).pack(pady=10)

    def start_quiz(self, subject):
        self.subject = subject
        self.questions = quiz_data[subject]
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()
        if self.question_index < len(self.questions):
            question, answer, options = self.questions[self.question_index]

            tk.Label(self.root, text=f"{self.subject} Quiz", font=("Arial", 18, "bold"), bg="#e6f2ff").pack(pady=10)
            tk.Label(self.root, text=question, font=("Arial", 16), bg="#e6f2ff").pack(pady=20)

            for option in options:
                tk.Button(self.root, text=option, font=("Arial", 14), width=25, bg="#d9f2d9",
                          command=lambda o=option: self.check_answer(o)).pack(pady=5)
        else:
            self.show_result()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.question_index][1]
        if selected_option == correct_answer:
            self.score += 1
        self.question_index += 1
        self.show_question()

    def show_result(self):
        self.clear_screen()
        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 20, "bold"), fg="green", bg="#e6f2ff").pack(pady=30)
        tk.Label(self.root, text=f"Your Score: {self.score} / {len(self.questions)}", font=("Arial", 18), bg="#e6f2ff").pack(pady=10)

        tk.Button(self.root, text="Try Another Subject", font=("Arial", 14), bg="#ffcc99", command=self.start_screen).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 14), bg="#ff9999", command=self.root.quit).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "_main_":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()