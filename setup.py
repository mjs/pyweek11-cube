
from distutils.core import setup
from os import walk
from os.path import join, normpath

import py2exe


IGNORE_DIRS = ['.svn']
IGNORE_EXTENSIONS = ['.pyc', '.pyo']


def all_files(source, dest=None):
    retval = []
    for (root, dirs, files) in walk(normpath(source)):
        dirs = filter(lambda d: d not in IGNORE_DIRS, dirs)
        files = filter(
            lambda f: not any(f.endswith(ext) for ext in IGNORE_EXTENSIONS),
            files)
        if files:
            if dest is None:
                dest = root
            retval.append((dest, [join(root, filename) for filename in files]))
    return retval


config = dict(
    # window=
    console=[
        dict(
            script='run.py',
            # icon_resources=[(1, 'data\%s.ico' % (NAME,))],
        )
    ],
    data_files=
        all_files('..\lib\Microsoft.VC90.CRT', dest='Microsoft.VC90.CRT') +
        all_files('data') +
        all_files(join('source', 'view', 'shaders')),
    options=dict(
        py2exe=dict(
            # ascii=True, # breaks unicode
            # bundle_files=1, # breaks C extensions loaded at runtime
            dist_dir='dist', # customize to separate py2exe output from sdist
            dll_excludes=[
                # "pywintypes26.dll",
                # "pywintypes27.dll",
            ],
            # optimize=2,
            excludes=[
                # silence some warnings of missing modules
                # '_imaging_gif',
                # '_scproxy',
                # 'dummy.Process',
                # 'email',
                # 'email.utils',
                # 'email.Utils',
                # 'ICCProfile',
                # 'Image',

                # filter out unused .pyd files
                # '_ssl',
                # '_imaging',
                # '_hashlib',
                # 'pyexpat',
                # 'pyreadline',
                # 'win32api',
                # 'bz2',
                # '_socket',
                # '_multiprocessing',
                # 'win32pipe',
                # 'select',

                # filter out unused .pyo files in library.zip
                # 'difflib',
                # 'doctest',
                # 'pdb',
                # 'pyglet.window.xlib',
                # 'pyglet.window.carbon',
                # 'pyglet.window.carbon.constants',
                # 'pyglet.window.carbon.types',
                # 'unittest',
                # 'tarfile',
                # 'locale',
                # 'urllib',
                # 'cookielib',
                # 'optparse',
                # 'urllib2',
                # 'win32con',
                # 'pickle',
                # 'zipfile',
                # 'threading',
                # 'calendar',
                # 'subprocess',
            ],
        ),
    ),
    # zipfile=None,
)

from pprint import pprint 
pprint(config)

setup(**config)

