
from math import copysign, cos, sin

from euclid import Vector3


def orbit(item, dt, time):
    item.position = Vector3(
        4 - sin(time) * 3,
        8 + cos(time),
        7.4,
    )


class directed_motion(object):

    SPEED = 0.06

    def __init__(self):
        self.input = None
        self.velocity = None
        self.next_move = None


    def _has_reached_destination(self, position):
        offset = position - self.destination
        return self._stop_moving_flag != copysign(1, sum(offset))


    def __call__(self, item, dt, time):
        position = item.position

        if self.input is not None:
            self.next_move = self.input

        if not self.velocity and self.next_move:
            # start moving
            self.destination = item.position + self.next_move
            self.velocity = self.next_move * self.SPEED
            self._stop_moving_flag = -copysign(1, sum(self.next_move))
            self.next_move = None

        if self.velocity:
            # is moving
            new_position = item.position + self.velocity
            if self._has_reached_destination(new_position):
                # stop moving
                item.position = self.destination
                self.velocity = None
                self.next_move = None
            else:
                # continue moving
                item.position = new_position

