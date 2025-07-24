import pygame
import sys
import time
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
LIGHT_BLUE = (173, 216, 230)
BLUE = (30, 144, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BACKGROUND = (240, 248, 255)

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

font_small = pygame.font.SysFont("arial", 26)
font_large = pygame.font.SysFont("arial", 40, bold=True)
font_title = pygame.font.SysFont("arial", 48, bold=True)

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect.",
    "Typing speed is a useful skill.",
    "Python is fun to learn and use.",
    "Stay focused and keep typing."
]
target_text = random.choice(sentences)

user_text = ''
start_time = None
finished = False
wpm = 0

def draw_text(text, font, color, surface, x, y, center=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def calculate_wpm(start, end, text):
    time_diff = (end - start) / 60  
    words = len(text.split())
    return round(words / time_diff) if time_diff > 0 else 0

def game_loop():
    global user_text, start_time, finished, wpm, target_text

    clock = pygame.time.Clock()
    
    while True:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not finished and event.type == pygame.KEYDOWN:
                if start_time is None:
                    start_time = time.time()

                if event.key == pygame.K_RETURN:
                    finished = True
                    end_time = time.time()
                    wpm = calculate_wpm(start_time, end_time, user_text)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            if finished and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    user_text = ''
                    finished = False
                    start_time = None
                    wpm = 0
                    target_text = random.choice(sentences)


        draw_text("Typing Speed Game", font_title, BLUE, screen, WIDTH // 2, 40, center=True)

        pygame.draw.rect(screen, WHITE, (100, 100, 700, 80), border_radius=10)
        pygame.draw.rect(screen, GRAY, (100, 100, 700, 80), 2, border_radius=10)
        draw_text("Target:", font_small, BLACK, screen, 110, 80)
        draw_text(target_text, font_large, BLACK, screen, 110, 125)

        pygame.draw.rect(screen, WHITE, (100, 220, 700, 60), border_radius=10)
        pygame.draw.rect(screen, GRAY, (100, 220, 700, 60), 2, border_radius=10)
        draw_text("Your Input:", font_small, BLACK, screen, 110, 200)
        draw_text(user_text, font_small, BLACK, screen, 110, 240)

        if finished:
            color = GREEN if user_text.strip() == target_text.strip() else RED
            draw_text(f"Your WPM: {wpm}", font_large, color, screen, WIDTH // 2, 330, center=True)
            draw_text("Press 'R' to retry", font_small, BLACK, screen, WIDTH // 2, 380, center=True)

        draw_text("Press [ENTER] to finish", font_small, BLACK, screen, 20, HEIGHT - 30)

        pygame.display.flip()
        clock.tick(60)

game_loop()
