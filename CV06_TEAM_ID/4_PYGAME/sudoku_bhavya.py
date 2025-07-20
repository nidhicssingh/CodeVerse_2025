import tkinter as tk
from tkinter import messagebox

# Example Sudoku puzzle (0 = empty)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.entries = []

        for i in range(9):
            row = []
            for j in range(9):
                e = tk.Entry(root, width=2, font=('Arial', 20), justify='center')
                e.grid(row=i, column=j, padx=3, pady=3)
                if puzzle[i][j] != 0:
                    e.insert(0, str(puzzle[i][j]))
                    e.config(state='disabled', disabledforeground='black')
                row.append(e)
            self.entries.append(row)

        check_button = tk.Button(root, text="Check", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=9, pady=10)

    def check_solution(self):
        try:
            for i in range(9):
                row = []
                for j in range(9):
                    val = self.entries[i][j].get()
                    if val == '':
                        messagebox.showerror("Error", "Please fill all cells.")
                        return
                    row.append(int(val))
                if len(set(row)) != 9:
                    messagebox.showerror("Error", f"Row {i+1} has duplicates.")
                    return

            for j in range(9):
                col = [int(self.entries[i][j].get()) for i in range(9)]
                if len(set(col)) != 9:
                    messagebox.showerror("Error", f"Column {j+1} has duplicates.")
                    return

            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    box = []
                    for x in range(3):
                        for y in range(3):
                            box.append(int(self.entries[i+x][j+y].get()))
                    if len(set(box)) != 9:
                        messagebox.showerror("Error", f"3x3 box starting at ({i+1},{j+1}) has duplicates.")
                        return

            messagebox.showinfo("Success", "Congratulations! Sudoku solved correctly.")
        except ValueError:
            messagebox.showerror("Error", "Only numbers 1-9 allowed.")

# Run the game
root = tk.Tk()
root.title("Sudoku Game")
SudokuGUI(root)
root.mainloop()