from __future__ import division

from ..model.gameitem import GameItem
from ..model.shape import Shape
from ..util.color import all_colors


def RoomShape(xmax, ymax, zmax, colors):
    xmin, ymin, zmin = (-0.5, -0.5, -0.5)
    xmax -= 0.5
    ymax -= 0.5
    zmax -= 0.5
    verts = [
        (xmin, ymin, zmin),
        (xmin, ymin, zmax),
        (xmin, ymax, zmin),
        (xmin, ymax, zmax),
        (xmax, ymin, zmin),
        (xmax, ymin, zmax),
        (xmax, ymax, zmin),
        (xmax, ymax, zmax),
    ]
    faces = [
        [2, 3, 1, 0], # 
        [5, 7, 6, 4], # 
        [5, 1, 3, 7], # 
        [4, 6, 2, 0], # 
        [5, 4, 0, 1], # -y bottom
        [2, 6, 7, 3], # +y top        
    ]
    return Shape(verts, faces, colors)


def Room(xsize, ysize, zsize):
    return GameItem(
        shape=RoomShape(xsize, ysize, zsize, all_colors),
    )

