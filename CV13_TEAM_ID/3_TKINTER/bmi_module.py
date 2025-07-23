import tkinter as tk
from tkinter import ttk
from style import apply_style

def bmi_calculator(app_instance):
    for widget in app_instance.root.winfo_children():
       widget.destroy()
    apply_style(app_instance.root)

    def calculate_bmi():
        try:
            height = float(entry_height.get()) / 100  # in meters
            weight = float(entry_weight.get())
            bmi = weight / (height ** 2)
            result_var.set(f"Your BMI is: {bmi:.2f}")
        except ValueError:
            result_var.set("Invalid input!")

    tk.Label(app_instance.root, text="Height (cm):").pack()
    entry_height = tk.Entry(app_instance.root)
    entry_height.pack()

    tk.Label(app_instance.root, text="Weight (kg):").pack()
    entry_weight = tk.Entry(app_instance.root)
    entry_weight.pack()

    tk.Button(app_instance.root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
    result_var = tk.StringVar()
    tk.Label(app_instance.root, textvariable=result_var).pack()
    ttk.Button(app_instance.root, text="Back", command=app_instance.main_menu).pack(pady=10)
