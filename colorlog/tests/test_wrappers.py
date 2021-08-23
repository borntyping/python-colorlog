"""Test the colorlog.wrappers module."""

import logging

import colorlog


def test_logging_module(test_logger):
    test_logger(logging)


def test_colorlog_module(test_logger):
    test_logger(colorlog)


def test_colorlog_basicConfig(test_logger):
    colorlog.basicConfig()
    test_logger(colorlog.getLogger())


def test_reexports():
    assert colorlog.root is logging.root
    assert colorlog.getLogger is logging.getLogger
    assert colorlog.StreamHandler is logging.StreamHandler

    assert colorlog.CRITICAL is logging.CRITICAL
    assert colorlog.FATAL is logging.FATAL
    assert colorlog.ERROR is logging.ERROR
    assert colorlog.WARNING is logging.WARNING
    assert colorlog.WARN is logging.WARN
    assert colorlog.INFO is logging.INFO
    assert colorlog.DEBUG is logging.DEBUG
    assert colorlog.NOTSET is logging.NOTSET


def test_wrappers():
    assert colorlog.debug is not logging.debug
    assert colorlog.info is not logging.info
    assert colorlog.warning is not logging.warning
    assert colorlog.error is not logging.error
    assert colorlog.critical is not logging.critical
    assert colorlog.log is not logging.log
    assert colorlog.exception is not logging.exception
