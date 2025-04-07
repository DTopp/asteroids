import pygame
from constants import *

def main():
    clock = pygame.time.Clock()
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))  # Fill the screen with black
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds

if __name__ == "__main__":
    main()