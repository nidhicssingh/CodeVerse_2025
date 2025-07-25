import tkinter as tk
from tkinter import colorchooser, Canvas
from standard_module import StandardCalculator
from scientific_module import ScientificCalculator
from currency_module import CurrencyConverter
from temperature_module import TemperatureConverter

class FancyButton(tk.Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.default_bg = self["bg"]
        self.default_fg = self["fg"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = self['activebackground']
        self['fg'] = self['activeforeground']

    def on_leave(self, e):
        self['bg'] = self.default_bg
        self['fg'] = self.default_fg

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Multi‑Function Calculator 🎉")
        self.root.geometry("600x500")
        self.primary_color = "#007ACC"
        self.accent_color = "#FFD700"
        self.bg = "#F5F5F5"
        self.root.configure(bg=self.bg)
        self.splash_screen()

    def splash_screen(self):
        self.clear_window()
        canvas = Canvas(self.root, width=600, height=200, bg=self.bg, highlightthickness=0)
        canvas.pack(pady=50)
        text = "Welcome to Calculator"
        x = 50

        def animate(i=0):
            if i <= len(text):
                canvas.delete("all")
                canvas.create_text(300, 100, text=text[:i], font=("Arial", 32, "bold"), fill=self.primary_color)
                self.root.after(100, animate, i+1)
            else:
                self.root.after(500, self.main_menu)
        animate()

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()

    def change_theme(self):
        color = colorchooser.askcolor(title="Pick Primary Color")[1]
        if color:
            self.primary_color = color

    def main_menu(self):
        self.clear_window()
        title = tk.Label(self.root, text="Select Calculator", font=("Helvetica", 24, "bold"),
                         bg=self.bg, fg=self.primary_color)
        title.pack(pady=20)

        # glow on hover effect
        title.bind("<Enter>", lambda e: title.config(fg=self.accent_color))
        title.bind("<Leave>", lambda e: title.config(fg=self.primary_color))

        options = [
            ("Standard Calculator", lambda: StandardCalculator(self)),
            ("Scientific Calculator", lambda: ScientificCalculator(self)),
            ("Currency Converter", lambda: CurrencyConverter(self)),
            ("Temperature Converter", lambda: TemperatureConverter(self)),
            ("Pick Theme Color", self.change_theme),
            ("Exit", self.root.quit),
        ]

        for text, cmd in options:
            btn = FancyButton(self.root, text=text, font=("Helvetica", 14, "bold"),
                              bg=self.primary_color, fg="white",
                              activebackground=self.accent_color, activeforeground=self.bg,
                              width=30, bd=0, command=cmd)
            btn.pack(pady=8)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
