#!/usr/bin/python

from setuptools import setup, find_packages
from colorlog import __version__, __doc__

setup(
    name             = 'colorlog',
    description      = 'Log formatting with colors!',
    long_description = __doc__,
    version          = __version__,

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/colorlog',
    
    py_modules       = ['colorlog'],
)
