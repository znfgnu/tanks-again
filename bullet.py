import cmath
import pygame
from math import radians

from configuration import BLACK, WIDTH, HEIGHT


class Bullet:
    def __init__(self, position, speed, direction):
        self.position = position
        self.speed = speed
        self.direction = direction
        self.radius = 4

    def collides_with_player(self, p):
        a = self
        b = p
        d = b.pos - a.position
        distance = abs(d)
        # print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False

    def is_outside_screen(self):
        return WIDTH <= self.position.real + self.radius or \
                HEIGHT <= self.position.imag + self.radius or \
                self.position.real - self.radius < 0 or \
                self.position.imag - self.radius < 0

    def draw(self, sur):
        pygame.draw.circle(sur, BLACK, (int(self.position.real), int(self.position.imag)), self.radius)

    def update(self):
        step = cmath.rect(self.speed, radians(self.direction))
        self.position += step
