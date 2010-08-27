
from ...util.color import black
from ..cube import Cube
from .gameitem import GameItem


def Exit(position):
    return GameItem(
        shape=Cube(1.01, black),
        position=position
    )

