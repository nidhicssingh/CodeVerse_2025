import pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("comicsans", 40)

# Sample grid (0 = empty)
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Draw grid
def draw_grid():
    block_size = WIDTH // 9
    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * block_size), (WIDTH, i * block_size), thickness)
        pygame.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, WIDTH), thickness)

# Draw numbers
def draw_numbers():
    block_size = WIDTH // 9
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(text, (j * block_size + 15, i * block_size + 10))

# Main loop
run = True
while run:
    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
