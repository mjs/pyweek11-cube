
from ..util.color import white
from ..util.vectors import origin
from .gameitem import GameItem
from .cube import Cube
from .gameitem import GameItem
from .move import directed_motion


def Player(**kwargs):
    return GameItem(
        position=origin,
        shape=Cube(1, white),
        update=directed_motion(),
        **kwargs
    )



