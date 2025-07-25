import tkinter as tk
from tkinter import ttk
from standard_calculator import standard_calculator_menu
from scientific_calculator import scientific_calculator_menu
from currency_converter import currency_converter_menu
from temperature_converter import temperature_converter_menu

def main_menu():
    root = tk.Tk()
    root.title("Multi-Function Calculator")
    root.geometry("450x500")
    root.configure(bg="#20e1ff")

    # Create a style for bigger ttk buttons
    style = ttk.Style()
    style.configure("Big.TButton", font=("Helvetica", 16), padding=10)

    # Title
    title = tk.Label(root, text="Multiple Calculator Converter", font=("Helvetica", 22, "bold"), bg="#C3FF00", fg="#FF002B")
    title.pack(pady=30)

    # Buttons with style
    ttk.Button(root, text="Standard Calculator", style="Big.TButton",
               command=lambda: [root.withdraw(), standard_calculator_menu(root)]).pack(pady=12, ipadx=10, ipady=5)

    ttk.Button(root, text="Scientific Calculator", style="Big.TButton",
               command=lambda: [root.withdraw(), scientific_calculator_menu(root)]).pack(pady=12, ipadx=10, ipady=5)

    ttk.Button(root, text="Currency Converter", style="Big.TButton",
               command=lambda: [root.withdraw(), currency_converter_menu(root)]).pack(pady=12, ipadx=10, ipady=5)

    ttk.Button(root, text="Temperature Converter", style="Big.TButton",
               command=lambda: [root.withdraw(), temperature_converter_menu(root)]).pack(pady=12, ipadx=10, ipady=5)

    ttk.Button(root, text="Exit", style="Big.TButton", command=root.destroy).pack(pady=20, ipadx=10, ipady=5)

    root.mainloop()

if __name__ == "__main__":
    main_menu()

