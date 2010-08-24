from __future__ import division

from pyglet.gl import gl, glu


class ModelView(object):
    '''
    Manage modelview matrix, performing the MVC's 'view' parts of the 'camera'
    '''
    def __init__(self, camera):
        self.camera = camera

    def set_identity(self):
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

    def set_world(self):
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        position = self.camera.position
        look_at = self.camera.look_at
        glu.gluLookAt(
            position.x, position.y, position.z,
            look_at.x, look_at.y, look_at.z,
            0, 1, 0)

