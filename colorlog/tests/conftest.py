"""Fixtures that can be used in other tests."""

import inspect
import logging
import sys

import pytest

import colorlog


class TestingStreamHandler(logging.StreamHandler):
    """Raise errors to be caught by py.test instead of printing to stdout."""

    def handleError(self, record):
        _type, value, _traceback = sys.exc_info()
        raise value


def assert_log_message(capsys, log_function, message, *args):
    """Call a log function and check the message has been output."""
    log_function(message, *args)
    out, err = capsys.readouterr()
    # Print the output so that py.test shows it when a test fails
    print(err, end="", file=sys.stderr)
    # Assert the message send to the logger was output
    assert message % args in err, "Log message not output to STDERR"
    return err


@pytest.fixture()
def reset_loggers():
    logging.root.handlers = list()
    logging.root.setLevel(logging.DEBUG)


@pytest.fixture()
def test_logger(reset_loggers, capsys):
    def function(logger, validator=None):
        lines = [
            assert_log_message(capsys, logger.debug, "a debug message %s", 1),
            assert_log_message(capsys, logger.info, "an info message %s", 2),
            assert_log_message(capsys, logger.warning, "a warning message %s", 3),
            assert_log_message(capsys, logger.error, "an error message %s", 4),
            assert_log_message(capsys, logger.critical, "a critical message %s", 5),
        ]

        if validator is not None:
            for line in lines:
                valid = validator(line.strip())
                assert valid, f"{line.strip()!r} did not validate"

        return lines

    return function


@pytest.fixture()
def create_and_test_logger(test_logger):
    def function(*args, **kwargs):
        validator = kwargs.pop("validator", None)
        formatter_cls = kwargs.pop("formatter_class", colorlog.ColoredFormatter)

        formatter = formatter_cls(*args, **kwargs)

        stream = TestingStreamHandler(stream=sys.stderr)
        stream.setLevel(logging.DEBUG)
        stream.setFormatter(formatter)

        logger = logging.getLogger(inspect.stack()[1][3])
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stream)

        return test_logger(logger, validator)

    return function
