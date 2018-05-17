import cmath
import pygame
from math import radians

from bullet import Bullet
from configuration import HEIGHT, WIDTH, BLACK, WHITE


class Player:
    def __init__(self, x, y, col):
        self.pos = x + y * 1j
        self.dir = 35
        self.radius = 20
        self.vel = 0
        self.vel_dir = 0
        self.color = col
        self.bullet = None
        self.health = 70

    def draw(self, sur):
        pygame.draw.circle(sur, self.color, (int(self.pos.real), int(self.pos.imag)), self.radius)
        c = self.pos + cmath.rect(self.radius/2, radians(self.dir))
        d = self.pos + cmath.rect(1.5*self.radius, radians(self.dir))
        pygame.draw.line(sur, BLACK, (int(c.real), int(c.imag)), (int(d.real), int(d.imag)), 3)

        # Draw healthbar
        if self.pos.imag > HEIGHT/2:
            v = -50-(self.radius+40)*1j     # Vector (-50, -(r+40))
        else:
            v = -50 + (self.radius+20)*1j
        healthbar_pos = self.pos + v
        pygame.draw.rect(sur, BLACK, (int(healthbar_pos.real), int(healthbar_pos.imag), 100, 20))
        pygame.draw.rect(sur, WHITE, (int(healthbar_pos.real), int(healthbar_pos.imag), self.health, 20))

    def start_moving(self):
        self.vel = 3

    def stop_moving(self):
        self.vel = 0

    def start_moving_backwards(self):
        self.vel = -3

    def start_rotating_left(self):
        self.vel_dir = -5
        #self.dir = self.dir - 10

    def start_rotating_right(self):
        self.vel_dir = 5
        #self.dir = self.dir + 10

    def stop_rotating(self):
        self.vel_dir = 0

    def is_outside_screen(self):
        return WIDTH <= self.pos.real + self.radius or \
                HEIGHT <= self.pos.imag + self.radius or \
                self.pos.real - self.radius < 0 or \
                self.pos.imag - self.radius < 0

    def collides_with_other_player(self, other_player):
        a = self
        b = other_player
        d = b.pos - a.pos
        distance = abs(d)
        # print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False

    def update(self, other_player):
        self.dir = self.dir + self.vel_dir
        self.pos = self.pos + cmath.rect(self.vel, radians(self.dir))
        if self.is_outside_screen():
            self.pos = self.pos - cmath.rect(self.vel, radians(self.dir))
        if self.collides_with_other_player(other_player):
            self.pos = self.pos - cmath.rect(self.vel, radians(self.dir))
        if self.bullet is not None:
            if self.bullet.collides_with_player(other_player):
                other_player.health -= 10
                self.bullet = None

    def fire_bullet(self):
        self.bullet = Bullet(self.pos, 10, self.dir)
