import tkinter as tk
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

class CalculatorApp:
    #This is the constructor method. It runs automatically when you create an object of CalculatorApp.

    def __init__(self, root):
        #Stores the root window in an instance variable so other methods in the class can use it.
        self.root = root
        self.root.title("Multi-Function Calculator")
        self.main_menu()
#Useful for navigating between different calculator screens
    def clear_window(self):
        for widget in self.root.winfo_children(): 
            #gets a list of all widgets inside the root window.
            widget.destroy()
            #deletes each widget to clear the screen before loading a new interface

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Select Calculator", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Standard Calculator", width=25, command=lambda: StandardCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Scientific Calculator", width=25, command=lambda: ScientificCalculator(self)).pack(pady=5)
        tk.Button(self.root, text="Currency Converter", width=25, command=lambda: CurrencyConverter(self)).pack(pady=5)
        tk.Button(self.root, text="Temperature Converter", width=25, command=lambda: TemperatureConverter(self)).pack(pady=5)
        tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
