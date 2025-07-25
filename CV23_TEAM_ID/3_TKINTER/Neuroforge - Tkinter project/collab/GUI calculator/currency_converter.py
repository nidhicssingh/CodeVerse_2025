import tkinter as tk
from tkinter import ttk, messagebox

def currency_converter_menu(parent):
    def convert():
        try:
            amount_val = float(amount.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        if from_curr not in rates or to_curr not in rates:
            messagebox.showerror("Error", "Unsupported currency.")
            return
        converted = amount_val * rates[to_curr] / rates[from_curr]
        result_var.set(f"{amount_val} {from_curr} = {converted:.2f} {to_curr}")

    def swap():
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        from_currency.set(to_curr)
        to_currency.set(from_curr)

    rates = {'INR': 1, 'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095}

    win = tk.Toplevel(parent)
    win.title("Currency Converter")
    win.geometry("350x300")

    ttk.Label(win, text="From Currency:").pack()
    from_currency = ttk.Combobox(win, values=list(rates.keys()))
    from_currency.set("INR")
    from_currency.pack()

    ttk.Label(win, text="To Currency:").pack()
    to_currency = ttk.Combobox(win, values=list(rates.keys()))
    to_currency.set("USD")
    to_currency.pack()

    ttk.Label(win, text="Amount:").pack()
    amount = ttk.Entry(win)
    amount.pack()

    ttk.Button(win, text="Convert", command=convert).pack(pady=10)
    ttk.Button(win, text="Swap", command=swap).pack(pady=5)

    result_var = tk.StringVar()
    ttk.Label(win, textvariable=result_var, font=("Arial", 14)).pack(pady=10)
