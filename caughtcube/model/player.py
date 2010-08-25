
from ..util.color import white
from ..util.vectors import origin
from .gameitem import GameItem
from .cube import Cube


def Player():
    return GameItem(
        position=origin,
        shape=Cube(1, white),
    )

