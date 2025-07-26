# Super Short Typing Game - Under 65 Lines!
import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Typing Game!")

DARK_GRAY = (40, 40, 40)
PALE_WHITE = (220, 220, 220)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
YELLOW = (255, 255, 100)

big_text = pygame.font.Font(None, 50)
normal_text = pygame.font.Font(None, 35)

sentences = ["Code matrix is group 6", "Hello everyone welcome to my channel", "S-Vyasa Deemed To Be University", "I just want to feel safe and have fun.", "This could be so fun!"]

current_sentence = random.choice(sentences)
typed = ""
start_time = 0
timer = 30

def get_time_left():
    if start_time == 0: return timer
    return max(0, timer - (pygame.time.get_ticks() - start_time) // 1000)

def reset_game():
    global current_sentence, typed, start_time
    current_sentence = random.choice(sentences)
    typed = ""
    start_time = 0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            time_left = get_time_left()
            
            if time_left > 0 and typed != current_sentence:
                if event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                elif event.unicode and len(event.unicode) == 1 and len(typed) < len(current_sentence):
                    if start_time == 0: start_time = pygame.time.get_ticks()
                    typed += event.unicode
            elif event.key == pygame.K_SPACE and (typed == current_sentence or time_left == 0):
                reset_game()
    
    screen.fill(DARK_GRAY)
    screen.blit(big_text.render("Type This Sentence!", True, PALE_WHITE), (200, 50))
    screen.blit(normal_text.render(f"Time: {get_time_left()} seconds", True, YELLOW), (50, 100))
    
    if start_time == 0:
        screen.blit(normal_text.render("Press any letter to start!", True, PALE_WHITE), (220, 150))
    
    x, y = 50, 200
    for i, letter in enumerate(current_sentence):
        color = GREEN if i < len(typed) and typed[i] == letter else RED if i < len(typed) else PALE_WHITE
        screen.blit(normal_text.render(letter, True, color), (x, y))
        x += 20
        if x > 750: x, y = 50, y + 40
    
    screen.blit(normal_text.render("You typed: " + typed, True, PALE_WHITE), (50, 350))
    screen.blit(normal_text.render(f"{len(typed)}/{len(current_sentence)} letters", True, PALE_WHITE), (50, 400))
    
    if typed == current_sentence:
        screen.blit(big_text.render("YOU DID IT!", True, GREEN), (250, 450))
        screen.blit(normal_text.render("Press SPACE for new sentence!", True, PALE_WHITE), (200, 500))
    elif get_time_left() == 0:
        screen.blit(big_text.render("Time's Up!", True, RED), (280, 450))
        screen.blit(normal_text.render("Press SPACE to try again!", True, PALE_WHITE), (220, 500))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()