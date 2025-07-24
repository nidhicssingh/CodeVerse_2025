import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
PURPLE = (138, 43, 226)

# Player
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Block
block_size = 30
block_x = random.randint(0, WIDTH - block_size)
block_y = -block_size
block_speed = 5

# Font and score
font = pygame.font.SysFont(None, 48)
score = 0
missed = 0
max_missed = 5

# Clock
clock = pygame.time.Clock()

def draw_text(text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move block
    block_y += block_speed

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, GREEN, player_rect)

    # Draw block
    block_rect = pygame.Rect(block_x, block_y, block_size, block_size)
    pygame.draw.rect(screen, PURPLE, block_rect)

    # Collision check
    if player_rect.colliderect(block_rect):
        score += 1
        block_speed += 0.3  # Increase difficulty
        block_x = random.randint(0, WIDTH - block_size)
        block_y = -block_size

    # Missed block
    elif block_y > HEIGHT:
        missed += 1
        block_x = random.randint(0, WIDTH - block_size)
        block_y = -block_size

    # Scoreboard
    draw_text(f"Score: {score}", 36, 10, 10, BLACK)
    draw_text(f"Missed: {missed}/{max_missed}", 36, 10, 50, BLACK)

    # Game over condition
    if missed >= max_missed:
        draw_text("Game Over!", 64, WIDTH // 2 - 150, HEIGHT // 2 - 30, (200, 0, 0))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
