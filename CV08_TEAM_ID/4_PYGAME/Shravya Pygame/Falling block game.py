import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Squares")

# Load background image
background_image = pygame.image.load('bg.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Colors
BLUE = "#c1d3fe"
RED = "#adc178"
BLACK = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 24)

# Paddle
paddle_width = 200
paddle_height = 15
paddle_y = HEIGHT - 30

# Square
square_size = 30
square_speed = 5

# Game variables
score = 0
total_squares = 0
max_squares = 100

# Generate first square
def new_square():
    x = random.randint(0, WIDTH - square_size)
    return pygame.Rect(x, -square_size, square_size, square_size)

square = new_square()

# Main loop
running = True
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    mouse_x = pygame.mouse.get_pos()[0]
    paddle_x = mouse_x - paddle_width // 2
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    # Move square
    square.y += square_speed

    # Check for collision
    if square.colliderect(paddle):
        score += 1
        total_squares += 1
        square = new_square()
    # Square missed
    elif square.y > HEIGHT:
        total_squares += 1
        square = new_square()

    # Draw paddle and square
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.rect(screen, RED, square)

    # Draw score and progress
    score_text = font.render(f"Score: {score}", True, BLACK)
    squares_left_text = font.render(f"Squares: {total_squares}/{max_squares}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(squares_left_text, (10, 40))

    # End condition
    if total_squares >= max_squares:
        end_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
        screen.blit(end_text, (WIDTH // 2 - 120, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()