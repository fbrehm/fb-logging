#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2021 Frank Brehm, Berlin
@license: GPL3
@summary: testing colored logging formatter
"""

import os
import sys
import logging

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger, pp

LOG = logging.getLogger('test_colored')


# =============================================================================
class TestColored(FbLoggingTestcase):

    # -------------------------------------------------------------------------
    def test_import_modules(self):

        LOG.info("Test importing module colored ...")

        LOG.debug("Importing fb_logging.colored ...")
        import fb_logging.colored

        LOG.debug("Version of fb_logging.colored: {!r}.".format(fb_logging.colored.__version__))

        LOG.debug("Checking available color keys ...")

        from fb_logging.colored import Colors
        colors = Colors.keys()
        if self.verbose >= 2:
            LOG.debug("Valid color names:\n{}".format(pp(colors)))

    # -------------------------------------------------------------------------
    def test_colorcode_4bit(self):

        LOG.info("Testing colored output 4 bit colors ...")

        from fb_logging.colored import Colors
        from fb_logging.colored import colorstr
        from fb_logging.colored import ColorNotFoundError, WrongColorTypeError

        msg = "Colored output"

        print('')
        for color in Colors.keys():
            LOG.debug("Testing color {clr!r} ({cls}) ...".format(clr=color, cls=color.__class__.__name__))
            try:
                print('{c!r}: {msg}'.format(c=color, msg=colorstr(msg, color)))
            except Exception as e:
                self.fail("Failed to generate colored string %r with %s: %s" % (
                    key, e.__class__.__name__, str(e)))

        print('')
        LOG.info("Testing combined colored output ...")
        print('')

        colors = (
            ('cyan',),
            ('green', 'strike'),
            ('dark_red', 'green_bg', 'underline'),
        )
        for color in colors:
            LOG.debug("Testing color {clr} ...".format(clr=pp(color)))
            try:
                print('{c}: {msg}'.format(c=pp(color), msg=colorstr(msg, color)))
            except Exception as e:
                self.fail("Failed to generate colored string %r with %s: %s" % (
                    key, e.__class__.__name__, str(e)))

        print('')
        LOG.info("Testing invalid colors ...")
        print('')

        wrong_colors = (
            None,
            False,
            { 2: 3},
            -4,
            'uhu',
        )
        for color in wrong_colors:
            LOG.debug("Testing wrong color {clr} ...".format(clr=pp(color)))
            with self.assertRaises((ColorNotFoundError, WrongColorTypeError)) as cm:
                msg = colorstr(msg, color)

            e = cm.exception
            LOG.debug("Got a {c}: {e}.".format(c=e.__class__.__name__, e=e))

    # -------------------------------------------------------------------------
    def test_colorcode_8bit(self):

        LOG.info("Testing colored output 8 bit colors ...")

        from fb_logging.colored import Colors
        from fb_logging.colored import colorstr
        from fb_logging.colored import ColorNotFoundError, WrongColorTypeError

        print('')
        LOG.info("Testing foreground colors ...")

        for i in list(range(256)):

            bg_color = 0
            modulus = i % 16
            if modulus < 8:
                bg_color = 15

            msg = (str(i) + ' ').rjust(5)
            out = Colors.colorize_8bit(msg, i, bg_color)
            if self.verbose:
                print(out, end='')
                if modulus == 15:
                    print()

        print('')
        LOG.info("Testing background colors ...")

        for i in list(range(256)):

            fg_color = 0
            modulus = i % 16
            if modulus < 8:
                fg_color = 15

            msg = (str(i) + ' ').rjust(5)
            out = Colors.colorize_8bit(msg, fg_color, i)
            if self.verbose:
                print(out, end='')
                if modulus == 15:
                    print()


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose)

    LOG.info("Starting tests ...")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestColored('test_import_modules', verbose))
    suite.addTest(TestColored('test_colorcode_4bit', verbose))
    suite.addTest(TestColored('test_colorcode_8bit', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list
