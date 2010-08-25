
from math import cos, sin

from euclid import Vector3

from ..util.vectors import round_down_to_int

def orbit(item, dt, time):
    item.position += Vector3(
        -sin(time),
        cos(time),
        0,
    ) * 0.01


class directed_motion(object):

    def __init__(self):
        self.delta = None
        self.next_move = None

    def __call__(self, item, dt, time):
        position = item.position

        if not self.delta and self.next_move:
            self.last_int_position = round_down_to_int(position)
            self.delta = self.next_move / 10.0
            print 'new: pos', position, 'int pos', self.last_int_position, 'next', self.next_move, 'delta', self.delta
            self.next_move = None

        if self.delta:
            item.position += self.delta
            int_position = round_down_to_int(position) 
            print 'last int', self.last_int_position, 'int', int_position, 'delta', self.delta
            if int_position != self.last_int_position:
                print 'done', item.position
                self.delta = None
            self.last_int_position = int_position
                
