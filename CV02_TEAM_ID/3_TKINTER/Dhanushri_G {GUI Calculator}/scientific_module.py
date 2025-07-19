from tkinter import ttk, messagebox
import math

class ScientificCalculator:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.app.root, text="Scientific Calculator", font=("Arial", 16)).pack(pady=10)

        self.entry1 = ttk.Entry(self.app.root)
        self.entry1.pack(pady=5)
        self.entry2 = ttk.Entry(self.app.root)
        self.entry2.pack(pady=5)

        functions = [
            "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent",
            "Factorial", "Absolute", "Modulus", "Exponential"
        ]

        grid_frame = ttk.Frame(self.app.root)
        grid_frame.pack(pady=10)

        for index, func in enumerate(functions):
            row = index // 2
            col = index % 2
            ttk.Button(
                grid_frame, text=func, width=20,
                command=lambda f=func: self.calculate(f)
            ).grid(row=row, column=col, padx=5, pady=5)

        self.result_label = ttk.Label(self.app.root, text="Result:")
        self.result_label.pack(pady=10)
        ttk.Button(self.app.root, text="Back", command=self.app.main_menu).pack(pady=10)

    def calculate(self, operation):
        try:
            if operation in ["Power", "Modulus"]:
                a = float(self.entry1.get())
                b = float(self.entry2.get())
                result = math.pow(a, b) if operation == "Power" else a % b
            elif operation == "Factorial":
                a = int(float(self.entry1.get()))
                result = math.factorial(a)
            else:
                a = float(self.entry1.get())
                if operation == "Square Root":
                    result = math.sqrt(a)
                elif operation == "Logarithm":
                    result = math.log10(a)
                elif operation == "Sine":
                    result = math.sin(math.radians(a))
                elif operation == "Cosine":
                    result = math.cos(math.radians(a))
                elif operation == "Tangent":
                    result = math.tan(math.radians(a))
                elif operation == "Absolute":
                    result = abs(a)
                elif operation == "Exponential":
                    result = math.exp(a)
                else:
                    raise ValueError("Unknown operation")

            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
