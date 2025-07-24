import tkinter as tk
from tkinter import messagebox
import time
import random

try:
    import winsound  # For Windows sound
except ImportError:
    winsound = None

sentences_easy = [
    "Hello world.",
    "Python is fun.",
    "Coding is cool."
]

sentences_medium = [
    "Practice typing every day.",
    "Typing games can help improve speed.",
    "Stay calm and type with focus."
]

sentences_hard = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming languages like Python are versatile.",
    "Accuracy and speed are both important in typing tests."
]

class TypingSpeedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Typing Speed Challenge")
        self.root.geometry("820x580")
        self.root.configure(bg="#111")

        # Variables
        self.start_time = None
        self.timer_running = False
        self.time_left = 60
        self.sound_on = True
        self.wpm_scores = []
        self.difficulty = "Medium"

        # UI Elements
        self.title_label = tk.Label(root, text="🎯 Typing Speed Challenge", font=("Helvetica", 24, "bold"), fg="#00ffcc", bg="#111")
        self.title_label.pack(pady=10)

        # Difficulty Option Menu
        self.diff_var = tk.StringVar(value="Medium")
        self.diff_menu = tk.OptionMenu(root, self.diff_var, "Easy", "Medium", "Hard", command=self.change_difficulty)
        self.diff_menu.config(font=("Arial", 12), bg="#00cc99", fg="white")
        self.diff_menu.pack()

        # Timer Label
        self.timer_label = tk.Label(root, text="Time: 60s", font=("Helvetica", 16), fg="white", bg="#111")
        self.timer_label.pack(pady=5)

        # Sentence Display
        self.display_label = tk.Label(root, text="", font=("Courier", 16), wraplength=750, fg="#00ffcc", bg="#222", padx=10, pady=15)
        self.display_label.pack(pady=10)

        # Typing Input
        self.text_box = tk.Text(root, height=5, width=80, font=("Helvetica", 14), wrap="word")
        self.text_box.pack()
        self.text_box.bind("<Key>", self.start_game)

        # Button to restart
        self.submit_btn = tk.Button(root, text="Restart", command=self.restart_game, font=("Arial", 12), bg="#007acc", fg="white")
        self.submit_btn.pack(pady=10)

        # Sound toggle
        self.sound_btn = tk.Checkbutton(root, text="🔊 Sound", variable=tk.IntVar(value=1), command=self.toggle_sound, font=("Arial", 10), bg="#111", fg="white", selectcolor="#111")
        self.sound_btn.pack()

        # Results
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="#00ffcc", bg="#111")
        self.result_label.pack(pady=10)

        # WPM History
        self.history_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#111")
        self.history_label.pack()

        self.set_sentence()

    def change_difficulty(self, level):
        self.difficulty = level
        self.restart_game()

    def set_sentence(self):
        if self.difficulty == "Easy":
            self.sentence = random.choice(sentences_easy)
        elif self.difficulty == "Medium":
            self.sentence = random.choice(sentences_medium)
        else:
            self.sentence = random.choice(sentences_hard)
        self.display_label.config(text=self.sentence)

    def toggle_sound(self):
        self.sound_on = not self.sound_on

    def play_sound(self, frequency=600, duration=100):
        if self.sound_on and winsound:
            winsound.Beep(frequency, duration)

    def start_game(self, event=None):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.countdown()
        if self.sound_on:
            self.play_sound(800, 30)

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.timer_label.config(text="Time's up!")
            self.calculate_results()

    def calculate_results(self):
        typed = self.text_box.get("1.0", tk.END).strip()
        time_spent = 60
        words_typed = len(typed.split())
        wpm = round((words_typed / time_spent) * 60)
        accuracy = self.calculate_accuracy(self.sentence, typed)

        self.wpm_scores.append(wpm)
        history = ", ".join(map(str, self.wpm_scores))

        self.result_label.config(text=f"🔥 WPM: {wpm}    🎯 Accuracy: {accuracy}%")
        self.history_label.config(text=f"📊 Previous WPMs: {history}")
        self.play_sound(1000, 150)

    def calculate_accuracy(self, original, typed):
        original_words = original.split()
        typed_words = typed.split()

        correct = sum(o == t for o, t in zip(original_words, typed_words))
        accuracy = round((correct / len(original_words)) * 100)
        return accuracy

    def restart_game(self):
        self.text_box.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.history_label.config(text="")
        self.timer_label.config(text="Time: 60s")
        self.start_time = None
        self.time_left = 60
        self.timer_running = False
        self.set_sentence()

# Run Game
if __name__ == "__main__":
    root = tk.Tk()
    game = TypingSpeedGame(root)
    root.mainloop()