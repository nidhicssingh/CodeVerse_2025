import tkinter as tk
from tkinter import messagebox

# Python quiz questions
questions = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["Tuple", "List", "String", "Integer"],
        "answer": "List"
    },
    {
        "question": "What is the output of: print('Hello' + 'World')?",
        "options": ["Hello World", "Hello+World", "HelloWorld", "Error"],
        "answer": "HelloWorld"
    },
    {
        "question": "Which symbol is used to comment a single line in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    }
]

# GUI App class
class PythonQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Meghana's Python Quiz App")
        self.master.geometry("500x400")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(master, text="", variable=self.var, value="", font=("Arial", 12), wraplength=450)
            rb.pack(anchor="w", padx=20, pady=5)
            self.options.append(rb)

        self.submit_btn = tk.Button(master, text="Submit", command=self.next_question, font=("Arial", 12))
        self.submit_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
        self.var.set(None)
        for i, opt in enumerate(q["options"]):
            self.options[i].config(text=opt, value=opt)

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an option!")
            return

        correct_answer = questions[self.q_index]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Meghana, your score is {self.score} out of {len(questions)}")
            self.master.quit()


root = tk.Tk()
app = PythonQuizApp(root)
root.mainloop()