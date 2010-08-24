A game written for PyWeek #11, the 'write a game in Python in a week'
competition. pyweek.org

Run from the command line using:

    python -O run.py [options]

Where options are:

    -f --fullscreen: Run fullscreen, at current desktop resolution, instead of
                     in a window.
    
As always for pyglet / OpenGL programs, the -O flag is important, it can
greatly improve the framerate.


DEPENDENCIES
------------

To be able to run, first you'll need:

    Windows or Linux (maybe Macs too, I haven't tried)
    Python 2.6 or 2.7 (from python.org)
    Pyglet 1.1.4 (easy_install or pip works, or from pyglet.org)

The version numbers for everything except Python probably aren't crucial, but
those are the versions I'm running.


THE GAME
--------

You have been caught! Can you escape from this fiendish trandimensional puzzle
space?

Keys:
    W A S D - forward left right back
    Up Down - up down
    Tab - switch camera view


DEVELOPMENT
-----------

As I write, there are no tests. If I add any, then I'll be using:

    unittest2 (only required for Python2.6, is built in to Python2.7)
    nose

Run tests using the command line 'nosetests'. Nose is just used for test
discovery (unittest2 discovery has some wrinkles for me)

Also I have some simple commands stored in a Makefile, which I run under Linux
or under Windows with Cygwin binaries on the PATH. If you're on Windows but
don't have make or Cygwin, open up the Makefile. The commands in there are
generally simple, hopefully you can figure out how to do the same thing on your
own system.


PROFILING
---------

For profiling, I'm using the standard library cProfile, with 3rd party tool
'RunSnakeRun' to draw the output graphically.

    make profile

will run the script under the profiler, then run RunSnakeRun on the output.

RunSnakeRun is installed using: ``easy_install RunSnakeRun`` (or pip) or
download from:

 * http://www.vrplumber.com/programming/runsnakerun/

RunSnakeRun also needs:

 * SquareMap: ``easy_install SquareMap`` (or pip)
 * wxPython from http://www.wxpython.org/download.php#binaries

Currently runs under Windows at 60fps on my modest 2005-era Thinkpad T60 laptop
(ATI Radeon X1400).


DESIGN NOTES
------------

The play area consists of a single cuboid rooms, about 20x20x10 high.

The player moves an axis aligned unit cube around on the floor of this volume.

Like all things in the world, the player moves in straight lines along the
axes, and can only come to rest or change direction at integer ordinates.

There is an exit in the room, defined as a unit cube volume, although this
will initially be embedded in a wall, just exposing a single face. This face
is black, bearing the word EXIT in tiny letters (a la gauntlet). When the
player cube occupies the same position as the exit cube, the player has
escaped the current room, and moves on to the next.

Obstacles:
 * The player can normally only move on the floor, so raised walls form a maze.


THANKS
------

Thanks to both Alex Holkner and Richard Jones for pyglet, Euclid, and PyWeek,
which have transformed my hobbyist game coding. We all owe you, big time.

Thanks to Chris DeLeon, for advice, moral support, and examples of how to do it
right.

