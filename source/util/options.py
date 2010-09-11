import sys

from .. import version


class Options(object):

    def __init__(self, argv):
        self.novsync = '--novsync' in argv
        self.fullscreen = '--window' not in argv and '-w' not in argv
        self.print_fps = '--print-fps' in argv
        self.display_fps = '--fps' in argv
        self.version = '--version' in argv

        if self.version:
            print version
            sys.exit()

