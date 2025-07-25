import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd
from subjects import Math_quiz, Data_structure_quiz, Python_quiz, GK_quiz, CN_quiz

# ✅ Corrected: access dictionary values using ["quiz_data"]
quiz_modules = {
    "Math": Math_quiz["quiz_data"],
    "Data Structure": Data_structure_quiz["quiz_data"],
    "Python": Python_quiz["quiz_data"],
    "General Knowledge": GK_quiz["quiz_data"],
    "Computer Networks": CN_quiz["quiz_data"]
}

user_name = ""
user_answers = []
selected_subject = ""
quiz_data = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESPONSE_DIR = os.path.join(BASE_DIR, "Response")

root = tk.Tk()
root.title("Modular Quiz App")
root.geometry("600x500")
root.configure(bg="#f0f2f5")

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

def add_banner(text):
    frame = tk.Frame(root, bg="#3b5998", height=60)
    frame.pack(fill=tk.X)
    tk.Label(frame, text=text, bg="#3b5998", fg="white", font=("Helvetica", 20, "bold")).pack(pady=10)

def start_screen():
    clear_root()
    add_banner("Welcome")
    tk.Label(root, text="Enter Your Name", font=("Arial", 18), bg="#f0f2f5").pack(pady=20)
    name_entry = tk.Entry(root, font=("Arial", 16))
    name_entry.pack()

    def proceed_to_subject():
        global user_name
        user_name = name_entry.get().strip()
        if user_name == "":
            messagebox.showerror("Error", "Please enter your name!")
        else:
            subject_selection()

    tk.Button(root, text="Proceed", command=proceed_to_subject, font=("Arial", 14), bg="blue", fg="white").pack(pady=20)

def subject_selection():
    clear_root()
    add_banner("Choose Subject")

    def start_subject(subject):
        global selected_subject, quiz_data
        selected_subject = subject
        quiz_data = quiz_modules[subject]
        user_answers.clear()
        show_question(0)

    for subject in quiz_modules:
        tk.Button(root, text=subject, font=("Arial", 14), width=30,
                  command=lambda s=subject: start_subject(s)).pack(pady=10)

def show_question(index):
    clear_root()
    add_banner(f"Question {index+1}")

    question_data = quiz_data[index]
    question = question_data["question"]
    options = question_data["options"]

    tk.Label(root, text=question, font=("Arial", 16), wraplength=500, bg="#f0f2f5").pack(pady=20)

    selected_option = tk.StringVar()

    for opt in options:
        tk.Radiobutton(root, text=opt, variable=selected_option, value=opt, font=("Arial", 14),
                       bg="#f0f2f5").pack(anchor="w", padx=100)

    def next_question():
        if not selected_option.get():
            messagebox.showwarning("Warning", "Please select an option.")
            return

        user_answers.append(selected_option.get())

        if index + 1 < len(quiz_data):
            show_question(index + 1)
        else:
            show_result()

    tk.Button(root, text="Next", command=next_question, font=("Arial", 14), bg="green", fg="white").pack(pady=20)

def show_result():
    score = 0
    result_text = ""

    for i, ans in enumerate(user_answers):
        correct = quiz_data[i]["answer"]
        result_text += f"Q{i+1}: {quiz_data[i]['question']}\n"
        result_text += f"Your Answer: {ans}\nCorrect Answer: {correct}\n\n"
        if ans == correct:
            score += 1

    result_text += f"Final Score: {score}/{len(quiz_data)}\n"

    clear_root()
    add_banner("Result")
    tk.Label(root, text=f"Thanks {user_name}!", font=("Arial", 18), bg="#f0f2f5").pack(pady=10)
    tk.Label(root, text=f"{selected_subject} Score: {score}/{len(quiz_data)}", font=("Arial", 16), bg="#f0f2f5").pack(pady=10)

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

        new_entry = {"Name": user_name, "Subject": selected_subject, "Score": score, "Total": len(quiz_data)}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_excel(excel_path, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save Excel file: {e}")
        return

    tk.Label(root, text="Response saved successfully!", font=("Arial", 12), fg="green", bg="#f0f2f5").pack(pady=10)

start_screen()
root.mainloop()
