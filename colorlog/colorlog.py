"""The ColoredFormatter class."""

from __future__ import absolute_import

import logging
import copy
import sys

from colorlog.escape_codes import escape_codes

__all__ = ('escape_codes', 'default_log_colors', 'ColoredFormatter')

# The default colors to use for the debug levels
default_log_colors = {
    'DEBUG':    'white',
    'INFO':     'green',
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'bold_red',
}

# The default format to use for each style
default_formats = {
    '%': "%(log_color)s%(levelname)s:%(name)s:%(message)s",
    '{': '{log_color}{levelname}:{name}:{message}',
    '$': '${log_color}${levelname}:${name}:${message}'
}


class ColoredFormatter(logging.Formatter):
    """
    A formatter that allows colors to be placed in the format string.

    Intended to help in creating more readable logging output.
    """

    def __init__(self, format=None, datefmt=None,
                 log_colors=None, reset=True, style='%'):
        """
        Set the format and colors the ColoredFormatter will use.

        The ``format``, ``datefmt`` and ``style`` args are passed on to the
        ``logging.Formatter`` constructor.

        :Parameters:
        - format (str): The format string to use
        - datefmt (str): A format string for the date
        - log_colors (dict):
            A mapping of log level names to color names
        - reset (bool):
            Implictly append a color reset to all records unless False
        - style ('%' or '{' or '$'):
            The format style to use. No meaning prior to Python 3.2.
        """
        if format is None:
            if sys.version_info > (3, 2):
                format = default_formats[style]
            else:
                format = default_formats['%']

        if sys.version_info > (3, 2):
            super(ColoredFormatter, self).__init__(format, datefmt, style)
        elif sys.version_info > (2, 7):
            super(ColoredFormatter, self).__init__(format, datefmt)
        else:
            logging.Formatter.__init__(self, format, datefmt)

        self.log_colors = (
            default_log_colors if log_colors is None else log_colors)
        self.reset = reset

    def format(self, record):
        """Format a message from a record object."""
        record = copy.copy(record)
        record.__dict__.update(escape_codes)

        # If we recognise the level name,
        # add the levels color as `log_color`
        if record.levelname in self.log_colors:
            color = self.log_colors[record.levelname]
            record.log_color = escape_codes[color]
        else:
            record.log_color = ""

        # Format the message
        if sys.version_info > (2, 7):
            message = super(ColoredFormatter, self).format(record)
        else:
            message = logging.Formatter.format(self, record)

        # Add a reset code to the end of the message
        # (if it wasn't explicitly added in format str)
        if self.reset and not message.endswith(escape_codes['reset']):
            message += escape_codes['reset']

        return message
