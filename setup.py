#!/usr/bin/python

from setuptools import setup, find_packages
from colorlog import __version__, __doc__

setup(
    name             = 'colorlog',
    description      = 'Log formatting with colors!',
    long_description = open("README.rst").read(),
    version          = __version__,
    license          = 'LICENSE.txt',
    
    py_modules       = ['colorlog'],

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/colorlog',
)
