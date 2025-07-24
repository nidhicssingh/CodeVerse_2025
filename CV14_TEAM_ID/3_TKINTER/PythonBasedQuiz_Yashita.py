import tkinter as tk

# Sample quiz data
quiz_data = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"question": "Which language is used for web apps?", "options": ["Python", "JavaScript", "C++", "Java"], "answer": "JavaScript"},
    {"question": "Who developed Python?", "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"], "answer": "Guido van Rossum"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")
        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font="Arial 16", wraplength=350)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="", font="Arial 14", anchor="w")
            rb.pack(fill="x", padx=20, pady=5)
            self.radio_buttons.append(rb)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font="Arial 14")
        self.submit_btn.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font="Arial 12")
        self.feedback_label.pack()

        self.load_question()

    def load_question(self):
        q = quiz_data[self.q_index]
        self.question_label.config(text=q["question"])
        self.var.set(None)
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def check_answer(self):
        selected = self.var.get()
        correct = quiz_data[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct: {correct}", fg="red")

        self.q_index += 1
        if self.q_index < len(quiz_data):
            self.root.after(1000, self.load_question)
        else:
            self.root.after(1500, self.show_result)

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Your Score: {self.score}/{len(quiz_data)}", font="Arial 18").pack(pady=50)

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
