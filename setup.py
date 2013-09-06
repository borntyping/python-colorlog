from setuptools import setup

setup(
    name             = 'colorlog',
    version          = '2.0.0',

    description      = 'Log formatting with colors!',
    long_description = open("README.rst").read(),

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/python-colorlog',
    license          = 'MIT License',

    packages         = ['colorlog'],

    classifiers      = [
        'Development Status :: 5 - Production/Stable',
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
        'Programming Language :: Python :: 3.3',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
