import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x320")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []

        self.info = tk.Label(root, text="Player X's Turn", font=("Arial", 14))
        self.info.pack(pady=5)

        self.frame = tk.Frame(root)
        self.frame.pack()

        for i in range(9):
            btn = tk.Button(self.frame, text="", font=("Arial", 20), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        self.reset_btn = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_btn.pack(pady=5)

    def make_move(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.info.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        win_combos = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
        for i,j,k in win_combos:
            if self.board[i] == self.board[j] == self.board[k] != "":
                return True
        return False

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        self.info.config(text="Player X's Turn")
        for btn in self.buttons:
            btn.config(text="", state="normal")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()