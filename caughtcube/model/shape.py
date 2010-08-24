
from itertools import repeat

from euclid import Vector3

from ..util.color import Color



class Face(object):
    '''
    A single flat face that forms part of a Shape.
    '''
    def __init__(self, indices, color, vertices):
        self.indices = indices
        self.color = color
        self.vertices = vertices
        self.normal = self.get_normal()


    def get_normal(self):
        '''
        Return the unit normal vector (at right angles to) this face.
        Note that the direction of the normal will be reversed if the
        face's winding is reversed.
        '''
        v0 = self.vertices[self.indices[0]]
        v1 = self.vertices[self.indices[1]]
        v2 = self.vertices[self.indices[2]]
        a = v0 - v1
        b = v2 - v1
        normal = b.cross(a)
        normal.normalize()
        return normal


    def tessellate(self):
        '''
        Return this face tesselated into a list of triangular faces, expressed
        as integer indices. The triangles will be wound in the same direction
        as the original poly. Does not work for concave faces.
        e.g. Face(verts, [0, 1, 2, 3, 4]) -> [[0, 1, 2], [0, 2, 3], [0, 3, 4]]
        '''
        return (
            [self.indices[0], self.indices[index], self.indices[index + 1]]
            for index in xrange(1, len(self.indices) - 1)
        )



class Shape(object):
    '''
    Defines a polyhedron, a 3D shape with flat faces and straight edges.
    Each vertex defines a point in 3d space. Each face is a list of integer
    indices into the vertex array, forming a coplanar convex ring defining the
    face's edges. Each face has its own color.
    '''    
    def __init__(self, vertices, faces, colors):

        # sanity checks
        len_verts = len(vertices)
        for face in faces:
            assert len(face) >= 3
            for index in face:
                assert 0 <= index < len_verts

        # convert vertices from tuple to Vector3 if required
        if len(vertices) > 0 and not isinstance(vertices[0], Vector3):
            vertices = [Vector3(*v) for v in vertices]

        # if given one color instead of a sequence of them,
        # then construct a sequence if identical colors out of it
        if isinstance(colors, Color):
            colors = repeat(colors)

        self.vertices = vertices
        self.faces = [
            Face(face, color, vertices)
            for face, color in zip(faces, colors)
        ]

