import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Blocks")

# Set up colors
WHITE = (13, 27, 42)      # New background color (Dark Navy)
RED = (46, 204, 113)      # New falling block color (Emerald Green)
BLACK = (236, 240, 241)   # New player & score color (Light Gray)

# Set up player
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 3

# Set up falling blocks
block_width, block_height = 30, 30
block_speed = 3
blocks = []

# Set up the clock for FPS
clock = pygame.time.Clock()

# Set up font for text
font = pygame.font.SysFont(None, 55)

def display_message(message, color, y_offset=0):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)

def spawn_block():
    block_x = random.randint(0, WIDTH - block_width)
    block_y = random.randint(-100, -block_height)
    return [block_x, block_y]

def main():
    global player_x
    running = True
    score = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move player based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Move, draw, and check blocks
        for block in blocks[:]:
            block[1] += block_speed
            if block[1] > HEIGHT:
                blocks.remove(block)
                score += 1
            
            # Draw the block BEFORE checking for collision
            pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))
            
            # Now, check for collision
            if (block[0] < player_x + player_width and block[0] + block_width > player_x) and \
               (block[1] < player_y + player_height and block[1] + block_height > player_y):
                
                display_message("Game Over!", (255, 0, 0), -50)
                display_message(f"Score: {score}", (255, 0, 0), 50)
                pygame.display.update()
                pygame.time.wait(2000)
                return

        # Add new blocks every 30 frames
        if random.randint(1, 30) == 1:
            blocks.append(spawn_block())

        # Draw player
        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

        # Display score during gameplay
        # We need to render the score on top of the blocks, so we call it again here.
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()