# quiz_app.py

import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd

# -------------------- QUIZ DATA --------------------

Math_quiz = {
    "quiz_data": [
        {
            "question": "What is the derivative of x²?",
            "options": ["2x", "x", "x²", "1"],
            "answer": "2x"
        },
        {
            "question": "What is 15 + 27?",
            "options": ["42", "32", "40", "52"],
            "answer": "42"
        }
    ]
}

Data_structure_quiz = {
    "quiz_data": [
        {
            "question": "What data structure uses FIFO?",
            "options": ["Stack", "Queue", "Tree", "Graph"],
            "answer": "Queue"
        },
        {
            "question": "Time complexity of binary search?",
            "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
            "answer": "O(log n)"
        }
    ]
}

Python_quiz = {
    "quiz_data": [
        {
            "question": "Which keyword defines a function?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "What does len() return?",
            "options": ["Sorts list", "Adds values", "None", "Number of elements"],
            "answer": "Number of elements"
        }
    ]
}

quiz_modules = {
    "Math": Math_quiz["quiz_data"],
    "Data Structure": Data_structure_quiz["quiz_data"],
    "Python": Python_quiz["quiz_data"]
}

# -------------------- GLOBAL VARIABLES --------------------

user_name = ""
user_answers = []
selected_subject = ""
quiz_data = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESPONSE_DIR = os.path.join(BASE_DIR, "Response")

# -------------------- UI SETUP --------------------

root = tk.Tk()
root.title("Modular Quiz App")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

# -------------------- FUNCTIONS --------------------

def start_screen():
    root.configure(bg="#f0f0f0")
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter Your Name", font=("Arial", 20, "bold"), fg="#2c3e50", bg="#f0f0f0").pack(pady=40)
    name_entry = tk.Entry(root, font=("Arial", 16))
    name_entry.pack()

    def proceed_to_subject():
        global user_name
        user_name = name_entry.get().strip()
        if user_name == "":
            messagebox.showerror("Error", "Please enter your name!")
        else:
            subject_selection()

    tk.Button(root, text="Proceed", command=proceed_to_subject, font=("Arial", 14),
              bg="#2980b9", fg="white", activebackground="#3498db").pack(pady=30)

def subject_selection():
    root.configure(bg="#f0f0f0")
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Choose Subject", font=("Arial", 20, "bold"), fg="#8e44ad", bg="#f0f0f0").pack(pady=30)

    def start_subject(subject):
        global selected_subject, quiz_data
        selected_subject = subject
        quiz_data = quiz_modules[subject]
        user_answers.clear()

        if subject == "Math":
            root.configure(bg="#FFFACD")
        elif subject == "Data Structure":
            root.configure(bg="#E0FFFF")
        elif subject == "Python":
            root.configure(bg="#F0FFF0")

        show_question(0)

    for subject in quiz_modules:
        tk.Button(root, text=subject, font=("Arial", 16), width=25,
                  command=lambda s=subject: start_subject(s),
                  bg="#d35400", fg="white", activebackground="#e67e22").pack(pady=10)

def show_question(index):
    for widget in root.winfo_children():
        widget.destroy()

    question_data = quiz_data[index]
    question = question_data["question"]
    options = question_data["options"]

    tk.Label(root, text=f"Question {index+1} of {len(quiz_data)}", font=("Arial", 12),
             bg=root["bg"], fg="#34495e").pack(pady=10)

    tk.Label(root, text=f"{question}", font=("Arial", 16, "bold"), wraplength=600,
             fg="#8e44ad", bg=root["bg"]).pack(pady=20)

    selected_option = tk.StringVar()

    for opt in options:
        tk.Radiobutton(root, text=opt, variable=selected_option, value=opt,
                       font=("Arial", 14), bg=root["bg"], anchor="w").pack(anchor="w", padx=100)

    def next_question():
        if not selected_option.get():
            messagebox.showwarning("Warning", "Please select an option.")
            return

        user_answers.append(selected_option.get())

        if index + 1 < len(quiz_data):
            show_question(index + 1)
        else:
            show_result()

    tk.Button(root, text="Next", command=next_question, font=("Arial", 14),
              bg="#27ae60", fg="white", activebackground="#2ecc71").pack(pady=30)

def show_result():
    score = 0
    result_text = ""

    for i, ans in enumerate(user_answers):
        correct = quiz_data[i]["answer"]
        result_text += f"Q{i+1}: {quiz_data[i]['question']}\n"
        result_text += f"Your Answer: {ans}\nCorrect Answer: {correct}\n\n"
        if ans.strip().lower() == correct.strip().lower():
            score += 1

    result_text += f"Final Score: {score}/{len(quiz_data)}\n"

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Thanks {user_name}!", font=("Arial", 20, "bold"), bg=root["bg"], fg="#34495e").pack(pady=10)
    tk.Label(root, text=f"{selected_subject} Score: {score}/{len(quiz_data)}", font=("Arial", 16), bg=root["bg"], fg="#e67e22").pack(pady=10)

    os.makedirs(RESPONSE_DIR, exist_ok=True)

    txt_path = os.path.join(RESPONSE_DIR, f"{user_name}_{selected_subject}.txt")
    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result_text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text file: {e}")
        return

    excel_path = os.path.join(RESPONSE_DIR, "results.xlsx")
    try:
        if os.path.exists(excel_path):
            df = pd.read_excel(excel_path)
        else:
            df = pd.DataFrame(columns=["Name", "Subject", "Score", "Total"])

        new_entry = {
            "Name": user_name,
            "Subject": selected_subject,
            "Score": score,
            "Total": len(quiz_data)
        }

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_excel(excel_path, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save Excel file: {e}")
        return

    tk.Label(root, text="Response saved successfully!", font=("Arial", 12), fg="green", bg=root["bg"]).pack(pady=10)

    # Add restart and exit options
    tk.Button(root, text="Take Another Quiz", command=start_screen, font=("Arial", 12),
              bg="#3498db", fg="white").pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12),
              bg="#c0392b", fg="white").pack(pady=5)

# -------------------- MAIN --------------------

start_screen()
root.mainloop()
