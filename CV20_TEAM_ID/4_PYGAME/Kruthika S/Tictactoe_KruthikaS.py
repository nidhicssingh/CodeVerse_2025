import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = SQUARE_SIZE // 3 - 15
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 5

BG_COLOR = (34, 40, 49)
LINE_COLOR = (0, 173, 181)
CIRCLE_COLOR = (238, 238, 238)
CROSS_COLOR = (255, 87, 34)
WIN_LINE_COLOR = (255, 255, 0)

FONT = pygame.font.SysFont('Arial', 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Enhanced UI")
screen.fill(BG_COLOR)

board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (20, i * SQUARE_SIZE), (WIDTH - 20, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 20), (i * SQUARE_SIZE, HEIGHT - 20), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            centerX = col * SQUARE_SIZE + SQUARE_SIZE // 2
            centerY = row * SQUARE_SIZE + SQUARE_SIZE // 2
            if board[row][col] == 1:
                offset = 5
                pygame.draw.line(screen, (0, 0, 0),
                                 (col * SQUARE_SIZE + SPACE + offset, row * SQUARE_SIZE + SPACE + offset),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE + offset,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE + offset),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, (0, 0, 0),
                                 (col * SQUARE_SIZE + SPACE + offset,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE + offset),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE + offset,
                                  row * SQUARE_SIZE + SPACE + offset),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                  row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, (0, 0, 0), (centerX + 5, centerY + 5), CIRCLE_RADIUS, CIRCLE_WIDTH)
                pygame.draw.circle(screen, CIRCLE_COLOR, (centerX, centerY), CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_win_line(start_pos, end_pos):
    pygame.draw.line(screen, WIN_LINE_COLOR, start_pos, end_pos, 15)
    pygame.display.update()
    pygame.time.wait(1000)

def check_win(player):
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            start_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 30)
            end_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 30)
            draw_win_line(start_pos, end_pos)
            return True
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            start_pos = (30, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            end_pos = (WIDTH - 30, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            draw_win_line(start_pos, end_pos)
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        draw_win_line((30, 30), (WIDTH - 30, HEIGHT - 30))
        return True
    if all(board[i][BOARD_COLS - i - 1] == player for i in range(BOARD_ROWS)):
        draw_win_line((WIDTH - 30, 30), (30, HEIGHT - 30))
        return True
    return False

def is_draw():
    for row in board:
        if 0 in row:
            return False
    return True

def display_message(message):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    text_surface = FONT.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)


def restart_game():
    global board, current_player
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    screen.fill(BG_COLOR)
    draw_lines()
    current_player = 1

draw_lines()
current_player = 1
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
            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = current_player
                if check_win(current_player):
                    display_message(f"Player {current_player} Wins!")
                    game_over = True
                elif is_draw():
                    display_message("It's a Draw!")
                    game_over = True
                current_player = 2 if current_player == 1 else 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
    draw_figures()
    pygame.display.update()
    if game_over:
        display_message("Press 'R' to Restart")
