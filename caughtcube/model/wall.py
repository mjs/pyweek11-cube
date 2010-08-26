from __future__ import division
from itertools import product

from ..util.color import grey
from .gameitem import GameItem
from .shape import Shape


def WallShape(size, colors, invert=False):
    '''
    returns a cuboid shape encompassing worldspace co-ords:
        x: 0 to size[0]-1
        y: 0 to size[1]-1
        z: 0 to size[2]-1
    If 'invert' is True, the faces are flipped to make the shape suitable
    for viewing from the inside
    '''
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
    return Shape(verts, faces, colors)


def Wall(size, position):
    return GameItem(
        position=position,
        shape=WallShape(size, grey),
    )

