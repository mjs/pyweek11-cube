
from .exit import Exit
from .room import Room
from .wall import Wall


def populate(world, number):
    for item in levels[number]:
        world.add(item)
    start_position = (2, 0, 2)
    return start_position


levels = {
    1: [
        Room(8, 16, 8),
        Wall((4, 1, 1), (0, 1, 1)),
        Wall((1, 5, 1), (1, 0, 1)),
        Wall((1, 1, 6), (1, 1, 0)),
        Wall((2, 3, 4), (6, 0, 0)),
        Exit((3, 3, 3)),
    ],
}

