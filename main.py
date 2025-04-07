import pygame
from constants import *
from player import Player

def main():
    clock = pygame.time.Clock()
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds

        

        

if __name__ == "__main__":
    main()