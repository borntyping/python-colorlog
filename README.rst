===========================
Log formatting with colors!
===========================

.. image:: http://img.shields.io/pypi/v/colorlog.svg?style=flat-square
	:target: https://pypi.python.org/pypi/colorlog
	:alt: colorlog on PyPI

.. image:: http://img.shields.io/pypi/l/colorlog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/colorlog
    :alt: colorlog on PyPI

.. image:: http://img.shields.io/travis/borntyping/python-colorlog/master.svg?style=flat-square
    :target: https://travis-ci.org/borntyping/python-colorlog
    :alt: Travis-CI build status for python-colorlog

.. image:: https://img.shields.io/github/issues/borntyping/python-colorlog.svg?style=flat-square
    :target: https://github.com/borntyping/python-colorlog/issues
    :alt: GitHub issues for python-colorlog

|

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

* `Source on GitHub <https://github.com/borntyping/python-colorlog>`_
* `Packages on PyPI <https://pypi.python.org/pypi/colorlog>`_

Codes
=====

The following values are made availible for use in the format string:

- ``{color}``, ``fg_{color}``, ``bg_{color}``: Foreground and background colors. The color names are ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``purple``, ``cyan`` and ``white``.
- ``bold``, ``bold_{color}``, ``fg_bold_{color}``, ``bg_bold_{color}``: Bold/bright colors.
- ``reset``: Clear all formatting (both foreground and background colors).
- ``log_color``: Return the color associated with the records level (from ``color_levels``).

Arguments
=========

``ColoredFormatter`` takes several arguments:

- ``format``: The format string used to output the message (required).
- ``datefmt``: An optional date format passed to the base class. See `logging.Formatter`_.
- ``reset``: Implicitly adds a color reset code to the message output, unless the output already ends with one. Defaults to ``True``.
- ``log_colors``: A mapping of record level names to color names. The defaults can be found in ``colorlog.default_log_colors``, or the below example.
- ``style``: Available on Python 3.2 and above. See `logging.Formatter`_.

Examples
========

.. image:: doc/example.png
	:alt: Example output

The following code creates a ColoredFormatter for use in a logging setup, passing each arguments defaults to the constructor::

	from colorlog import ColoredFormatter

	formatter = ColoredFormatter(
		"%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
		datefmt=None,
		reset=True,
		log_colors={
			'DEBUG':    'cyan',
			'INFO':     'green',
			'WARNING':  'yellow',
			'ERROR':    'red',
			'CRITICAL': 'red',
		}
	)

With `dictConfig`_
------------------

::

	logging.config.dictConfig({
		'formatters': {
			'colored': {
				'()': 'colorlog.ColoredFormatter',
				'format': "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
			}
		},

		...
	})

A full example dictionary can be found in ``tests/test_colorlog.py``.


With `fileConfig`_
------------------

::

	...

	[formatters]
	keys=color

	[formatter_color]
	class=colorlog.ColoredFormatter
	format=%(log_color)s%(levelname)-8s%(reset)s %(bg_blue)s[%(name)s]%(reset)s %(message)s from fileConfig
	datefmt=%m-%d %H:%M:%S

	...

An instance of ColoredFormatter created with those arguments will then be used by any handlers that are configured to use the ``color`` formatter.

A full example configuration can be found in ``tests/test_config.ini``.

Compatibility
=============

colorlog works on Python 2.6 and above, including Python 3.

On Windows, requires `colorama`_ to work properly. A dependancy on `colorama`_ is included as an optional package dependancy - depending on ``colorlog[windows]`` instead of ``colorlog`` will ensure it is included when installing.

Tests
=====

Tests similar to the above examples are found in ``tests/test_colorlog.py``.

`tox`_ will run the tests under all compatible python versions.

Licence
=======

Copyright (c) 2012 Sam Clements <sam@borntyping.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. _logging.Formatter: http://docs.python.org/3/library/logging.html#logging.Formatter
.. _dictConfig: http://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
.. _fileConfig: http://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
.. _tox: http://tox.readthedocs.org/
.. _colorama: https://pypi.python.org/pypi/colorama
