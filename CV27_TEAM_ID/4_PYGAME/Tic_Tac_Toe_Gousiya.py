import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_board():
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 100), (300, i * 100), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * 100, 0), (i * 100, 300), LINE_WIDTH)

    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                font = pygame.font.Font(None, 72)
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * 100 + 30, row * 100 + 20))

def check_winner():
    for row in board:
        if row.count(row[0]) == 3 and row[0] != "":
            return row[0]

    for col in range(3):
        if all(board[row][col] == board[0][col] != "" for row in range(3)):
            return board[0][col]

    if all(board[i][i] == board[0][0] != "" for i in range(3)):
        return board[0][0]
    if all(board[i][2 - i] == board[0][2] != "" for i in range(3)):
        return board[0][2]

    return None

def is_draw():
    return all(all(cell != "" for cell in row) for row in board)

while True:
    draw_board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            if board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    game_over = True
                elif is_draw():
                    print("Draw!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
