import pygame
import random
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

clock = pygame.time.Clock()

player = pygame.Rect(WIDTH // 2, HEIGHT - 30, 80, 10)
block = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
speed = 5
score = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, block)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    block.y += speed
    if block.y > HEIGHT:
        block.y = 0
        block.x = random.randint(0, WIDTH - 20)

    if player.colliderect(block):
        score += 1
        block.y = 0
        block.x = random.randint(0, WIDTH - 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 7
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += 7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
