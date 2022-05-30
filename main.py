import sys
import math
import pygame

from models import HEIGHT, WIDTH
from planets import get_planets

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Simulation")

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)
        for planet in get_planets():
            planet.draw(screen)

if __name__ == "__main__":
    main()