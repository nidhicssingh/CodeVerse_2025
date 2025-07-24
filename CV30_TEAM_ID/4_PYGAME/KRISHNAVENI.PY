import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 20)

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)

# Sample puzzle (0 = empty)
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

original_board = [row[:] for row in board]  # To lock original numbers

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Selected cell
selected = None


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK if x % (CELL_SIZE * 3) == 0 else LIGHT_GRAY, (x, 0), (x, WIDTH))
        pygame.draw.line(screen, BLACK if x % (CELL_SIZE * 3) == 0 else LIGHT_GRAY, (0, x), (WIDTH, x))


def draw_numbers():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                color = BLACK if original_board[i][j] != 0 else BLUE
                text = FONT.render(str(board[i][j]), True, color)
                screen.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))


def draw_selected():
    if selected:
        pygame.draw.rect(screen, RED, (selected[1] * CELL_SIZE, selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)


def is_valid(num, row, col):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def is_full():
    return all(board[i][j] != 0 for i in range(9) for j in range(9))


def draw_message(message, color=GREEN):
    text = SMALL_FONT.render(message, True, color)
    screen.blit(text, (10, HEIGHT - 40))


def main():
    global selected
    running = True
    message = ""

    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        draw_selected()
        if message:
            draw_message(message)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < WIDTH:
                    selected = (y // CELL_SIZE, x // CELL_SIZE)

            elif event.type == pygame.KEYDOWN and selected:
                row, col = selected
                if original_board[row][col] == 0:
                    if event.unicode.isdigit():
                        num = int(event.unicode)
                        if 1 <= num <= 9:
                            if is_valid(num, row, col):
                                board[row][col] = num
                                message = ""
                                if is_full():
                                    message = "Sudoku Completed!"
                            else:
                                message = "Invalid Move!"
                        elif num == 0:
                            board[row][col] = 0
                            message = ""

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
