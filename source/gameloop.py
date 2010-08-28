from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from .model.item.gameitem import GameItem
from .model.item.player import Player
from .model.levels import populate
from .model.world import World
from .model.move import orbit
from .view.render import Render
from .util.vectors import origin


class Gameloop(object):

    def __init__(self, options):
        self.options = options
        self.window = None
        self.fpss = []
        self.time = 0.0


    def prepare(self, options):
        self.window = Window(
            fullscreen=options.fullscreen,
            vsync=not options.novsync,
            visible=False,
            resizable=True)
        self.window.on_draw = self.draw_window

        self.world = World()

        start_pos = populate(self.world, 1)

        self.player = Player(self.world)
        self.world.add(self.player, position=start_pos)

        self.camera = GameItem(
            position=origin,
            look_at=self.player,
            update=orbit,
        )
        self.world.add(self.camera)

        self.render = Render(self.world, self.window, self.camera)
        self.render.init()


    def run(self):
        pyglet.clock.schedule(self.update)
        self.window.set_visible()
        pyglet.app.run()


    def update(self, dt):
        if self.options.print_fps:
            self.fpss.append(1/max(1e-6, dt))
        dt = min(dt, 1 / 30)
        self.time += dt

        self.world.update(dt, self.time)
        self.window.invalid = True


    def draw_window(self):
        self.window.clear()
        self.render.draw_world()
        if self.options.display_fps:
            self.render.draw_hud()
        self.window.invalid = False
        return EVENT_HANDLED


    def stop(self):
        if self.window:
            self.window.close()
        if self.options.print_fps:
            print '  '.join("%6.1f" % (dt, ) for dt in self.fpss)

