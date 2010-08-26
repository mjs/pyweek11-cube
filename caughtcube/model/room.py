from __future__ import division
from itertools import product

from ..util.color import white, blue
from .gameitem import GameItem
from .shape import Shape
from .wall import WallShape


def Room(xsize, ysize, zsize):
    paleblue = white.tinted(blue, 0.1)
    return GameItem(
        shape=WallShape((xsize, ysize, zsize), paleblue, invert=True),
    )

