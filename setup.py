from distutils.core import setup

setup(
    name             = 'colorlog',
    version          = '1.5',

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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
