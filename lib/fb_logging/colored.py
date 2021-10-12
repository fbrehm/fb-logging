#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: additional logging formatter for colored output via console
"""

import logging
import copy
import re

from collections.abc import Sequence

__version__ = '0.3.0'


# =============================================================================
class ColorNotFoundError(KeyError):
    """Class for an exception in case that a color was not found."""

    # -------------------------------------------------------------------------
    def __init__(self, color):

        self.color = address

    # -------------------------------------------------------------------------
    def __str__(self):

        return "Color {!r} not found.".format(self.color)


# =============================================================================
class Colors:
    ENDC = 0
    BOLD = 1
    UNDERLINE = 4
    BLINK = 5
    INVERT = 7
    CONCEALD = 8
    STRIKE = 9
    GREY30 = 90
    GREY40 = 2
    GREY65 = 37
    GREY70 = 97
    GREY20_BG = 40
    GREY33_BG = 100
    GREY80_BG = 47
    GREY93_BG = 107
    DARK_RED = 31
    RED = 91
    RED_BG = 41
    LIGHT_RED_BG = 101
    DARK_YELLOW = 33
    YELLOW = 93
    YELLOW_BG = 43
    LIGHT_YELLOW_BG = 103
    DARK_BLUE = 34
    BLUE = 94
    BLUE_BG = 44
    LIGHT_BLUE_BG = 104
    DARK_MAGENTA = 35
    PURPLE = 95
    MAGENTA_BG = 45
    LIGHT_PURPLE_BG = 105
    DARK_CYAN = 36
    AQUA = 96
    CYAN = 96
    CYAN_BG = 46
    LIGHT_AQUA_BG = 106
    LIGHT_CYAN_BG = 106
    DARK_GREEN = 32
    GREEN = 92
    GREEN_BG = 42
    LIGHT_GREEN_BG = 102
    BLACK = 30

    # -------------------------------------------------------------------------
    @classmethod
    def termcode(cls, value):
        """
        Tries to get the numeric value of given color value.

        @param color: The color to use, must be a valid color code.
        @type color: str or int

        @raises: ColorNotFoundError if the color was not found.

        @return: The numeric terminal code of the color.
        @rtype: int
        """

        if isinstance(value, int):
            return value
        key = value.upper()
        if not hasattr(cls, key):
            raise ColorNotFoundError(value)
        return getattr(cls, key)

    # -------------------------------------------------------------------------
    @classmethod
    def termout(cls, color):
        """
        Output of an ANSII terminal code.

        @param color: The color to use, must be a valid color code.
        @type color: str or int

        @return: The terminal output to start colorized message.
        @rtype: str
        """

        num = cls.termcode(color)
        return '\x1b[{}m'.format(num)

    # -------------------------------------------------------------------------
    @classmethod
    def colorize(cls, message, color):
        """
        Wrapper function to colorize the message.

        @param message: The message to colorize
        @type message: str
        @param color: The color to use, must be one or a sequence of color codes.
        @type color: str

        @return: the colorized message
        @rtype: str

        """

        start_out = ''
        if isinstance(color, Sequence):
            for single_color in color:
                start_out += cls.termout(single_color)
        else:
            start_out = cls.termout(single_color)

        return start_out + message + cls.termout('endc')

    # -------------------------------------------------------------------------
    @classmethod
    def keys(cls):

        ret = []
        re_capital = re.compile(r'^[A-Z][A-Z_]*[A-Z]$')
        for key in sorted(cls.__dict__.keys()):
            if re_capital.match(key):
                ret.append(key)
        return ret

# =============================================================================
def colorstr(message, color):
    """
    Wrapper function for Color.colorize()

    @param message: The message to colorize
    @type message: str
    @param color: The color to use, must be one or a sequence of color codes.
    @type color: str

    @return: the colorized message
    @rtype: str

    """

    return Color.colorize(message, color)


# =============================================================================
# vim: fileencoding=utf-8 filetype=python ts=4 et list
