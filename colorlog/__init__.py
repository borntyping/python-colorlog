"""A logging formatter for colored output."""

from __future__ import absolute_import

import sys
import warnings

from colorlog.colorlog import (
    escape_codes,
    default_log_colors,
    ColoredFormatter,
    LevelFormatter,
    TTYColoredFormatter,
)

from colorlog.logging import (
    basicConfig,
    root,
    getLogger,
    log,
    debug,
    info,
    warning,
    error,
    exception,
    critical,
    StreamHandler,
)

__all__ = (
    "ColoredFormatter",
    "default_log_colors",
    "escape_codes",
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
)

if sys.version_info < (3, 5):
    warnings.warn(
        "Colorlog 6.0.0 will require Python 3.5 or above. Pin 'colorlog<5' to your "
        "dependencies if you require compatibility with older versions of Python. See "
        "https://github.com/borntyping/python-colorlog#status for more information."
    )
