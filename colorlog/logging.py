"""Wrappers around the logging module."""

from __future__ import absolute_import

import functools
import logging

from colorlog.colorlog import ColoredFormatter

BASIC_FORMAT = "%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"


def basicConfig(style='%', log_colors=None, reset=True,
                secondary_log_colors=None, **kwargs):
    """Call ``logging.basicConfig`` and override the formatter it creates."""
    logging.basicConfig(**kwargs)
    logging._acquireLock()
    try:
        stream = logging.root.handlers[0]
        stream.setFormatter(
            ColoredFormatter(
                fmt=kwargs.get('format', BASIC_FORMAT),
                datefmt=kwargs.get('datefmt', None),
                style=style,
                log_colors=log_colors,
                reset=reset,
                secondary_log_colors=secondary_log_colors
            ))
    finally:
        logging._releaseLock()


def ensure_configured(func):
    """Modify a function to call ``basicConfig`` first if no handlers exist."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(logging.root.handlers) == 0:
            basicConfig()
        return func(*args, **kwargs)
    return wrapper


root = logging.root
getLogger = logging.getLogger
loggings = ['debug', 'info', 'warning', 'error', 'critical', 'log', 'exception']
for l in loggings:
    exec(l+' = ensure_configured(logging.'+l+')')

StreamHandler = logging.StreamHandler
