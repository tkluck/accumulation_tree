import os
from distutils.core import setup, Extension

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

have_cython = False
try:
    from Cython.Distutils import build_ext
    have_cython = True
except ImportError:
    from distutils.command.build_ext import build_ext

ext_modules = []
if have_cython:
    ext_modules.append( Extension('accumulation_tree.accumulation_tree', ['accumulation_tree/accumulation_tree.pyx']) )
else:
    ext_modules.append( Extension('accumulation_tree.accumulation_tree', ['accumulation_tree/accumulation_tree.c']) )


setup(
    name = 'accumulation_tree',
    version = '0.1',
    description = 'Red/black tree with support for fast accumulation of values in a key range',
    author = 'Timo Kluck',
    author_email = 'tkluck@infty.nl',
    url='https://github.com/tkluck/accumulation_tree',
    packages=['accumulation_tree'],
    long_description=read('README.md'),
    install_requires=['bintrees'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    license='GPLv3+',
    keywords='BST, data structure, accumulation',
    py_modules = ["accumulation_tree"],
    ext_modules = ext_modules,
    cmdclass={'build_ext': build_ext},
)

