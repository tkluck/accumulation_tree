import os
from setuptools import setup, Extension

setup(
    name = 'accumulation_tree',
    version = '0.5',
    description = 'Red/black tree with support for fast accumulation of values in a key range',
    author = 'Timo Kluck',
    author_email = 'tkluck@infty.nl',
    url='https://github.com/tkluck/accumulation_tree',
    long_description="""
A red/black tree which also stores partial aggregations at each node, making
getting aggregations of key range slices an O(log(N)) operation.
""",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    license='MIT',
    keywords='BST, data structure, accumulation',
    setup_requires=["cython"],
    packages=['accumulation_tree'],
    ext_modules = [
        Extension('accumulation_tree.accumulation_tree', ['accumulation_tree/accumulation_tree.pyx'])
    ],
)
