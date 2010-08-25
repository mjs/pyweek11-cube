
from ..util.color import white
from .gameitem import GameItem
from .cube import Cube


def Player(**kwargs):
    return GameItem(
        shape=Cube(1, white),
        update=directed_motion(),
        **kwargs
    )


class directed_motion(object):

    def __init__(self):
        self.moving_to = None

    def __call__(self, item, dt, time):
        pass #print item, dt, time


