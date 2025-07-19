import tkinter as tk

class AreaCalculator:
    def __init__(self, app):
        app.clear_window()
        app.root.configure(bg="#E1F5FE")

        def calculate():
            try:
                side = float(entry.get())
                area = side * side
                result.config(text=f"Area of square: {area} sq units")
            except:
                result.config(text="Please enter a valid number")

        tk.Label(app.root, text="Area Calculator", font=("Arial", 18), bg="#E1F5FE").pack(pady=20)
        tk.Label(app.root, text="Enter side length of square:", bg="#E1F5FE").pack()
        entry = tk.Entry(app.root)
        entry.pack(pady=10)
        tk.Button(app.root, text="Calculate Area", command=calculate).pack(pady=5)
        result = tk.Label(app.root, text="", font=("Arial", 14), bg="#E1F5FE")
        result.pack(pady=10)
        tk.Button(app.root, text="Back", command=app.main_menu).pack(pady=10)
