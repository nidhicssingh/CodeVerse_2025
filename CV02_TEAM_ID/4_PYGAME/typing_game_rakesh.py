import pygame
import random
import time
import sys
pygame.init()
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")
FONT = pygame.font.SysFont("Segoe UI", 36)
BIG_FONT = pygame.font.SysFont("Segoe UI", 48, bold=True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (30, 144, 255)
words = ["python", "typing", "speed", "keyboard", "program", "game", "pygame", "function", "display", "loop", "time"]
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    rect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, rect)
def game_loop():
    input_text = ''
    word = random.choice(words)
    score = 0
    start_time = time.time()
    time_limit = 60
    is_active = True
    while True:
        win.fill(WHITE)
        elapsed = time.time() - start_time
        remaining_time = max(0, int(time_limit - elapsed))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if is_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.strip() == word:
                            score += 1
                        word = random.choice(words)
                        input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return game_loop()
        draw_text(f"Time Left: {remaining_time}s", FONT, BLUE, win, WIDTH // 2, 30)
        draw_text(f"Word: {word}", BIG_FONT, BLACK, win, WIDTH // 2, 120)
        draw_text(f"Your Input: {input_text}", FONT, GRAY, win, WIDTH // 2, 180)
        draw_text(f"Score: {score}", FONT, GREEN, win, WIDTH // 2, 240)
        if remaining_time <= 0:
            is_active = False
            draw_text("Time's Up!", BIG_FONT, RED, win, WIDTH // 2, 310)
            draw_text("Press 'R' to Restart", FONT, BLACK, win, WIDTH // 2, 350)
        pygame.display.update()
game_loop()