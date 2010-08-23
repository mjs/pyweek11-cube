from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from .view.render import Render
from .model.world import World
from .model.gameitem import GameItem


class Gameloop(object):

    def __init__(self, options):
        self.options = options
        self.window = None
        self.fpss = []


    def prepare(self, options):
        self.world = World()
        self.world.add(GameItem())

        self.window = Window(
            fullscreen=options.fullscreen,
            vsync=options.vsync,
            visible=False,
            resizable=True)
        self.window.on_draw = self.draw_window

        self.render = Render(self.window)


    def run(self):
        pyglet.clock.schedule(self.update)
        self.window.set_visible()
        pyglet.app.run()


    def update(self, dt):
        if self.options.print_fps:
            self.fpss.append(1/max(1e-6, dt))
        dt = min(dt, 1 / 30)

        self.window.invalid = True


    def draw_window(self):
        self.window.clear()
        # draw world

        if self.options.display_fps:
            self.render.draw_hud()

        return EVENT_HANDLED


    def stop(self):
        if self.window:
            self.window.close()

        if self.options.print_fps:
            print '  '.join("%6.1f" % (dt, ) for dt in self.fpss)

