
class World(object):

    def __init__(self):
        self.items = {}

    def __iter__(self):
        return self.items.itervalues()

    def add(self, item):
        self.items[item.id] = item

    def remove(self, item):
        del self.items[item.id]

