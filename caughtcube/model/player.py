
from ..util.color import white
from ..util.vectors import origin
from .gameitem import GameItem
from .cube import Cube


def Player():
    return GameItem(
        position=origin,
        shape=Cube(1, white),
        update=directed_motion(),
    )


class directed_motion(object):

    def __init__(self):
        self.moving_to = None

    def __call__(self, item, dt, time):
        print item, dt, time

