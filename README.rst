===========================
Log formatting with colors!
===========================

``colorlog.ColoredFormatter`` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, which is mostly useful when paired with a StreamHandler that is outputting to a terminal. This is accomplished by added a set of terminal color codes to the record before it is used to format the string.

A usage example, using the default color mapping::

	>>> from colorlog import ColoredFormatter
	>>> formatstring = "%(bg_level)s%(levelname)-8s%(reset)s %(blue)%(message)s"
	>>> levels = {
			'DEBUG':    'cyan',
			'INFO':     'green',
			'WARNING':  'yellow',
			'ERROR':    'red',
			'CRITICAL': 'red',
		}
	>>> ColoredFormatter(formatstring, reset=True, color_levels=levels)
