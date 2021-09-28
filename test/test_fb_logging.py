#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2021 Frank Brehm, Berlin
@license: GPL3
@summary: test script (and module) for unit tests on logging objects
'''

import os
import sys
import logging
import logging.handlers

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger

LOG = logging.getLogger('test_fb_logging')


# =============================================================================
class TestFbLogging(FbLoggingTestcase):

    # -------------------------------------------------------------------------
    def test_import_modules(self):

        LOG.info("Test importing main module ...")

        LOG.debug("Importing fb_logging ...")
        import fb_logging

        LOG.debug("Version of fb_logging: {!r}.".format(fb_logging.__version__))

    # -------------------------------------------------------------------------
    def test_use_unix_syslog_handler(self):

        LOG.info("Testing fb_logging.use_unix_syslog_handler() ...")

        os_name = os.uname()[0]
        LOG.debug("Current OS kernel name: {!r}.".format(os_name))

        from fb_logging import use_unix_syslog_handler

        use_ux_handler = use_unix_syslog_handler()
        LOG.debug("Return value of use_unix_syslog_handler(): {!r}.".format(use_ux_handler))

        if os_name.lower() == 'sunos':
            self.assertTrue(
                    use_ux_handler,
                    "On a {os!r} system {func}() must return {ret!r}.".format(
                        os=os_name, func='use_unix_syslog_handler', ret=True))
        else:
            self.assertFalse(
                    use_ux_handler,
                    "On a {os!r} system {func}() must return {ret!r}.".format(
                        os=os_name, func='use_unix_syslog_handler', ret=False))

# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose)

    LOG.info("Starting tests ...")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestFbLogging('test_import_modules', verbose))
    suite.addTest(TestFbLogging('test_use_unix_syslog_handler', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list




