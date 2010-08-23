from __future__ import division
import sys

from .gameloop import Gameloop
from .options import Options


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

