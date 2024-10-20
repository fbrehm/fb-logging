#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: Test script (and module) for unit tests on the colored log formatter.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2024 Frank Brehm, Berlin
@license: LGPL3
"""

import logging
import logging.handlers
import os
import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase
from general import get_arg_verbose
from general import init_root_logger
from general import pp
from general import terminal_can_colors

__app__ = 'test_colored_formatter'
LOG = logging.getLogger(__app__)


# =============================================================================
class TestColoredFormatter(FbLoggingTestcase):
    """Testcase for unit tests on fb_logging.colored."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

    # -------------------------------------------------------------------------
    def test_import(self):
        """Test importing fb_logging.colored."""
        LOG.info(self.get_method_doc())

        import fb_logging.colored

        LOG.debug('Version of fb_logging.colored: {!r}.'.format(fb_logging.colored.__version__))

    # -------------------------------------------------------------------------
    def test_init(self):
        """Test init of a ColoredFormatter object."""
        LOG.info(self.get_method_doc())

        from fb_logging.colored import ColoredFormatter

        try:
            formatter = ColoredFormatter(
                '%(name)s: %(message)s (%(filename)s:%(lineno)d)')
            LOG.debug('Formatter: {!r}'.format(formatter))
        except Exception as e:
            self.fail('Could not instatiate ColoredFormatter object with %s: %s' % (
                e.__class__.__name__, str(e)))

    # -------------------------------------------------------------------------
    @unittest.skipUnless(terminal_can_colors(), "Current terminal doesn't support colored output.")
    def test_formatted_logging(self):
        """Test logging of colorized log messages."""
        LOG.info(self.get_method_doc())

        from fb_logging.colored import ColoredFormatter

        format_str = self.appname + ' [%(asctime)s]: %(name)s(%(lineno)d) %(funcName)s() '
        format_str += '%(levelname)s - %(message)s'

        msgs = (
            (logging.DEBUG, 'This is a DEBUG message.'),
            (logging.INFO, 'This is a INFO message.'),
            (logging.WARNING, 'This is a WARNING message.'),
            (logging.ERROR, 'This is a ERROR message.'),
            (logging.CRITICAL, 'This is a CRITICAL message.'),
        )

        bright_fmt = ColoredFormatter(format_str)
        LOG.debug('Bright formatter: {!r}'.format(bright_fmt))
        bright_handler = logging.StreamHandler(sys.stderr)
        bright_handler.setLevel(logging.DEBUG)
        bright_handler.setFormatter(bright_fmt)

        if self.verbose > 1:
            LOG.debug("Used color levels in bright mode:\n" + pp(bright_fmt.level_color))

        dark_fmt = ColoredFormatter(format_str, dark=True)
        LOG.debug('Dark formatter: {!r}'.format(dark_fmt))
        dark_handler = logging.StreamHandler(sys.stderr)
        dark_handler.setLevel(logging.DEBUG)
        dark_handler.setFormatter(dark_fmt)

        if self.verbose > 1:
            LOG.debug("Used color levels in dark mode:\n" + pp(dark_fmt.level_color))

        tst_logger = logging.getLogger('color_tester')
        tst_logger.addHandler(bright_handler)
        tst_logger.addHandler(dark_handler)

        for token in msgs:
            lvl = token[0]
            msg = token[1]

            if self.verbose >= 1:
                print()
            LOG.info("Logging with level {!r}.".format(lvl))
            tst_logger.log(lvl, msg)


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose, __app__)

    LOG.info('Starting tests ...')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestColoredFormatter('test_import', verbose))
    suite.addTest(TestColoredFormatter('test_init', verbose))
    suite.addTest(TestColoredFormatter('test_formatted_logging', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list
