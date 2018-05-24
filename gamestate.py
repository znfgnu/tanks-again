import pygame

from player import Player

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GameState:
    def __init__(self):
        self.p1 = Player(20, 20, RED)
        self.p2 = Player(780, 580, BLUE)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.p1.start_moving()
                if event.key == pygame.K_DOWN:
                    self.p1.start_moving_backwards()
                if event.key == pygame.K_w:
                    self.p2.start_moving()
                if event.key == pygame.K_LEFT:
                    self.p1.start_rotating_left()
                if event.key == pygame.K_RIGHT:
                    self.p1.start_rotating_right()
                if event.key == pygame.K_a:
                    self.p2.start_rotating_left()
                if event.key == pygame.K_d:
                    self.p2.start_rotating_right()
                if event.key == pygame.K_s:
                    self.p2.start_moving_backwards()
                if event.key == pygame.K_t:
                    self.p2.fire_bullet()
                if event.key == pygame.K_COMMA:
                    self.p1.fire_bullet()
                if event.key == pygame.K_m:
                    self.p1.fire_mine()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.p1.stop_moving()
                if event.key == pygame.K_DOWN:
                    self.p1.stop_moving()
                if event.key == pygame.K_w:
                    self.p2.stop_moving()
                if event.key == pygame.K_s:
                    self.p2.stop_moving()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.p1.stop_rotating()
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    self.p2.stop_rotating()

    def update(self):
        self.p1.update(self.p2)
        self.p2.update(self.p1)
        for b in self.p1.bullets:
            b.update()
        for b in self.p2.bullets:
            b.update()
        if self.p1.health <= 0 or self.p2.health <= 0:
            running = False

    def draw(self, screen):
        screen.fill(GREEN)
        # Draw things here
        self.p1.draw(screen)
        self.p2.draw(screen)

        for b in self.p1.bullets:
            b.draw(screen)
        for b in self.p2.bullets:
            b.draw(screen)
