import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 6
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CROSS_COLOR = (66, 66, 66)
CIRCLE_COLOR = (242, 85, 96)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# Game state
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = "X"

def draw_lines():
    # Vertical
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (SQUARE_SIZE * col, 0), (SQUARE_SIZE * col, HEIGHT), LINE_WIDTH)
    # Horizontal
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE * row), (WIDTH, SQUARE_SIZE * row), LINE_WIDTH)

def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   SQUARE_SIZE // 3, LINE_WIDTH)
            elif board[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + 30, row * SQUARE_SIZE + 30),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 30, row * SQUARE_SIZE + SQUARE_SIZE - 30), 
                                 LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + 30, row * SQUARE_SIZE + SQUARE_SIZE - 30),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 30, row * SQUARE_SIZE + 30), 
                                 LINE_WIDTH)

def check_winner():
    for row in board:
        if row.count(row[0]) == BOARD_COLS and row[0] is not None:
            return row[0]
    for col in range(BOARD_COLS):
        check = [board[row][col] for row in range(BOARD_ROWS)]
        if check.count(check[0]) == BOARD_ROWS and check[0] is not None:
            return check[0]
    if all(board[i][i] == board[0][0] for i in range(BOARD_ROWS)) and board[0][0] is not None:
        return board[0][0]
    if all(board[i][BOARD_ROWS - i - 1] == board[0][BOARD_ROWS - 1] for i in range(BOARD_ROWS)) and board[0][BOARD_ROWS - 1] is not None:
        return board[0][BOARD_ROWS - 1]
    return None

def restart():
    global board, player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = "X"
    screen.fill(WHITE)
    draw_lines()

# Main loop
draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_pos = event.pos[0] // SQUARE_SIZE
            y_pos = event.pos[1] // SQUARE_SIZE

            if board[y_pos][x_pos] is None:
                board[y_pos][x_pos] = player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    pygame.time.wait(2000)
                    restart()
                player = "O" if player == "X" else "X"
    draw_symbols()
    pygame.display.update()