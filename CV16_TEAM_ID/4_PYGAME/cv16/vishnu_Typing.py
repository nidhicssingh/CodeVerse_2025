import tkinter as tk
import random
import time

# List of words for the player to type
WORDS = ["I am using python", "I am in svyasa", "I am living in tadipatri", "where are you from", "tkinter", "how is your health", "when are you coming from home"]

class TypingSpeedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Game")
        self.root.geometry("400x250")
        
        self.word = random.choice(WORDS)
        self.start_time = None

        self.instructions = tk.Label(root, text="Type the word shown below:", font=("Arial", 14))
        self.instructions.pack(pady=10)

        self.word_label = tk.Label(root, text=self.word, font=("Arial", 24), fg="blue")
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_input)
        self.entry.focus()

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Try Another", command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.start_timer()

    def start_timer(self):
        self.start_time = time.time()

    def check_input(self, event):
        typed = self.entry.get().strip()
        elapsed = round(time.time() - self.start_time, 2)
        if typed == self.word:
            self.result_label.config(text=f"✅ Correct! Time: {elapsed} seconds", fg="green")
        else:
            self.result_label.config(text=f"❌ Incorrect. Try again.", fg="red")

    def reset_game(self):
        self.word = random.choice(WORDS)
        self.word_label.config(text=self.word)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_timer()

root = tk.Tk()
app = TypingSpeedGame(root)
root.mainloop()