
from itertools import product, repeat

from .shape import Shape


def Cube(edge, colors=None):
    e2 = edge / 2.
    verts = list(product(*repeat([-e2, +e2], 3)))
    faces = [
        [0, 1, 3, 2], # left
        [4, 6, 7, 5], # right
        [7, 3, 1, 5], # front
        [0, 2, 6, 4], # back
        [3, 7, 6, 2], # top
        [1, 0, 4, 5], # bottom
    ]
    return Shape(verts, faces, colors)

