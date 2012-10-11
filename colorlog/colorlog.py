"""	The Formatter class """

import logging

from escape_codes import escape_codes

# The default colors to use for the debug levels
default_log_colors =  {
	'DEBUG':    'white',
	'INFO':     'green',
	'WARNING':  'yellow',
	'ERROR':    'red',
	'CRITICAL': 'bold_red',
}

class ColoredFormatter (logging.Formatter):
	"""
	A log record formatter providing color codes for terminal output,
	by providing additional values to the format string.
	"""

	def __init__ (self, format, log_colors=default_log_colors, reset=False):
		"""
		format (str): The format string to use
		reset (bool): Implictly appends a reset code to all records unless set to False
		log_colors (dict): A mapping of logging level names to color names
		"""
		super(ColoredFormatter, self).__init__(format)

		#: Set to true to not place a reset code at the end of the message
		self.reset = reset

		#: A mapping of log level names to color names
		self.log_colors = log_colors

	def format (self, record):
		# Add the color codes to the dict
		record.__dict__.update(escape_codes)

		# If we recognise the level name,
		# add the levels color as `fg_level` and `bg_level`
		if record.levelname in self.log_colors:
			color = self.log_colors[record.levelname]
			record.fg_log = escape_codes['fg_' + color]
			record.bg_log = escape_codes['bg_' + color]

		# Format the message
		message = super(ColoredFormatter, self).format(record)

		# Add a reset code to the end of the message
		if not self.reset:
			message += escape_codes['reset']

		return message
