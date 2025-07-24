import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_COLOR = (255, 0, 0)
BASKET_COLOR = (0, 100, 255)

# Basket properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

# Block properties
block_width = 30
block_height = 30
block_speed = 5
block_spawn_time = 1000  # milliseconds

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Block list
blocks = []

# Timer event for spawning blocks
SPAWN_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOCK, block_spawn_time)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_BLOCK:
            x = random.randint(0, WIDTH - block_width)
            blocks.append(pygame.Rect(x, 0, block_width, block_height))

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Update and draw blocks
    for block in blocks[:]:
        block.y += block_speed
        pygame.draw.rect(screen, BLOCK_COLOR, block)

        # Check collision with basket
        basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height)
        if block.colliderect(basket_rect):
            blocks.remove(block)
            score += 1
        elif block.y > HEIGHT:
            blocks.remove(block)

    # Draw basket
    pygame.draw.rect(screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


