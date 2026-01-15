import pygame, random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width = LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        new_direction_left = self.velocity.rotate(split_angle)
        new_direction_right = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_left.velocity = new_direction_left * 1.2
        asteroid_right.velocity = new_direction_right * 1.2