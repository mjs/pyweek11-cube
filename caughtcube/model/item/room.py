from __future__ import division

from ...util.color import white, cyan
from .gameitem import GameItem
from .wall import WallShape


def Room(xsize, ysize, zsize):
    '''
    Interior of room goes from:
        x: 0 to xsize-1
        y: 0 to ysize-1
        z: 0 to zsize-1
    Shape of Room is 0.5 larger than that in every direction, so that
    player (or any other 1.0 sized object) can sit at any location in
    the room and not intersect with the room walls
    '''
    paleblue = white.tinted(cyan, 0.1)
    return GameItem(
        shape=WallShape((xsize, ysize, zsize), paleblue, invert=True),
    )

