"""
Tests for the colorlog library

Some tests are only loaded on Python 2.7 and above.
"""

from __future__ import absolute_import, print_function

from os.path import join, dirname, realpath
from sys import version_info
from unittest import TestCase, TestLoader, TextTestRunner

from logging import StreamHandler, DEBUG, getLogger
from logging.config import fileConfig

from colorlog import ColoredFormatter

class TestColoredFormatter (TestCase):
    logformat = "%(bg_black)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(bold_black)s%(name)s:%(reset)s%(message)s"
    datefmt = "%H:%M:%S"

    def example_log_messages (self, logger):
        """Passes if the code does not throw an exception"""
        logger.debug('a debug message')
        logger.info('an info message')
        logger.warning('a warning message')
        logger.error('an error message')
        logger.critical('a critical message')

    def test_basic (self):
        """Manually build the logger"""
        formatter = ColoredFormatter(self.logformat, datefmt=self.datefmt)

        stream = StreamHandler()
        stream.setLevel(DEBUG)
        stream.setFormatter(formatter)

        self.logger = getLogger('pythonConfig')
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(stream)

        self.example_log_messages(self.logger)

    def test_z_file_config (self):
        """Build the logger from a config file"""
        filename = join(dirname(realpath(__file__)), "test_config.ini")
        with open(filename, 'r') as f:
            fileConfig(f.name)
        self.example_log_messages(getLogger('fileConfig'))

if version_info > (2, 7):
    from unittest import skipUnless
    from logging.config import dictConfig

    class TestColoredFormatter (TestColoredFormatter):
        @skipUnless(version_info > (2, 7), "requires python 2.7 or above")
        def test_dict_config (self):
            """Build the logger from a dictionary"""
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
                        'class':        'logging.StreamHandler',
                        'formatter':    'colored',
                    },
                },

                'loggers':{
                    'dictConfig': {
                        'handlers':    ['stream'],
                        'level': 'DEBUG',
                    },
                },
            })

            self.example_log_messages(getLogger('dictConfig'))

        @skipUnless(version_info > (3, 2), "requires python 3.2 or above")
        def test_py3 (self):
            """Manually build the logger using {} style formatting"""
            formatter = ColoredFormatter("{bg_black}{asctime}{reset} {log_color}{levelname:8}{reset} {bold_black}{name}:{reset}{message}", datefmt=self.datefmt, style="{")

            stream = StreamHandler()
            stream.setLevel(DEBUG)
            stream.setFormatter(formatter)

            self.logger = getLogger('py3-formatting')
            self.logger.setLevel(DEBUG)
            self.logger.addHandler(stream)

            self.example_log_messages(self.logger)

if __name__ == '__main__':
    tests = TestLoader().loadTestsFromTestCase(TestColoredFormatter)
    result = TextTestRunner(verbosity=0).run(tests)
    exit(len(result.errors) + len(result.failures))
