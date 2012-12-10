"""	Test the colorlog module """

from __future__ import print_function

from sys import version_info

from os.path import join, dirname, realpath
from unittest import skipUnless, TestCase, main, skip

import logging
from logging import DEBUG, StreamHandler, getLogger
from logging.config import fileConfig, dictConfig

from colorlog import ColoredFormatter

class TestColoredFormatter (TestCase):
	logformat = "%(bg_black)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(bold_black)s%(name)s:%(reset)s%(message)s"
	datefmt = "%H:%M:%S"

	def example_log_messages (self, logger):
		"""	Simply passes if the code does not throw an exception """
		print()
		logger.debug('a debug message')
		logger.info('an info message')
		logger.warn('a warning message')
		logger.error('an error message')
		logger.critical('a critical message')
	
	def test_basic (self):
		formatter = ColoredFormatter(self.logformat, datefmt=self.datefmt)

		stream = StreamHandler()
		stream.setLevel(DEBUG)
		stream.setFormatter(formatter)

		self.logger = getLogger('basic')
		self.logger.setLevel(DEBUG)
		self.logger.addHandler(stream)
		
		self.example_log_messages(self.logger)

	def test_dict_config (self):
		dictConfig({
			'version':1,
			
			'formatters': {
				'colored': {
					'()': 'colorlog.ColoredFormatter',
					'format': self.logformat,
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
				'dict': {
					'handlers':	['stream'],
					'level': 'DEBUG',
				},
			},
		})
		
		self.example_log_messages(getLogger('dict'))
	
	@skipUnless(version_info > (3, 2), "requires python 3.2 or above")
	def test_py3 (self):		
		formatter = ColoredFormatter("{bg_black}{asctime}{reset} {log_color}{levelname:8}{reset} {bold_black}{name}:{reset}{message}", datefmt=self.datefmt, style="{")

		stream = StreamHandler()
		stream.setLevel(DEBUG)
		stream.setFormatter(formatter)

		self.logger = getLogger('py3')
		self.logger.setLevel(DEBUG)
		self.logger.addHandler(stream)
		
		self.example_log_messages(self.logger)

	def test_z_file_config (self):
		filename = join(dirname(realpath(__file__)), "test_config.ini")
		with open(filename, 'r') as f:
			fileConfig(f.name)
		self.example_log_messages(getLogger('file'))
		
if __name__ == '__main__':
	main()
