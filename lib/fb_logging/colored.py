#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: additional logging formatter for colored output via console
"""

import logging
import copy
import re

from numbers import Number
from collections.abc import Sequence

__version__ = '0.3.0'


# =============================================================================
class ColorNotFoundError(KeyError):
    """Class for an exception in case that a color was not found."""

    # -------------------------------------------------------------------------
    def __init__(self, color):

        self.color = color

    # -------------------------------------------------------------------------
    def __str__(self):

        return "Color {!r} not found.".format(self.color)


# =============================================================================
class WrongColorTypeError(TypeError):
    """Class for an exception in case that a wrong type for a color was given."""

    # -------------------------------------------------------------------------
    def __init__(self, color):

        self.color = color

    # -------------------------------------------------------------------------
    def __str__(self):

        return "Color {c!r} has wrong type {t}.".format(
                c=self.color, t=self.color.__class__.__name__)


# =============================================================================
class Colors:
    ENDC = 0
    RESET = 0
    BOLD = 1
    GREY40 = 2
    UNDERLINE = 4
    BLINK = 5
    INVERT = 7
    CONCEALD = 8
    STRIKE = 9
    BLACK = 30
    DARK_RED = 31
    DARK_GREEN = 32
    DARK_YELLOW = 33
    DARK_BLUE = 34
    DARK_MAGENTA = 35
    DARK_CYAN = 36
    DARK_WHITE = 37
    BLACK_BG = 40
    RED_BG = 41
    GREEN_BG = 42
    YELLOW_BG = 43
    BLUE_BG = 44
    MAGENTA_BG = 45
    CYAN_BG = 46
    GREY80_BG = 47
    WHITE_BG = 47
    BRIGHT_BLACK = 90
    RED = 91
    BRIGHT_RED = 91
    GREEN = 92
    BRIGHT_GREEN = 92
    YELLOW = 93
    BRIGHT_YELLOW = 93
    BLUE = 94
    BRIGHT_BLUE = 94
    MAGENTA = 95
    BRIGHT_MAGENTA = 95
    CYAN = 96
    BRIGHT_CYAN = 96
    WHITE = 97
    BRIGHT_WHITE = 97
    BRIGHT_BLACK_BG = 100
    BRIGHT_RED_BG = 101
    BRIGHT_GREEN_BG = 102
    BRIGHT_YELLOW_BG = 103
    BRIGHT_BLUE_BG = 104
    BRIGHT_PURPLE_BG = 105
    BRIGHT_CYAN_BG = 106
    BRIGHT_WHITE_BG = 107

    # -------------------------------------------------------------------------
    @classmethod
    def termcode_4bit(cls, value):
        """
        Tries to get the numeric value of given 4 Bit color value or font effect name.

        @param color: The color to use, must be a valid 4 Bit color code.
        @type color: str or int

        @raises: ColorNotFoundError if the color was not found.

        @return: The numeric terminal code of the color.
        @rtype: int
        """

        if isinstance(value, bool):
            raise WrongColorTypeError(value)

        if isinstance(value, int):
            return value

        if not isinstance(value, (str, bytes)):
            raise WrongColorTypeError(value)

        key = str(value).upper()
        if not hasattr(cls, key):
            raise ColorNotFoundError(value)
        return getattr(cls, key)

    # -------------------------------------------------------------------------
    @classmethod
    def termout_8bit_fg(cls, color):

        if isinstance(color, Number):
            if isinstance(color, bool):
                raise WrongColorTypeError(color)
            v_int = int(color)
            if v_int != color:
                raise ColorNotFoundError(color)
            if v_int < 0 or v_int > 255:
                raise ColorNotFoundError(color)
            return '\x1b[38;5;{}m'.format(v_int)

        raise WrongColorTypeError(color)

    # -------------------------------------------------------------------------
    @classmethod
    def termout_8bit_bg(cls, color):

        if isinstance(color, Number):
            if isinstance(color, bool):
                raise WrongColorTypeError(color)
            v_int = int(color)
            if v_int != color:
                raise ColorNotFoundError(color)
            if v_int < 0 or v_int > 255:
                raise ColorNotFoundError(color)
            return '\x1b[48;5;{}m'.format(v_int)

        raise WrongColorTypeError(color)

    # -------------------------------------------------------------------------
    @classmethod
    def colorize_8bit(cls, message, color_fg=None, color_bg=None, font_effect=None):

        start_out = ''
        if color_fg is not None:
            start_out += cls.termout_8bit_fg(color_fg)
        if color_bg is not None:
            start_out += cls.termout_8bit_bg(color_bg)
        if font_effect is not None:
            start_out += cls.termcode_4bit(font_effect)

        return start_out + message + cls.termout('reset')

    # -------------------------------------------------------------------------
    @classmethod
    def termout_fg(cls, color):

        if isinstance(color, (list, tuple)):

            if len(color) != 3:
                raise WrongColorTypeError(color)

            for val in color:

                if not isinstance(val, Number):
                    raise WrongColorTypeError(color)

                if isinstance(val, bool):
                    raise WrongColorTypeError(color)

                v_int = int(val)
                if v_int != val:
                    raise WrongColorTypeError(color)
                if v_int < 0 or v_int > 255:
                    raise ColorNotFoundError(color)

            return '\x1b[38;2;{};{};{}m'.format(
                    color[0], color[1], color[2])

        raise WrongColorTypeError(color)

    # -------------------------------------------------------------------------
    @classmethod
    def termout_bg(cls, color):

        if isinstance(color, (list, tuple)):

            if len(color) != 3:
                raise WrongColorTypeError(color)

            for val in color:

                if not isinstance(val, Number):
                    raise WrongColorTypeError(color)

                if isinstance(val, bool):
                    raise WrongColorTypeError(color)

                v_int = int(val)
                if v_int != val:
                    raise WrongColorTypeError(color)
                if v_int < 0 or v_int > 255:
                    raise ColorNotFoundError(color)

            return '\x1b[48;2;{};{};{}m'.format(
                    color[0], color[1], color[2])

        raise WrongColorTypeError(color)

    # -------------------------------------------------------------------------
    @classmethod
    def colorize_24bit(cls, message, color_fg=None, color_bg=None, font_effect=None):

        start_out = ''
        if color_fg is not None:
            start_out += cls.termout_fg(color_fg)
        if color_bg is not None:
            start_out += cls.termout_bg(color_fg)
        if font_effect is not None:
            start_out += cls.termcode_4bit(font_effect)

        return start_out + message + cls.termout('reset')

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

        if isinstance(color, (str, bytes)):
            num = cls.termcode_4bit(color)
            return '\x1b[{}m'.format(num)

        if isinstance(color, Number):
            return cls.termout_8bit_fg(color)

        if isinstance(color, (list, tuple)):
            return cls.termout_fg(color)

        raise WrongColorTypeError(color)

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
        if isinstance(color, Sequence) and not isinstance(color, (str, bytes)):
            for single_color in color:
                start_out += cls.termout(single_color)
        else:
            start_out = cls.termout(color)

        return start_out + message + cls.termout('reset')

    # -------------------------------------------------------------------------
    @classmethod
    def keys(cls):

        ret = []
        re_capital = re.compile(r'^[A-Z][A-Z_0-9]*$')
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

    return Colors.colorize(message, color)


# =============================================================================
def colorstr_8bit(message, message, color_fg=None, color_bg=None, font_effect=None):
    """
    Wrapper function for Color.colorize_8bit()

    @return: the colorized message
    @rtype: str

    """

    return Colors.colorize_8bit(
            message, color_fg=color_fg, color_bg=color_bg, font_effect=font_effect)


# =============================================================================
def colorstr_24bit(message, message, color_fg=None, color_bg=None, font_effect=None):
    """
    Wrapper function for Color.colorize_24bit()

    @return: the colorized message
    @rtype: str

    """

    return Colors.colorize_24bit(
            message, color_fg=color_fg, color_bg=color_bg, font_effect=font_effect)


# =============================================================================
# vim: fileencoding=utf-8 filetype=python ts=4 et list
