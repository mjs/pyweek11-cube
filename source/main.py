from __future__ import division
import sys

from .util.options import Options
from .controller.gameloop import Gameloop


def run_game():
    options = Options(sys.argv)
    try:
        gameloop = Gameloop(options)
        gameloop.prepare(options)
        gameloop.run()
    finally:
        gameloop.stop()


def main():
    run_game()

