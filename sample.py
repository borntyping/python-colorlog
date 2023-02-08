import logging
import colorlog

fmt = "{log_color}{levelname} {name}: {message}"
colorlog.basicConfig(level=logging.DEBUG, style="{", format=fmt)

log = logging.getLogger()

log.warning("hello")
