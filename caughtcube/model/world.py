
from ..util.color import Color
from ..util.event import Event


class World(object):

    clear_color = Color(0.2, 0.7, 1.0, 1.0)

    def __init__(self):
        self.items = {}
        self.item_added = Event()
        self.item_removed = Event()

    def __iter__(self):
        return self.items.itervalues()

    def add(self, item):
        self.items[item.id] = item
        self.item_added.fire(item)

    def remove(self, item):
        del self.items[item.id]
        self.item_removed.fire(item)

