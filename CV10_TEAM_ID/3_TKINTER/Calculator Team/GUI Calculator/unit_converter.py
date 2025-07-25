import tkinter as tk
from tkinter import messagebox

class UnitConverter:
    def __init__(self, app):
        self.app = app
        self.app.clear_window()
        self.build_ui()

    def build_ui(self):
        self.app.root.configure(bg="#fefefe")

        # 🎨 Canvas banner
        canvas = tk.Canvas(self.app.root, width=500, height=100, bg="#20b2aa", highlightthickness=0)
        canvas.pack()
        canvas.create_text(250, 50, text="📏 Unit Converter", font=("Verdana", 20, "bold"), fill="white")

        frame = tk.Frame(self.app.root, bg="#fefefe")
        frame.pack(pady=20)

        tk.Label(frame, text="Enter value to convert:", font=("Arial", 12), bg="#fefefe").pack(pady=5)
        self.value_entry = tk.Entry(frame, font=("Arial", 12), width=20, justify='center')
        self.value_entry.pack(pady=5)

        tk.Label(frame, text="From unit:", font=("Arial", 12), bg="#fefefe").pack(pady=5)
        self.from_unit = tk.StringVar()
        self.from_unit.set("Select")
        tk.OptionMenu(frame, self.from_unit, "m", "cm", "inch", "kg", "g", "lb").pack(pady=5)

        tk.Label(frame, text="To unit:", font=("Arial", 12), bg="#fefefe").pack(pady=5)
        self.to_unit = tk.StringVar()
        self.to_unit.set("Select")
        tk.OptionMenu(frame, self.to_unit, "m", "cm", "inch", "kg", "g", "lb").pack(pady=5)

        tk.Button(frame, text="🔁 Convert", font=("Arial", 12, "bold"), bg="#e0ffff", fg="#333",
                  activebackground="#7fffd4", command=self.convert).pack(pady=10)

        self.result_label = tk.Label(frame, text="Result will appear here", font=("Arial", 13, "italic"), bg="#fefefe")
        self.result_label.pack(pady=10)

        tk.Button(self.app.root, text="⬅ Back", font=("Arial", 11), bg="#e1e1e1",
                  command=self.app.main_menu).pack(pady=10)

    def convert(self):
        try:
            val = float(self.value_entry.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            conversions = {
                "m": {"cm": val * 100, "inch": val * 39.3701},
                "cm": {"m": val / 100, "inch": val / 2.54},
                "inch": {"m": val / 39.3701, "cm": val * 2.54},
                "kg": {"g": val * 1000, "lb": val * 2.20462},
                "g": {"kg": val / 1000, "lb": val / 453.592},
                "lb": {"kg": val / 2.20462, "g": val * 453.592}
            }

            if from_u == to_u:
                result = val
            else:
                result = conversions.get(from_u, {}).get(to_u)

            if result is not None:
                self.result_label.config(text=f"✅ {val} {from_u} = {result:.2f} {to_u}")
            else:
                raise ValueError("Invalid unit conversion.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
