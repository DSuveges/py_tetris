from distutils.core import setup

# This script defines the installation and packaging properties for the python packages
# included in this repository

setup(
    name='py-tetris',
    version='0.1',
    packages=['modules'],
    entry_points={
        "console_scripts": ['py-tetris = tetris:main']
    },
    url='https://github.com/DSuveges/py_tetris',
    license='MIT',
    author='Daniel Suveges',
    author_email='dsuveges@ebi.ac.uk',
    description='A simple tetris implementation in Python using pygame',
)
