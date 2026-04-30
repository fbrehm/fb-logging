#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: A script for converting a CHANGELOG.md file into log entries of a RPM spec file.

@author: Frank Brehm
@contact: frank@brehm.online.com
@copyright: © 2026 by Frank Brehm, Berlin
"""
from __future__ import print_function

# Standard modules
import logging
import os
import platform
import re
import shutil
import sys
import textwrap
from pathlib import Path

# 3rd party modules
import click

try:
    from semver import Version
except ImportError:
    from semver import VersionInfo as Version

# Own modules
from . import __version__ as __pkg_version__
from . import pp
from .changelog import ChangelogParsingError
from .changelog import load as load_changelog
from .colored import ColoredFormatter

__version__ = "0.2.0"

LOG = logging.getLogger(__name__)

DEFAULT_MAINT_NAME = "Frank Brehm"
DEFAULT_MAINT_EMAIL = "frank@brehm-online.com"
DEFAULT_REVISION = 1
DEFAULT_TERMINAL_WIDTH = 99
DEFAULT_TERMINAL_HEIGHT = 40


# =============================================================================
class Changelog2SpecLogEnv(object):
    """
    Click context environment class for the changelog2speclog application.

    Converts a CHANGELOG.md into log entries of a RPM spec file.
    """

    output_line_width = 70

    # -------------------------------------------------------------------------
    @classmethod
    def get_generic_appname(cls, appname=None):
        """Get the base name of the currently running application."""
        if appname:
            v = str(appname).strip()
            if v:
                return v
        return os.path.basename(sys.argv[0])

    # -------------------------------------------------------------------------
    @classmethod
    def terminal_can_colors(cls, debug=False):
        """
        Detect, whether the current terminal is able to perform ANSI color sequences.

        Both stdout and stderr file handles are inspected.

        @return: both stdout and stderr can perform ANSI color sequences
        @rtype: bool
        """
        cur_term = ""
        if "TERM" in os.environ:
            cur_term = os.environ["TERM"].lower().strip()

        colored_term_list = (
            r"ansi",
            r"linux.*",
            r"screen.*",
            r"[xeak]term.*",
            r"gnome.*",
            r"rxvt.*",
            r"interix",
        )
        term_pattern = r"^(?:" + r"|".join(colored_term_list) + r")$"
        re_term = re.compile(term_pattern)

        ansi_term = False
        env_term_has_colors = False

        if cur_term:
            if cur_term == "ansi":
                env_term_has_colors = True
                ansi_term = True
            elif re_term.search(cur_term):
                env_term_has_colors = True
        if debug:
            sys.stderr.write(
                "ansi_term: {a!r}, env_term_has_colors: {h!r}\n".format(
                    a=ansi_term, h=env_term_has_colors
                )
            )

        has_colors = False
        if env_term_has_colors:
            has_colors = True
        for handle in [sys.stdout, sys.stderr]:
            if hasattr(handle, "isatty") and handle.isatty():
                if debug:
                    msg = "{} is a tty.".format(handle.name)
                    sys.stderr.write(msg + "\n")
                if platform.system() == "Windows" and not ansi_term:
                    if debug:
                        sys.stderr.write("Platform is Windows and not ansi_term.\n")
                    has_colors = False
            else:
                if debug:
                    msg = "{} is not a tty.".format(handle.name)
                    sys.stderr.write(msg + "\n")
                if ansi_term:
                    pass
                else:
                    has_colors = False

        return has_colors

    # -------------------------------------------------------------------------
    def __init__(
        self, changelog_file, default_revision=DEFAULT_REVISION, error_if_unreleased=True,
        maintainer_name=DEFAULT_MAINT_NAME, maintainer_email=DEFAULT_MAINT_EMAIL,
        appname=None, verbose=0, version=__pkg_version__, has_colors=None
    ):
        """Initialise the application object."""
        if changelog_file is None:
            self.changelog_file = None
        else:
            self.changelog_file = Path(changelog_file)
        if appname:
            self.appname = self.get_generic_appname()
        else:
            self.appname = self.get_generic_appname()
        self.verbose = verbose
        self.version = version
        if has_colors is not None:
            self.has_colors = bool(has_colors)
        else:
            self.has_colors = self.terminal_can_color()

        self.default_revision = default_revision

        self.maintainer_name = maintainer_name.strip()
        self.maintainer_email = maintainer_email.strip().lower()

        if not self.maintainer_name:
            LOG.error("Empty name of the maintainer given.")
            sys.exit(1)

        if not self.maintainer_email:
            LOG.error("Empty E-Mail address of the maintainer given.")
            sys.exit(1)

        self.has_unreleased = False
        self.error_if_unreleased = error_if_unreleased

        self.init_logging()

        if self.verbose > 1:
            LOG.debug(f"Parameter 'has_colors' was {has_colors!r}.")

    # -------------------------------------------------------------------------
    def __repr__(self):
        """Typecasting into a string for reproduction."""
        out = "<%s(" % (self.__class__.__name__)

        fields = []
        cfile = None
        if self.changelog_file is not None:
            cfile = str(self.changelog_file)

        fields.append(f"changelog_file={cfile!r}")
        fields.append(f"appname={self.appname!r}")
        fields.append(f"verbose={self.verbose!r}")
        fields.append(f"version={self.version!r}")
        fields.append(f"has_colors={self.has_colors!r}")

        out += ", ".join(fields) + ")>"
        return out

    # -------------------------------------------------------------------------
    def terminal_can_color(self):
        """
        Detect, whether the current terminal is able to perform ANSI color sequences.

        Both stdout and stderr file handles are inspected.

        @return: both stdout and stderr can perform ANSI color sequences
        @rtype: bool

        """
        if self.verbose > 3:
            return self.terminal_can_colors(debug=True)
        return self.terminal_can_colors(debug=False)

    # -------------------------------------------------------------------------
    def init_logging(self):
        """
        Initialize the logger object.

        It creates a colored loghandler with all output to STDERR.
        Maybe overridden in descendant classes.

        @return: None
        """
        log_level = logging.INFO
        if self.verbose:
            log_level = logging.DEBUG

        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)

        # create formatter
        format_str = ""
        if self.verbose:
            format_str = "[%(asctime)s]: "
        format_str += self.appname + ": "
        if self.verbose:
            if self.verbose > 1:
                format_str += "%(name)s(%(lineno)d) %(funcName)s() "
            else:
                format_str += "%(name)s "
        format_str += "%(levelname)s - %(message)s"
        formatter = None
        if self.has_colors:
            formatter = ColoredFormatter(format_str)
        else:
            formatter = logging.Formatter(format_str)

        # create log handler for console output
        lh_console = logging.StreamHandler(sys.stderr)
        lh_console.setLevel(log_level)
        lh_console.setFormatter(formatter)

        root_logger.addHandler(lh_console)

        return

    # -------------------------------------------------------------------------
    def __call__(self):
        """
        Execute the main action of converting.

        Makes the application object callable.
        """
        if self.changelog_file:
            cfile = str(self.changelog_file)
            LOG.debug(f"Reading {cfile!r} ...")
            with self.changelog_file.open("r", encoding="utf-8", errors="backslashreplace") as fh:
                self.convert(fh, str(self.changelog_file))
        else:
            self.convert(sys.stdin, "STDIN")

    # -------------------------------------------------------------------------
    def mangle_change(self, action, change):
        """Transform the change nto the RPM chngelog format witht the prepended action."""
        lines = []

        change = change.strip()
        if not change:
            return []

        # Substituting newlines by spaces
        change = action.lower().capitalize() + ": " + change.replace("\n", " ").replace("`", "")

        for line in textwrap.wrap(
            change, width=self.output_line_width, initial_indent="-   ", subsequent_indent="    ",
        ):
            lines.append(line)

        return lines

    # -------------------------------------------------------------------------
    def convert(self, fh, filename):
        """Transform the complete contenet of the given changelog file into RPM changelog files."""
        LOG.debug(f"Loading Changelog file {filename!r} ...")
        try:
            ch = load_changelog(fh)
        except ChangelogParsingError as e:
            LOG.error(f"Error on parsing {filename!r}: " + str(e))
            sys.exit(5)

        for entry in ch:
            cur_version = entry["version"]
            if isinstance(cur_version, Version):
                if cur_version.prerelease is None:
                    new_version = Version(
                        major=cur_version.major, minor=cur_version.minor, patch=cur_version.patch,
                        prerelease=self.default_revision, build=cur_version.build)
                    entry["version"] = new_version
            else:
                if cur_version.lower() == "unreleased":
                    self.has_unreleased = True
                else:
                    LOG.error(f"Found invalid version {cur_version!r} in {filename!r}.")
                    sys.exit(6)

        LOG.debug(f"Loaded content of {filename!r}:\n" + pp(ch))

        if self.has_unreleased:
            LOG.warn(f"Found an UNRELEASED version in {filename!r}.")
            if self.error_if_unreleased:
                sys.exit(2)

        days = {}
        for entry in ch:
            lines = []
            day = entry["date"].strftime("%Y-%m-%d")
            date = entry["date"].strftime("%a %b %d %Y")
            version = str(entry["version"])
            author = self.maintainer_name
            email = self.maintainer_email

            if day not in days:
                days[day] = [f"*   {date} {author} <{email}> {version}"]

            for action in ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"):
                action_lc = action.lower()
                if action_lc not in entry:
                    continue

                for change in entry[action_lc]:
                    for line in self.mangle_change(action_lc, change):
                        lines += [line]
            days[day] += lines

        for day in sorted(days.keys(), reverse=True):
            click.echo("\n".join(days[day]))

        sys.exit(0)


# =============================================================================

TERM_SIZE = shutil.get_terminal_size((DEFAULT_TERMINAL_WIDTH, DEFAULT_TERMINAL_HEIGHT))

CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
    "show_default": True,
    "terminal_width": TERM_SIZE.columns,
}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument(
    "changelog_file",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True, path_type=Path),
    required=False,
)
@click.option(
    "-R", "--default-revision", type=click.IntRange(min=1), default=DEFAULT_REVISION,
    metavar="REVISION",
    help=("The default revision, if there is no revision included "
          "in the current version from Changelog.")
)
@click.option(
    "--error-if-unreleased/--no-error-if-unreleased", " /-N", default=True,
    help="Return with code 2, if an UNRELEASED version was found."
)
@click.option(
    "--maintainer-name", "-M", default=DEFAULT_MAINT_NAME,
    metavar="NAME",
    help="The name of the package maintainer used for speclog."
)
@click.option(
    "--maintainer-email", "-E", default=DEFAULT_MAINT_EMAIL,
    metavar="EMAIL",
    help=(
        "The E-Mail address of the package maintainer used for speclog."
    )
)
@click.option(
    "--color/--no-color", "has_color", default=None, help="Set colored output for messages."
)
@click.option(
    "-v", "--verbose", count=True, type=click.IntRange(0, 5), help="Increase the verbosity level."
)
@click.version_option()
@click.pass_context
def main(
    ctx, changelog_file, default_revision, error_if_unreleased, maintainer_name, maintainer_email,
    has_color, verbose,
):
    """
    Convert a CHANGELOG_FILE markdown file into log entries of a RPM spec file.

    If CHANGELOG_FILE is omitted, then the input will be read from STDIN.
    """
    ctx.obj = Changelog2SpecLogEnv(
        changelog_file, default_revision=default_revision, error_if_unreleased=error_if_unreleased,
        maintainer_name=maintainer_name, maintainer_email=maintainer_email,
        verbose=verbose, has_colors=has_color,
    )

    if verbose > 2:
        click.echo(
            "{c}-Object:\n{a}".format(c=ctx.__class__.__name__, a=pp(ctx.__dict__)),
            file=sys.stderr,
        )

    ctx.obj()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
