import pygame
import random
import time
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (220, 220, 220)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 40)

# Sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect.",
    "Typing games improve speed and accuracy.",
    "Python is a versatile language.",
    "Never give up on learning."
]

# Select random sentence
target_text = random.choice(sentences)
user_text = ""
start_time = None
active = True
result = None

def draw_text(text, pos, color=BLACK, fnt=font):
    txt_surface = fnt.render(text, True, color)
    screen.blit(txt_surface, pos)

def calculate_results():
    global result
    total_time = time.time() - start_time
    total_time = max(total_time, 0.1)  # avoid zero division
    num_words = len(user_text.split())
    wpm = round((num_words / total_time) * 60)
    correct = sum(1 for i, c in enumerate(user_text) if i < len(target_text) and c == target_text[i])
    accuracy = round((correct / len(target_text)) * 100)
    result = (wpm, accuracy, total_time)

def reset_game():
    global user_text, target_text, start_time, result, active
    user_text = ""
    target_text = random.choice(sentences)
    start_time = None
    result = None
    active = True

def main():
    global user_text, start_time, active

    clock = pygame.time.Clock()
    input_box = pygame.Rect(50, 250, 600, 50)

    while True:
        screen.fill(WHITE)
        pygame.draw.rect(screen, LIGHT_GRAY, input_box, 0)
        pygame.draw.rect(screen, BLACK, input_box, 2)

        draw_text("Type the sentence:", (50, 50), BLACK, big_font)
        draw_text(target_text, (50, 100), BLACK, font)
        draw_text(user_text, (input_box.x + 5, input_box.y + 10), BLACK)

        if result:
            wpm, accuracy, total_time = result
            draw_text(f"WPM: {wpm}", (50, 350), GREEN)
            draw_text(f"Accuracy: {accuracy}%", (250, 350), GREEN)
            draw_text(f"Time: {round(total_time, 2)}s", (500, 350), GREEN)
            draw_text("Press R to retry", (50, 400), RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if active:
                if event.type == pygame.KEYDOWN:
                    if start_time is None:
                        start_time = time.time()

                    if event.key == pygame.K_RETURN:
                        calculate_results()
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    reset_game()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
