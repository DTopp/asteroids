import pygame
import sys
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    clock = pygame.time.Clock()
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    lives = 3
    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        # Check for collisions with asteroids
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Life Lost!")
                lives -= 1
                player.kill()
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                asteroidfield = AsteroidField()

        # Check for collisions between shots and asteroids
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
                        
        screen.fill("black")  # Fill the screen with black
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds

    print("Game Over!")

        

        

if __name__ == "__main__":
    main()