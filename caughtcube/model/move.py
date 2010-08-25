
from math import cos, sin

from euclid import Vector3

def orbit(item, dt, time):
    item.position += Vector3(
        -sin(time),
        cos(time),
        0,
    ) * 0.01

