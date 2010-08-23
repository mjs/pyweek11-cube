from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window



class Gameloop(object):

    def __init__(self, options):
        self.options = options
        self.camera = None
        self.projection = None
        self.render = None
        self.window = None
        self.world = None
        self.fpss = []


    def prepare(self, options):
        self.window = Window(
            fullscreen=options.fullscreen,
            vsync=False,
            visible=False,
            resizable=True)
        self.window.on_draw = self.draw

        pyglet.clock.schedule(self.update)
        self.clock_display = pyglet.clock.ClockDisplay()


    def run(self):
        self.window.set_visible()
        pyglet.app.run()


    def update(self, dt):
        if self.options.print_fps:
            self.fpss.append(1/max(1e-3, dt))

        dt = min(dt, 1 / 30)

        self.window.invalid = True


    def draw(self):
        self.window.clear()

        return EVENT_HANDLED


    def stop(self):
        if self.window:
            self.window.close()

        if self.options.print_fps:
            print '  '.join("%6.1f" % (dt, ) for dt in self.fpss)

