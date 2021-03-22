import logging

from colorlog import ColoredFormatter

logging.addLevelName(5, "TRACE")


def main():
    """Create and use a logger."""
    formatter = ColoredFormatter(log_colors={"TRACE": "yellow"})

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger("example")
    logger.addHandler(handler)
    logger.setLevel("TRACE")

    logger.log(5, "a message using a custom level")


if __name__ == "__main__":
    main()
