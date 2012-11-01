===========================
Log formatting with colors!
===========================

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

Usage
=====

``ColoredFormatter`` requires at minumum a format string, and takes two options - ``reset`` (implictly add a reset  code at the end of message strings, defaults to true) and ``color_levels`` (a mapping of record level names to color names, defaults to ``colorlog.DEFAULT_COLOR_LEVELS``).

::

	from colorlog import ColoredFormatter

	formatstring = "%(bg_level)s%(levelname)-8s%(reset)s %(blue)%(message)s"

	levels = {
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red',
	}

	formatter = ColoredFormatter(formatstring, reset=True, color_levels=levels)

The formatter can then be used in a normal ``logging`` setup.

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
