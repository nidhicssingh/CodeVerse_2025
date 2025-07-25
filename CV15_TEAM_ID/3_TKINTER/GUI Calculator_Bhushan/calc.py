import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")  # Light background
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="📱 Multi-Function Calculator", font=("Helvetica", 18, "bold"), bg="#f0f8ff").pack(pady=20)

        tk.Button(self.root, text="Standard Calculator", width=25, font=("Arial", 12),
                  command=lambda: StandardCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Scientific Calculator", width=25, font=("Arial", 12),
                  command=lambda: ScientificCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Currency Converter", width=25, font=("Arial", 12),
                  command=lambda: CurrencyConverter(self)).pack(pady=5)
        tk.Button(self.root, text="Temperature Converter", width=25, font=("Arial", 12),
                  command=lambda: TemperatureConverter(self)).pack(pady=5)
        tk.Button(self.root, text="Age Calculator", width=25, font=("Arial", 12),
                  command=self.age_calculator).pack(pady=5)
        tk.Button(self.root, text="Date Difference", width=25, font=("Arial", 12),
                  command=self.date_difference).pack(pady=5)
        tk.Button(self.root, text="Exit", width=25, font=("Arial", 12),
                  command=self.root.quit).pack(pady=20)

    def age_calculator(self):
        self.clear_window()
        tk.Label(self.root, text="Age Calculator", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text="Enter DOB (YYYY-MM-DD):", bg="#f0f8ff").pack()
        dob_entry = tk.Entry(self.root)
        dob_entry.pack(pady=5)

        def calculate_age():
            try:
                dob = datetime.strptime(dob_entry.get(), "%Y-%m-%d")
                today = datetime.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                messagebox.showinfo("Age", f"You are {age} years old.")
            except:
                messagebox.showerror("Error", "Please enter a valid date (YYYY-MM-DD).")

        tk.Button(self.root, text="Calculate Age", command=calculate_age).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def date_difference(self):
        self.clear_window()
        tk.Label(self.root, text="Date Difference Calculator", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text="Enter Start Date (YYYY-MM-DD):", bg="#f0f8ff").pack()
        start_entry = tk.Entry(self.root)
        start_entry.pack(pady=5)
        tk.Label(self.root, text="Enter End Date (YYYY-MM-DD):", bg="#f0f8ff").pack()
        end_entry = tk.Entry(self.root)
        end_entry.pack(pady=5)

        def calculate_diff():
            try:
                start = datetime.strptime(start_entry.get(), "%Y-%m-%d")
                end = datetime.strptime(end_entry.get(), "%Y-%m-%d")
                days = abs((end - start).days)
                messagebox.showinfo("Result", f"Difference: {days} days")
            except:
                messagebox.showerror("Error", "Please enter valid dates.")

        tk.Button(self.root, text="Calculate", command=calculate_diff).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
