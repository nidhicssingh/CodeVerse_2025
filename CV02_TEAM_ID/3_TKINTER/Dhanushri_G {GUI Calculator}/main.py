import tkinter as tk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

from age_module import AgeCalculator
from area_module import AreaCalculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#E0F7FA")  
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()
        self.root.configure(bg="#E0F7FA")
        tk.Label(self.root, text="Select Calculator", font=("Arial", 20, "bold"),
                 bg="#E0F7FA", fg="#006064").pack(pady=30)

        buttons = [
            ("Standard Calculator", lambda: StandardCalculator(self), "#AED581"),
            ("Scientific Calculator", lambda: ScientificCalculator(self), "#FF8A65"),
            ("Currency Converter", lambda: CurrencyConverter(self), "#4DD0E1"),
            ("Temperature Converter", lambda: TemperatureConverter(self), "#BA68C8"),
            ("Age Calculator", lambda: AgeCalculator(self), "#FFD54F"),
            ("Area Calculator", lambda: AreaCalculator(self), "#90CAF9"),
            ("Exit", self.root.quit, "#EF9A9A")
        ]

        for text, command, color in buttons:
            tk.Button(self.root, text=text, width=25, height=2,
                      bg=color, fg="black", font=("Arial", 12),
                      command=command).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
