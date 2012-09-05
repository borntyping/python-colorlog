===========================
Log formatting with colors!
===========================

`colorlog.ColoredFormatter` is a formatter for use with pythons logging module.

It allows colors to be placed in the format string, mostly useful when paired with a StreamHandler that is outputting to a terminal.

This is accomplished by added a set of terminal color codes to the record before it is used to format the string. The codes are mostly in the format `fg_{colorname}` or `bg_{colorname}` (foreground and background colors). Also provided are `bold` (for bold output), `reset` (to reset all formatting), and `fg_level` / `bg_level`, which return the color associated with the records level (which is defined by either `DEFAULT_COLOR_LEVELS` or a user-provided dict (`color_levels`) containing a mapping of level names to color names.

The colors names are `black`, `red`, `green`, `yellow`, `blue`, `purple`, `cyan` and `white`.

A reset code is implictly appended to all messages unless `reset == False`.

A usage example, also showing the default color mapping::

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
