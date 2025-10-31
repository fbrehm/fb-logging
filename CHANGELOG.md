# Changelog

All notable changes to this project will be documented in this file.

## [0.5.0] - 2022-07-18

### Added

* Adding modules `fb_logging.deb_changelog` and `fb_logging.deb_version`
  took from the debian-python project.
* Adding `.gitlab-ci.yml` for creating and deploying packages with GitLab.

### Changed

* Changing `changelog-deb2rpm.py` to `bin/dch2speclog`.
* Completing all docstrings in all modules and scripts according to flake8.
* Updating all CI control files for bin/ directory.

## [0.4.6] - 2022-04-23

### Changed

* Supporting Ubuntu 22.04 Jammy Jellyfish.

## [0.4.5] - 2022-01-30

### Added

* Adding flake8 config to setup.cfg.

### Changed

* Support creating RPMs for CentOS Stream 9.
* Changing Distro for building EL-8 packages to CentOS Stream 8.

## [0.4.4] - 2021-11-11

### Added

* Adding Github workflow job to upload to my repo server.

## [0.4.3] - 2021-10-28

### Added

* Adding MANIFEST.in file.

### Changed

* Minor change in Github workflow job notify_success.

## [0.4.2] - 2021-10-25

### Added

* Adding Github workflow job for uploading Python package to PyPi

### Changed

* Checking matching of tag with module version in Github workflow linter job
* Updating PyPi classifiers

## [0.4.1] - 2021-10-21

### Added

* Adding path `tmp/` to .gitignore

### Changed

* Definition of legacy colors
* Fixing `Colors.colorize_24bit()` and removing parameter `font_effect`
  from `Colors.colorize_24bit()` and `colorstr_24bit()`.

## [0.4.0] - 2021-10-21

### Added

* Adding Python 3.10 to test matrix in Github workflow
* Adding module `lib/fb_logging/colored.py` with classes
  `ColorNotFoundError`, `WrongColorTypeError`, `Colors` and `ColoredFormatter`
* Adding `test/test_colored.py` for testing classes and functions in `lib/fb_logging/colored.py`.
* Adding functions `stdout_is_redirected()` and `stderr_is_redirected()` to `lib/fb_logging/__init__.py`.
* Adding `lib/fb_logging/syslog_handler.py` with class FbSysLogHandler
* Adding `lib/fb_logging/unix_handler.py` with class UnixSyslogHandler

## [0.3.2] - 2021-10-13

### Added

* Adding files template.spec, get-rpm-version, get-rpm-release and changelog-deb2rpm.py
* Adding job for creating RPM packages to .github/workflows/packages.yaml

## [0.3.1] - 2021-10-12

### Added

* Creating Github workflow for building Debian and Ubuntu packages.

## [0.3.0] - 2021-10-01

### Added

* Creating Github workflow for building Debian and Ubuntu packages.

## [0.2.4] - 2021-10-01

### Added

* Initial release


[0.4.0]: https://github.com/fbrehm/fb-logging/compare/0.3.2...0.4.0
[0.3.2]: https://github.com/fbrehm/fb-logging/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/fbrehm/fb-logging/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/fbrehm/fb-logging/releases/tag/0.3.0
