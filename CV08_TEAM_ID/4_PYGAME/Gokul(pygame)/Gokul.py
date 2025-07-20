import pygame as pg, sys, time
from pygame.locals import *

# Setup
WIDTH, HEIGHT = 400, 400
STATUS_H = 80
LINE_W = 4

BG = (30, 30, 30)
LINE = (200, 200, 200)
COLOR_X = (255, 50, 50)
COLOR_O = (50, 200, 255)
STATUS_C = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT + STATUS_H))
pg.display.set_caption("tic tac toe")
clock = pg.time.Clock()
font_small = pg.font.Font(None, 36)
font_sym = pg.font.Font(None, 100)

# Game state
board = [[None]*3 for _ in range(3)]
current = 'x'
winner = None
is_draw = False

# Drawing functions
def draw_grid():
    for i in (1, 2):
        pg.draw.line(screen, LINE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_W)
        pg.draw.line(screen, LINE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_W)

def draw_figures():
    for r in range(3):
        for c in range(3):
            sym = board[r][c]
            if sym:
                color = COLOR_X if sym == 'x' else COLOR_O
                text = font_sym.render(sym.upper(), True, color)
                pos = (
                    c * WIDTH//3 + WIDTH//6 - text.get_width()//2,
                    r * HEIGHT//3 + HEIGHT//6 - text.get_height()//2
                )
                screen.blit(text, pos)

def draw_status():
    if winner:
        msg = f"{winner.upper()} wins!"
    elif is_draw:
        msg = "Draw!"
    else:
        msg = f"{current.upper()}'s turn"
    txt = font_small.render(msg, True, STATUS_C)
    screen.fill(BG, (0, HEIGHT, WIDTH, STATUS_H))
    screen.blit(txt, (10, HEIGHT + 20))

def check_win():
    global winner, is_draw
    lines = board + [list(c) for c in zip(*board)] + [
        [board[i][i] for i in range(3)],
        [board[i][2-i] for i in range(3)]
    ]
    for ln in lines:
        if ln[0] and ln.count(ln[0]) == 3:
            winner = ln[0]
            return
    if all(cell for row in board for cell in row):
        is_draw = True

def handle_click(pos):
    global current
    x, y = pos
    if x < WIDTH and y < HEIGHT and not (winner or is_draw):
        r, c = y // (HEIGHT//3), x // (WIDTH//3)
        if board[r][c] is None:
            board[r][c] = current
            check_win()
            current = 'o' if current == 'x' else 'x'

# Main loop
while True:
    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit(); sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            handle_click(e.pos)

    screen.fill(BG)
    draw_grid()
    draw_figures()
    draw_status()
    pg.display.flip()
    clock.tick(60)

    if winner or is_draw:
        time.sleep(2)
        board = [[None]*3 for _ in range(3)]
        current, winner, is_draw = 'x', None, False
