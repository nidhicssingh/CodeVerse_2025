def currency_converter_menu():
    print("\n-- Currency Converter --")
    print("Supported: INR, USD, EUR, GBP")

    rates = {
        'INR': 1,
        'USD': 0.012,
        'EUR': 0.011,
        'GBP': 0.0095,
    }

    from_currency = input("From Currency (e.g., INR): ").upper()
    to_currency = input("To Currency (e.g., USD): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency.")
        return

    amount = float(input(f"Amount in {from_currency}: "))
    converted = amount * rates[to_currency] / rates[from_currency]
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
