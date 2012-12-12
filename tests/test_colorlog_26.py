"""	Test the colorlog module """

from sys import version_info

from os.path import join, dirname, realpath
from unittest import TestCase, main

from logging import StreamHandler, DEBUG, getLogger
from logging.config import fileConfig

from colorlog import ColoredFormatter

class TestColoredFormatter27 (TestCase):
	logformat = "%(bg_black)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(bold_black)s%(name)s:%(reset)s%(message)s"
	datefmt = "%H:%M:%S"

	def example_log_messages (self, logger):
		"""	Simply passes if the code does not throw an exception """
		print
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

	def test_z_file_config (self):
		filename = join(dirname(realpath(__file__)), "test_config.ini")
		with open(filename, 'r') as f:
			fileConfig(f.name)
		self.example_log_messages(getLogger('file'))
		
if __name__ == '__main__':
	main()
