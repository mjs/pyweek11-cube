
from .exit import Exit
from .room import Room
from .wall import Wall


def populate(world, number):
    for item in levels[number]:
        world.add(item)
    start_position = (0, 0, 0)
    return start_position


levels = {
    1: [
        Room(8, 16, 8),
        Wall((1, 1, 7), (2, 0, 1)),
        Wall((1, 1, 9), (2, 1, 0)),
        Wall((1, 1, 5), (4, 0, 0)),
        Wall((1, 1, 5), (4, 0, 6)),
        Wall((1, 1, 9), (4, 1, 0)),
        Wall((1, 1, 9), (6, 1, 0)),
        Wall((1, 1, 1), (6, 0, 7)),
        Wall((1, 1, 6), (6, 0, 0)),
        Exit((6, 0, 6)),
    ],
}

