
from ..util.color import white
from .gameitem import GameItem
from .cube import Cube
from .move import directed_motion


def Player():
    return GameItem(
        shape=Cube(0.8, white),
        update=directed_motion(),
    )

