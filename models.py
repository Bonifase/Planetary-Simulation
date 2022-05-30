import pygame
import math

WIDTH, HEIGHT = 800, 800


class Planet:
    ASTRONOMICAL_UNIT = 149.6e6 * 1000 # Distance of the earth from the sun.
    GRAVITATIONAL_CONSTANT = 6.67428e-11
    SCALE = 250/ASTRONOMICAL_UNIT # 1AU = 100 pixels
    TIME_STEP = 3600 * 24 # 1 DAY
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_from_sun = 0

        self.x_velocity = 0
        self.y_velocity = 0
    
    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

class Star:
    pass

class Asteroid:
    pass