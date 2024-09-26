from setuptools import setup, Extension

setup(
    packages=['accumulation_tree'],
    ext_modules = [
        Extension('accumulation_tree.accumulation_tree', ['accumulation_tree/accumulation_tree.pyx'])
    ],
)
