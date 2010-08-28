import sys
from os.path import join

from ..util import color
from ..util import path
from .item.exit import Exit
from .item.room import Room
from .item.wall import Wall


LEVEL_DIR = join(path.DATA, 'level')
sys.path.append(LEVEL_DIR)



class Level(object):

    def __init__(self, world):
        self.world = world
        self.number = None


    def load(self, number):
        self.number = number
        level = __import__('level%02d' % (self.number,))

        blocks = self.get_blocks(level.layout)
        room_size = self.get_room_size(blocks)   
        self.world.add(Room(*room_size))

        self.add_items(blocks)


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


    def clear(self):
        for item in self.world:
            self.world.remove(item)
        self.world.start = None


    def add_items(self, blocks):
        for y, block in enumerate(blocks):
            for z, line in enumerate(block):
                for x, char in enumerate(line):
                    position = (x, y, z)
                    if char == ' ':
                        pass
                    elif char == '#':
                        self.add_wall(position)
                    elif char == 's':
                        self.world.start = position
                    elif char == 'e':
                        self.world.add(Exit(position))
                    else:
                        print 'unknown char %c loading level %d' % (
                            char, self.number)


    def add_wall(self, position):
        self.world.add(
            Wall(
                size=(1, 1, 1),
                position=position,
                color=color.paleblue,
            )
        )

