import pygame
import sys
import random

pygame.init()
pygame.font.init()

# Screen setup
WIDTH, HEIGHT = 600, 700
ROWS, COLS = 3, 3
SQSIZE = WIDTH // COLS
LINE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Deluxe Showdown")

# Colors
BG_TOP = (20, 20, 40)
BG_BOTTOM = (40, 20, 60)
LINE_COLOR = (240, 240, 240)
X_COLOR = (255, 100, 100)
O_COLOR = (100, 200, 255)
WIN_LINE_COLOR = (255, 255, 100)
HIGHLIGHT = (100, 255, 150, 50)

# Board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
player = 1
scores = [0, 0]
game_over = False

font = pygame.font.SysFont("consolas", 36)
title_font = pygame.font.SysFont("impact", 48)

def draw_background():
    for y in range(HEIGHT):
        blend = y / HEIGHT
        r = int(BG_TOP[0] * (1 - blend) + BG_BOTTOM[0] * blend)
        g = int(BG_TOP[1] * (1 - blend) + BG_BOTTOM[1] * blend)
        b = int(BG_TOP[2] * (1 - blend) + BG_BOTTOM[2] * blend)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, WIDTH), LINE_WIDTH)

def draw_scores():
    p1_text = font.render(f"Player 1 (O): {scores[0]}", True, O_COLOR)
    p2_text = font.render(f"Player 2 (X): {scores[1]}", True, X_COLOR)
    screen.blit(p1_text, (20, HEIGHT - 90))
    screen.blit(p2_text, (20, HEIGHT - 50))

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            cx, cy = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
            if board[row][col] == 1:
                pygame.draw.circle(screen, O_COLOR, (cx, cy), SQSIZE // 3, 6)
            elif board[row][col] == 2:
                offset = SQSIZE // 3
                pygame.draw.line(screen, X_COLOR, (cx - offset, cy - offset), (cx + offset, cy + offset), 6)
                pygame.draw.line(screen, X_COLOR, (cx - offset, cy + offset), (cx + offset, cy - offset), 6)

def highlight_hover(pos):
    if game_over:
        return
    x, y = pos
    row, col = y // SQSIZE, x // SQSIZE
    if row < ROWS and col < COLS and board[row][col] == 0:
        surf = pygame.Surface((SQSIZE, SQSIZE), pygame.SRCALPHA)
        pygame.draw.rect(surf, HIGHLIGHT, (0, 0, SQSIZE, SQSIZE))
        screen.blit(surf, (col * SQSIZE, row * SQSIZE))

def mark_square(row, col, player):
    board[row][col] = player

def is_available(row, col):
    return board[row][col] == 0

def draw_win_line(start, end):
    pygame.draw.line(screen, WIN_LINE_COLOR, start, end, 10)

def check_win(player):
    for row in range(ROWS):
        if all(board[row][col] == player for col in range(COLS)):
            draw_win_line((20, row * SQSIZE + SQSIZE // 2), (WIDTH - 20, row * SQSIZE + SQSIZE // 2))
            return True
    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            draw_win_line((col * SQSIZE + SQSIZE // 2, 20), (col * SQSIZE + SQSIZE // 2, WIDTH - 20))
            return True
    if all(board[i][i] == player for i in range(ROWS)):
        draw_win_line((20, 20), (WIDTH - 20, WIDTH - 20))
        return True
    if all(board[i][COLS - 1 - i] == player for i in range(ROWS)):
        draw_win_line((20, WIDTH - 20), (WIDTH - 20, 20))
        return True
    return False

def restart():
    global board, game_over, player
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False
    player = random.choice([1, 2])

# First draw
draw_background()
draw_grid()
player = random.choice([1, 2])
clock = pygame.time.Clock()

# Main loop
while True:
    draw_background()
    draw_grid()
    draw_scores()
    draw_figures()
    highlight_hover(pygame.mouse.get_pos())

    if game_over:
        over_text = font.render("Game Over! Press R to Restart", True, (255, 255, 255))
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT - 140))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = pygame.mouse.get_pos()
            if my < SQSIZE * ROWS:
                row, col = my // SQSIZE, mx // SQSIZE
                if is_available(row, col):
                    mark_square(row, col, player)
                    if check_win(player):
                        scores[player - 1] += 1
                        game_over = True
                    player = 2 if player == 1 else 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
    clock.tick(60)