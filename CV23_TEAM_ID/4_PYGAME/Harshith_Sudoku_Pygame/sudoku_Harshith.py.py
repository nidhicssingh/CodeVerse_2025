import pygame
import sys
import time

pygame.init()

# Initial Constants
GRID_SIZE = 9
MARGIN = 20
BOTTOM_SPACE = 60  # For messages
TOP_SPACE = 40     # For timer and score
WIDTH, HEIGHT = 600, 600 + BOTTOM_SPACE + TOP_SPACE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (220, 220, 220)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts (dynamic later)
BASE_FONT_SIZE = 40
SMALL_FONT_SIZE = 20

# Sudoku Puzzle (0 = empty)
puzzle = [
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
original = [[puzzle[r][c] != 0 for c in range(9)] for r in range(9)]
selected = None

# Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sudoku - Easy Level (Resizable with Timer & Score)")

# Start timer
start_time = time.time()
score = 0

def get_dynamic_sizes():
    win_w, win_h = screen.get_size()
    grid_area = min(win_w - 2*MARGIN, win_h - TOP_SPACE - BOTTOM_SPACE - 2*MARGIN)
    cell_size = grid_area // GRID_SIZE
    grid_size = cell_size * GRID_SIZE
    top_left_x = (win_w - grid_size) // 2
    top_left_y = TOP_SPACE + (win_h - TOP_SPACE - BOTTOM_SPACE - grid_size) // 2
    font = pygame.font.SysFont("comicsans", cell_size // 2)
    small_font = pygame.font.SysFont("comicsans", 18)
    return cell_size, top_left_x, top_left_y, font, small_font

def draw_grid(cell_size, top_left_x, top_left_y):
    for i in range(GRID_SIZE + 1):
        width = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, 
                         (top_left_x, top_left_y + i * cell_size), 
                         (top_left_x + GRID_SIZE * cell_size, top_left_y + i * cell_size), width)
        pygame.draw.line(screen, BLACK, 
                         (top_left_x + i * cell_size, top_left_y), 
                         (top_left_x + i * cell_size, top_left_y + GRID_SIZE * cell_size), width)

def draw_numbers(cell_size, top_left_x, top_left_y, font):
    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]
            if val != 0:
                text = font.render(str(val), True, BLACK if original[r][c] else BLUE)
                x = top_left_x + c * cell_size + cell_size // 3
                y = top_left_y + r * cell_size + cell_size // 4
                screen.blit(text, (x, y))

def highlight_cell(row, col, cell_size, top_left_x, top_left_y):
    if row is not None and col is not None:
        pygame.draw.rect(screen, GREY, (
            top_left_x + col * cell_size,
            top_left_y + row * cell_size,
            cell_size,
            cell_size
        ))

def is_valid(num, row, col):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[box_row + i][box_col + j] == num:
                return False
    return True

def display_message(message, small_font):
    text = small_font.render(message, True, RED)
    screen.blit(text, (20, screen.get_height() - 35))

def display_timer_and_score(small_font, score, elapsed_time):
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    time_text = small_font.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
    score_text = small_font.render(f"Score: {score}", True, BLACK)
    screen.blit(time_text, (20, 10))
    screen.blit(score_text, (screen.get_width() - 120, 10))

def main():
    global selected, score
    clock = pygame.time.Clock()
    message = ""
    running = True

    while running:
        screen.fill(WHITE)
        cell_size, top_left_x, top_left_y, font, small_font = get_dynamic_sizes()

        # Display timer & score
        elapsed_time = time.time() - start_time
        display_timer_and_score(small_font, score, elapsed_time)

        if selected:
            highlight_cell(*selected, cell_size, top_left_x, top_left_y)

        draw_numbers(cell_size, top_left_x, top_left_y, font)
        draw_grid(cell_size, top_left_x, top_left_y)
        display_message(message, small_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(event.size, pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x = (x - top_left_x) // cell_size
                grid_y = (y - top_left_y) // cell_size
                if 0 <= grid_x < 9 and 0 <= grid_y < 9:
                    selected = (grid_y, grid_x)

            elif event.type == pygame.KEYDOWN and selected:
                row, col = selected
                if not original[row][col]:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        val = event.key - pygame.K_0
                        if is_valid(val, row, col):
                            puzzle[row][col] = val
                            score += 10
                            message = ""
                        else:
                            message = f"{val} is not valid here!"
                    elif event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
                        puzzle[row][col] = 0
                        message = ""

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



