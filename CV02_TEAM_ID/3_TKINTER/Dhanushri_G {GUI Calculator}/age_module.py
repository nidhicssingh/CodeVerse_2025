import tkinter as tk
from datetime import datetime

class AgeCalculator:
    def __init__(self, app):
        app.clear_window()
        app.root.configure(bg="#FFF9C4")

        def calculate_age():
            try:
                birth = datetime.strptime(entry.get(), "%Y-%m-%d")
                today = datetime.today()
                age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
                result.config(text=f"Your Age: {age} years")
            except:
                result.config(text="Enter date in YYYY-MM-DD format")

        tk.Label(app.root, text="Age Calculator", font=("Arial", 18), bg="#FFF9C4").pack(pady=20)
        tk.Label(app.root, text="Enter your birthdate (YYYY-MM-DD):", bg="#FFF9C4").pack()
        entry = tk.Entry(app.root)
        entry.pack(pady=10)
        tk.Button(app.root, text="Calculate", command=calculate_age).pack(pady=5)
        result = tk.Label(app.root, text="", font=("Arial", 14), bg="#FFF9C4")
        result.pack(pady=10)
        tk.Button(app.root, text="Back", command=app.main_menu).pack(pady=10)
