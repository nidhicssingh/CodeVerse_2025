from standard_calculator import standard_calculator_menu
from scientific_calculator import scientific_calculator_menu
from currency_converter import currency_converter_menu
from temperature_converter import temperature_converter_menu

def main():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. Standard Calculator")
        print("2. Scientific Calculator")
        print("3. Currency Converter")
        print("4. Temperature Converter")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            standard_calculator_menu()
        elif choice == '2':
            scientific_calculator_menu()
        elif choice == '3':
            currency_converter_menu()
        elif choice == '4':
            temperature_converter_menu()
        elif choice == '0':
            print("Thanks for using the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
