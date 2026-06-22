#!/usr/bin/env python
"""python-colorlog example."""

import logging
from colorlog import ColoredFormatter


def setup_logger():
    """Return a logger with a ColoredFormatter using the default values for
    each argument.
    """
    formatter = ColoredFormatter(
        fmt="%(log_color)s%(levelname)s:%(name)s:%(message)s",
        datefmt=None,
        style='%',
        validate=True,
        defaults=None,
        reset=True,
        log_colors={
            "DEBUG": "white",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
        secondary_log_colors={},
        stream=None,
        no_color=False,
        force_color=False
    )

    logger = logging.getLogger("example")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


def main():
    """Create and use a logger."""
    logger = setup_logger()

    logger.debug("a debug message")
    logger.info("an info message")
    logger.warning("a warning message")
    logger.error("an error message")
    logger.critical("a critical message")


if __name__ == "__main__":
    main()
