import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = []

        for row in range(9):
            row_entries = []
            for col in range(9):
                e = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
                e.grid(row=row, column=col, padx=2, pady=2)
                row_entries.append(e)
            self.entries.append(row_entries)

        solve_btn = tk.Button(root, text="Solve", command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=9, pady=10)

    def get_grid(self):
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.entries[row][col].get()
                current_row.append(int(val) if val.isdigit() else 0)
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    self.entries[row][col].insert(0, str(grid[row][col]))

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row//3), 3 * (col//3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists for this puzzle.")

root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()