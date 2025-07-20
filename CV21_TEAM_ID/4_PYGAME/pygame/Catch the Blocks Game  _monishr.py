import pygame
import random

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Ball - Mouse Control 🎮")

# Colors (Improved Contrast)
BG_COLOR = (240, 240, 240)       # Light gray background
PADDLE_COLOR = (20, 30, 120)     # Dark blue paddle
BALL_COLOR = (255, 140, 0)       # Bright orange ball
TEXT_COLOR = (0, 0, 0)           # Black text

# Font
font = pygame.font.SysFont("Arial", 24)

# Paddle
paddle_width = 100
paddle_height = 15
paddle_y = HEIGHT - 40

# Ball
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score and tracking
score = 0
missed = 0
total_balls = 50
balls_dropped = 0

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse x-position
    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = mouse_x - paddle_width // 2

    # Keep paddle within screen
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # Draw paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Ball logic
    if balls_dropped < total_balls:
        ball_y += ball_speed

        # Catch check
        if paddle_y < ball_y + ball_radius < paddle_y + paddle_height:
            if paddle_x < ball_x < paddle_x + paddle_width:
                score += 1
                balls_dropped += 1
                ball_x = random.randint(ball_radius, WIDTH - ball_radius)
                ball_y = 0

        # Missed check
        elif ball_y > HEIGHT:
            missed += 1
            balls_dropped += 1
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)
            ball_y = 0

        # Draw ball
        pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)

    # Score display
    score_text = font.render(f"Caught: {score}   Missed: {missed}   Total: {balls_dropped}/{total_balls}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))

    # Game Over
    if balls_dropped >= total_balls:
        result = font.render(f"Game Over! You caught {score} balls.", True, TEXT_COLOR)
        screen.blit(result, (WIDTH // 2 - 180, HEIGHT // 2))
        end_msg = font.render("Press ESC to exit.", True, TEXT_COLOR)
        screen.blit(end_msg, (WIDTH // 2 - 100, HEIGHT // 2 + 30))

        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        continue

    pygame.display.update()
    clock.tick(60)

pygame.quit()
