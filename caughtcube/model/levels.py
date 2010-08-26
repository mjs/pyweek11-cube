from .exit import Exit
from .wall import Wall

levels = [
    [
        Wall((1, 2, 1), (-2, 0, -4)),
        Wall((1, 3, 4), ( 2, 0, -2)),
        Exit((3, 3, 3)),
    ],
]