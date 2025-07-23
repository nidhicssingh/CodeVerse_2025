import tkinter as tk
from datetime import datetime
from style import apply_style

def date_calculator(app_instance):
    for widget in app_instance.root.winfo_children():
        widget.destroy()
    apply_style(app_instance.root)

    def calculate_days():
        try:
            d1 = datetime.strptime(entry_date1.get(), "%Y-%m-%d")
            d2 = datetime.strptime(entry_date2.get(), "%Y-%m-%d")
            delta = abs((d2 - d1).days)
            result_var.set(f"Difference: {delta} days")
        except ValueError:
            result_var.set("Enter date as YYYY-MM-DD")

    tk.Label(app_instance.root, text="Date 1 (YYYY-MM-DD):").pack()
    entry_date1 = tk.Entry(app_instance.root)
    entry_date1.pack()

    tk.Label(app_instance.root, text="Date 2 (YYYY-MM-DD):").pack()
    entry_date2 = tk.Entry(app_instance.root)
    entry_date2.pack()

    tk.Button(app_instance.root, text="Calculate Days", command=calculate_days).pack(pady=10)
    result_var = tk.StringVar()
    tk.Label(app_instance.root, textvariable=result_var).pack()
    tk.Button(app_instance.root, text="Back", command=app_instance.main_menu).pack(pady=10) # Added back button



