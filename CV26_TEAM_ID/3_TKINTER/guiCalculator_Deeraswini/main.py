import tkinter as tk
from tkinter import ttk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter
from history_module import HistoryPanel
from unit_module import UnitConverter

def apply_modern_theme(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TButton", font=("Segoe UI", 12), padding=6)
    style.configure("TLabel", font=("Segoe UI", 12))
    style.configure("TEntry", font=("Segoe UI", 12))
    style.configure("TCombobox", font=("Segoe UI", 12))

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.center_window()
        apply_modern_theme(self.root)
        self.main_menu()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()
        ttk.Label(self.root, text="Select Calculator", font=("Arial", 16)).pack(pady=20)

        ttk.Button(self.root, text="Standard Calculator", width=25, command=lambda: StandardCalculator(self)).pack(pady=5)
        ttk.Button(self.root, text="Scientific Calculator", width=25, command=lambda: ScientificCalculator(self)).pack(pady=5)
        ttk.Button(self.root, text="Currency Converter", width=25, command=lambda: CurrencyConverter(self)).pack(pady=5)
        ttk.Button(self.root, text="Temperature Converter", width=25, command=lambda: TemperatureConverter(self)).pack(pady=5)
        ttk.Button(self.root, text="Unit Converter", width=25, command=lambda: UnitConverter(self)).pack(pady=5)
        ttk.Button(self.root, text="History", width=25, command=lambda: HistoryPanel(self)).pack(pady=5)
        ttk.Button(self.root, text="Clear History", width=25, command=lambda: self.clear_history()).pack(pady=5)
        ttk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
