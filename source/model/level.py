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

    def __init__(self, gameloop):
        self.gameloop = gameloop
        self.number = 0


    def next(self, world):
        self.clear(world)
        return self.load(world, self.number + 1)


    def clear(self, world):
        items = world.items.values()
        for item in items:
            world.remove(item)


    def load(self, world, number):
        try:
            level = __import__('level%02d' % (number,))
        except ImportError:
            return False

        blocks = self.get_blocks(level.layout)
        room_size = self.get_room_size(blocks)   
        world.add(Room(*room_size))

        self.add_items(world, blocks)
        self.number = number
        return True


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
                        world.add(
                            Wall(
                                size=(1, 1, 1),
                                position=position,
                                color=color.paleblue,
                            )
                        )
                    elif char == 's':
                        world.add(
                            self.gameloop.player,
                            position=position,
                        )
                    elif char == 'e':
                        world.add(Exit(position))
                    elif char == 'c':
                        world.add(
                            self.gameloop.camera,
                            position=position,
                        )
                    else:
                        print 'unknown char %c loading level %d' % (
                            char, self.number)

