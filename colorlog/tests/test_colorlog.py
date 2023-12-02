"""Test the colorlog.colorlog module."""

import sys

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
