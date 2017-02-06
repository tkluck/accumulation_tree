import os
from setuptools import setup, Extension

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'accumulation_tree',
    version = '0.2',
    description = 'Red/black tree with support for fast accumulation of values in a key range',
    author = 'Timo Kluck',
    author_email = 'tkluck@infty.nl',
    url='https://github.com/tkluck/accumulation_tree',
    long_description=read('README.md'),
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
    setup_requires=["cython"],
    packages=['accumulation_tree'],
    ext_modules = [
        Extension('accumulation_tree.accumulation_tree', ['accumulation_tree/accumulation_tree.pyx'])
    ],
)
