from __future__ import division

from ..model.gameitem import GameItem
from ..model.shape import Shape
from ..util.color import all_colors


def RoomShape(edge, colors):
    e = edge / 2
    verts = [
        (-e/2 - 0.5,        0.5, -e/2 - 0.5,),
        (-e/2 - 0.5,        0.5, +e/2 + 0.5,),
        (-e/2 - 0.5, +e/2 + 0.5, -e/2 - 0.5,),
        (-e/2 - 0.5, +e/2 + 0.5, +e/2 + 0.5,),
        (+e/2 + 0.5,        0.5, -e/2 - 0.5,),
        (+e/2 + 0.5,        0.5, +e/2 + 0.5,),
        (+e/2 + 0.5, +e/2 + 0.5, -e/2 - 0.5,),
        (+e/2 + 0.5, +e/2 + 0.5, +e/2 + 0.5,),
    ]
    faces = [
        [2, 3, 1, 0],
        [5, 7, 6, 4],
        [5, 1, 3, 7],
        [4, 6, 2, 0],
        [5, 4, 0, 1]
    ]
    return Shape(verts, faces, colors)


def Room(width):
    return GameItem(
        shape=RoomShape(width, all_colors),
    )

