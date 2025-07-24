import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 24)

# Paddle
paddle_width = 100
paddle_height = 15
paddle_y = HEIGHT - 30

# Block
block_width = 30
block_height = 30
block_speed = 5

# Game variables
score = 0
total_blocks = 0
max_blocks = 100

# Generate first block
def new_block():
    x = random.randint(0, WIDTH - block_width)
    return pygame.Rect(x, -block_height, block_width, block_height)

block = new_block()

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    mouse_x = pygame.mouse.get_pos()[0]
    paddle_x = mouse_x - paddle_width // 2
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    # Move block
    block.y += block_speed

    # Check for collision
    if block.colliderect(paddle):
        score += 1
        total_blocks += 1
        block = new_block()

    # Block missed
    elif block.y > HEIGHT:
        total_blocks += 1
        block = new_block()

    # Draw paddle and block
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.rect(screen, RED, block)

    # Draw score and progress
    score_text = font.render(f"Score: {score}", True, BLACK)
    blocks_left_text = font.render(f"Blocks: {total_blocks}/{max_blocks}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(blocks_left_text, (10, 40))

    # End condition
    if total_blocks >= max_blocks:
        end_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
        screen.blit(end_text, (WIDTH // 2 - 120, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
