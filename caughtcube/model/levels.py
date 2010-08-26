
from .exit import Exit
from .room import Room
from .wall import Wall


def populate(world, number):
    for item in levels[number]:
        world.add(item)
    start_position = (1, 0, 1)
    return start_position


levels = {
    1: [
        Room(8, 16, 8),
        Wall((1, 2, 1), (2, 0, 4)),
        Wall((1, 3, 4), (2, 0, 2)),
        Exit((3, 3, 3)),
    ],
}

