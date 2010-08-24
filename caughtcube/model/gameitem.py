
from euclid import Vector3

from ..util.vectors import origin


class GameItem(object):

    _next_id = 0

    def __init__(self, position=origin, shape=None):
        self.id = GameItem._next_id
        GameItem._next_id += 1

        if not isinstance(position, Vector3):
            position = Vector3(*position)
        self.position = position

        self.shape = shape

        self.glyph = None

