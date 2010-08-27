

class Collision(object):
    '''
    detects if any objects in the world collide
    '''
    def __init__(self):
        self.occupied = {}

    def occupies(self, item):
        '''
        the locations that the given item occupies
        '''
        if hasattr(item, 'position'):
            return {
                tuple(offset + item.position)
                for offset in item.bounds
            }
        else:
            return item.bounds


    def add(self, item):
        '''
        add a new item to the world. Raise if it interpenetrates existing items
        '''
        if hasattr(item, 'bounds'):
            for location in self.occupies(item):
                if location in self.occupied:
                    raise Exception(
                        'location %s already occupied by %s while adding %s' % (
                            location, item, self.occupied[location]
                        ) )
                self.occupied[location] = item


    def remove(self, item):
        '''
        remove an item from the world. Raise if it was not present
        '''
        if hasattr(item, 'bounds'):
            for location in self.occupies(item):
                if self.occupied[location] != item:
                    raise Exception(
                        'location %s not occupied by %s while removing' % (
                            location, item
                    ) )
                del self.occupied[location]

