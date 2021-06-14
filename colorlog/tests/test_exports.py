"""Test that `from colorlog import *` works correctly."""

from colorlog import *  # noqa


def test_exports():
    assert {
        "ColoredFormatter",
        "default_log_colors",
        "basicConfig",
        "root",
        "getLogger",
        "debug",
        "info",
        "warning",
        "error",
        "exception",
        "critical",
        "log",
        "exception",
    } < set(globals())
