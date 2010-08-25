
from __future__ import division

from euclid import Vector3

from pyglet.window import key 


class KeyHandler(object):

    def __init__(self, world, player):
        self.world = world
        self.player = player

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.player.update.next_move = Vector3(-1, 0 ,0)
        elif symbol == key.D:
            self.player.update.next_move = Vector3(1, 0 ,0)
        elif symbol == key.W:
            self.player.update.next_move = Vector3(0, 1 ,0)
        elif symbol == key.S:
            self.player.update.next_move = Vector3(0, -1 ,0)
            


