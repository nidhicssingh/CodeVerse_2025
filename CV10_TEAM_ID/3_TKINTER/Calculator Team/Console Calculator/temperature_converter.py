def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return celsius_to_kelvin(fahrenheit_to_celsius(f))
def kelvin_to_fahrenheit(k): return celsius_to_fahrenheit(kelvin_to_celsius(k))

def temperature_converter_menu():
    while True:
        print("\n-- Temperature Converter --")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '0': break

        try:
            temp = float(input("Enter the temperature: "))

            if choice == '1': print("Result:", celsius_to_fahrenheit(temp), "\u00b0F")
            elif choice == '2': print("Result:", fahrenheit_to_celsius(temp), "\u00b0C")
            elif choice == '3': print("Result:", celsius_to_kelvin(temp), "K")
            elif choice == '4': print("Result:", kelvin_to_celsius(temp), "\u00b0C")
            elif choice == '5': print("Result:", fahrenheit_to_kelvin(temp), "K")
            elif choice == '6': print("Result:", kelvin_to_fahrenheit(temp), "\u00b0F")
            else: print("Invalid choice.")
        except Exception as e:
            print("Error:", e)
