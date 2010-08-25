
from euclid import Vector3


class GameItem(object):

    _next_id = 0

    def __init__(self, position=None, shape=None, update=None):
        self.id = GameItem._next_id
        GameItem._next_id += 1

        if isinstance(position, tuple):
            position = Vector3(*position)
        self.position = position

        self.shape = shape
        self.update = update

