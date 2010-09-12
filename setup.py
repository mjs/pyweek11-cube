
from distutils.core import setup
from os import walk
from os.path import join, normpath

import py2exe


IGNORE_DIRS = ['.svn']
IGNORE_EXTENSIONS = ['.pyc', '.pyo']


def all_files(src):
    retval = []
    for (root, dirs, files) in walk(normpath(src)):
        dirs = filter(lambda d: d not in IGNORE_DIRS, dirs)
        files = filter(
            lambda f: not any(f.endswith(ext) for ext in IGNORE_EXTENSIONS),
            files)
        retval.append((root, [join(root, filename) for filename in files]))
    return retval


config = dict(
    console=[
        dict(
            script='run.py',
            # icon_resources=[(1, 'data\%s.ico' % (NAME,))],
        )
    ],
    data_files=
        all_files('data') +
        all_files(join('source', 'view', 'shaders')),
)

from pprint import pprint 
pprint(config)

setup(**config)

