import sys
from os.path import join

from ..util import color
from ..util import path
from .item.exit import Exit
from .item.room import Room
from .item.wall import Wall


LEVEL_DIR = join(path.DATA, 'level')
sys.path.append(LEVEL_DIR)


def populate(world, number):
    level = Level(number)
    level.create(world)


class Level(object):

    def __init__(self, number):
        self.number = number


    def create(self, world):
        level = __import__('level%02d' % (self.number,))

        blocks = self.get_blocks(level.layout)
        room_size = self.get_room_size(blocks)   
        world.add(Room(*room_size))

        self.add_items(world, blocks)


    def get_blocks(self, layout):
        blocks = layout.split('\n\n')
        return [block.split('\n') for block in blocks]


    def get_room_size(self, blocks):
        height = len(blocks)
        length = max(len(block) for block in blocks)
        width = max(
            len(line)
            for block in blocks
            for line in block
        )
        return (width, height, length)


    def add_items(self, world, blocks):
        for y, block in enumerate(blocks):
            for z, line in enumerate(block):
                for x, char in enumerate(line):
                    position = (x, y, z)
                    if char == ' ':
                        pass
                    elif char == '#':
                        self.add_wall(world, position)
                    elif char == 's':
                        world.start = position
                    elif char == 'e':
                        world.add(Exit(position))
                    else:
                        print 'unknown', repr(char)


    def add_wall(self, world, position):
        world.add(
            Wall(
                size=(1, 1, 1),
                position=position,
                color=color.paleblue,
            )
        )

