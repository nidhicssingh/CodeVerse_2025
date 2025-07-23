import pygame
import sys

# Initialize
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700
ROWS, COLS = 3, 3
SQSIZE = WIDTH // COLS
LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20
OFFSET = 50

# Colors
BG_COLOR = (30, 30, 60)
LINE_COLOR = (200, 200, 200)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (255, 80, 80)
WIN_LINE_COLOR = (50, 205, 50)
TEXT_COLOR = (255, 255, 255)

# Fonts
FONT = pygame.font.SysFont("arial", 36)
BIG_FONT = pygame.font.SysFont("arial", 48, bold=True)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Navya G")
screen.fill(BG_COLOR)

# Board data
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Draw grid lines
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, SQSIZE * ROWS), LINE_WIDTH)

# Draw pieces
def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                # Draw X
                start1 = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                end1 = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                start2 = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                end2 = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                pygame.draw.line(screen, CROSS_COLOR, start1, end1, CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, start2, end2, CROSS_WIDTH)
            elif board[row][col] == 2:
                # Draw O
                center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
                pygame.draw.circle(screen, CIRC_COLOR, center, SQSIZE // 3, CIRC_WIDTH)

# Mark cell
def mark_cell(row, col, player):
    board[row][col] = player

# Check if cell is empty
def is_empty(row, col):
    return board[row][col] == 0

# Check for win
def check_win(player):
    # Vertical
    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            draw_win_line((col, 0), (col, 2))
            return True
    # Horizontal
    for row in range(ROWS):
        if all(board[row][col] == player for col in range(COLS)):
            draw_win_line((0, row), (2, row))
            return True
    # Diagonal
    if all(board[i][i] == player for i in range(ROWS)):
        draw_win_line((0, 0), (2, 2))
        return True
    if all(board[i][2 - i] == player for i in range(ROWS)):
        draw_win_line((0, 2), (2, 0))
        return True
    return False

# Draw winning line
def draw_win_line(start, end):
    x1 = start[0] * SQSIZE + SQSIZE // 2
    y1 = start[1] * SQSIZE + SQSIZE // 2
    x2 = end[0] * SQSIZE + SQSIZE // 2
    y2 = end[1] * SQSIZE + SQSIZE // 2
    pygame.draw.line(screen, WIN_LINE_COLOR, (x1, y1), (x2, y2), 12)

# Draw text
def draw_text(text):
    label = BIG_FONT.render(text, True, TEXT_COLOR)
    screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 620))

def draw_subtext(text):
    sub = FONT.render(text, True, TEXT_COLOR)
    screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 660))

# Restart game
def restart():
    screen.fill(BG_COLOR)
    draw_grid()
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

# Game setup
draw_grid()
player = 1
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            if mouseY < SQSIZE * 3:
                clicked_row = mouseY // SQSIZE
                clicked_col = mouseX // SQSIZE

                if is_empty(clicked_row, clicked_col):
                    mark_cell(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = 2 if player == 1 else 1
                    draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    if game_over:
        draw_text("Game Over!")
        draw_subtext("Press R to Restart")

    pygame.display.update()
