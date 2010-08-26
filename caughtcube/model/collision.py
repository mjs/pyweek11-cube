

class Collision(object):
    '''
    The collision object detects if any objects in the world are currently
    colliding
    '''
    def __init__(self):
        self.occupied = {}

    def add(self, item):
        if hasattr(item, 'bounds'):
            for offset in item.bounds:
                location = self.position + offset
                if location in self.occupied:
                    raise Exception(
                        'location %s already occupied by %s while adding %s' % (
                            location, item, self.occupied[location]
                        ) )
                self.occupied[location] = item

    def remove(self, item):
        if hasattr(item, 'bounds'):
            for offset in item.bounds:
                location = self.position + offset
                del self.occupied[location]

