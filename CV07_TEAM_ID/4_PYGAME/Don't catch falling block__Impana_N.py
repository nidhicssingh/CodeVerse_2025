import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Block")
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 24)
player_width = 120
player_height = 15
player_y = HEIGHT - 30
block_width = 50
block_height = 30
block_speed = 5
score = 0
total_blocks = 0
max_blocks = 50
def new_block():
    x = random.randint(0, WIDTH - block_width)
    return pygame.Rect(x, -block_height, block_width, block_height)

block = new_block()
running = True
game_over = False
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        mouse_x = pygame.mouse.get_pos()[0]
        player_x = mouse_x - player_width // 2
        player_x = max(0, min(WIDTH - player_width, player_x))
        player = pygame.Rect(player_x, player_y, player_width, player_height)

        block.y += block_speed

        if block.colliderect(player):
            game_over = True

        elif block.y > HEIGHT:
            score += 1
            total_blocks += 1
            block = new_block()

        pygame.draw.rect(screen, BLACK, player)
        pygame.draw.rect(screen, RED, block)

        score_text = font.render(f"Score: {score}", True, BLACK)
        blocks_text = font.render(f"Blocks Dodged: {total_blocks}/{max_blocks}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(blocks_text, (10, 40))
        if total_blocks >= max_blocks:
            game_over = True

    else:
        over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
        screen.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
        restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 20))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            score = 0
            total_blocks = 0
            block = new_block()
            game_over = False
        elif keys[pygame.K_q]:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
