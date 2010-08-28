A game written for PyWeek #11, the 'write a game in Python in a week'
competition. pyweek.org

Run from the command line using:

    python -O run.py [options]

Where options are:

    --novsync, disable vsync
    --fullscreen or -f, run fullscreen instead of windowed
    --print-fps, print fps to stdout on exit
    --fps, display fps on screen
    --version, display version on stdout and exit

As always for pyglet / OpenGL programs, the -O flag is important, it can
greatly improve the framerate.


DEPENDENCIES
------------

To be able to run, first you'll need:

    Windows or Linux (maybe Macs too, I haven't tried)
    Python 2.6 or 2.7 (from python.org)
    Pyglet 1.1.4 (easy_install or pip works, or from pyglet.org)
        with AVBin if you want sound and music.

AVBin is included in the Windows binary download of Pyglet. Otherwise you'll
have to download it from here:
http://code.google.com/p/avbin/downloads/list


THE GAME
--------

You have been caught! Can you escape from this fiendish trandimensional puzzle
space?

Keys:
    W A S D - forward left right back
    Up Down - up down, when you are granted the ability to move vertically


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


THANKS
------

Thanks to both Alex Holkner and Richard Jones for pyglet, Euclid, and PyWeek,
which have transformed my hobbyist game coding. We all owe you, big time.

Thanks to Chris DeLeon, for advice, moral support, and examples of how to do it
right.

Music is I Wonder If God Was Sleeping (Transcendence Edit),
(cc) 2008 scottaltham
Licensed to the public under http://creativecommons.org/licenses/by-nc/3.0/
Verify at http://ccmixter.org/files/scottaltham/18129

