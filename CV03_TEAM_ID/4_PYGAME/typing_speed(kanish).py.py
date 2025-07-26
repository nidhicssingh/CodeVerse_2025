import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Fonts and colors
font_large = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Word list
words = ["python", "codeverse", "keyboard", "speed", "typing", "game", "challenge", "developer", "function", "variable"]
current_word = random.choice(words)
input_text = ""
score = 0
start_time = time.time()
game_duration = 60  # seconds

# Game loop
running = True
while running:
    screen.fill(WHITE)

    elapsed_time = time.time() - start_time
    time_left = max(0, int(game_duration - elapsed_time))

    # End game after time runs out
    if time_left == 0:
        running = False

    # Display current word
    word_surface = font_large.render(current_word, True, BLACK)
    screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, HEIGHT // 3))

    # Display input text
    input_surface = font_large.render(input_text, True, BLACK)
    screen.blit(input_surface, (WIDTH // 2 - input_surface.get_width() // 2, HEIGHT // 2))

    # Display timer and score
    timer_surface = font_small.render(f"Time Left: {time_left}s", True, BLACK)
    score_surface = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(timer_surface, (20, 20))
    screen.blit(score_surface, (20, 60))

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.lower() == current_word.lower():
                    score += 1
                input_text = ""
                current_word = random.choice(words)
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

# Final screen
screen.fill(WHITE)
final_surface = font_large.render(f"Final Score: {score}", True, BLACK)
screen.blit(final_surface, (WIDTH // 2 - final_surface.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()