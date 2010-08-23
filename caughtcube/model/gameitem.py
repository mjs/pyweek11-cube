
from euclid import Vector3


class GameItem(object):

    _next_id = 0

    def __init__(self, position=(0, 0, 0)):
        self.id = GameItem._next_id
        GameItem._next_id += 1

        if not isinstance(position, Vector3):
            position = Vector3(*position)
        self.position = position

