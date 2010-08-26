
from math import copysign, cos, sin

from euclid import Vector3

from ..util.vectors import round_down_to_int

def orbit(item, dt, time):
    item.position = Vector3(
        -sin(time),
        4 + cos(time),
        4,
    ) * 2


class directed_motion(object):

    def __init__(self):
        self.delta = None
        self.next_move = None


    def _has_reached_destination(self, position):
        offset = position - self.destination
        return self._stop_moving_flag != copysign(1, sum(offset))


    def __call__(self, item, dt, time):
        position = item.position

        if not self.delta and self.next_move:
            # start moving
            self.destination = item.position + self.next_move
            self.delta = self.next_move / 10.0
            self._stop_moving_flag = -copysign(1, sum(self.next_move))
            self.next_move = None

        if self.delta:
            # is moving
            next_position = item.position + self.delta
            if self._has_reached_destination(next_position):
                # stop moving
                self.delta = None
                self.next_move = None
            else:
                # continue moving
                item.position = next_position

