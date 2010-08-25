from __future__ import division
from math import cos, sin

from euclid import Vector3
import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import Window

from .model.camera import Camera
from .model.player import Player
from .model.room import Room
from .model.world import World
from .util.vectors import origin
from .view.render import Render


class Gameloop(object):

    def __init__(self, options):
        self.options = options
        self.window = None
        self.fpss = []
        self.time = 0.0


    def prepare(self, options):
        self.window = Window(
            fullscreen=options.fullscreen,
            vsync=options.vsync,
            visible=False,
            resizable=True)
        self.window.on_draw = self.draw_window

        self.world = World()
        self.camera = Camera((2, 5, 10), origin)
        self.render = Render(self.world, self.window, self.camera)
        self.render.init()
        
        self.world.add(Room(32))
        self.player = Player()
        self.world.add(self.player)


    def run(self):
        pyglet.clock.schedule(self.update)
        self.window.set_visible()
        pyglet.app.run()


    def update(self, dt):
        if self.options.print_fps:
            self.fpss.append(1/max(1e-6, dt))
        dt = min(dt, 1 / 30)
        self.time += dt

        self.camera.position += Vector3(
            -sin(self.time),
            cos(self.time),
            0,
        ) * 0.01
        self.window.invalid = True


    def draw_window(self):
        self.window.clear()
        self.render.draw_world()
        if self.options.display_fps:
            self.render.draw_hud()
        return EVENT_HANDLED


    def stop(self):
        if self.window:
            self.window.close()
        if self.options.print_fps:
            print '  '.join("%6.1f" % (dt, ) for dt in self.fpss)

