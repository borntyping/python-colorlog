===========================
Log formatting with colors!
===========================

.. image:: https://pypip.in/v/colorlog/badge.png
    :target: https://crate.io/packages/colorlog/
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/colorlog.png
   :target: https://travis-ci.org/borntyping/colorlog

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

Codes
=====

The following values are made availible for use in the format string:

  - ``fg_{colorname}``, ``bg_{colorname}``: Foreground and background colors. The colors names are ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``purple``, ``cyan`` and ``white``.
  - ``bold``: Bold output.
  - ``reset``: Clear all formatting (both foreground and background colors).
  - ``log_color``: Return the color associated with the records level (from ``color_levels``).
  
Arguments
=========

``ColoredFormatter`` takes several arguments:
	
	- ``format``: The format string used to output the message (required).
	- ``datefmt``: An optional date format passed to the base class. See `logging.Formatter`_.
	- ``reset``: Implicitly adds a color reset code to the message output, unless the output already ends with one. Defaults to ``True``.
	- ``log_colors``: A mapping of record level names to color names. The defaults can be found in ``colorlog.default_log_colors``, or the below example.
	- ``style``: Availible on Python 3.2 and above. See `logging.Formatter`_.

Examples
========

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

Tests
=====

Tests similar to the above examples are found in ``tests/test_colorlog.py``.
They require colorlog to be installed or otherwise available to Python.

`tox`_ will run the tests under all compatible python versions.

Licence
=======

colorlog is distributed under the MIT Licence.

.. _logging.Formatter: http://docs.python.org/3/library/logging.html#logging.Formatter
.. _dictConfig: http://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
.. _fileConfig: http://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
.. _tox: http://tox.readthedocs.org/
