"""A logging formatter for colored output."""

import sys
import warnings

from colorlog.formatter import (
    ColoredFormatter,
    LevelFormatter,
    TTYColoredFormatter,
    default_log_colors,
)
from colorlog.wrappers import (
    CRITICAL,
    DEBUG,
    ERROR,
    FATAL,
    INFO,
    NOTSET,
    StreamHandler,
    WARN,
    WARNING,
    basicConfig,
    critical,
    debug,
    error,
    exception,
    getLogger,
    info,
    log,
    root,
    warning,
)

__all__ = (
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
    "StreamHandler",
    "LevelFormatter",
    "TTYColoredFormatter",
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARNING",
    "WARN",
    "INFO",
    "DEBUG",
    "NOTSET",
)

if sys.version_info < (3, 6):
    warnings.warn(
        "Colorlog requires Python 3.6 or above. Pin 'colorlog<5' to your dependencies "
        "if you require compatibility with older versions of Python. See "
        "https://github.com/borntyping/python-colorlog#status for more information."
    )
