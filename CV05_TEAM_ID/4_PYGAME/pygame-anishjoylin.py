import pygame
import sys
import time
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
FONT = pygame.font.SysFont("arial", 28)
BIG_FONT = pygame.font.SysFont("arial", 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Test")
clock = pygame.time.Clock()

# Sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing games improve your keyboard skills.",
    "Practice makes a person perfect in typing.",
    "Speed is important but accuracy matters more.",
    "Python is a versatile programming language."
]

def draw_text(surface, text, pos, font, color=BLACK):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, pos)

def get_wpm(start_time, input_text):
    elapsed = max(time.time() - start_time, 1)
    words = len(input_text.split())
    wpm = (words / elapsed) * 60
    return round(wpm)

def main():
    input_text = ''
    target_text = random.choice(sentences)
    result = ''
    start_time = 0
    active = False
    finished = False
    wpm = 0

    while True:
        screen.fill(WHITE)

        draw_text(screen, "Typing Speed Test", (WIDTH//2 - 150, 20), BIG_FONT)
        draw_text(screen, "Type the sentence below:", (50, 80), FONT)
        draw_text(screen, target_text, (50, 120), FONT, GRAY)

        pygame.draw.rect(screen, GRAY, (48, 200, 700, 40), 2)
        draw_text(screen, input_text, (50, 210), FONT)

        # Show WPM live
        if active and not finished:
            wpm = get_wpm(start_time, input_text)
            draw_text(screen, f"Speed: {wpm} WPM", (50, 270), FONT, GREEN)

        if finished:
            draw_text(screen, result, (50, 320), FONT, RED)
            draw_text(screen, "Press Enter to restart", (50, 360), FONT, GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if not active and not finished:
                    start_time = time.time()
                    active = True

                if event.key == pygame.K_RETURN:
                    if finished:
                        # Reset
                        input_text = ''
                        target_text = random.choice(sentences)
                        result = ''
                        active = False
                        finished = False
                        wpm = 0
                    else:
                        if input_text.strip() == target_text.strip():
                            result = f"✅ Correct! Final Speed: {wpm} WPM"
                        else:
                            result = f"❌ Incorrect text. Final Speed: {wpm} WPM"
                        finished = True
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif not finished:
                    input_text += event.unicode

        pygame.display.update()
        clock.tick(60)

main()

