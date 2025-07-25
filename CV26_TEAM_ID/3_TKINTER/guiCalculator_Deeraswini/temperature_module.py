import tkinter as tttk
from tkinter import ttk, messagebox

class TemperatureConverter:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        tttk.Label(self.app.root, text="Temperature Converter", font=("Segoe UI", 16)).pack(pady=5, padx=10, fill="x", expand=True)

        self.temp_entry = tttk.Entry(self.app.root)
        self.temp_entry.pack(pady=5, padx=10, fill="x", expand=True)

        options = [
            "Celsius to Fahrenheit", "Fahrenheit to Celsius",
            "Celsius to Kelvin", "Kelvin to Celsius",
            "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"]

        self.temp_choice = tttk.Combobox(self.app.root, values=options)
        self.temp_choice.set("Select Conversion")
        self.temp_choice.pack(pady=5, padx=10, fill="x", expand=True)

        tttk.Button(self.app.root, text="Convert", command=self.convert).pack(pady=5, padx=10, fill="x", expand=True)

        self.result_label = tttk.Label(self.app.root, text="Temperature Result:")
        self.result_label.pack(pady=5, padx=10, fill="x", expand=True)
        tttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=5, padx=10, fill="x", expand=True)

    def convert(self):
        try:
            temp = float(self.temp_entry.get())
            option = self.temp_choice.get()
            if option == "Celsius to Fahrenheit":
                res = (temp * 9/5) + 32
            elif option == "Fahrenheit to Celsius":
                res = (temp - 32) * 5/9
            elif option == "Celsius to Kelvin":
                res = temp + 273.15
            elif option == "Kelvin to Celsius":
                res = temp - 273.15
            elif option == "Fahrenheit to Kelvin":
                res = (temp - 32) * 5/9 + 273.15
            elif option == "Kelvin to Fahrenheit":
                res = (temp - 273.15) * 9/5 + 32
            else:
                raise ValueError("Invalid conversion option")
            self.result_label.config(text=f"{res:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

