import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
def mark_square(row, col, player):
    board[row][col] = player
def available_square(row, col):
    return board[row][col] == 0
def is_board_full():
    return all(all(cell != 0 for cell in row) for row in board)
def check_win(player):
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == player for i in range(BOARD_COLS)) or all(board[i][BOARD_COLS - i - 1] == player for i in range(BOARD_COLS)):
        return True
    return False
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
draw_lines()
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                elif is_board_full():
                    game_over = True
                player = 2 if player == 1 else 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    draw_figures()
    pygame.display.update()