
from __future__ import division

from pyglet.window import key 

from .util.vectors import (
    neg_x_axis, neg_y_axis, neg_z_axis, x_axis, y_axis, z_axis,
)

class KeyHandler(object):

    def __init__(self, world, player):
        self.world = world
        self.player = player

    def on_key_press(self, symbol, modifiers):
        if symbol == key.D:
            self.player.update.next_move = x_axis
        elif symbol == key.A:
            self.player.update.next_move = neg_x_axis
        elif symbol == key.S:
            self.player.update.next_move = z_axis
        elif symbol == key.W:
            self.player.update.next_move = neg_z_axis
        elif symbol == key.UP:
            self.player.update.next_move = y_axis
        elif symbol == key.DOWN:
            self.player.update.next_move = neg_y_axis
            


