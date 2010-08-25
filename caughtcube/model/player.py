
from ..util.color import white
from .gameitem import GameItem
from .cube import Cube
from .move import directed_motion


def Player(**kwargs):
    return GameItem(
        shape=Cube(1, white),
        update=directed_motion(),
        **kwargs
    )



