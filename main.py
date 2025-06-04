import sys
import pygame
import os
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        font = pygame.font.Font('fonts/EduSAHand-Regular.ttf', 36)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                player.hurt()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    #largest asteroids have most points encouraging more chaotic gameplay
                    player.score += asteroid.radius 
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        score_text = font.render(f"Score: {player.score}", True, (255,255,255))
        screen.blit(score_text, (10,10))

        health_text = font.render(f"Health: {player.health}", True, (255,255,255))
        screen.blit(health_text, (10,65))

        pygame.display.flip()
        dt = clock.tick(60) / 1000 #pauses game loop till 1/60th of a second passed
        

if __name__ == "__main__":
    main()
