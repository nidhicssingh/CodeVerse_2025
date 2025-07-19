import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_COLOR = (255, 0, 0)
BONUS_COLOR = (0, 255, 0)
HARMFUL_COLOR = (0, 0, 0)
TIME_COLOR = (0, 255, 255)
BASKET_COLOR = (0, 0, 255)
# FLASH_COLOR removed
ENEMY_COLOR = (255, 165, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Blocks - Catch the Blocks Game")

# Basket settings
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10

# Enemy settings
enemy_width = 100
enemy_x = 0
enemy_y = basket_y - 100
enemy_direction = 1

# Block settings
block_size = 30
max_blocks = 100
block_speed = 2
next_block_timer = 0
block_delay = 50
blocks = []

# Score, lives, font, level, timer
score = 0
lives = 5
level = 1
timer = 60  # seconds
start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 36)

# Scoreboard file
high_score_file = "high_score.txt"
if not os.path.exists(high_score_file):
    with open(high_score_file, "w") as f:
        f.write("0")
with open(high_score_file, "r") as f:
    high_score = int(f.read())

# Clock
clock = pygame.time.Clock()

# Function to display text
def draw_text(text, x, y, color=BLACK, size=36):
    font_obj = pygame.font.SysFont(None, size)
    screen.blit(font_obj.render(text, True, color), (x, y))

# Welcome screen
def show_welcome():
    screen.fill(WHITE)
    draw_text("Welcome to Falling Blocks Game!", 100, 100)
    draw_text("Instructions:", 100, 160)
    draw_text("Catch RED blocks to score.", 100, 200, size=24)
    draw_text("Catch GREEN for bonus, avoid BLACK blocks!", 100, 230, size=24)
    draw_text("Catch CYAN to extend time! Avoid the enemy!", 100, 260, size=24)
    draw_text("Move your mouse to control the catcher.", 100, 290, size=24)
    
    draw_text("Press any key to START.", 100, 350, size=28)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

show_welcome()

# Game loop
running = True
flash_timer = 0
flash_location = None

while running:
    screen.fill(WHITE)
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = max(timer - seconds_passed, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            basket_x = mouse_x - basket_width // 2

    # Keep basket inside screen
    basket_x = max(0, min(WIDTH - basket_width, basket_x))

    # Move enemy
    enemy_x += enemy_direction * 5
    if enemy_x <= 0 or enemy_x + enemy_width >= WIDTH:
        enemy_direction *= -1

    if (enemy_y < basket_y + basket_height and
        enemy_y + basket_height > basket_y and
        enemy_x < basket_x + basket_width and
        enemy_x + enemy_width > basket_x):
        lives -= 1
        enemy_x = 0

    if score > 0 and score % 10 == 0:
        level = score // 10 + 1
        block_speed = 2 + level

    next_block_timer += 1
    if len(blocks) < max_blocks and next_block_timer >= block_delay:
        kind = random.choices(["normal", "bonus", "harmful", "time"], weights=[70, 10, 10, 10])[0]
        blocks.append({"x": random.randint(0, WIDTH - block_size), "y": 0, "type": kind})
        next_block_timer = 0

    for block in blocks[:]:
        block["y"] += block_speed

        if block["y"] > HEIGHT:
            if block["type"] == "normal":
                lives -= 1
                flash_timer = 10
                flash_location = (block["x"], HEIGHT - 50)
            blocks.remove(block)
            continue

        if (basket_y < block["y"] + block_size and
            basket_y + basket_height > block["y"] and
            basket_x < block["x"] + block_size and
            basket_x + basket_width > block["x"]):

            if block["type"] == "normal":
                score += 1
            elif block["type"] == "bonus":
                score += 3
            elif block["type"] == "harmful":
                lives -= 2
            elif block["type"] == "time":
                timer += 5

            flash_timer = 10
            flash_location = (block["x"], block["y"])
            blocks.remove(block)
            continue

        if block["type"] == "bonus":
            color = BONUS_COLOR
            pygame.draw.circle(screen, color, (block["x"] + block_size // 2, block["y"] + block_size // 2), block_size // 2)
        elif block["type"] == "harmful":
            color = HARMFUL_COLOR
            pygame.draw.polygon(screen, color, [
                (block["x"], block["y"]),
                (block["x"] + block_size, block["y"]),
                (block["x"] + block_size // 2, block["y"] + block_size)
            ])
        elif block["type"] == "time":
            pygame.draw.ellipse(screen, TIME_COLOR, (block["x"], block["y"], block_size, block_size // 1.5))
        else:
            pygame.draw.rect(screen, BLOCK_COLOR, (block["x"], block["y"], block_size, block_size))



    pygame.draw.rect(screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.rect(screen, ENEMY_COLOR, (enemy_x, enemy_y, enemy_width, basket_height))

    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Lives: {lives}", 10, 50)
    draw_text(f"High Score: {high_score}", 400, 10)
    draw_text(f"Level: {level}", 400, 50)
    draw_text(f"Time: {remaining_time}", 250, 10)

    if lives <= 0 or remaining_time == 0:
        if score > high_score:
            with open(high_score_file, "w") as f:
                f.write(str(score))
            high_score = score

        screen.fill(WHITE)
        draw_text("GAME OVER", WIDTH//2 - 80, HEIGHT//2 - 60, (255, 0, 0))
        draw_text(f"Final Score: {score}", WIDTH//2 - 100, HEIGHT//2 - 20)
        draw_text("Press R to Restart or Q to Quit", WIDTH//2 - 150, HEIGHT//2 + 30, size=28)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        basket_x = WIDTH // 2 - basket_width // 2
                        enemy_x = 0
                        score = 0
                        lives = 5
                        level = 1
                        blocks = []
                        timer = 60
                        start_ticks = pygame.time.get_ticks()
                        waiting = False
                    elif event.key == pygame.K_q:
                        waiting = False
                        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
