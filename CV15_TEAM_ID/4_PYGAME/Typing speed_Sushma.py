import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

sentences = [
    "Pygame makes Python gaming fun.",
    "Speed and precision unlock high scores.",
    "Type like lightning, code like thunder!",
    "Artificial intelligence is fascinating.",
]

target = random.choice(sentences)
user_text = ""
start_time = None
game_active = False

def draw_text(surface, text, position, color=(255, 255, 255)):
    txt = font.render(text, True, color)
    surface.blit(txt, position)

def calculate_speed(start, end, text):
    elapsed = end - start
    words = len(text.split())
    wpm = round((words / elapsed) * 60, 2)
    return wpm

running = True
while running:
    win.fill((30, 30, 30))
    draw_text(win, "Type this:", (50, 50))
    draw_text(win, target, (50, 100))
    draw_text(win, user_text, (50, 150), color=(0, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_active:
                start_time = time.time()
                game_active = True
            if event.key == pygame.K_RETURN:
                end_time = time.time()
                wpm = calculate_speed(start_time, end_time, target)
                accuracy = round((sum(1 for a, b in zip(user_text, target) if a == b) / len(target)) * 100, 2)
                user_text = f"Speed: {wpm} WPM | Accuracy: {accuracy}%"
                game_active = False
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.update()
    clock.tick(60)

pygame.quit()
