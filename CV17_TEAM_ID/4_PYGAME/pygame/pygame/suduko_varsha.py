import pygame
import time

pygame.init()

WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Fonts
FONT = pygame.font.SysFont("comicsans", 40)
SMALL_FONT = pygame.font.SysFont("comicsans", 20)

# Colors
WHITE = (255, 255, 255)
GREY = (120, 120, 120)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Sample Sudoku Board (0 = Empty)
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
        self.cubes = [[Cube(board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.model = None
        self.selected = None

    def draw(self, win):
        gap = self.width / 9
        # Draw grid lines
        for i in range(self.rows + 1):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(win, BLACK, (0, i * gap), (self.width, i * gap), line_width)
            pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, self.height), line_width)

        # Draw cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = int(pos[0] // gap)
            y = int(pos[1] // gap)
            return (y, x)
        return None

    def select(self, row, col):
        # Deselect all first
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def place(self, val):
        row, col = self.selected
        self.cubes[row][col].value = val
        self.board[row][col] = val

    def is_valid(self, num, row, col):
        # Check row
        for i in range(9):
            if self.board[row][i] == num and col != i:
                return False
        # Check column
        for i in range(9):
            if self.board[i][col] == num and row != i:
                return False
        # Check box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True


class Cube:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = FONT.render(str(self.value), True, BLACK)
            win.blit(text, (x + 20, y + 10))

        if self.selected:
            pygame.draw.rect(win, BLUE, (x, y, gap, gap), 3)


def redraw_window(win, board):
    win.fill(WHITE)
    board.draw(win)
    pygame.display.update()


def main():
    win = WIN
    board_obj = Grid(9, 9, WIDTH, WIDTH, board)
    key = None
    run = True

    while run:
        redraw_window(win, board_obj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_KP1]: key = 1
                elif event.key in [pygame.K_2, pygame.K_KP2]: key = 2
                elif event.key in [pygame.K_3, pygame.K_KP3]: key = 3
                elif event.key in [pygame.K_4, pygame.K_KP4]: key = 4
                elif event.key in [pygame.K_5, pygame.K_KP5]: key = 5
                elif event.key in [pygame.K_6, pygame.K_KP6]: key = 6
                elif event.key in [pygame.K_7, pygame.K_KP7]: key = 7
                elif event.key in [pygame.K_8, pygame.K_KP8]: key = 8
                elif event.key in [pygame.K_9, pygame.K_KP9]: key = 9
                elif event.key == pygame.K_DELETE:
                    row, col = board_obj.selected
                    board_obj.cubes[row][col].value = 0
                    board_obj.board[row][col] = 0
                    key = None

                if board_obj.selected and key is not None:
                    row, col = board_obj.selected
                    if board_obj.is_valid(key, row, col):
                        board_obj.place(key)
                    key = None

            # Mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board_obj.click(pos)
                if clicked:
                    board_obj.select(clicked[0], clicked[1])

    pygame.quit()


if __name__ == "__main__":
    main()
