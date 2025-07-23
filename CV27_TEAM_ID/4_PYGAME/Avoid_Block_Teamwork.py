import pygame
import random
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Block")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 0)

clock = pygame.time.Clock()

player = pygame.Rect(WIDTH // 2, HEIGHT - 30, 80, 10)
block = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
speed = 5
score = 0
game_over = False

font = pygame.font.Font(None, 36)

while not game_over:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, ORANGE, block)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    block.y += speed
    if block.y > HEIGHT:
        block.y = 0
        block.x = random.randint(0, WIDTH - 20)
        score += 1

    if player.colliderect(block):
        game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 7
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += 7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
