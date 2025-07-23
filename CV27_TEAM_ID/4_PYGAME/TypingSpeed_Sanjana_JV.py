import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Fonts
font_big = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Word List
word_list = ["python", "keyboard", "game", "pygame", "typing", "speed", "challenge", "fun", "project", "timer"]

# Game variables
input_text = ''
target_word = random.choice(word_list)
start_time = None
game_over = False
result = ''

# Draw screen
def draw():
    screen.fill(WHITE)

    # Title
    title = font_big.render("Typing Speed Game", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Target Word
    word_display = font_small.render(f"Type this: {target_word}", True, BLACK)
    screen.blit(word_display, (WIDTH // 2 - word_display.get_width() // 2, 120))

    # User Input
    user_input = font_small.render(f"Your input: {input_text}", True, BLACK)
    screen.blit(user_input, (WIDTH // 2 - user_input.get_width() // 2, 180))

    # Result
    if game_over:
        result_display = font_big.render(result, True, BLACK)
        screen.blit(result_display, (WIDTH // 2 - result_display.get_width() // 2, 250))

    pygame.display.update()

# Main loop
running = True
while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif not game_over and event.type == pygame.KEYDOWN:
            if start_time is None:
                start_time = time.time()

            if event.key == pygame.K_RETURN:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)

                if input_text.strip().lower() == target_word.lower():
                    wpm = round(len(target_word) * 60 / (5 * total_time), 2)
                    result = f"Correct! WPM: {wpm}"
                else:
                    result = "Incorrect word! Try again."

                game_over = True

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

            else:
                input_text += event.unicode

pygame.quit()
sys.exit()
