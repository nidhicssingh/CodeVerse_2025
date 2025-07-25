from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.app.root, text="Currency Converter", font=("Arial", 16)).pack(pady=10)

        self.amount_entry = ttk.Entry(self.app.root)
        self.amount_entry.pack(pady=5)

        currencies = ["INR", "USD", "EUR", "GBP"]
        self.from_currency = ttk.Combobox(self.app.root, values=currencies)
        self.from_currency.set("From")
        self.from_currency.pack(pady=5)

        self.to_currency = ttk.Combobox(self.app.root, values=currencies)
        self.to_currency.set("To")
        self.to_currency.pack(pady=5)

        ttk.Button(self.app.root, text="Convert", command=self.convert).pack(pady=10)

        self.result_label = ttk.Label(self.app.root, text="Result:")
        self.result_label.pack(pady=10)
        ttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=10)

    def convert(self):
        rates = {'INR': 1, 'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095}
        try:
            amount = float(self.amount_entry.get())
            from_cur = self.from_currency.get()
            to_cur = self.to_currency.get()
            if from_cur not in rates or to_cur not in rates:
                raise ValueError("Unsupported currency.")
            result = amount * rates[to_cur] / rates[from_cur]
            self.result_label.config(text=f"{amount} {from_cur} = {result:.2f} {to_cur}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


