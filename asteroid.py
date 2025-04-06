import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers: tuple[pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group]

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        _ = Asteroid(self.position.x, self.position.y, new_radius)  # type: ignore
        _.velocity = vector_1 * 1.2
        _ = Asteroid(self.position.x, self.position.y, new_radius)  # type: ignore
        _.velocity = vector_2 * 1.2
