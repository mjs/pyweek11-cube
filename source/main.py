from __future__ import division
import logging
import sys

from . import version, name
from .util.options import Options
from .controller.gameloop import Gameloop


def run_game():
    logging.basicConfig(
        filename='%s-debug.log' % (name,),
        filemode='w',
        level=logging.DEBUG,
    )
    logging.debug('%s v%s' % (name, version,))

    options = Options(sys.argv)
    try:
        gameloop = Gameloop(options)
        gameloop.prepare(options)
        gameloop.run()
    finally:
        gameloop.stop()
        logging.debug('gameloop.stop')

    logging.debug('end of program')


def main():
    run_game()

