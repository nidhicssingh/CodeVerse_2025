import tkinter as tk
from tkinter import messagebox

# --------------------------
# Mixed Category Questions
# --------------------------
questions = [
    {
        "category": "Python",
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "def"
    },
    {
        "category": "Math",
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "category": "General Knowledge",
        "question": "Who is the President of the USA in 2025?",
        "options": ["Joe Biden", "Donald Trump", "Barack Obama", "George Bush"],
        "answer": "Joe Biden"
    },
    {
        "category": "Movies",
        "question": "Who played Iron Man in the Marvel movies?",
        "options": ["Chris Evans", "Robert Downey Jr.", "Tom Holland", "Mark Ruffalo"],
        "answer": "Robert Downey Jr."
    },
    {
        "category": "Python",
        "question": "What is the output of print(5 // 2)?",
        "options": ["2.5", "2", "3", "Error"],
        "answer": "2"
    },
    {
        "category": "Movies",
        "question": "In which movie did the character 'Jack Dawson' appear?",
        "options": ["Inception", "Titanic", "Avatar", "The Revenant"],
        "answer": "Titanic"
    },
    {
        "category": "General Knowledge",
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "category": "Math",
        "question": "What is 15 * 3?",
        "options": ["30", "45", "60", "75"],
        "answer": "45"
    }
]

# --------------------------
# Quiz App Class
# --------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Ultimate Quiz App 🌟")
        self.root.geometry("700x500")
        self.root.config(bg="#e6f2ff")

        self.score = 0
        self.q_index = 0

        self.setup_welcome_screen()

    def setup_welcome_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="🎉 Welcome to the Ultimate Quiz App 🎉", font=("Comic Sans MS", 22, "bold"), bg="#e6f2ff", fg="#333")
        title.pack(pady=30)

        subtitle = tk.Label(self.root, text="Test your brain: Python, Math, GK, Movies & more!", font=("Comic Sans MS", 14), bg="#e6f2ff", fg="#555")
        subtitle.pack(pady=10)

        start_btn = tk.Button(self.root, text="Start Quiz", font=("Helvetica", 14, "bold"),
                              bg="#28a745", fg="white", padx=20, pady=10, relief="groove",
                              command=self.start_quiz)
        start_btn.pack(pady=30)

    def start_quiz(self):
        self.score = 0
        self.q_index = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()

        if self.q_index < len(questions):
            current_q = questions[self.q_index]

            category_frame = tk.Frame(self.root, bg="#003366", height=40)
            category_frame.pack(fill="x")
            cat_label = tk.Label(category_frame, text=f"Category: {current_q['category']}", font=("Helvetica", 12, "bold"), fg="white", bg="#003366", padx=10)
            cat_label.pack(anchor="w", pady=5)

            self.q_label = tk.Label(self.root, text=f"Q{self.q_index + 1}: {current_q['question']}", font=("Helvetica", 16, "bold"),
                                    bg="#e6f2ff", wraplength=600, justify="left", fg="#222")
            self.q_label.pack(pady=30, padx=20)

            self.var = tk.StringVar()
            self.option_buttons = []

            for option in current_q["options"]:
                rb = tk.Radiobutton(self.root, text=option, variable=self.var, value=option, font=("Helvetica", 13),
                                    bg="#e6f2ff", fg="#000", activebackground="#d9eaff", wraplength=600, anchor="w", padx=20)
                rb.pack(fill="x", padx=50, pady=5)
                self.option_buttons.append(rb)

            next_btn = tk.Button(self.root, text="Next ➡", command=self.evaluate_answer, font=("Helvetica", 13, "bold"),
                                 bg="#007bff", fg="white", padx=20, pady=5, relief="ridge")
            next_btn.pack(pady=30)
        else:
            self.show_result()

    def evaluate_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("❗ No Answer", "Please choose an option before proceeding.")
            return

        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1

        self.q_index += 1
        self.show_question()

    def show_result(self):
        self.clear_screen()

        result_text = f"🎯 You scored {self.score} out of {len(questions)}!"
        result_label = tk.Label(self.root, text=result_text, font=("Comic Sans MS", 20, "bold"), bg="#e6f2ff", fg="#444")
        result_label.pack(pady=50)

        restart_btn = tk.Button(self.root, text="🔁 Restart Quiz", font=("Helvetica", 14, "bold"), bg="#17a2b8", fg="white",
                                command=self.setup_welcome_screen, padx=20, pady=10)
        restart_btn.pack(pady=10)

        quit_btn = tk.Button(self.root, text="❌ Quit", font=("Helvetica", 14, "bold"), bg="#dc3545", fg="white",
                             command=self.root.quit, padx=20, pady=10)
        quit_btn.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# --------------------------
# Launch the App
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()