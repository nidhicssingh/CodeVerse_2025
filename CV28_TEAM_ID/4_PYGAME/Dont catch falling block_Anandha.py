import pygame
import random
import sys
import os

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Block")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images (optional)
def load_image(file_name, fallback_color, size):
    if os.path.exists(file_name):
        img = pygame.image.load(file_name)
        return pygame.transform.scale(img, size)
    else:
        return None

background_img = load_image("background.jpg", WHITE, (WIDTH, HEIGHT))
player_img = load_image("player.png", None, (60, 60))
block_img = load_image("block.png", None, (50, 50))

# Player
player_size = 60
player_pos = [WIDTH // 2, HEIGHT - 80]
player_speed = 10

# Blocks
block_size = 50
block_speed = 5
num_blocks = 4
blocks = [[random.randint(0, WIDTH - block_size), random.randint(-600, -50)] for _ in range(num_blocks)]

# Score
score = 0
font = pygame.font.SysFont("Comic Sans MS", 30)

def draw_player():
    if player_img:
        screen.blit(player_img, player_pos)
    else:
        pygame.draw.rect(screen, (0, 128, 255), (*player_pos, player_size, player_size), border_radius=10)

def draw_blocks():
    for bx, by in blocks:
        if block_img:
            screen.blit(block_img, (bx, by))
        else:
            pygame.draw.rect(screen, (255, 50, 50), (bx, by, block_size, block_size), border_radius=8)

def update_blocks():
    global score
    for i in range(len(blocks)):
        blocks[i][1] += block_speed
        if blocks[i][1] > HEIGHT:
            blocks[i] = [random.randint(0, WIDTH - block_size), random.randint(-200, -50)]
            score += 1

def check_collision():
    player_rect = pygame.Rect(*player_pos, player_size, player_size)
    for bx, by in blocks:
        block_rect = pygame.Rect(bx, by, block_size, block_size)
        if player_rect.colliderect(block_rect):
            return True
    return False

def show_game_over():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))
    pygame.display.update()
    pygame.time.wait(3000)

# Game Loop
running = True
while running:
    screen.blit(background_img, (0, 0)) if background_img else screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    draw_player()
    draw_blocks()
    update_blocks()

    # Score display
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if check_collision():
        show_game_over()
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
