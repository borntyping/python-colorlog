"""Test the colorlog.colorlog module."""

import io
import logging
import pickle
import sys
import unittest.mock

import pytest

import colorlog


def test_colored_formatter(create_and_test_logger):
    create_and_test_logger()


def test_custom_colors(create_and_test_logger):
    """Disable all colors and check no escape codes are output."""
    create_and_test_logger(
        log_colors={}, reset=False, validator=lambda line: "\x1b[" not in line
    )


def test_reset(create_and_test_logger):
    create_and_test_logger(reset=True, validator=lambda line: line.endswith("\x1b[0m"))


def test_no_reset(create_and_test_logger):
    create_and_test_logger(
        fmt="%(reset)s%(log_color)s%(levelname)s:%(name)s:%(message)s",
        reset=False,
        # Check that each line does not end with an escape code
        validator=lambda line: not line.endswith("\x1b[0m"),
    )


def test_secondary_colors(create_and_test_logger):
    expected = ":\x1b[31mtest_secondary_colors:\x1b[34m"
    create_and_test_logger(
        fmt=(
            "%(log_color)s%(levelname)s:"
            "%(name_log_color)s%(name)s:"
            "%(message_log_color)s%(message)s"
        ),
        secondary_log_colors={
            "name": {
                "DEBUG": "red",
                "INFO": "red",
                "WARNING": "red",
                "ERROR": "red",
                "CRITICAL": "red",
            },
            "message": {
                "DEBUG": "blue",
                "INFO": "blue",
                "WARNING": "blue",
                "ERROR": "blue",
                "CRITICAL": "blue",
            },
        },
        validator=lambda line: expected in line,
    )


def test_some_secondary_colors(create_and_test_logger):
    lines = create_and_test_logger(
        fmt="%(message_log_color)s%(message)s",
        secondary_log_colors={"message": {"ERROR": "red", "CRITICAL": "red"}},
    )
    # Check that only two lines are colored
    assert len([line for line in lines if "\x1b[31m" in line]) == 2


def test_percent_style(create_and_test_logger):
    create_and_test_logger(
        fmt="%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s", style="%"
    )


def test_braces_style(create_and_test_logger):
    create_and_test_logger(
        fmt="{log_color}{levelname}{reset}:{name}:{message}", style="{"
    )


def test_template_style(create_and_test_logger):
    create_and_test_logger(
        fmt="${log_color}${levelname}${reset}:${name}:${message}", style="$"
    )


class TestLevelFormatter:
    def test_level_formatter(self, create_and_test_logger):
        create_and_test_logger(
            formatter_class=colorlog.LevelFormatter,
            fmt={
                "DEBUG": "%(message)s",
                "INFO": "%(message)s",
                "WARNING": "%(message)s",
                "ERROR": "%(message)s",
                "CRITICAL": "%(message)s",
            },
        )

    def test_unlisted_level_uses_default(self):
        """A level missing from fmt must not raise; it uses the fallback."""
        logging.addLevelName(25, "NOTICE")
        formatter = colorlog.LevelFormatter(fmt={"INFO": "%(message)s"})
        record = logging.LogRecord(
            "test", 25, "path", 1, "a notice message", None, None
        )
        assert "a notice message" in formatter.format(record)

    def test_explicit_default_key(self):
        """A 'DEFAULT' entry overrides the fallback format for unlisted levels."""
        logging.addLevelName(25, "NOTICE")
        formatter = colorlog.LevelFormatter(
            fmt={
                "INFO": "%(message)s",
                "DEFAULT": "DEFAULT: %(message)s",
            }
        )
        record = logging.LogRecord(
            "test", 25, "path", 1, "a notice message", None, None
        )
        assert "DEFAULT: a notice message" in formatter.format(record)


def test_ttycolorlog(create_and_test_logger, monkeypatch):
    monkeypatch.setattr(sys.stderr, "isatty", lambda: True)
    create_and_test_logger(
        formatter_class=colorlog.TTYColoredFormatter,
        validator=lambda line: "\x1b[" in line,
        stream=sys.stderr,
    )


def test_ttycolorlog_notty(create_and_test_logger, monkeypatch):
    monkeypatch.setattr(sys.stderr, "isatty", lambda: False)
    create_and_test_logger(
        formatter_class=colorlog.TTYColoredFormatter,
        validator=lambda line: "\x1b[" not in line,
        stream=sys.stderr,
    )


if sys.version_info >= (3, 13):

    @pytest.mark.parametrize("tty", [True, False])
    def test_formatException(tty: bool, monkeypatch):
        stream = unittest.mock.Mock()
        stream.isatty = unittest.mock.Mock(return_value=tty)

        formatter = colorlog.ColoredFormatter(stream=stream)
        try:
            raise KeyError("test")
        except KeyError:
            ei = sys.exc_info()
            text = formatter.formatException(ei)

        assert ("\x1b[" in text) == tty

    @pytest.fixture
    def exception_record() -> logging.LogRecord:
        try:
            raise ValueError("example failure")
        except ValueError:
            return logging.LogRecord(
                "example", logging.ERROR, "example.py", 1, "failed", (), sys.exc_info()
            )

    @pytest.mark.parametrize(
        "plain_formatter",
        [
            logging.Formatter("%(message)s"),
            colorlog.ColoredFormatter("%(message)s", no_color=True),
            colorlog.ColoredFormatter("%(message)s", stream=io.StringIO()),
        ],
        ids=["stdlib", "no_color", "non_tty"],
    )
    @pytest.mark.parametrize("color_first", [True, False])
    def test_exception_colors_are_per_formatter(
        exception_record, plain_formatter, color_first
    ):
        colored_formatter = colorlog.ColoredFormatter("%(message)s", force_color=True)
        if color_first:
            colored = colored_formatter.format(exception_record)
            plain = plain_formatter.format(exception_record)
        else:
            plain = plain_formatter.format(exception_record)
            colored = colored_formatter.format(exception_record)

        assert "\x1b[" not in plain
        assert "\x1b[" in colored.split("\n", 1)[1]

    def test_exception_text_survives_record_forwarding(exception_record):
        colorlog.ColoredFormatter("%(message)s", force_color=True).format(
            exception_record
        )
        exception_record.exc_info = None
        forwarded = pickle.loads(pickle.dumps(exception_record))
        output = logging.Formatter("%(message)s").format(forwarded)

        assert "ValueError: example failure" in output
        assert "\x1b[" not in output

    @pytest.mark.parametrize("force_color", [True, False])
    def test_cached_exception_text_without_exc_info(exception_record, force_color):
        exception_record.exc_info = None
        exception_record.exc_text = "ValueError: remotely cached failure"
        formatter = colorlog.ColoredFormatter(
            "%(message)s", force_color=force_color, no_color=not force_color
        )

        assert formatter.format(exception_record).endswith(exception_record.exc_text)
        assert exception_record.exc_text == "ValueError: remotely cached failure"
