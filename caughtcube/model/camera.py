
from math import cos, sin

from euclid import Vector3

from .gameitem import GameItem


class Camera(object):

    def __init__(self, position, look_at):
        if not isinstance(position, Vector3):
            position = Vector3(*position)
        self.position = position

        self._look_at = look_at
    

    @property
    def look_at(self):
        if isinstance(self._look_at, Vector3):
            return self._look_at
        elif isinstance(self._look_at, GameItem):
            return self._look_at.position
        else:
            raise TypeError(str(self._look_at))


    def update(self):
        self.position += Vector3(
            -sin(self.time),
            cos(self.time),
            0,
        ) * 0.01

