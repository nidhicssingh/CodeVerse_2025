import pygame
import time
pygame.font.init()

# Board (0 represents empty cells)
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
    board = board

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.model = None
        self.selected = None
        self.win = win

    def draw(self):
        gap = self.width / 9
        for i in range(self.rows + 1):
            line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.width, i * gap), line_width)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), line_width)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            if valid(self.board, val, (row, col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].temp = val

    def select(self, row, col):
        self.clear()
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        for row in self.cubes:
            for cube in row:
                cube.selected = False

    def solve(self):
        find = find_empty(self.board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.board, i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

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
        fnt = pygame.font.SysFont("comicsans", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap - text.get_width())/2, y + (gap - text.get_height())/2))
        elif self.temp != 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def redraw_window(win, board):
    win.fill((255, 255, 255))
    board.draw()

def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    key = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: key = 1
                if event.key == pygame.K_2: key = 2
                if event.key == pygame.K_3: key = 3
                if event.key == pygame.K_4: key = 4
                if event.key == pygame.K_5: key = 5
                if event.key == pygame.K_6: key = 6
                if event.key == pygame.K_7: key = 7
                if event.key == pygame.K_8: key = 8
                if event.key == pygame.K_9: key = 9
                if event.key == pygame.K_DELETE:
                    row, col = board.selected
                    board.cubes[row][col].set(0)
                    key = None
                if event.key == pygame.K_RETURN:
                    row, col = board.selected
                    if board.cubes[row][col].temp != 0:
                        if board.place(board.cubes[row][col].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // (board.width // 9)
                y = pos[1] // (board.height // 9)
                board.select(int(y), int(x))
                key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(win, board)
        pygame.display.update()

main()
pygame.quit()
