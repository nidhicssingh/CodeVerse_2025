import tkinter as tk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter
from age_calculator import AgeCalculator
from unit_converter import UnitConverter

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("500x600")  # Optional
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()

        canvas = tk.Canvas(self.root, width=500, height=100, bg="#4a90e2", highlightthickness=0)
        canvas.pack()
        canvas.create_text(250, 50, text="🧮 Multi-Function Calculator", font=("Helvetica", 20, "bold"), fill="white")

        def styled_button(label, action):
            tk.Button(self.root, text=label, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333",
                      width=25, height=2, command=action).pack(pady=5)

        styled_button("Standard Calculator", lambda: StandardCalculator(self))
        styled_button("Scientific Calculator", lambda: ScientificCalculator(self))
        styled_button("Currency Converter", lambda: CurrencyConverter(self))
        styled_button("Temperature Converter", lambda: TemperatureConverter(self))
        styled_button("Age Calculator", lambda: AgeCalculator(self))
        styled_button("Unit Converter", lambda: UnitConverter(self))
        styled_button("Exit", self.root.quit)

    def clear_window(self):
        for widget in self.root.winfo_children(): 
            widget.destroy()

    # def main_menu(self):
    #     self.clear_window()
    #     tk.Label(self.root, text="Select Calculator", font=("Arial", 16)).pack(pady=20)

    #     tk.Button(self.root, text="Standard Calculator", width=25, command=lambda: StandardCalculator(self)).pack(pady=5)
    #     tk.Button(self.root, text="Scientific Calculator", width=25, command=lambda: ScientificCalculator(self)).pack(pady=5)
    #     tk.Button(self.root, text="Currency Converter", width=25, command=lambda: CurrencyConverter(self)).pack(pady=5)
    #     tk.Button(self.root, text="Temperature Converter", width=25, command=lambda: TemperatureConverter(self)).pack(pady=5)
    #     tk.Button(self.root, text="Age Calculator", width=25, command=lambda: AgeCalculator(self)).pack(pady=5)
    #     tk.Button(self.root, text="Unit Converter", width=25, command=lambda: UnitConverter(self)).pack(pady=5)
    #     tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=20)
    
def main_menu(self):
    self.clear_window()

    canvas = tk.Canvas(self.root, width=500, height=100, bg="#4a90e2", highlightthickness=0)
    canvas.pack()
    canvas.create_text(250, 50, text="🧮 Multi-Function Calculator", font=("Helvetica", 20, "bold"), fill="white")

    def styled_button(label, action):
        tk.Button(self.root, text=label, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333",
                  width=25, height=2, command=action).pack(pady=5)

    styled_button("Standard Calculator", lambda: StandardCalculator(self))
    styled_button("Scientific Calculator", lambda: ScientificCalculator(self))
    styled_button("Currency Converter", lambda: CurrencyConverter(self))
    styled_button("Temperature Converter", lambda: TemperatureConverter(self))
    styled_button("Age Calculator", lambda: AgeCalculator(self))
    styled_button("Unit Converter", lambda: UnitConverter(self))
    styled_button("Exit", self.root.quit)



if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
