# Changelog

All notable changes to this project will be documented in this file.

## Release [0.4.0](https://github.com/fbrehm/fb-logging/releases/tag/0.4.0) (2021-10-21)

### Added

* Adding Python 3.10 to test matrix in Github workflow
* Adding module `lib/fb_logging/colored.py` with classes
  `ColorNotFoundError`, `WrongColorTypeError`, `Colors` and `ColoredFormatter`
* Adding `test/test_colored.py` for testing classes and functions in `lib/fb_logging/colored.py`.
* Adding functions `stdout_is_redirected()` and `stderr_is_redirected()` to `lib/fb_logging/__init__.py`.
* Adding `lib/fb_logging/syslog_handler.py` with class FbSysLogHandler
* Adding `lib/fb_logging/unix_handler.py` with class UnixSyslogHandler

## Release [0.3.2](https://github.com/fbrehm/fb-logging/releases/tag/0.3.2) (2021-10-13)

### Added

* Adding files template.spec, get-rpm-version, get-rpm-release and changelog-deb2rpm.py
* Adding job for creating RPM packages to .github/workflows/packages.yaml

## Release [0.3.1](https://github.com/fbrehm/fb-logging/releases/tag/0.3.1) (2021-10-12)

### Added

* Creating Github workflow for building Debian and Ubuntu packages.

## Release [0.3.0](https://github.com/fbrehm/fb-logging/releases/tag/0.3.0) (2021-10-01)

### Added

* Creating Github workflow for building Debian and Ubuntu packages.

## Release [0.2.4](https://github.com/fbrehm/fb-logging/releases/tag/0.2.4) (2021-10-01)

### Added

* Initial release

