
from math import cos, sin

from euclid import Vector3


def orbit(item, dt, time):
    item.position = Vector3(
        -sin(time),
        4 + cos(time),
        4,
    ) * 2

