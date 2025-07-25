import tkinter as tk
from tkinter import messagebox

# Quiz data (You can extend this list)
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "PHP", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"],
        "answer": "Guido van Rossum"
    }
]

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x350")

        self.q_no = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("Arial", 12))
            btn.pack(anchor="w")
            self.radio_buttons.append(btn)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def display_question(self):
        self.selected_option.set(None)
        question_data = questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}: {question_data['question']}")

        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def next_question(self):
        chosen = self.selected_option.get()
        if not chosen:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        if chosen == questions[self.q_no]["answer"]:
            self.score += 1

        self.q_no += 1

        if self.q_no >= len(questions):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(questions)}")
        self.root.quit()

# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    quiz = Quiz(root)
    root.mainloop()
