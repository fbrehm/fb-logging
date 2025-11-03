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

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger, pp

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
        self.changelog_ok = self.test_dir / 'CHANGELOG-ok.md'
        self.changelog_broken = self.test_dir / 'CHANGELOG-broken.md'

        if not self.changelog_file.exists():
            raise RuntimeError(f"File {str(self.changelog_file)!r} not found.")

        if not self.changelog_file.is_file():
            raise RuntimeError(f"Path {str(self.changelog_file)!r} is not a regular file.")

        LOG.debug(f"Using {str(self.changelog_ok)!r} for testing.")

    # -------------------------------------------------------------------------
    def test_import_module(self):
        """Test importing module fb_logging.changelog."""
        LOG.info(self.get_method_doc())

        import fb_logging.changelog
        ver = fb_logging.changelog.__version__
        LOG.debug(f"Version of fb_logging.changelog: {ver!r}.")

    # -------------------------------------------------------------------------
    def test_load(self):
        """Test loading a changelog as a Changelog object."""
        LOG.info(self.get_method_doc())

        from fb_logging import changelog

        with self.changelog_ok.open("rb") as fp:
            changes = changelog.load(fp)

        count = len(changes)
        LOG.debug(f"Found {count} changes in {str(self.changelog_ok)!r}.")
        if self.verbose > 2:
            LOG.debug("Changes object:\n" + pp(changes))

    # -------------------------------------------------------------------------
    def test_load_broken(self):
        """Test for raising an exception on trying to load an invalid CHANGELOG file."""
        LOG.info(self.get_method_doc())

        from fb_logging import changelog
        from fb_logging.changelog import ChangelogParsingError

        LOG.debug(f"Testing broken Changelog file {str(self.changelog_broken)!r} ...")

        with self.assertRaises(ChangelogParsingError) as cm:
            with self.changelog_broken.open("rb") as fp:
                changes = changelog.load(fp)
                print(pp(changes))
        e = cm.exception
        LOG.debug('Got a {c}: {e}.'.format(c=e.__class__.__name__, e=e))


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
    suite.addTest(ChangelogTestcase('test_load', verbose))
    suite.addTest(ChangelogTestcase('test_load_broken', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
