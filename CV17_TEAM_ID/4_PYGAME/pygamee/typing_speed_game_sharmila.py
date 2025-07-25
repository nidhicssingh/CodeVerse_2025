import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Master - Sharmila Edition")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 200)  # bluish green
RED = (255, 50, 50)

# Fonts
font = pygame.font.SysFont("Comic Sans MS", 40)
small_font = pygame.font.SysFont("Comic Sans MS", 30)

# Game variables
word_list = ["mango", "guitar", "laptop", "coding", "future", "school", "dream", "sky", "ocean", "planet"]
word = random.choice(word_list)
word_x = random.randint(50, WIDTH - 150)
word_y = 0
word_speed = 1

typed_text = ""
score = 0
missed = 0
max_missed = 5
clock = pygame.time.Clock()
game_over = False

def draw_text(text, size, color, x, y):
    font_ = pygame.font.SysFont("Comic Sans MS", size)
    label = font_.render(text, True, color)
    screen.blit(label, (x, y))

# Main game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if typed_text == word:
                        score += 1
                        word = random.choice(word_list)
                        word_x = random.randint(50, WIDTH - 150)
                        word_y = 0
                        typed_text = ""
                        word_speed += 0.2
                    else:
                        missed += 1
                        typed_text = ""
                        if missed >= max_missed:
                            game_over = True
                else:
                    typed_text += event.unicode

    if not game_over:
        word_y += word_speed
        if word_y > HEIGHT:
            missed += 1
            word = random.choice(word_list)
            word_x = random.randint(50, WIDTH - 150)
            word_y = 0
            if missed >= max_missed:
                game_over = True

        draw_text(word, 40, BLACK, word_x, int(word_y))
        draw_text("Type: " + typed_text, 30, GREEN, 50, HEIGHT - 60)
        draw_text(f"Score: {score}", 25, BLACK, 10, 10)
        draw_text(f"Missed: {missed}/{max_missed}", 25, RED, WIDTH - 170, 10)
    else:
        draw_text("Game Over!", 60, RED, WIDTH // 2 - 150, HEIGHT // 2 - 60)
        draw_text(f"Final Score: {score}", 40, BLACK, WIDTH // 2 - 120, HEIGHT // 2)
        draw_text("Press R to Restart", 30, BLACK, WIDTH // 2 - 100, HEIGHT // 2 + 50)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            word = random.choice(word_list)
            word_x = random.randint(50, WIDTH - 150)
            word_y = 0
            typed_text = ""
            score = 0
            missed = 0
            word_speed = 1
            game_over = False

    # Add your name
    draw_text("Made by Sharmila", 20, (100, 100, 100), WIDTH - 180, HEIGHT - 30)

    pygame.display.update()
    clock.tick(60)