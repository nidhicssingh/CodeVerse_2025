import tkinter as tk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

from bmi_module import bmi_calculator
from date_module import date_calculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#DD1515")  
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()
        self.root.configure(bg="#000000")
        tk.Label(self.root, text="Select Calculator", font=("Helvetica", 25, "italic", "underline"),
                 bg="#100F0F", fg="#E4EDED").pack(pady=30)

        buttons = [
            ("Standard Calculator", lambda: StandardCalculator(self), "#E20C5E"),
            ("Scientific Calculator", lambda: ScientificCalculator(self), "#38DB07"),
            ("Currency Converter", lambda: CurrencyConverter(self), "#BFEB21"),
            ("Temperature Converter", lambda: TemperatureConverter(self), "#9612AD"),
            ("BMI Calculator", lambda: bmi_calculator(self), "#F1F0EA"),
            ("Date Calculator", lambda: date_calculator(self), "#347AB4"),
            ("Exit", self.root.quit, "#F30909")
        ]

        for text, command, color in buttons:
            tk.Button(self.root, text=text, width=25, height=2,
                      bg=color, fg="black", font=("Arial", 12),
                      command=command).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()