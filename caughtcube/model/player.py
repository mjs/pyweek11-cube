
from ..util.color import white
from .gameitem import GameItem
from .shape import MultiShape
from .cube import Cube, Cuboid
from .move import directed_motion


def PlayerShape():
    multi = MultiShape()
    multi.add(Cube(0.8, white))
    multi.add(Cuboid(30, 0.6, 0.6, (255, 255, 128, 35)))
    multi.add(Cuboid(0.6, 30, 0.6, (255, 255, 128, 35)))
    multi.add(Cuboid(0.6, 0.6, 30, (255, 255, 128, 35)))
    return multi

def Player():
    return GameItem(
        shape=PlayerShape(),
        update=directed_motion(),
    )

