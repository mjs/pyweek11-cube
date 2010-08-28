
from math import floor

from euclid import Vector3


origin = Vector3(0, 0, 0)
x_axis = Vector3(1, 0, 0)
y_axis = Vector3(0, 1, 0)
z_axis = Vector3(0, 0, 1)
neg_x_axis = Vector3(-1, 0, 0)
neg_y_axis = Vector3(0, -1, 0)
neg_z_axis = Vector3(0, 0, -1)


def round_to_int(v):
    return Vector3(
        floor(v.x + 0.5),
        floor(v.y + 0.5),
        floor(v.z + 0.5),
    )

def round_down_to_int(v):
    return Vector3(
        floor(v.x),
        floor(v.y),
        floor(v.z),
    )
