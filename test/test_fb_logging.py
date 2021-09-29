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
import syslog

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger, pp

LOG = logging.getLogger('test_fb_logging')


# =============================================================================
class TestFbLogging(FbLoggingTestcase):

    # -------------------------------------------------------------------------
    def test_import_modules(self):

        LOG.info("Test importing main module ...")

        LOG.debug("Importing fb_logging ...")
        import fb_logging
        from fb_logging import valid_syslog_facilities, syslog_facility_names

        LOG.debug("Version of fb_logging: {!r}.".format(fb_logging.__version__))

        facilities = valid_syslog_facilities()
        fac_names = syslog_facility_names()
        if self.verbose >= 3:
            LOG.debug("Valid syslog facilities:\n{}".format(pp(facilities)))
            LOG.debug("Syslog facility names:\n{}".format(pp(fac_names)))

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


    # -------------------------------------------------------------------------
    def test_get_syslog_facility_name(self):

        LOG.info("Testing fb_logging.get_syslog_facility_name() ...")

        from fb_logging import use_unix_syslog_handler, get_syslog_facility_name
        from fb_logging import SyslogFacitityError

        use_ux_handler = use_unix_syslog_handler()

        if use_ux_handler:
            valid_test_data = [
                [syslog.LOG_AUTH, 'syslog.LOG_AUTH', 'auth'],
                [syslog.LOG_DAEMON, 'syslog.LOG_DAEMON', 'daemon'],
                [syslog.LOG_LOCAL2, 'syslog.LOG_LOCAL2', 'local2'],
                [syslog.LOG_MAIL, 'syslog.LOG_MAIL', 'mail'],
                [0.0, 'syslog.LOG_KERN', 'kern'],
            ]
            invalid_test_data = [ 10, None, 'blah', 1024, -3, 0.4, 99.4]
        else:
            valid_test_data = [
                [
                    logging.handlers.SysLogHandler.LOG_AUTH,
                    'logging.handlers.SysLogHandler.LOG_AUTH',
                    'auth',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_AUTHPRIV,
                    'logging.handlers.SysLogHandler.LOG_AUTHPRIV',
                    'authpriv',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_DAEMON,
                    'logging.handlers.SysLogHandler.LOG_DAEMON',
                    'daemon',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_LOCAL2,
                    'logging.handlers.SysLogHandler.LOG_LOCAL2',
                    'local2',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_MAIL,
                    'logging.handlers.SysLogHandler.LOG_MAIL',
                    'mail',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_SYSLOG,
                    'logging.handlers.SysLogHandler.LOG_SYSLOG',
                    'syslog',
                ],
                [
                    0.0,
                    'logging.handlers.SysLogHandler.LOG_KERN',
                    'kern',
                ],
            ]
            invalid_test_data = [ None, 'blah', 1024, -3, 0.4, 99.4]

        for test_tuple in valid_test_data:

            fac_id = test_tuple[0]
            fac_origin = test_tuple[1]
            expected = test_tuple[2]

            LOG.debug("Test get_syslog_facility_name({id}) -> {ex!r} ({origin}).".format(
                id=fac_id, ex=expected, origin=fac_origin))
            result = get_syslog_facility_name(fac_id)
            LOG.debug("Got {!r}.".format(result))
            self.assertEqual(expected, result)

        for test_id in invalid_test_data:

            LOG.debug("Test exception on get_syslog_facility_name({!r}).".format(test_id))

            with self.assertRaises(SyslogFacitityError) as cm:
                result = get_syslog_facility_name(test_id)

            e = cm.exception
            LOG.debug("Got a {c}: {e}.".format(c=e.__class__.__name__, e=e))

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
    suite.addTest(TestFbLogging('test_get_syslog_facility_name', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list




