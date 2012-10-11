"""	Test the colorlog module """

from __future__ import print_function

import unittest, logging

import colorlog

class TestColoredFormatter (unittest.TestCase):
	logformat = "%(fg_log)s%(levelname)-8s%(reset)s %(fg_black)s%(name)s%(reset)s %(message)s"

	def setUp(self):
		formatter = colorlog.ColoredFormatter(self.logformat)

		stream = logging.StreamHandler()
		stream.setLevel(logging.DEBUG)
		stream.setFormatter(formatter)

		self.logger = logging.getLogger('colorlog')
		self.logger.setLevel(logging.DEBUG)
		self.logger.addHandler(stream)

	def test_log_messages (self):
		"""	Simply passes if the code does not throw an exception """
		self.logger.debug('debug message')
		self.logger.info('info message')
		self.logger.warn('warn message')
		self.logger.error('error message')
		self.logger.critical('critical message')

if __name__ == '__main__':
	unittest.main()
