import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 500
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Blocks - Catch the Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Fonts
font = pygame.font.SysFont("comicsans", 32)
game_over_font = pygame.font.SysFont("comicsans", 48)

# Clock
clock = pygame.time.Clock()

# Player (bucket)
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_vel = 7

# Block (falling)
block_width = 30
block_height = 30
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_vel = 5

# Game variables
score = 0
lives = 3
run = True

def draw_game():
    win.fill(WHITE)
    # Draw player
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_width, player_height))
    # Draw block
    pygame.draw.rect(win, RED, (block_x, block_y, block_width, block_height))
    # Draw score and lives
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    win.blit(score_text, (10, 10))
    win.blit(lives_text, (WIDTH - 120, 10))
    pygame.display.update()

def game_over_screen():
    win.fill(WHITE)
    over_text = game_over_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    win.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 60))
    win.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Game loop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_vel

    # Move block
    block_y += block_vel

    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)

    if player_rect.colliderect(block_rect):
        score += 1
        block_x = random.randint(0, WIDTH - block_width)
        block_y = -block_height
        block_vel += 0.2  # speed up gradually

    # Missed the block
    if block_y > HEIGHT:
        lives -= 1
        block_x = random.randint(0, WIDTH - block_width)
        block_y = -block_height

    # Game over condition
    if lives <= 0:
        game_over_screen()

    draw_game()

pygame.quit()

 