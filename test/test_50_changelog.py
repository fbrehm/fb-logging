#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: Test script (and module) for unit tests on Changelog class.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2025 Frank Brehm, Berlin
@license: LGPL3
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path

try:
    import unittest2 as unittest
except ImportError:
    import unittest

srcdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, srcdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger

__app__ = 'test_changelog'
LOG = logging.getLogger(__app__)


# =============================================================================
class ChangelogTestcase(FbLoggingTestcase):
    """Testcase for unit tests on fb_logging.changelog."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

        self.test_dir = Path(__file__).parent.resolve()
        self.workdir = self.test_dir.parent

        self.changelog_file = self.workdir / 'CHANGELOG.md'

        if not self.changelog_file.exists():
            raise RuntimeError(f"File {str(self.changelog_file)!r} not found.")

        if not self.changelog_file.is_file():
            raise RuntimeError(f"Path {str(self.changelog_file)!r} is not a regular file.")

        LOG.debug(f"Using {str(self.changelog_file)!r} for testing.")

    # -------------------------------------------------------------------------
    def test_import_module(self):
        """Test importing module fb_logging.changelog."""
        LOG.info(self.get_method_doc())

        import fb_logging.changelog
        ver = fb_logging.changelog.__version__
        LOG.debug(f"Version of fb_logging.changelog: {ver!r}.")


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose, __app__)

    LOG.info('Starting tests ...')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(ChangelogTestcase('test_import_module', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
