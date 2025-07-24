import pygame
pygame.init()

WIDTH = 540
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid():
    block_size = WIDTH // 9
    for i in range(10):
        line_width = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * block_size), (WIDTH, i * block_size), line_width)
        pygame.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, HEIGHT), line_width)

def draw_numbers():
    font = pygame.font.Font(None, 40)
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                num = font.render(str(grid[row][col]), True, BLACK)
                screen.blit(num, (col * 60 + 20, row * 60 + 15))

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
