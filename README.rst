===========================
Log formatting with colors!
===========================

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

Usage
=====

``ColoredFormatter`` requires at minumum a format string, and takes two options - ``reset`` and ``color_levels``, which are shown using values equivalent to the defaults the following example.

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

Licence
=======
	
``colorlog`` is distributed under the MIT Licence.
