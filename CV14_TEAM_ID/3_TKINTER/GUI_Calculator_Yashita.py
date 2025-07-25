import tkinter as tk
from tkinter import ttk
from datetime import datetime

# These modules should exist and be implemented
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#e6f7ff")
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Select Calculator", font=("Helvetica", 18, "bold"), bg="#e6f7ff", fg="#004d66").pack(pady=20)

        button_style = {"font": ("Verdana", 12), "bg": "#ccf2ff", "fg": "#004d66", "activebackground": "#b3ecff"}

        tk.Button(self.root, text="Standard Calculator", width=25, **button_style, command=lambda: StandardCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Scientific Calculator", width=25, **button_style, command=lambda: ScientificCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Currency Converter", width=25, **button_style, command=lambda: CurrencyConverter(self)).pack(pady=5)
        tk.Button(self.root, text="Temperature Converter", width=25, **button_style, command=lambda: TemperatureConverter(self)).pack(pady=5)

        tk.Button(self.root, text="Unit Converter", width=25, **button_style, command=self.unit_converter).pack(pady=5)
        tk.Button(self.root, text="Date Calculator", width=25, **button_style, command=self.date_calculator).pack(pady=5)

        tk.Button(self.root, text="Exit", width=25, **button_style, command=self.root.quit).pack(pady=20)

    def unit_converter(self):
        self.clear_window()
        self.root.configure(bg="#fffbea")

        tk.Label(self.root, text="Unit Converter", font=("Helvetica", 16, "bold"), bg="#fffbea", fg="#5a3e36").pack(pady=10)

        units = ["Meter", "Kilometer", "Centimeter", "Millimeter"]
        conversion_factors = {
            ("Meter", "Kilometer"): 0.001,
            ("Kilometer", "Meter"): 1000,
            ("Meter", "Centimeter"): 100,
            ("Centimeter", "Meter"): 0.01,
            ("Kilometer", "Centimeter"): 100000,
            ("Centimeter", "Kilometer"): 0.00001,
            ("Meter", "Millimeter"): 1000,
            ("Millimeter", "Meter"): 0.001,
            ("Kilometer", "Millimeter"): 1000000,
            ("Millimeter", "Kilometer"): 0.000001
        }

        var_from = tk.StringVar(value="Meter")
        var_to = tk.StringVar(value="Kilometer")
        var_input = tk.StringVar()
        var_result = tk.StringVar()

        tk.Label(self.root, text="Enter value:", bg="#fffbea", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=var_input, font=("Arial", 12)).pack(pady=5)

        tk.Label(self.root, text="From:", bg="#fffbea", font=("Arial", 12)).pack(pady=5)
        ttk.Combobox(self.root, values=units, textvariable=var_from, state='readonly', font=("Arial", 12)).pack(pady=5)

        tk.Label(self.root, text="To:", bg="#fffbea", font=("Arial", 12)).pack(pady=5)
        ttk.Combobox(self.root, values=units, textvariable=var_to, state='readonly', font=("Arial", 12)).pack(pady=5)

        def convert():
            try:
                val = float(var_input.get())
                factor = conversion_factors.get((var_from.get(), var_to.get()))
                if factor is not None:
                    result = val * factor
                    var_result.set(f"{result:.4f} {var_to.get()}")
                else:
                    var_result.set("Conversion not available.")
            except ValueError:
                var_result.set("Invalid input.")

        tk.Button(self.root, text="Convert", font=("Arial", 12), bg="#ffdbac", command=convert).pack(pady=10)
        tk.Label(self.root, textvariable=var_result, font=("Arial", 14), bg="#fffbea", fg="#7b2d26").pack(pady=10)

        tk.Button(self.root, text="Back to Menu", font=("Arial", 12), bg="#ffcccb", command=self.main_menu).pack(pady=20)

    def date_calculator(self):
        self.clear_window()
        self.root.configure(bg="#f0fff0")

        tk.Label(self.root, text="Date Calculator", font=("Helvetica", 16, "bold"), bg="#f0fff0", fg="#004d00").pack(pady=20)

        tk.Label(self.root, text="Enter Start Date (YYYY-MM-DD):", bg="#f0fff0", font=("Arial", 12)).pack(pady=5)
        start_entry = tk.Entry(self.root, font=("Arial", 12))
        start_entry.pack(pady=5)

        tk.Label(self.root, text="Enter End Date (YYYY-MM-DD):", bg="#f0fff0", font=("Arial", 12)).pack(pady=5)
        end_entry = tk.Entry(self.root, font=("Arial", 12))
        end_entry.pack(pady=5)

        result_var = tk.StringVar()

        def calculate_days():
            try:
                start_date = datetime.strptime(start_entry.get(), "%Y-%m-%d")
                end_date = datetime.strptime(end_entry.get(), "%Y-%m-%d")
                delta = (end_date - start_date).days
                result_var.set(f"Difference: {abs(delta)} day(s)")
            except Exception:
                result_var.set("Invalid date format")

        tk.Button(self.root, text="Calculate", font=("Arial", 12), bg="#b2fab4", command=calculate_days).pack(pady=10)
        tk.Label(self.root, textvariable=result_var, font=("Arial", 14), bg="#f0fff0", fg="#004d00").pack(pady=10)

        tk.Button(self.root, text="Back to Menu", font=("Arial", 12), bg="#ffcccb", command=self.main_menu).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
