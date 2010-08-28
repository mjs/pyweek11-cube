import sys

from .. import version


class Options(object):

    def __init__(self, argv):
        self.novsync = '--novsync' in argv
        self.fullscreen = '--fullscreen' in argv or '-f' in argv
        self.print_fps = '--print-fps' in argv
        self.display_fps = '--fps' in argv
        self.version = '--version' in argv

        if self.version:
            print version
            sys.exit()

