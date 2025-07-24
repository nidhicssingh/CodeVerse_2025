import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Emoji Face")

# Colors
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw face (circle)
    pygame.draw.circle(screen, YELLOW, (200, 200), 100)

    # Draw eyes (two black circles)
    pygame.draw.circle(screen, BLACK, (170, 170), 10)
    pygame.draw.circle(screen, BLACK, (230, 170), 10)

    # Draw smiling mouth (arc)
    pygame.draw.arc(screen, BLACK, (150, 180, 100, 60), 3.14, 0, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
