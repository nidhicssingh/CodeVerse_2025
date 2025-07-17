import tkinter as tttk
from tkinter import ttk, messagebox

class UnitConverter:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.app.root, text="Unit Converter", font=("Segoe UI", 16)).pack(pady=10)

        self.input_entry = ttk.Entry(self.app.root)
        self.input_entry.pack(pady=5, padx=10, fill="x")

        self.unit_choice = ttk.Combobox(self.app.root, values=[
            "Meters to Feet", "Feet to Meters",
            "Kilograms to Pounds", "Pounds to Kilograms",
            "Centimeters to Inches", "Inches to Centimeters"
        ])
        self.unit_choice.set("Select Conversion")
        self.unit_choice.pack(pady=5, padx=10, fill="x")

        ttk.Button(self.app.root, text="Convert", command=self.convert).pack(pady=10)

        self.result_label = ttk.Label(self.app.root, text="Result:")
        self.result_label.pack(pady=10)
        ttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=10)

    def convert(self):
        try:
            value = float(self.input_entry.get())
            option = self.unit_choice.get()
            if option == "Meters to Feet":
                result = value * 3.28084
            elif option == "Feet to Meters":
                result = value / 3.28084
            elif option == "Kilograms to Pounds":
                result = value * 2.20462
            elif option == "Pounds to Kilograms":
                result = value / 2.20462
            elif option == "Centimeters to Inches":
                result = value / 2.54
            elif option == "Inches to Centimeters":
                result = value * 2.54
            else:
                raise ValueError("Invalid conversion selected.")
            self.result_label.config(text=f"{result:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
