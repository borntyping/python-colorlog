from distutils.core import setup
from colorlog import __version__

setup(
    name             = 'colorlog',
    version          = __version__,

    description      = 'Log formatting with colors!',
    long_description = open("README.rst").read(),

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/colorlog',
    license          = open("LICENCE.txt").read(),

    packages         = ['colorlog'],

    classifiers      = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
