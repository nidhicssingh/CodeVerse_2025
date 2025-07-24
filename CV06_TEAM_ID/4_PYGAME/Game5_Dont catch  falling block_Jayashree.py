import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 800
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)


PLAYER_WIDTH = 80
PLAYER_HEIGHT = 20
PLAYER_SPEED = 8


BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
BLOCK_SPEED = 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Catch the Falling Block")
clock = pygame.time.Clock()


class Player(pygame.Rect):
    def __init__(self):
        super().__init__((WIDTH - PLAYER_WIDTH) // 2, HEIGHT - 60, PLAYER_WIDTH, PLAYER_HEIGHT)

    def move(self, dx):
        self.x += dx

        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - PLAYER_WIDTH:
            self.x = WIDTH - PLAYER_WIDTH


class Block(pygame.Rect):
    def __init__(self):
        x = random.randint(0, WIDTH - BLOCK_WIDTH)
        y = -BLOCK_HEIGHT
        super().__init__(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)

    def fall(self):
        self.y += BLOCK_SPEED

def main():
    player = Player()
    blocks = []
    spawn_timer = 0
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            player.move(PLAYER_SPEED)


        spawn_timer += 1
        if spawn_timer > 30:
            blocks.append(Block())
            spawn_timer = 0


        for block in blocks:
            block.fall()
            if block.colliderect(player):

                print(f"Game Over! Final Score: {score}")
                running = False


        blocks = [block for block in blocks if block.y < HEIGHT]


        score += 1

        
        pygame.draw.rect(screen, BLUE, player)
        for block in blocks:
            pygame.draw.rect(screen, RED, block)

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
