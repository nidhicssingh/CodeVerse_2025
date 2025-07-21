import pygame
import random
import time

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Test")
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()

# Word list
words = ["python", "development", "keyboard", "typing", "function", "loop", "game", "speed", "input", "output"]
current_word = random.choice(words)
typed_text = ''
start_time = None
game_over = False

def render_text(text, x, y, color=(255, 255, 255)):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def calculate_wpm(start, end, total_chars):
    minutes = (end - start) / 60
    words_typed = total_chars / 5
    return round(words_typed / minutes)

# Game loop
while not game_over:
    screen.fill((30, 30, 30))
    render_text("Type the word:", 50, 50)
    render_text(current_word, 50, 100, (0, 255, 0))
    render_text(typed_text, 50, 200, (255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if start_time is None:
                start_time = time.time()

            if event.key == pygame.K_RETURN:
                if typed_text.lower() == current_word.lower():
                    end_time = time.time()
                    total_time = end_time - start_time
                    wpm = calculate_wpm(start_time, end_time, len(typed_text))
                    render_text(f"Correct! Your WPM: {wpm}", 50, 300, (0, 255, 255))
                    pygame.display.update()
                    time.sleep(2)
                typed_text = ''
                current_word = random.choice(words)
                start_time = None
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            else:
                typed_text += event.unicode

    pygame.display.update()
    clock.tick(60)

pygame.quit()