from __future__ import division
from itertools import product

from ..util.color import grey
from .gameitem import GameItem
from .shape import Shape


def WallShape(size, color, invert=False):
    xmax, ymax, zmax = size
    xmin, ymin, zmin = (-0.5, -0.5, -0.5) 
    xmax -= 0.5
    ymax -= 0.5
    zmax -= 0.5
    verts = list(product((xmin, xmax), (ymin, ymax), (zmin, zmax)))
    faces = [
        [0, 1, 3, 2], # left
        [4, 6, 7, 5], # right
        [7, 3, 1, 5], # front
        [0, 2, 6, 4], # back
        [3, 7, 6, 2], # top
        [1, 0, 4, 5], # bottom
    ]
    if invert:
        for face in faces:
            face.reverse()
    return Shape(verts, faces, color)


def Wall(size, position):
    return GameItem(
        position=position,
        shape=WallShape(size, grey),
    )

