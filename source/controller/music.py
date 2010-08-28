
from os import listdir
from os.path import join
from random import choice

from pyglet import clock

from ..util import path


load = None
MediaPlayer = None


class Music(object):

    def __init__(self):
        self.current_source = None
        self.mediaplayer = None
        self.tracks = []


    def load(self):
        try:
            global load, MediaPlayer
            from pyglet import media
            load = media.load
            MediaPlayer = media.Player
            music_dir = join(path.DATA, 'music')
            self.tracks = sorted([
                join(music_dir, track)
                for track in listdir(music_dir)
            ])
            self.current_source = load(choice(self.tracks))
        except Exception:
            print "WARNING: can't start music"
            self.mediaplayer = None


    def play(self):
        self.mediaplayer = MediaPlayer()
        self.mediaplayer.volume = 0.45
        self.mediaplayer.eos_action = self.mediaplayer.EOS_LOOP
        self.mediaplayer.queue(self.current_source)

        # if we play music immediately, it stutters a little at the start
        # so schedule it to start a second from now
        clock.schedule_once(lambda _: self.mediaplayer.play(), 1)


    def toggle(self):
        if self.mediaplayer:
            if self.mediaplayer.playing:
                self.mediaplayer.pause()
            else:
                self.mediaplayer.play()

