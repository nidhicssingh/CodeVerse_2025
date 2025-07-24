import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")

font_small = pygame.font.Font(None, 36)
font_big = pygame.font.Font(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

word_list = ["pygame", "random"]

current_word = random.choice(word_list)
user_input = ""
score = 0
start_time = time.time()
time_limit = 60  

running = True
while running:
    screen.fill(WHITE)
    elapsed_time = time.time() - start_time
    time_left = max(0, int(time_limit - elapsed_time))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if time_left > 0 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.lower() == current_word.lower():
                    score += 1
                current_word = random.choice(word_list)
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    word_surface = font_big.render(current_word, True, BLACK)
    screen.blit(word_surface, (WIDTH//2 - word_surface.get_width()//2, HEIGHT//3))

    input_surface = font_small.render("Your Input: " + user_input, True, BLACK)
    screen.blit(input_surface, (WIDTH//2 - input_surface.get_width()//2, HEIGHT//2))

    score_surface = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (10, 10))

    timer_surface = font_small.render(f"Time Left: {time_left}s", True, BLACK)
    screen.blit(timer_surface, (WIDTH - 180, 10))

    if time_left == 0:
        end_surface = font_big.render(f"Time's up! Final Score: {score}", True, BLACK)
        screen.blit(end_surface, (WIDTH//2 - end_surface.get_width()//2, HEIGHT//1.5))

    pygame.display.flip()

pygame.quit()
