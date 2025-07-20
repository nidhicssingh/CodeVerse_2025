import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Fonts
FONT_BIG = pygame.font.SysFont("arial", 48)
FONT_MED = pygame.font.SysFont("arial", 36)
FONT_SMALL = pygame.font.SysFont("arial", 28)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
GRAY = (230, 230, 230)

# Word List
words = [
    "python", "developer", "keyboard", "gaming", "speed",
    "screen", "window", "display", "typing", "project",
    "timer", "music", "function", "variable", "sprite",
    "player", "score", "input", "output", "loop"
]

# Game Variables
current_word = random.choice(words)
user_input = ""
start_time = 0
score = 0
mistakes = 0
total_words = 10
words_typed = 0
game_active = False

def draw_ui():
    screen.fill(GRAY)

    draw_center_text("Typing Speed Game", FONT_BIG, BLUE, HEIGHT // 8)
    draw_center_text("Type the word shown below:", FONT_SMALL, BLACK, HEIGHT // 8 + 50)

    # Show word to type
    draw_center_text(current_word, FONT_BIG, BLACK, HEIGHT // 2 - 30)

    # User input box
    pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2 + 30, WIDTH // 2, 50), border_radius=8)
    input_text = FONT_MED.render(user_input, True, BLACK)
    screen.blit(input_text, (WIDTH // 4 + 10, HEIGHT // 2 + 40))

    # Show score
    draw_center_text(f"Score: {score}    Mistakes: {mistakes}", FONT_SMALL, GREEN, HEIGHT - 100)

def draw_center_text(text, font, color, y):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    screen.blit(rendered, rect)

def show_result():
    screen.fill(GRAY)
    time_taken = max(time.time() - start_time, 1)
    wpm = round((score / time_taken) * 60)

    draw_center_text("Game Over!", FONT_BIG, RED, HEIGHT // 4)
    draw_center_text(f"Your WPM: {wpm}", FONT_MED, BLUE, HEIGHT // 2 - 20)
    draw_center_text(f"Correct Words: {score}  |  Mistakes: {mistakes}", FONT_MED, BLACK, HEIGHT // 2 + 40)
    draw_center_text("Press R to Restart", FONT_SMALL, BLACK, HEIGHT // 2 + 100)

    pygame.display.update()

def reset_game():
    global current_word, user_input, score, mistakes, words_typed, start_time, game_active
    current_word = random.choice(words)
    user_input = ""
    score = 0
    mistakes = 0
    words_typed = 0
    start_time = time.time()
    game_active = True

# Game loop
reset_game()
running = True
while running:
    screen.fill(WHITE)

    if game_active:
        draw_ui()
    else:
        show_result()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.strip() == current_word:
                    score += 1
                else:
                    mistakes += 1

                words_typed += 1
                user_input = ""
                current_word = random.choice(words)

                if words_typed >= total_words:
                    game_active = False

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

        elif not game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

pygame.quit()
