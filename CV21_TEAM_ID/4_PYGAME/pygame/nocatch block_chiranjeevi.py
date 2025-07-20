import pygame
import random

# Initialize
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Block 🟥")

# Colors
BG_COLOR = (240, 240, 240)
PADDLE_COLOR = (30, 30, 120)
BLOCK_COLOR = (200, 0, 0)
TEXT_COLOR = (0, 0, 0)

# Paddle settings
paddle_width = 100
paddle_height = 15
paddle_y = HEIGHT - 40

# Block settings
block_width = 30
block_height = 30
block_x = random.randint(0, WIDTH - block_width)
block_y = 0
block_speed = 5

# Font and clock
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

# Score
score = 0
game_over = False

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouse movement for paddle
    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = mouse_x - paddle_width // 2
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # Draw paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Move and draw block
    if not game_over:
        block_y += block_speed
        pygame.draw.rect(screen, BLOCK_COLOR, (block_x, block_y, block_width, block_height))

        # Collision detection (DON'T touch the block!)
        if (
            paddle_y < block_y + block_height < paddle_y + paddle_height and
            paddle_x < block_x + block_width and
            paddle_x + paddle_width > block_x
        ):
            game_over = True

        # Block goes off screen → reset position
        if block_y > HEIGHT:
            block_x = random.randint(0, WIDTH - block_width)
            block_y = -block_height
            score += 1  # survive = score

    # Score display
    score_text = font.render(f"Score (Survived): {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))

    # Game Over screen
    if game_over:
        over_text = font.render("Game Over! You caught the block!", True, BLOCK_COLOR)
        end_text = font.render("Press ESC to exit.", True, TEXT_COLOR)
        screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        screen.blit(end_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
