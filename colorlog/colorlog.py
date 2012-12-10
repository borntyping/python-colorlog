"""	The ColoredFormatter class """

from __future__ import absolute_import

import logging

from colorlog.escape_codes import escape_codes

__all__ = ['escape_codes', 'default_log_colors', 'ColoredFormatter']

# The default colors to use for the debug levels
default_log_colors =  {
	'DEBUG':    'white',
	'INFO':     'green',
	'WARNING':  'yellow',
	'ERROR':    'red',
	'CRITICAL': 'bold_red',
}

class ColoredFormatter (logging.Formatter):
	"""	A formatter that allows colors to be placed in the format string, intended to help in creating prettier, more readable logging output. """

	def __init__ (self, format, datefmt=None, log_colors=default_log_colors, reset=True):
		"""
		:Parameters:
		- format (str): The format string to use
		- datefmt (str): Allow for special date formatting (if ommited, standard ISO8601 formatting applied by base class).
		- log_colors (dict): A mapping of log level names to color names
		- reset (bool): Implictly appends a reset code to all records unless set to False
		"""
		super(ColoredFormatter, self).__init__(format, datefmt)
		self.log_colors = log_colors
		self.reset = reset

	def format (self, record):
		# Add the color codes to the record
		record.__dict__.update(escape_codes)

		# If we recognise the level name,
		# add the levels color as `log_color`
		if record.levelname in self.log_colors:
			color = self.log_colors[record.levelname]
			record.log_color = escape_codes[color]

		# Format the message
		message = super(ColoredFormatter, self).format(record)

		# Add a reset code to the end of the message (if it wasn't explicitly added in format str)
		if self.reset and not message.endswith(escape_codes['reset']):
			message += escape_codes['reset']

		return message
