import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Clicker")

font = pygame.font.SysFont(None, 36)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

score = 0
lives = 3
radius = 30
circle_x = random.randint(radius, WIDTH - radius)
circle_y = random.randint(radius, HEIGHT - radius)
circle_timer = 60  

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    circle_timer -= 1

    pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dist = ((mouse_x - circle_x)*2 + (mouse_y - circle_y)*2) ** 0.5
            if dist <= radius:
                score += 1
                circle_x = random.randint(radius, WIDTH - radius)
                circle_y = random.randint(radius, HEIGHT - radius)
                circle_timer = max(20, 60 - score * 2) 

    if circle_timer <= 0:
        lives -= 1
        circle_x = random.randint(radius, WIDTH - radius)
        circle_y = random.randint(radius, HEIGHT - radius)
        circle_timer = max(20, 60 - score * 2)

    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, (0, 0, 0)), (10, 40))

    if lives <= 0:
        screen.blit(font.render("Game Over!", True, RED), (180, 220))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)