"""
Based on an example provided by Ricardo Reis.
https://github.com/ricardo-reis-1970/colorlog-YAML

This configures the `logging` module from a YAML file, and provides

"""

import logging.config
import pathlib

import yaml

logging.Formatter

def config():
    """
    Configure `logging` from a YAML file. You might adjust this function to provide the
    configuration path as an argument.
    """
    path = pathlib.Path(__file__).with_suffix('.yaml')
    logging.config.dictConfig(yaml.safe_load(path.read_text()))


if __name__ == '__main__':
    config()

    root = logging.getLogger()
    root.debug("Root logs debug example")
    root.info("Root logs written to console without colours")
    root.warning("Root logs warning")
    root.error("Root logs error")
    root.critical("Root logs critical")

    unknown = logging.getLogger('unknown')
    unknown.debug("Unknown logs debug example")
    unknown.info("Unknown logs propagated to root logger, and then console")
    unknown.warning("Unknown logs warning")
    unknown.error("Unknown logs error")
    unknown.critical("Unknown logs critical")

    application = logging.getLogger('application')
    application.debug("Application logs debug filtered by log level")
    application.info("Application logs written to console with colours and file")
    application.warning("Application logs not propagated to the root logger")
    application.error("Application logs error example")
    application.critical("Application logs critical example")

    example = logging.getLogger('example')
    example.debug("Example logs debug filtered by log level")
    example.info("Example logs configured to write to file")
    example.warning("Example logs propagated to the root logger, and then console")
    example.error("Example logs error example")
    example.critical("Example logs critical example")
