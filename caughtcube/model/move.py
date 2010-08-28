
from math import copysign, cos, sin

from euclid import Vector3


def orbit(item, dt, time):
    item.position = Vector3(
        4 - sin(time) * 3,
        7 + cos(time),
        7.4,
    )


class directed_motion(object):

    SPEED = 0.06

    def __init__(self, world):
        self.world = world
        self.input = None
        self.velocity = None
        self.next_move = None


    def _try_to_move(self, item):
        # not moving and a move has been requested
        destination = item.position + self.next_move
        # TODO: should check all entries in item.bounds + destination,
        # not just { (0,0,0) } + destination
        item_at_dest = self.world.collision.occupied.get(
            tuple(destination), None)
        # is item_at_dest one we can move into? (e.g. exit)
        if not (
            item_at_dest and
            hasattr(item_at_dest, 'collide') and
            item_at_dest.collide
        ):
            self._start_moving(destination)
        self.next_move = None


    def _start_moving(self, destination):
        self.destination = destination
        self.velocity = self.next_move * self.SPEED
        self._stop_moving_flag = -copysign(1, sum(self.next_move))


    def _moving(self, item):
        new_position = item.position + self.velocity
        if self._has_reached_destination(new_position):
            self._stop_moving(item)
        else:
            item.position = new_position


    def _has_reached_destination(self, position):
        offset = position - self.destination
        return self._stop_moving_flag != copysign(1, sum(offset))


    def _stop_moving(self, item):
        item.position = self.destination
        self.velocity = None
        self.next_move = None


    def __call__(self, item, dt, time):
        position = item.position

        if self.input is not None:
            self.next_move = self.input

        if not self.velocity and self.next_move:
            self._try_to_move(item)

        if self.velocity:
            self._moving(item)

