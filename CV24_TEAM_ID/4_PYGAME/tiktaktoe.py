import pygame, sys
pygame.init()
pygame.mixer.init()

# --- Config ---
WIDTH, HEIGHT = 300, 350
LINE_WIDTH = 5
BOARD_SIZE = 3
SQUARE = WIDTH // BOARD_SIZE
SPACE = SQUARE // 4
CIRCLE_RADIUS = SQUARE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
MOVE_TIME = 5

# Colors
BG = (255, 248, 220)
LINE = (150, 150, 150)
CIRCLE = (173, 216, 230)
CROSS = (255, 182, 193)
TEXT = (50, 50, 50)
HIGHLIGHT = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe – Enhanced")
font = pygame.font.SysFont("arialrounded", 26, bold=True)

# Optional sounds
try:
    move_sound = pygame.mixer.Sound("move.wav")
    win_sound = pygame.mixer.Sound("win.wav")
except:
    move_sound = win_sound = None

board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
current = 1
game_over = False
winner_combo = None
winner_player = None

timer = MOVE_TIME
last_tick = pygame.time.get_ticks()
frame_count = 0

def draw_background():
    for y in range(HEIGHT):
        color = (255 - y // 3, 248 - y // 5, 220 - y // 6)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

def draw_lines():
    draw_background()
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE, (0, i * SQUARE), (WIDTH, i * SQUARE), LINE_WIDTH)
        pygame.draw.line(screen, LINE, (i * SQUARE, 0), (i * SQUARE, WIDTH), LINE_WIDTH)

def draw_grid_boxes():
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            rect = pygame.Rect(c * SQUARE, r * SQUARE, SQUARE, SQUARE)
            pygame.draw.rect(screen, (255, 255, 255), rect, border_radius=12)
            pygame.draw.rect(screen, LINE, rect, width=2, border_radius=12)

def draw_figures():
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            val = board[r][c]
            if val == 1:
                pygame.draw.line(screen, CROSS,
                                 (c * SQUARE + SPACE, r * SQUARE + SPACE),
                                 (c * SQUARE + SQUARE - SPACE, r * SQUARE + SQUARE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS,
                                 (c * SQUARE + SPACE, r * SQUARE + SQUARE - SPACE),
                                 (c * SQUARE + SQUARE - SPACE, r * SQUARE + SPACE),
                                 CROSS_WIDTH)
            elif val == 2:
                pygame.draw.circle(screen, CIRCLE,
                                   (c * SQUARE + SQUARE // 2, r * SQUARE + SQUARE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_hover():
    if not game_over:
        x, y = pygame.mouse.get_pos()
        if y < WIDTH:
            r, c = y // SQUARE, x // SQUARE
            if board[r][c] == 0:
                s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
                s.fill((255, 255, 255, 50))
                screen.blit(s, (c * SQUARE, r * SQUARE))

def animate(player, row, col):
    cx = col * SQUARE + SQUARE // 2
    cy = row * SQUARE + SQUARE // 2
    top_r = CIRCLE_RADIUS if player == 2 else SQUARE // 2
    for r in range(1, top_r, 3):
        draw_lines()
        draw_grid_boxes()
        draw_figures()
        if player == 2:
            pygame.draw.circle(screen, CIRCLE, (cx, cy), r, CIRCLE_WIDTH)
        else:
            pygame.draw.line(screen, CROSS, (cx - r, cy - r), (cx + r, cy + r), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS, (cx - r, cy + r), (cx + r, cy - r), CROSS_WIDTH)
        pygame.display.update()
        pygame.time.delay(10)

def check_win(pl):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == pl for j in range(BOARD_SIZE)):
            return ("row", i)
        if all(board[j][i] == pl for j in range(BOARD_SIZE)):
            return ("col", i)
    if all(board[i][i] == pl for i in range(BOARD_SIZE)):
        return ("diag", 0)
    if all(board[i][BOARD_SIZE - i - 1] == pl for i in range(BOARD_SIZE)):
        return ("diag", 1)
    return None

def draw_win_line(combo):
    typ, idx = combo
    if typ == "row":
        y = idx * SQUARE + SQUARE // 2
        pygame.draw.line(screen, HIGHLIGHT, (20, y), (WIDTH - 20, y), LINE_WIDTH * 2)
    elif typ == "col":
        x = idx * SQUARE + SQUARE // 2
        pygame.draw.line(screen, HIGHLIGHT, (x, 20), (x, WIDTH - 20), LINE_WIDTH * 2)
    else:
        if idx == 0:
            pygame.draw.line(screen, HIGHLIGHT, (20, 20), (WIDTH - 20, WIDTH - 20), LINE_WIDTH * 2)
        else:
            pygame.draw.line(screen, HIGHLIGHT, (20, WIDTH - 20), (WIDTH - 20, 20), LINE_WIDTH * 2)

def draw_win_line_flash(combo, frame):
    if (frame // 30) % 2 == 0:
        draw_win_line(combo)

def draw_status():
    pygame.draw.rect(screen, BG, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
    if not game_over:
        txt = f"Player {current}'s turn • {timer}s left"
    elif winner_player:
        txt = f"Player {winner_player} wins! Press R to restart."
    else:
        txt = "Draw! Press R to restart."
    text_surf = font.render(txt, True, TEXT)
    rect = text_surf.get_rect(center=(WIDTH // 2, WIDTH + (HEIGHT - WIDTH) // 2))
    screen.blit(text_surf, rect)

def draw_turn_indicator():
    center = (WIDTH - 30, WIDTH + (HEIGHT - WIDTH) // 2)
    color = CIRCLE if current == 2 else CROSS
    pygame.draw.circle(screen, color, center, 10)

# Initial draw
draw_lines()
draw_grid_boxes()
draw_status()
pygame.display.update()

# Game loop
while True:
    now = pygame.time.get_ticks()
    if now - last_tick >= 1000 and not game_over:
        timer -= 1
        last_tick = now
        if timer <= 0:
            current = 2 if current == 1 else 1
            timer = MOVE_TIME

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_r:
            board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            current = 1
            game_over = False
            winner_combo = None
            winner_player = None
            timer = MOVE_TIME
            draw_lines()
        elif ev.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = ev.pos
            if y < WIDTH:
                r, c = y // SQUARE, x // SQUARE
                if board[r][c] == 0:
                    board[r][c] = current
                    if move_sound: move_sound.play()
                    animate(current, r, c)
                    combo = check_win(current)
                    if combo:
                        game_over = True
                        winner_combo = combo
                        winner_player = current
                        if win_sound: win_sound.play()
                    elif all(board[i][j] != 0 for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
                        game_over = True
                    else:
                        current = 2 if current == 1 else 1
                        timer = MOVE_TIME

    draw_lines()
    draw_grid_boxes()
    draw_figures()
    draw_hover()
    if winner_combo:
        draw_win_line_flash(winner_combo, frame_count)
    draw_status()
    draw_turn_indicator()
    pygame.display.update()
    frame_count += 1