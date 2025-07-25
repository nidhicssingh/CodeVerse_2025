import pygame
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 25)

# Sample Sudoku board (0 = empty)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

class Grid:
    def __init__(self, rows, cols, width, height, board):
        self.rows = rows
        self.cols = cols
        self.board = board
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.selected = None

    def draw(self, win):
        gap = self.width / 9
        for i in range(self.rows + 1):
            thick = 4 if i % 3 == 0 else 1
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

        if self.selected:
            row, col = self.selected
            pygame.draw.rect(win, (255, 0, 0), (col * gap, row * gap, gap, gap), 3)

    def click(self, pos):
        if pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            self.selected = (int(y), int(x))
            return True
        return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set(val)

class Cube:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def set(self, val):
        if val >= 0 and val <= 9:
            self.value = val

    def draw(self, win):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

def redraw_window(win, board):
    win.fill((255, 255, 255))
    board.draw(win)

def main():
    win = WIN
    board_obj = Grid(9, 9, 540, 540, board)
    key = None
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board_obj.click(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_0:
                    key = 0

                if board_obj.selected and key is not None:
                    board_obj.sketch(key)
                    key = None

        redraw_window(win, board_obj)
        pygame.display.update()

main()
pygame.quit()
