import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *
import sys

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.health = PLAYER_HEALTH
        self.score = 0
        self.health = 10
    
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_RATE * dt)
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

            
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def hurt(self):
        if self.health > 0:
            self.health -= 1
            print("OUCH")
        else:
            print("Game over!")
            sys.exit()
        
