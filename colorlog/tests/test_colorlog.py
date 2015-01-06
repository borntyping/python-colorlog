"""Test the colorlog.colorlog module."""

import logging
import logging.config
import os.path
import sys

import pytest


def path(filename):
    """Return an absolute path to a file in the current directory."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def test_colored_formatter(create_and_test_logger):
    create_and_test_logger()


def test_custom_colors(create_and_test_logger):
    """Disable all colors and check no escape codes are output."""
    create_and_test_logger(
        log_colors={}, reset=False,
        validator=lambda line: '\x1b[' not in line)


def test_reset(create_and_test_logger):
    create_and_test_logger(
        reset=True, validator=lambda l: l.endswith('\x1b[0m'))


def test_no_reset(create_and_test_logger):
    create_and_test_logger(
        format="%(reset)s%(log_color)s%(levelname)s:%(name)s:%(message)s",
        reset=False,
        # Check that each line does not end with an escape code
        validator=lambda line: not line.endswith('\x1b[0m'))


def test_build_from_file(test_logger):
    logging.config.fileConfig(path("test_config.ini"))
    test_logger(logging.getLogger(), lambda l: ':test_config.ini' in l)


@pytest.mark.skipif(sys.version_info < (2, 7), reason="requires python2.7")
def test_build_from_dictionary(test_logger):
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format':
                    "%(log_color)s%(levelname)s:%(name)s:%(message)s:dict",
            }
        },
        'handlers': {
            'stream': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': 'DEBUG'
            },
        },
        'loggers': {
            '': {
                'handlers': ['stream'],
                'level': 'DEBUG',
            },
        },
    })
    test_logger(logging.getLogger(), lambda l: ':dict' in l)


@pytest.mark.skipif(sys.version_info < (3, 2), reason="requires python3.2")
def test_braces_style(create_and_test_logger):
    create_and_test_logger(style='{')


@pytest.mark.skipif(sys.version_info < (3, 2), reason="requires python3.2")
def test_template_style(create_and_test_logger):
    create_and_test_logger(style='$')
