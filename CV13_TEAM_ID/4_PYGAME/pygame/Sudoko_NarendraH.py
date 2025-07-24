import pygame
import sys
import random

# --- Constants ---
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 2
THICK_LINE_WIDTH = 4
FONT_SIZE = 40
BUTTON_HEIGHT = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180) # Selection color
RED = (200, 0, 0)    # Invalid number color
GREEN = (0, 150, 0)  # Solved number color (optional)
LIGHT_GRAY = (230, 230, 230) # For button

class SudokuGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pygame Sudoku")
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.button_font = pygame.font.SysFont("Arial", 25)

        # Initial board (0 represents empty cells) - Example board
        self.board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]
        self.original_board = [row[:] for row in self.board] # Keep a copy of the initial puzzle
        self.solved_board = [row[:] for row in self.board] # For solving
        self.selected_cell = None
        self.running = True

        # Solve the board once at the start to have a solution for validation/display
        self.solve_sudoku(self.solved_board)

    def draw_grid(self):
        for i in range(GRID_SIZE + 1):
            line_thickness = THICK_LINE_WIDTH if i % 3 == 0 else LINE_WIDTH
            # Vertical lines
            pygame.draw.line(self.screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), line_thickness)
            # Horizontal lines
            pygame.draw.line(self.screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_thickness)

    def draw_numbers(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                num = self.board[row][col]
                if num != 0:
                    text_color = BLACK
                    if self.original_board[row][col] == 0: # User-entered number
                        # Check if the user-entered number is valid
                        if not self.is_valid_move(row, col, num, self.board):
                            text_color = RED
                        else:
                            text_color = GREEN # Or just BLACK if you don't want green for correct user input
                    
                    text_surface = self.font.render(str(num), True, text_color)
                    text_rect = text_surface.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2,
                                                               row * CELL_SIZE + CELL_SIZE // 2))
                    self.screen.blit(text_surface, text_rect)

    def draw_selection(self):
        if self.selected_cell:
            row, col = self.selected_cell
            pygame.draw.rect(self.screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def draw_solve_button(self):
        button_rect = pygame.Rect(0, WIDTH, WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(self.screen, LIGHT_GRAY, button_rect)
        pygame.draw.rect(self.screen, BLACK, button_rect, 2)
        text_surface = self.button_font.render("Solve", True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_valid_move(self, r, c, num, board_state):
        # Check row
        for x in range(GRID_SIZE):
            if board_state[r][x] == num and c != x:
                return False

        # Check column
        for x in range(GRID_SIZE):
            if board_state[x][c] == num and r != x:
                return False

        # Check 3x3 box
        start_row = r - r % 3
        start_col = c - c % 3
        for i in range(3):
            for j in range(3):
                if board_state[i + start_row][j + start_col] == num and (i + start_row != r or j + start_col != c):
                    return False
        return True

    def find_empty(self, board_state):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if board_state[r][c] == 0:
                    return (r, c) # row, col
        return None

    def solve_sudoku(self, board_state):
        find = self.find_empty(board_state)
        if not find:
            return True # Board is full, puzzle solved
        else:
            row, col = find

        for i in range(1, 10): # Try numbers 1 to 9
            if self.is_valid_move(row, col, i, board_state):
                board_state[row][col] = i

                if self.solve_sudoku(board_state): # Recursively try to solve
                    return True

                board_state[row][col] = 0 # Backtrack: reset the last placed number
        return False

    def handle_click(self, pos):
        if pos[1] < WIDTH: # Click within the grid
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            if self.original_board[row][col] == 0: # Only allow selection of empty cells
                self.selected_cell = (row, col)
            else:
                self.selected_cell = None
        else: # Click on the button area
            if pos[1] >= WIDTH and pos[1] < HEIGHT:
                self.solve_current_board()

    def handle_keypress(self, event):
        if self.selected_cell:
            row, col = self.selected_cell
            if event.key == pygame.K_BACKSPACE:
                self.board[row][col] = 0
            elif event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                self.board[row][col] = int(event.unicode)

    def solve_current_board(self):
        # Reset the current board to the original puzzle state
        # and then apply the solved board's numbers
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                self.board[r][c] = self.solved_board[r][c]
        self.selected_cell = None # Deselect any cell after solving

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    self.handle_keypress(event)

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_numbers()
            self.draw_selection()
            self.draw_solve_button()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SudokuGame()
    game.run()