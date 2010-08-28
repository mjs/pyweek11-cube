from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from .model.item.gameitem import GameItem
from .model.item.player import Player
from .model.level import Level
from .model.world import World
from .model.move import Orbit
from .view.render import Render
from .util.vectors import origin, dist2_from_int_ords, EPSILON2


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
        self.player = Player(self.world)
        self.camera = GameItem(
            position=origin,
            look_at=self.player,
            update=Orbit((3,2,0)),
        )
        self.level = Level(self)
        self.load_next_level()

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

        for item in self.world:
            if hasattr(item, 'update'):
                item.update(item, dt, self.time)

        if self.player_at_exit():
            self.load_next_level()

        self.window.invalid = True


    def player_at_exit(self):
        items = self.world.collision.get_items(self.player.position)
        if any(hasattr(item, 'exit') for item in items):
            dist2_to_exit = dist2_from_int_ords(self.player.position)
            if dist2_to_exit < EPSILON2:
                return True
        return False


    def load_next_level(self):
        if not self.level.next(self.world):
            self.level.load(self.world, 1)


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

