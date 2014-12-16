"""Wrappers around the logging module"""

from __future__ import absolute_import

import functools
import logging

from colorlog.colorlog import ColoredFormatter

BASIC_FORMAT = "%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"


def basicConfig(**kwargs):
    """This calls basicConfig() and then overrides the formatter it creates"""
    logging.basicConfig(**kwargs)
    logging._acquireLock()
    try:
        stream = logging.root.handlers[0]
        stream.setFormatter(
            ColoredFormatter(kwargs.get('format', BASIC_FORMAT),
                             datefmt=kwargs.get('datefmt')))
    finally:
        logging._releaseLock()


def ensure_configured(func):
    """This ensures basicConfig is called if no handlers exist"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(logging.root.handlers) == 0:
            basicConfig()
        return func(*args, **kwargs)
    return wrapper

root = logging.root
getLogger = logging.getLogger
debug = ensure_configured(logging.debug)
info = ensure_configured(logging.info)
warning = ensure_configured(logging.warning)
error = ensure_configured(logging.error)
critical = ensure_configured(logging.critical)
log = ensure_configured(logging.log)
exception = ensure_configured(logging.exception)
