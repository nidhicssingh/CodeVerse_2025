def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error" if b == 0 else a / b

def standard_calculator_menu():
    while True:
        print("\n-- Standard Calculator --")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Back")
        choice = input("Choose: ")
        if choice == '0': break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1': print("Result:", add(a, b))
        elif choice == '2': print("Result:", subtract(a, b))
        elif choice == '3': print("Result:", multiply(a, b))
        elif choice == '4': print("Result:", divide(a, b))
        else: print("Invalid choice.")

