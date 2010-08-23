from __future__ import division

import sys

from . import version
from .gameloop import Gameloop


class Options(object):

    def __init__(self, argv):
        self.vsync = '--vsync' in argv
        self.fullscreen = '--fullscreen' in argv or '-f' in argv
        self.print_fps = '--print-fps' in argv
        self.display_fps = '--fps' in argv
        self.version = '--version' in argv

        if self.version:
            print version
            sys.exit()


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

