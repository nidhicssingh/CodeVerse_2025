import tkinter as tk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x400")
        self.root.configure(bg="#a9bac6")
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()

        title = tk.Label(self.root, text="Select Calculator", font=("Helvetica", 18, "bold"), bg="#a9bac6", fg="#333")
        title.pack(pady=30)

        button_frame = tk.Frame(self.root, bg="#a9bac6")
        button_frame.pack(pady=10)

        btn_style = {
            "font": ("Helvetica", 12),
            "width": 25,
            "height": 2,
            "bg": "#3B5065",
            "fg": "white",
            "activebackground": "#3B5065",
            "relief": tk.RAISED,
            "bd": 2
        }

        tk.Button(button_frame, text="Standard Calculator", command=lambda: StandardCalculator(self), **btn_style).pack(pady=8)
        tk.Button(button_frame, text="Scientific Calculator", command=lambda: ScientificCalculator(self), **btn_style).pack(pady=8)
        tk.Button(button_frame, text="Currency Converter", command=lambda: CurrencyConverter(self), **btn_style).pack(pady=8)
        tk.Button(button_frame, text="Temperature Converter", command=lambda: TemperatureConverter(self), **btn_style).pack(pady=8)
        tk.Button(self.root, text="Exit", command=self.root.quit, **btn_style).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()