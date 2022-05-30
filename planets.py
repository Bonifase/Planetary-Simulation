from models import Planet
from color_codes import YELLOW

def get_planets():
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    return [sun]