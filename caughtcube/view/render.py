
import pyglet
from pyglet.gl import gl

from .modelview import ModelView
from .projection import Projection


class Render(object):

    def __init__(self, window, camera):
        self.projection = Projection(window)
        self.modelview = ModelView(camera)
        self.clock_display = pyglet.clock.ClockDisplay()


    def draw_world(self):
        self.projection.set_perspective(45)
        self.modelview.set_world()
        # TODO draw world glyphs


    def draw_hud(self):
        self.projection.set_screen()
        self.modelview.set_identity()
        gl.glDisableClientState(gl.GL_NORMAL_ARRAY)
        self.clock_display.draw()

