import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TypeStorm - Typing Speed Game")

# Fonts and colors
FONT = pygame.font.SysFont("consolas", 32)
BIG_FONT = pygame.font.SysFont("consolas", 48)
WHITE = (255, 255, 255)
NEON = (0, 255, 204)
BG = (15, 15, 15)
RED = (255, 60, 60)
GREEN = (50, 255, 120)

# Word list
words = ["princess", "glow", "speed", "dream", "keyboard", "python", "storm", "magic", "romance", "focus", "code", "light"]

# Game variables
input_text = ''
current_word = random.choice(words)
score = 0
correct = 0
total = 0
start_time = None
time_limit = 30
game_over = False

# Draw the screen
def draw():
    screen.fill(BG)

    title = BIG_FONT.render("TypeStorm", True, NEON)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    word_surface = FONT.render("Word: " + current_word, True, WHITE)
    screen.blit(word_surface, (100, 150))

    typed_surface = FONT.render("Your input: " + input_text, True, NEON)
    screen.blit(typed_surface, (100, 200))

    if start_time:
        elapsed = time.time() - start_time
        remaining = max(0, int(time_limit - elapsed))
        timer_surface = FONT.render(f"⏱ Time Left: {remaining}s", True, RED if remaining <= 5 else WHITE)
        screen.blit(timer_surface, (100, 260))

        if remaining == 0:
            show_results()

    pygame.display.flip()

# Show results
def show_results():
    global game_over
    game_over = True
    screen.fill(BG)
    accuracy = (correct / total * 100) if total > 0 else 0
    wpm = (correct / (time_limit / 60))

    result1 = BIG_FONT.render("Game Over! ✨", True, GREEN)
    result2 = FONT.render(f"WPM: {int(wpm)}", True, WHITE)
    result3 = FONT.render(f"Accuracy: {int(accuracy)}%", True, WHITE)

    screen.blit(result1, (WIDTH // 2 - result1.get_width() // 2, 150))
    screen.blit(result2, (WIDTH // 2 - result2.get_width() // 2, 220))
    screen.blit(result3, (WIDTH // 2 - result3.get_width() // 2, 260))
    pygame.display.flip()

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    if not game_over:
        draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if not start_time:
                    start_time = time.time()

                if event.key == pygame.K_RETURN:
                    total += 1
                    if input_text.strip() == current_word:
                        correct += 1
                    current_word = random.choice(words)
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

pygame.quit()
