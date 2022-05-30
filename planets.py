import sys
import math
import pygame

from models import (
    Planet,
    HEIGHT,
    WIDTH
)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Simulation")

WHITE = (255, 255, 255)


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # screen.fill(WHITE)
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)

if __name__ == "__main__":
    main()