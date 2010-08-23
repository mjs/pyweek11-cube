
import pyglet
from pyglet.gl import gl

from .projection import Projection


class Render(object):

    def __init__(self, window):
        self.projection = Projection(window)
        self.clock_display = pyglet.clock.ClockDisplay()


    def draw_world(self):
        self.projection.set_perspective(45)


    def draw_hud(self):
        self.projection.set_screen()
        gl.glDisableClientState(gl.GL_NORMAL_ARRAY)
        self.clock_display.draw()

