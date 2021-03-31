"""Wrappers around the logging module."""

from __future__ import absolute_import

import functools
import logging

from colorlog.colorlog import ColoredFormatter

BASIC_FORMAT = "%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"


def basicConfig(
    style="%",
    log_colors=None,
    reset=True,
    secondary_log_colors=None,
    format=BASIC_FORMAT,
    datefmt=None,
    **kwargs
):
    """Call ``logging.basicConfig`` and override the formatter it creates."""
    logging.basicConfig(**kwargs)
    logging._acquireLock()
    try:
        stream = logging.root.handlers[0]
        stream.setFormatter(
            ColoredFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                log_colors=log_colors,
                reset=reset,
                secondary_log_colors=secondary_log_colors,
            )
        )
    finally:
        logging._releaseLock()


def colorize(
    formatter=None,
    handler=None,
    logger=None,
    log_colors=None,
    secondary_log_colors=None,
    color_msg=True,
    replace=True,
    **kwargs
):
    """Colorize an existing formatter/handler/logger.

    If you want to be able to log events in a failsafe way even if 'colorlog'
    is not installed, you can use it as following:
        >>> import logging
        >>> logging.basicConfig(
        ...     format='%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        ...     datefmt='%H:%M:%S')
        >>> try:
        ...     import colorlog
        ... except ImportError
        ...     pass
        ... else:
        ...     colorlog.colorize()
    This will colorize the log, if 'colorlog' is available and keep the same
    format as given in 'logging.basicConfig()' without supplying the formats
    a second time to 'colorlog.basicConfig()'.

    Here is another, more fancy example:
        >>> import logging
        >>> logging.basicConfig(
        ...     format='%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        ...     datefmt='%H:%M:%S')
        >>> try:
        ...     import colorlog
        ... except ImportError:
        ...     pass
        ... else:
        ...     colorlog.colorize(
        ...         log_colors={
        ...             'DEBUG':    'cyan',
        ...             'INFO':     'green',
        ...             'WARNING':  'yellow',
        ...             'ERROR':    'red',
        ...             'CRITICAL': 'bold_red'},
        ...         secondary_log_colors={
        ...             'message': {
        ...                 'ERROR':    'red',
        ...                 'CRITICAL': 'bold_red'}},
        ...         color_msg=False,
        ...         levelname='log_color',
        ...         name='bold',
        ...         message='message_log_color')

    Args:
        formatter (logging.Formatter, optional):
            Use the given formatter as a basis. This takes precedence over
            'handler' and 'logger'.
            Defaults to 'None', which uses the formatter from the handler
            given in the 'handler' argument.
        handler (logging.Handler, optional):
            Use the formatter from this handler. This takes precedence over
            'logger'.
            Defaults to 'None', which uses the first handler of type
            'logging.StreamHandler' from the logger given in the 'logger'
            argument.
        logger (logging.Logger, optional):
            Use the formatter from the first 'logging.StreamHandler' found in
            this logger.
            Defaults to 'None', which uses the default root logger.
        log_colors (dict, optional):
            The primary colours passed to 'colorlog'.
            Defaults to 'None', using the default colours.
        secondary_log_colors(dict(dict), optional):
            The secondary colours passed to 'colorlog'.
            Defaults to 'None', meaning no secondary colors are defined.
        color_msg (bool, optional):
            If 'True', put a 'log_color' in front of the whole line. Set to
            'False', if you want to do something fancy with the keyword
            arguments (see '**kwargs').
        replace (bool, optional):
            If 'True', the formatter is replaced in the given or found handler.
        **kwargs:
            The keyword is the formatting token in the format string to be
            encapsulated with a colour, given as value, if the format is:
                '%(levelname)s:%(name)s:%(message)s'
            and this function is called with:
                levelname='log_color'
            the format string becomes:
                '%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s'
                 ^^^^^^^^^^^^^             ^^^^^^^^^

    Returns:
        logger.Formatter:
            The new, colorized formatter.

    """
    if formatter is None:

        if handler is None:

            if logger is None:
                # Use default logger
                logger = logging.getLogger()

            # Use first 'StreamHandler' as handler
            for handler in logger.handlers:
                if isinstance(handler, logging.StreamHandler):
                    break
            else:
                raise TypeError(
                    # f"No 'StreamHandler' found in logger '{logger}'.") # PY3
                    f"No 'StreamHandler' found in logger '%s'." % logger)

        # Use handler's formatter
        formatter = handler.formatter

    # Get the message and date formats
    fmt = handler.formatter._fmt
    datefmt = handler.formatter.datefmt

    # Encapsulate all format tokens between the supplied colour and '%(reset)s'
    for token, color in kwargs.items():
        # Find full token between % and s
        # We could use a regex for this, but don't want to load an extra module
        try:
            # Find the start
            # start = fmt.find(f'%({token})') # PY3
            start = fmt.find('%%(%s)' % token)
        except ValueError:
            # Ignore it
            continue
        try:
            # Find end of it starting at the end of '%(token)', hence the '+3'
            end = fmt.find('s', start + len(token) + 3)
        except ValueError:
            # Ignore it
            continue

        # Replace the token with its colour encapsulation
        fulltoken = fmt[start:end+1]
        #fmt = fmt.replace(fulltoken, f'%({color})s{fulltoken}%(reset)s') # PY3
        fmt = fmt.replace(
            fulltoken, f'%%(%s)s%s%%(reset)s' % (color, fulltoken))

    if color_msg:
        # Colorize the whole message
        # fmt = f'%(log_color)s{fmt}' # PY3
        fmt = f'%%(log_color)s%s' % fmt

    # Make the new colored formatter
    colored_formatter = ColoredFormatter(
        fmt,
        datefmt=datefmt,
        log_colors=log_colors,
        secondary_log_colors=secondary_log_colors)

    if replace:
        # Replace the default handler with the new colored version
        handler.setFormatter(colored_formatter)

    return colored_formatter


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
