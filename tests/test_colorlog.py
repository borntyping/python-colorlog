"""	Test the colorlog module """

from __future__ import print_function

from os.path import join, dirname, realpath
from unittest import TestCase, main

from logging import DEBUG, StreamHandler, getLogger
from logging.config import fileConfig, dictConfig

from colorlog import ColoredFormatter

class TestColoredFormatter (TestCase):
	logformat = "%(bg_black)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(bold_black)s%(name)s:%(reset)s%(message)s"
	datefmt = "%H:%M:%S"
	
	def example_log_messages (self):
		"""	Simply passes if the code does not throw an exception """
		print()
		self.logger.debug('a debug message')
		self.logger.info('an info message')
		self.logger.warn('a warning message')
		self.logger.error('an error message')
		self.logger.critical('a critical message')

	def test_basic (self):
		formatter = ColoredFormatter(self.logformat, datefmt=self.datefmt)

		stream = StreamHandler()
		stream.setLevel(DEBUG)
		stream.setFormatter(formatter)

		self.logger = getLogger('root')
		self.logger.setLevel(DEBUG)
		self.logger.addHandler(stream)
		
		self.example_log_messages()
	
	def test_file_config (self):
		with open(join(dirname(realpath(__file__)), "test_config.ini"), 'r') as f:
			fileConfig(f.name)
		self.logger = getLogger('')
		self.example_log_messages()

	def test_dict_config (self):
		dictConfig({
			'version':1,
			
			'formatters': {
				'colored': {
					'()': 'colorlog.ColoredFormatter',
					'format': self.logformat + " from dictConfig",
					'datefmt': "%H:%M:%S",
				}
			},
			
			'handlers':{
				'stream': {
					'class':		'logging.StreamHandler',
					'formatter':	'colored',
				},
			},

			'loggers':{
				'root': {
					'handlers':	['stream'],
					'level': 'DEBUG',
				},
			},
		})
		
		self.logger = getLogger('root')
		self.example_log_messages()
		
if __name__ == '__main__':
	main()
