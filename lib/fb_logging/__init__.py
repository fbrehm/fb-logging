#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2021 by Frank Brehm, Berlin
@summary: All modules for python logging stuff
"""

__author__ = 'Frank Brehm <frank@brehm-online.com>'
__copyright__ = '(C) 2021 by Frank Brehm, Berlin'
__contact__ = 'frank@brehm-online.com'
__version__ = '0.1.0'
__license__ = 'AGPL'

# Standard modules
import os
import copy
import logging
import logging.handlers
import syslog

# -----------------------------------------------------------------------------
# Module variables

VALID_SYSLOG_FACILITIES = {}
"""
a dictionary with all valid syslog facility names as keys and their
integer value as values.
@type: dict
"""

SYSLOG_FACILITY_NAMES = {}
"""
The reverse dictionary to VALID_SYSLOG_FACILITIES with all facility values
as keys and their names as values.
"""

# =============================================================================
def valid_syslog_facilities():
    """
    Returns a copy of VALID_SYSLOG_FACILITIES.
    """

    return copy.copy(VALID_SYSLOG_FACILITIES)


# =============================================================================
def syslog_facility_names():
    """
    Returns a copy of SYSLOG_FACILITY_NAMES.
    """

    return copy.copy(SYSLOG_FACILITY_NAMES)


# =============================================================================
def use_unix_syslog_handler():
    """
    Use UnixSyslogHandler for logging instead of SyslogHandler.

    @return: using UnixSyslogHandler
    @rtype: bool

    """

    use_syslog = False
    un = os.uname()
    os_name = un[0].lower()
    if os_name == 'sunos':
        use_syslog = True

    return use_syslog


# =============================================================================
def _init_valid_facilities():
    """
    Initialise the module variables VALID_SYSLOG_FACILITY and
    SYSLOG_FACILITY_NAME.

    """

    global VALID_SYSLOG_FACILITIES, SYSLOG_FACILITY_NAMES

    if use_unix_syslog_handler():

        VALID_SYSLOG_FACILITIES = {
            'auth': syslog.LOG_AUTH,
            'cron': syslog.LOG_CRON,
            'daemon': syslog.LOG_DAEMON,
            'kern': syslog.LOG_KERN,
            'local0': syslog.LOG_LOCAL0,
            'local1': syslog.LOG_LOCAL1,
            'local2': syslog.LOG_LOCAL2,
            'local3': syslog.LOG_LOCAL3,
            'local4': syslog.LOG_LOCAL4,
            'local5': syslog.LOG_LOCAL5,
            'local6': syslog.LOG_LOCAL6,
            'local7': syslog.LOG_LOCAL7,
            'lpr': syslog.LOG_LPR,
            'mail': syslog.LOG_MAIL,
            'news': syslog.LOG_NEWS,
            'user': syslog.LOG_USER,
            'uucp': syslog.LOG_UUCP,
        }

    else:

        VALID_SYSLOG_FACILITIES = {
            'auth': logging.handlers.SysLogHandler.LOG_AUTH,
            'authpriv': logging.handlers.SysLogHandler.LOG_AUTHPRIV,
            'cron': logging.handlers.SysLogHandler.LOG_CRON,
            'daemon': logging.handlers.SysLogHandler.LOG_DAEMON,
            'kern': logging.handlers.SysLogHandler.LOG_KERN,
            'local0': logging.handlers.SysLogHandler.LOG_LOCAL0,
            'local1': logging.handlers.SysLogHandler.LOG_LOCAL1,
            'local2': logging.handlers.SysLogHandler.LOG_LOCAL2,
            'local3': logging.handlers.SysLogHandler.LOG_LOCAL3,
            'local4': logging.handlers.SysLogHandler.LOG_LOCAL4,
            'local5': logging.handlers.SysLogHandler.LOG_LOCAL5,
            'local6': logging.handlers.SysLogHandler.LOG_LOCAL6,
            'local7': logging.handlers.SysLogHandler.LOG_LOCAL7,
            'lpr': logging.handlers.SysLogHandler.LOG_LPR,
            'mail': logging.handlers.SysLogHandler.LOG_MAIL,
            'news': logging.handlers.SysLogHandler.LOG_NEWS,
            'syslog': logging.handlers.SysLogHandler.LOG_SYSLOG,
            'user': logging.handlers.SysLogHandler.LOG_USER,
            'uucp': logging.handlers.SysLogHandler.LOG_UUCP,
        }

    SYSLOG_FACILITY_NAMES = {}
    for fac_name in VALID_SYSLOG_FACILITIES.keys():
        fac_nr = VALID_SYSLOG_FACILITIES[fac_name]
        SYSLOG_FACILITY_NAMES[fac_nr] = fac_name


# =============================================================================
def get_syslog_facility_name(syslog_facility):
    """
    Returns the name of the given syslog facility.
    Returns None, if not found.

    @return: syslog facility name
    @rtype: str
    """

    global SYSLOG_FACILITY_NAMES

    if syslog_facility in SYSLOG_FACILITY_NAMES:
        return SYSLOG_FACILITY_NAMES[syslog_facility]

    return None


# =============================================================================
def get_syslog_facility_of_name(facility_name):
    """
    Returns the numeric value of the given syslog facility name.
    Returns None, if not found.

    @return: syslog facility value
    @rtype: int
    """

    global valid_syslog_facility, syslog_facility_name

    if facility_name in SYSLOG_FACILITY_NAMES:
        return facility_name

    fname = facility_name.lower()
    if facility_name in VALID_SYSLOG_FACILITIES:
        return VALID_SYSLOG_FACILITIES[facility_name]

    return None


# =============================================================================

_init_valid_facilities()


# =============================================================================
# vim: fileencoding=utf-8 filetype=python ts=4 et list
