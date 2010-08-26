
from ..util.color import black
from .gameitem import GameItem
from .cube import Cube


def Exit(position):
    return GameItem(
        shape=Cube(1.0, black),
        position=position
    )
