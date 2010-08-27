
from os import path
from ..util import color
from .item.exit import Exit
from .item.room import Room
from .item.wall import Wall


LEVEL_DIR = path.join(path.dirname(__file__), '..', '..', 'data')

def populate(world, number):
    for item in load_level(file(get_level_path(number))):
        world.add(item)
    start_position = (5, 0, 0)
    return start_position


def get_level_path(number):
    return path.join(LEVEL_DIR, '%02d.lvl' % number)
    

def load_level(fileobj):
    for line in fileobj:
        parts = map(str.strip, line.split(':'))
        yield loaders[parts[0]](*parts[1:])
        

def load_room(dim):
    return Room(*parse_triple(dim))


def load_wall(a, b, color_name):
    return Wall(parse_triple(a),
                parse_triple(b),
                getattr(color, color_name))


def load_exit(where):
    return Exit(parse_triple(where))


loaders = {
    'room': load_room,
    'wall': load_wall,
    'exit': load_exit,
}


def parse_triple(triple_str):
    t = tuple(int(x.strip()) for x in triple_str.split(','))
    assert len(t) == 3
    return t 



