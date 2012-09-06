__version__ = '0.6'
__all__ = ['ColoredFormatter', 'CODES', 'DEFAULT_COLOR_LEVELS']

import logging

# The color names
colors = enumerate([
	'black',
	'red',
	'green',
	'yellow',
	'blue',
	'purple',
	'cyan',
	'white'
])

# The initial set of escape codes
CODES = {
	'reset': "\033[0m",
	'bold': "\033[1m",
}

# Generate color escape codes
FOREGROUND_PREFIX = 'fg_'
BACKGROUND_PREFIX = 'bg_'

for i, name in colors:
	CODES[FOREGROUND_PREFIX + name] = "\033[3%sm" % i
	CODES[BACKGROUND_PREFIX + name] = "\033[4%sm" % i

# The default colors to use
DEFAULT_COLOR_LEVELS =  {
	'DEBUG':    'cyan',
	'INFO':     'green',
	'WARNING':  'yellow',
	'ERROR':    'red',
	'CRITICAL': 'red',
}

class ColoredFormatter (logging.Formatter):
	"""
	A log record formatter providing color codes for terminal output,
	by providing additional values to the format string.
	"""
	
	def __init__ (self, format, reset=False, color_levels=DEFAULT_COLOR_LEVELS):
		"""
		format (str): The format string to use
		reset (bool): Implictly appends a reset code to all records unless set to False
		color_levels (dict): A mapping of logging level names to color names
		"""
		super(ColoredFormatter, self).__init__(format)
		
		#: Set to true to not place a reset code at the end of the message
		self.reset = reset
		
		#: A mapping of log level names to color names
		self.color_levels = color_levels
		
	def format (self, record):
		# Add the color codes to the dict
		record.__dict__.update(CODES)
		
		# If we recognise the level name, 
		# add the levels color as `fg_level` and `bg_level`
		if record.levelname in self.color_levels:
			color = self.color_levels[record.levelname]
			record.fg_level = CODES[FOREGROUND_PREFIX + color]
			record.bg_level = CODES[BACKGROUND_PREFIX + color]
		
		# Format the message
		message = super(ColoredFormatter, self).format(record)
		
		# Add a reset code to the end of the message
		if not self.reset:
			message += CODES['reset']
		
		return message

if __name__ == '__main__':
	logger = logging.getLogger('colorlog_test')
	logger.setLevel(logging.DEBUG)
	
	stream = logging.StreamHandler()
	stream.setLevel(logging.DEBUG)

	stream.setFormatter(ColoredFormatter("%(bold)s%(fg_level)s%(levelname)-8s%(reset)s %(bold)s%(fg_black)s%(name)s%(reset)s %(message)s"))

	logger.addHandler(stream)

	logger.debug('debug message')
	logger.info('info message')
	logger.warn('warn message')
	logger.error('error message')
	logger.critical('critical message')
