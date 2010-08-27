
from ..util.color import white, cyan
from .exit import Exit
from .room import Room
from .wall import Wall


def populate(world, number):
    for item in levels[number]:
        world.add(item)
    start_position = (5, 0, 0)
    return start_position


paleblue = white.tinted(cyan, 0.15)

levels = {
    1: [
        Room(8, 16, 8),
        Wall((1, 1, 1), (6, 0, 0), paleblue),
        Wall((6, 1, 1), (1, 0, 1), paleblue),
        Wall((3, 1, 1), (0, 0, 3), paleblue),
        Wall((1, 1, 4), (4, 0, 2), paleblue),
        Wall((2, 1, 1), (6, 0, 3), paleblue),
        Wall((5, 1, 1), (2, 0, 5), paleblue),
        Wall((1, 1, 1), (0, 0, 4), paleblue),
        Wall((2, 1, 1), (1, 0, 6), paleblue),
        Wall((1, 1, 1), (6, 0, 6), paleblue),
        Wall((1, 1, 1), (4, 0, 7), paleblue),
        Exit((7, 0, -1)),
    ],
}

