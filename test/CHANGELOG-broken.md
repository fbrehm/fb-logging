# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] -    2025-11-03

### Added

* Adding CHANGELOG.md.
* Adding `test/test_50_changelog.py` for testing `fb_logging.changelog`.

### Fixed

* Fixing `src/fb_logging/changelog.py` for incompatible versions of *semver*.

## [1.3.5] - 2025-10-30

### Changed

* Minor changes because of the CI build chain.

## [1.3.4] - 2025-10-30

### Changed

* Minor changes because of the CI build chain.

## [1.3.3] - 2025-10-29

### Changed

* Refactoring update-env.sh.
* Enable build of EL-10 RPM packages in `.github/workflows/build-packages.yaml`.
* Enabling building of packages for EL 10 in CI workflows.

## [1.3.1] - 2025-10-09

### Changed

* Changing build tool from setuptools to flit

### Fixed

* Fixing .gitlab-ci.yml for new build chain.

## [1.2.1] - 2025-04-17

### Changed

* Setting Copyright to year 2025.

## [1.2.0] - 2024-10-20

### Added

* Adding function `terminal_can_colors()` to test/general.py.
* Adding `test/test_colored_formatter.py` for testing colorized logging output.

### Changed

* Decolorize the underlaying logging message.

### Fixed

* Fixing `lib/fb_logging/colored.py` for dark mode.
* Fixing update-env.sh for Python 3.12.

## [1.1.1] - 2024-06-24

### Fixed

* Fixing .gitlab-ci.yml.

## [1.1.0] - 2024-06-23

### Changed

* Using external Gitlab workflow for installing build packages.

### Removed

* Removing no more needed GitHub workflow and actions.

## [1.0.1] - 2024-05-07

### Changed

* Updating .gitlab-ci.yml to the latest version of Digitas packaging tools.

## [1.0.0] - 2024-02-04

### Added

* Extending linter checks in Github workflow.

### Changed

* Improving Github workflow.

### Fixed

* Fixing flake8 linter error messages in bin/dch2speclog and test/.

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


[Unreleased]: https://github.com/fbrehm/fb-logging/compare/1.3.5...develop
[1.3.5]: https://github.com/fbrehm/fb-logging/compare/1.3.4...1.3.5
[1.3.4]: https://github.com/fbrehm/fb-logging/compare/1.3.3...1.3.4
[1.3.3]: https://github.com/fbrehm/fb-logging/compare/1.3.1...1.3.3
[1.3.1]: https://github.com/fbrehm/fb-logging/compare/1.2.1...1.3.1
[1.2.1]: https://github.com/fbrehm/fb-logging/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/fbrehm/fb-logging/compare/1.1.1...1.2.0
[1.1.1]: https://github.com/fbrehm/fb-logging/compare/1.1.0...1.1.1
[1.1.0]: https://github.com/fbrehm/fb-logging/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/fbrehm/fb-logging/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/fbrehm/fb-logging/compare/0.4.0...1.0.0
[0.4.0]: https://github.com/fbrehm/fb-logging/compare/0.3.2...0.4.0
[0.3.2]: https://github.com/fbrehm/fb-logging/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/fbrehm/fb-logging/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/fbrehm/fb-logging/releases/tag/0.3.0
