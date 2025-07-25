import tkinter as tk

class TemperatureConverter:
    def __init__(self, app):
        app.clear_window()
        tk.Label(app.root, text="Temperature Converter", font=("Arial", 16)).pack(pady=20)
        tk.Button(app.root, text="Back", command=app.main_menu).pack(pady=10)
