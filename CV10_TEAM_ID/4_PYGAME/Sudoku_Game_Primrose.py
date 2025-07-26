import pygame
import time
import copy

pygame.init()
WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

FONT = pygame.font.SysFont("comicsans", 40)
SMALL_FONT = pygame.font.SysFont("comicsans", 25)

# Sample Sudoku Board (0 = empty)
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

original_board = copy.deepcopy(board)

selected = None

def draw_grid(win):
    gap = WIDTH // 9
    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(win, (0, 0, 0), (0, i * gap), (WIDTH, i * gap), thickness)
        pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, WIDTH), thickness)

def draw_numbers(win, board):
    gap = WIDTH // 9
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = FONT.render(str(board[i][j]), True, (0, 0, 0))
                win.blit(text, (j * gap + 20, i * gap + 10))

def draw_selected(win, row, col):
    if row is not None and col is not None:
        gap = WIDTH // 9
        pygame.draw.rect(win, (0, 255, 0), (col * gap, row * gap, gap, gap), 3)

def is_valid(bo, num, pos):
    row, col = pos
    for i in range(9):
        if bo[row][i] == num and i != col:
            return False
        if bo[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def is_complete(bo):
    for i in range(9):
        for j in range(9):
            num = bo[i][j]
            if num == 0 or not is_valid(bo, num, (i, j)):
                return False
    return True

def main():
    global selected
    run = True
    key = None
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        WIN.fill((255, 255, 255))
        draw_grid(WIN)
        draw_numbers(WIN, board)
        if selected:
            draw_selected(WIN, selected[0], selected[1])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                gap = WIDTH // 9
                col = x // gap
                row = y // gap
                selected = (row, col)

            # Keyboard input
            if event.type == pygame.KEYDOWN:
                if selected and original_board[selected[0]][selected[1]] == 0:
                    if event.key == pygame.K_1:
                        key = 1
                    elif event.key == pygame.K_2:
                        key = 2
                    elif event.key == pygame.K_3:
                        key = 3
                    elif event.key == pygame.K_4:
                        key = 4
                    elif event.key == pygame.K_5:
                        key = 5
                    elif event.key == pygame.K_6:
                        key = 6
                    elif event.key == pygame.K_7:
                        key = 7
                    elif event.key == pygame.K_8:
                        key = 8
                    elif event.key == pygame.K_9:
                        key = 9
                    elif event.key == pygame.K_DELETE:
                        board[selected[0]][selected[1]] = 0
                        key = None
                    elif event.key == pygame.K_RETURN:
                        if is_complete(board):
                            print("Sudoku Solved!")
                        else:
                            print("Not correct yet!")

                    if key:
                        board[selected[0]][selected[1]] = key
                        key = None

    pygame.quit()

if __name__ == "__main__":
    main()
