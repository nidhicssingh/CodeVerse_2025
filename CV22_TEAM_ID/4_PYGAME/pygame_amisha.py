import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Fonts
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Word list
words = ["python", "keyboard", "function", "loop", "code", "speed", "typing", "game", "random", "logic"]

# Game variables
input_text = ""
current_word = random.choice(words)
score = 0
total_words = 10
typed_words = 0
start_time = None
game_over = False

# Functions
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    surface.blit(textobj, (x, y))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    if not start_time and not game_over:
        start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.strip() == current_word:
                        score += 1
                    input_text = ""
                    typed_words += 1
                    if typed_words >= total_words:
                        game_over = True
                        end_time = time.time()
                        total_time = end_time - start_time
                        wpm = (score / total_time) * 60
                        accuracy = (score / total_words) * 100
                    else:
                        current_word = random.choice(words)
                else:
                    input_text += event.unicode

    if not game_over:
        draw_text("Type the word:", font_medium, BLACK, screen, 50, 50)
        draw_text(current_word, font_large, RED, screen, 50, 100)
        draw_text("Your input: " + input_text, font_medium, GREEN, screen, 50, 200)
        draw_text(f"Words typed: {typed_words}/{total_words}", font_medium, BLACK, screen, 50, 300)
    else:
        draw_text("Game Over!", font_large, RED, screen, 300, 80)
        draw_text(f"Time Taken: {total_time:.2f} seconds", font_medium, BLACK, screen, 300, 150)
        draw_text(f"Words Per Minute: {wpm:.2f}", font_medium, BLACK, screen, 300, 200)
        draw_text(f"Accuracy: {accuracy:.2f}%", font_medium, BLACK, screen, 300, 250)
        draw_text("Press ESC to exit", font_medium, BLACK, screen, 300, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
