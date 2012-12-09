===========================
Log formatting with colors!
===========================

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

Usage
=====

From Python
-----------

``ColoredFormatter`` requires at minumum a format string, and takes several options - ``datefmt`` (an optional date format string passed to base class), ``reset`` (implictly add a reset  code at the end of message strings, defaults to true), and ``log_colors`` (a mapping of record level names to color names, defaults to ``colorlog.default_log_colors``).

::

	from colorlog import ColoredFormatter

	formatstring = "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"

	levels = {
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red',
	}

	formatter = ColoredFormatter(formatstring, reset=True, color_levels=levels)

The formatter can then be used in a normal ``logging`` setup.

From Configuration File
-----------------------

The ``ColoredFormatter`` may also be instantiated. from a standard logging (INI-style) configuration file.  Notably, it will only be passed the format and datefmt parameters by the python logging format initializer (all other params will be default).

::
	[formatter_color]
	format=%(asctime)s,%(msecs)03d %(levelname)-8s %(log_color)s%(threadName)s %(message)s
	datefmt = %m-%d %H:%M:%S
	class = colorlog.ColoredFormatter

The formatter will then be used by any handlers that are configured to use the ``color`` logger (for example above).

Codes
=====

The following values are made availible for use in the format string:

  - ``fg_{colorname}``, ``bg_{colorname}``: Foreground and background colors. The colors names are ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``purple``, ``cyan`` and ``white``.
  - ``bold``: Bold output.
  - ``reset``: Clear all formatting (both foreground and background colors).
  - ``log_color``: Return the color associated with the records level (from ``color_levels``).

Compatibility
=============

``colorlog`` should work with both Python 2 and 3. At a minimum, it's been tested on Python 2.7 and 3.2.

Licence
=======

``colorlog`` is distributed under the MIT Licence.
