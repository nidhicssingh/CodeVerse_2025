import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AgeCalculator:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        self.app.root.configure(bg="#f0f8ff")  # Light background color

        # 🎨 Header Canvas
        canvas = tk.Canvas(self.app.root, width=500, height=100, bg="#6a5acd", highlightthickness=0)
        canvas.pack()
        canvas.create_text(250, 50, text="🎂 Age Calculator", font=("Verdana", 20, "bold"), fill="white")

        frame = tk.Frame(self.app.root, bg="#f0f8ff")
        frame.pack(pady=20)

        tk.Label(frame, text="Enter Date of Birth (YYYY-MM-DD):", font=("Arial", 12), bg="#f0f8ff").pack(pady=8)
        self.dob_entry = tk.Entry(frame, font=("Arial", 12), width=25, justify='center')
        self.dob_entry.pack(pady=5)

        tk.Button(frame, text="🎈 Calculate Age", font=("Arial", 12, "bold"), bg="#dcdcdc", fg="#333",
                  activebackground="#87cefa", command=self.calculate_age).pack(pady=12)

        self.result_label = tk.Label(frame, text="Age will appear here", font=("Arial", 13, "italic"), fg="#333", bg="#f0f8ff")
        self.result_label.pack(pady=10)

        tk.Button(self.app.root, text="⬅ Back", font=("Arial", 11), bg="#e1e1e1",
                  command=self.app.main_menu).pack(pady=10)

    def calculate_age(self):
        try:
            dob_str = self.dob_entry.get()
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            today = datetime.today()

            age_years = today.year - dob.year
            age_months = today.month - dob.month
            age_days = today.day - dob.day

            if age_days < 0:
                age_months -= 1
                age_days += 30
            if age_months < 0:
                age_years -= 1
                age_months += 12

            self.result_label.config(
                text=f"🎉 You are {age_years} years, {age_months} months, {age_days} days old!"
            )
        except Exception:
            messagebox.showerror("Error", "Please enter the date in YYYY-MM-DD format.")
