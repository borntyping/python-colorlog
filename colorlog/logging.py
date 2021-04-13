"""Wrappers around the logging module."""

from __future__ import absolute_import

import functools
import logging
import typing

from colorlog.colorlog import ColoredFormatter, LogColors, SecondaryLogColors

BASIC_FORMAT = "%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"


def basicConfig(
    style: str = "%",
    log_colors: typing.Optional[LogColors] = None,
    reset: bool = True,
    secondary_log_colors: typing.Optional[SecondaryLogColors] = None,
    format: str = BASIC_FORMAT,
    datefmt: typing.Optional[str] = None,
    **kwargs
) -> None:
    """Call ``logging.basicConfig`` and override the formatter it creates."""
    logging.basicConfig(**kwargs)
    logging._acquireLock()  # type: ignore
    try:
        handler = logging.root.handlers[0]
        handler.setFormatter(
            ColoredFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                log_colors=log_colors,
                reset=reset,
                secondary_log_colors=secondary_log_colors,
                stream=kwargs.get("stream", None),
            )
        )
    finally:
        logging._releaseLock()  # type: ignore


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
debug = ensure_configured(logging.debug)
info = ensure_configured(logging.info)
warning = ensure_configured(logging.warning)
error = ensure_configured(logging.error)
critical = ensure_configured(logging.critical)
log = ensure_configured(logging.log)
exception = ensure_configured(logging.exception)

StreamHandler = logging.StreamHandler
