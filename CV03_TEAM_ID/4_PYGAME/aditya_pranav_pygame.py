import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)


font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)


choices = ["Rock", "Paper", "Scissors"]


class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        txt = small_font.render(self.text, True, BLACK)
        surface.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
buttons = [
    Button("Rock", 60, 300, 100, 50),
    Button("Paper", 200, 300, 100, 50),
    Button("Scissors", 340, 300, 100, 50)
]

def get_winner(player, computer):
    if player == computer:
        return "Draw!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

player_choice = None
computer_choice = None
result = ""

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw title
    title = font.render("Rock Paper Scissors", True, BLUE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Draw buttons
    for btn in buttons:
        btn.draw(screen)

    # Show choices and result
    if player_choice:
        player_txt = small_font.render(f"You: {player_choice}", True, BLACK)
        comp_txt = small_font.render(f"Computer: {computer_choice}", True, BLACK)
        result_txt = font.render(result, True, BLUE)
        screen.blit(player_txt, (60, 200))
        screen.blit(comp_txt, (60, 230))
        screen.blit(result_txt, (WIDTH // 2 - result_txt.get_width() // 2, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i, btn in enumerate(buttons):
                if btn.is_clicked(pos):
                    player_choice = choices[i]
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)
    pygame.display.flip()

pygame.quit()
sys.exit()