from __future__ import division
import sys

from .gameloop import Gameloop
from .options import Options
from .keyhandler import KeyHandler

def run_game():
    options = Options(sys.argv)
    try:
        gameloop = Gameloop(options)
        gameloop.prepare(options)

        keyhandler = KeyHandler(gameloop.world, gameloop.player)
        gameloop.window.push_handlers(keyhandler.on_key_press)

        gameloop.run()
    finally:
        gameloop.stop()


def main():
    run_game()

