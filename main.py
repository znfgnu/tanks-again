import pygame

from configuration import WIDTH, HEIGHT
from gamestate import GameState

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

state = GameState()

while running:
    # 1. Process input
    state.process_input()
    # 2. Update game
    state.update()
    # 3. Render screen (draw things)
    state.draw(screen)

    pygame.display.update()
    # 4. Wait some time
    clock.tick(60)
