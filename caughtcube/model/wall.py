from __future__ import division

from itertools import product, repeat
from ..model.gameitem import GameItem
from ..model.shape import Shape
from ..util.color import grey


def WallShape(size, color):
    verts = list(product(*repeat([-0.5, +0.5], 3)))
    def stretch(v):
        return (v[0]*size[0], v[1]*size[1], v[2]*size[2])
    verts = map(stretch, verts)
    faces = [
            [0, 1, 3, 2], # left
            [4, 6, 7, 5], # right
            [7, 3, 1, 5], # front
            [0, 2, 6, 4], # back
            [3, 7, 6, 2], # top
            [1, 0, 4, 5], # bottom
            ]
    return Shape(verts, faces, color)


def Wall(size, position):
    return GameItem(
        position=position,
        shape=WallShape(size, grey),
    )

