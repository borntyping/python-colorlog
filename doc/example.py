#!/usr/bin/env python
"""python-colorlog example."""

import logging
from colorlog import ColoredFormatter


def setup_logger():
    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red",
        },
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
