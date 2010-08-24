
class Event(object):

    def __init__(self):
        self.listeners = []

    def __iadd__(self, listener):
        print 'Event.iadd {'
        self.listeners.append(listener)
        print self.listeners
        print '} Event.iadd'
        return self

    def fire(self, *args, **kwargs):
        print 'Event.fire {'
        for listener in self.listeners:
            print listener
            listener(*args, **kwargs)
        print '} Event.fire'

