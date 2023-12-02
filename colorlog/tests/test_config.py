"""Test using colorlog with logging.config"""

import logging
import logging.config
import os.path


def path(filename):
    """Return an absolute path to a file in the current directory."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def test_build_from_file(test_logger):
    logging.config.fileConfig(path("test_config.ini"))
    test_logger(logging.getLogger(), lambda line: ":test_config.ini" in line)


def test_build_from_dictionary(test_logger):
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "colored": {
                    "()": "colorlog.ColoredFormatter",
                    "format": "%(log_color)s%(levelname)s:%(name)s:%(message)s:dict",
                }
            },
            "handlers": {
                "stream": {
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                    "level": "DEBUG",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["stream"],
                    "level": "DEBUG",
                },
            },
        }
    )
    test_logger(logging.getLogger(), lambda line: ":dict" in line)
