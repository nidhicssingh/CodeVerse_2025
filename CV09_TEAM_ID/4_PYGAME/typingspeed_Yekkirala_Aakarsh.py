import pygame
import sys
import random
import time
import threading
import requests

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TypeItRite")

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (220, 220, 220)
BLUE = (100, 149, 237)
GREEN = (34, 177, 76)
RED = (200, 50, 50)
DARK_GRAY = (80, 80, 80)

# Fonts
FONT_LARGE = pygame.font.SysFont("consolas", 44)
FONT_MEDIUM = pygame.font.SysFont("consolas", 28)
FONT_SMALL = pygame.font.SysFont("consolas", 22)
FONT_TITLE = pygame.font.SysFont("consolas", 48, bold=True)

# Timer options (seconds)
TIMER_OPTIONS = [
    ("10s", 10),
    ("30s", 30),
    ("60s", 60),
    ("5m", 300),
    ("10m", 600)
]

def fetch_words_api(n=100):
    try:
        resp = requests.get(f"https://random-word-api.herokuapp.com/word?number={n}")
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    # fallback
    fallback = [
        "python", "developer", "keyboard", "function", "variable", "pygame", "speed",
        "challenge", "algorithm", "syntax", "object", "inheritance", "loop", "string",
        "integer", "boolean", "exception", "module", "package", "import", "random",
        "display", "window", "mouse", "event", "timer", "score", "correct", "wrong",
        "minute", "second", "letter", "space", "backspace", "return", "screen", "font",
        "color", "draw", "rect", "center", "caption", "input", "output", "logic", "test"
    ]
    return random.sample(fallback, min(n, len(fallback)))

def draw_text(surface, text, font, color, pos, center=False, strike=False):
    text_obj = font.render(text, True, color)
    rect = text_obj.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surface.blit(text_obj, rect)
    if strike:
        y = rect.centery
        pygame.draw.line(surface, color, (rect.left, y), (rect.right, y), 3)

def draw_textbox(surface, rect, active, text, font, color, wrong=False):
    pygame.draw.rect(surface, WHITE, rect, border_radius=8)
    pygame.draw.rect(surface, BLUE if active else DARK_GRAY, rect, 3, border_radius=8)
    if wrong:
        draw_text(surface, text, font, RED, (rect.x+10, rect.y+8), strike=True)
    else:
        draw_text(surface, text, font, color, (rect.x+10, rect.y+8))

def main():
    clock = pygame.time.Clock()
    input_text = ""
    active = True
    timer_running = False
    selected_time = None
    timer_left = 0
    total_words = 0
    correct_words = 0
    wrong_words = 0
    words_list = []
    word_index = 0
    wpm = 0

    # UI elements
    textbox_rect = pygame.Rect(150, 250, 600, 60)
    timer_buttons = []
    for i, (label, _) in enumerate(TIMER_OPTIONS):
        timer_buttons.append(pygame.Rect(120 + i*150, 120, 120, 45))

    # Fetch words (threaded for speed)
    words_ready = threading.Event()
    def load_words():
        nonlocal words_list
        words_list = fetch_words_api(200)
        words_ready.set()
    threading.Thread(target=load_words, daemon=True).start()

    # Game loop
    start_time = None
    running = True
    show_results = False
    wrong_flag = False

    while running:
        SCREEN.fill(WHITE)
        # Title
        draw_text(SCREEN, "TypeItRite", FONT_TITLE, BLUE, (WIDTH//2, 40), center=True)

        # Timer selection
        if not timer_running and not show_results:
            draw_text(SCREEN, "Choose a time mode:", FONT_MEDIUM, BLACK, (WIDTH//2, 90), center=True)
            for i, rect in enumerate(timer_buttons):
                pygame.draw.rect(SCREEN, BLUE if selected_time == i else GRAY, rect, border_radius=8)
                draw_text(SCREEN, TIMER_OPTIONS[i][0], FONT_MEDIUM, WHITE if selected_time == i else BLACK, rect.center, center=True)
            if not words_ready.is_set():
                draw_text(SCREEN, "Loading words...", FONT_SMALL, RED, (WIDTH//2, HEIGHT//2), center=True)
        elif timer_running:
            # Timer
            draw_text(SCREEN, f"Time Left: {int(timer_left)}s", FONT_MEDIUM, BLACK, (WIDTH-180, 20))
            # Current word
            draw_text(SCREEN, "Type the word:", FONT_MEDIUM, BLACK, (150, 180))
            if words_list:
                draw_text(SCREEN, words_list[word_index], FONT_LARGE, BLUE, (350, 180))
            # Textbox
            draw_textbox(SCREEN, textbox_rect, True, input_text, FONT_LARGE, BLACK, wrong=wrong_flag)
            # Stats
            draw_text(SCREEN, f"Total: {total_words}", FONT_SMALL, BLACK, (150, 340))
            draw_text(SCREEN, f"Correct: {correct_words}", FONT_SMALL, GREEN, (350, 340))
            draw_text(SCREEN, f"Wrong: {wrong_words}", FONT_SMALL, RED, (550, 340))
            draw_text(SCREEN, f"WPM: {wpm:.2f}", FONT_SMALL, BLACK, (750, 340))
        elif show_results:
            # Results
            draw_text(SCREEN, "Time's up!", FONT_LARGE, RED, (WIDTH//2, 120), center=True)
            draw_text(SCREEN, f"Total Words Typed: {total_words}", FONT_MEDIUM, BLACK, (WIDTH//2, 200), center=True)
            draw_text(SCREEN, f"Correct Words: {correct_words}", FONT_MEDIUM, GREEN, (WIDTH//2, 250), center=True)
            draw_text(SCREEN, f"Wrong Words: {wrong_words}", FONT_MEDIUM, RED, (WIDTH//2, 300), center=True)
            draw_text(SCREEN, f"WPM: {wpm:.2f}", FONT_LARGE, BLUE, (WIDTH//2, 370), center=True)
            draw_text(SCREEN, "Press ENTER to play again", FONT_MEDIUM, BLACK, (WIDTH//2, 420), center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not timer_running and not show_results:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, rect in enumerate(timer_buttons):
                        if rect.collidepoint(event.pos):
                            selected_time = i
                if event.type == pygame.KEYDOWN and selected_time is not None and words_ready.is_set():
                    # Start game
                    timer_running = True
                    timer_left = TIMER_OPTIONS[selected_time][1]
                    start_time = time.time()
                    input_text = ""
                    total_words = 0
                    correct_words = 0
                    wrong_words = 0
                    word_index = 0
                    wpm = 0
                    wrong_flag = False
                    random.shuffle(words_list)
            elif timer_running:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not words_list:
                            continue
                        total_words += 1
                        if input_text.strip() == words_list[word_index]:
                            correct_words += 1
                        else:
                            wrong_words += 1
                        word_index = (word_index + 1) % len(words_list)
                        input_text = ""
                        wrong_flag = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isprintable():
                        input_text += event.unicode
                # Check correctness for coloring
                if words_list and input_text and input_text.strip() != words_list[word_index][:len(input_text.strip())]:
                    wrong_flag = True
                else:
                    wrong_flag = False
            elif show_results:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    show_results = False
                    timer_running = False
                    selected_time = None

        # Timer logic
        if timer_running:
            elapsed = time.time() - start_time
            timer_left = TIMER_OPTIONS[selected_time][1] - elapsed
            if timer_left <= 0:
                timer_running = False
                show_results = True
                timer_left = 0
            # WPM calculation
            minutes = elapsed / 60 if elapsed > 0 else 1
            wpm = correct_words / minutes

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()