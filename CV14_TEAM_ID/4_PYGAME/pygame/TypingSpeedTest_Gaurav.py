import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Fonts
font_large = pygame.font.SysFont("comicsans", 40)
font_small = pygame.font.SysFont("comicsans", 30)
font_medium = pygame.font.SysFont("comicsans", 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Word list
words = ["python", "speed", "typing", "keyboard", "monitor", "screen", "pygame", "function", "loop", "event"]

# Game state
input_text = ''
word = random.choice(words)
start_time = None
game_over = False
wpm = 0

def draw_screen():
    win.fill(WHITE)

    # Heading
    title = font_large.render("Typing Speed Test", True, BLACK)
    win.blit(title, (WIDTH//2 - title.get_width()//2, 30))

    # Show word
    prompt = font_medium.render("Type this:", True, BLACK)
    word_display = font_large.render(word, True, (0, 128, 0))
    win.blit(prompt, (WIDTH//2 - prompt.get_width()//2, 150))
    win.blit(word_display, (WIDTH//2 - word_display.get_width()//2, 200))

    # User input
    input_display = font_large.render(input_text, True, BLACK)
    pygame.draw.rect(win, GRAY, (WIDTH//2 - 200, 300, 400, 50), 2)
    win.blit(input_display, (WIDTH//2 - input_display.get_width()//2, 310))

    # WPM
    if game_over:
        result_text = font_large.render(f"Speed: {wpm:.2f} WPM", True, (255, 0, 0))
        win.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 400))

    pygame.display.update()

def calculate_wpm(start, end, length):
    time_taken = end - start
    wpm = (length / 5) / (time_taken / 60)
    return wpm

# Main loop
running = True
while running:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.KEYDOWN:
            if start_time is None:
                start_time = time.time()

            if event.key == pygame.K_RETURN:
                if input_text.strip() == word:
                    end_time = time.time()
                    wpm = calculate_wpm(start_time, end_time, len(word))
                    game_over = True
                else:
                    word = random.choice(words)
                    input_text = ''
                    start_time = None
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset game
                input_text = ''
                word = random.choice(words)
                start_time = None
                game_over = False
                wpm = 0

pygame.quit()
