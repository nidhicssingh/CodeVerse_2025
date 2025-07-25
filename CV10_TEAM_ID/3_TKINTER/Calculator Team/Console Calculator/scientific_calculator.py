import math

def power(a, b): return math.pow(a, b)
def square_root(a): return math.sqrt(a)
def logarithm(a, base=10): return math.log(a, base)
def sine(a): return math.sin(math.radians(a))
def cosine(a): return math.cos(math.radians(a))
def tangent(a): return math.tan(math.radians(a))
def factorial(n): return math.factorial(n)
def absolute(a): return abs(a)
def modulus(a, b): return a % b
def exponential(a): return math.exp(a)

def scientific_calculator_menu():
    while True:
        print("\n-- Scientific Calculator --")
        print("1. Power\n2. Square Root\n3. Logarithm\n4. Sine\n5. Cosine")
        print("6. Tangent\n7. Factorial\n8. Absolute\n9. Modulus\n10. Exponential")
        print("0. Back")
        choice = input("Choose: ")

        if choice == '0': break

        try:
            if choice in ['1', '9']:
                a = float(input("a: "))
                b = float(input("b: "))
            elif choice in ['7']:
                a = int(input("Enter integer: "))
            else:
                a = float(input("a: "))

            if choice == '1': print("Result:", power(a, b))
            elif choice == '2': print("Result:", square_root(a))
            elif choice == '3': print("Result:", logarithm(a))
            elif choice == '4': print("Result:", sine(a))
            elif choice == '5': print("Result:", cosine(a))
            elif choice == '6': print("Result:", tangent(a))
            elif choice == '7': print("Result:", factorial(a))
            elif choice == '8': print("Result:", absolute(a))
            elif choice == '9': print("Result:", modulus(a, b))
            elif choice == '10': print("Result:", exponential(a))
            else: print("Invalid")
        except Exception as e:
            print("Error:", e)
