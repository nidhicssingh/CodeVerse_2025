import tkinter as tk
from tkinter import ttk, messagebox

def temperature_converter_menu(parent):
    def convert_temperature():
        try:
            value = float(temp_entry.get())
            conv = conversion.get()
            result_val = None

            if conv == "Celsius to Fahrenheit":
                result_val = (value * 9/5) + 32
            elif conv == "Fahrenheit to Celsius":
                result_val = (value - 32) * 5/9
            elif conv == "Celsius to Kelvin":
                result_val = value + 273.15
            elif conv == "Kelvin to Celsius":
                result_val = value - 273.15
            elif conv == "Fahrenheit to Kelvin":
                result_val = ((value - 32) * 5/9) + 273.15
            elif conv == "Kelvin to Fahrenheit":
                result_val = ((value - 273.15) * 9/5) + 32
            else:
                messagebox.showwarning("Warning", "Please select a conversion type.")
                return

            result.set(f"Result: {round(result_val, 2)}")
        except ValueError:
            messagebox.showerror("Input Error", "Enter a valid temperature.")

    win = tk.Toplevel(parent)
    win.title("Temperature Converter")
    win.geometry("400x300")

    ttk.Label(win, text="Select Conversion Type:", font=("Helvetica", 12)).pack(pady=5)
    conversion = ttk.Combobox(win, values=[
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius",
        "Fahrenheit to Kelvin",
        "Kelvin to Fahrenheit"
    ])
    conversion.set("Celsius to Fahrenheit")
    conversion.pack(pady=5)

    ttk.Label(win, text="Enter Temperature:", font=("Helvetica", 12)).pack()
    temp_entry = ttk.Entry(win, font=("Helvetica", 12))
    temp_entry.pack(pady=5)

    ttk.Button(win, text="Convert", command=convert_temperature).pack(pady=10)

    result = tk.StringVar()
    ttk.Label(win, textvariable=result, font=("Helvetica", 14), foreground="blue").pack(pady=10)
