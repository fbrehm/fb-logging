# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2025-11-03

### Added

* Adding CHANGELOG.md.

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

## [0.6.2] - 2024-04-02

### Fixed

* Fixing Github workflow.

## [0.6.1] - 2024-02-04

### Added

* Adding tests for Python 3.12 to CI tests.
* Adding distros Debian 13 (trixie) and Ubuntu 24.04 (Noble Numbat) to
  Github workflow packages for building OS packages.

### Changed

* Using Python 3.12 for CI linter tests.
* Updating external Guthub actions.

### Removed

* Removing deprecated OS versions Ubuntu 18.04 (Bionic Beaver) and
  Enterprise Linux 7 from Github workflow.

## [0.6.0] - 2023-02-18

### Added

* Adding additional flake8 tests in .github/workflows/packages.yaml.
* Adding update-env.sh.
* Adding Debian 12 (bookworm) for building binary packages on Github.

### Fixed

* Fixing linter errors.

## [0.5.5] - 2022-12-30

### Changed

* Cleaning up .gitlab-ci.yml.
* Setting a defined version of shared Gitlab CI pipeline.

## [0.5.4] - 2022-12-29

### Fixed

* Fixing .gitlab-ci.yml.

## [0.5.3] - 2022-12-29

### Changed

* Changing .gitlab-ci.yml to use shared CI scripts.

## [0.5.2] - 2022-11-02

### Added

* Adding Python 3.11 for testing in CI definitions.

### Changed

* Updating Github workflow.

## [0.5.1] - 2022-07-19

### Fixed

* Fixing Signing job in .gitlab-ci.yml.

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


[Unreleased]: https://github.com/fbrehm/fb-logging/compare/1.3.5...HEAD
[1.3.5]: https://github.com/fbrehm/fb-logging/compare/1.3.4...1.3.5
[1.3.4]: https://github.com/fbrehm/fb-logging/compare/1.3.3...1.3.4
[1.3.3]: https://github.com/fbrehm/fb-logging/compare/1.3.1...1.3.3
[1.3.1]: https://github.com/fbrehm/fb-logging/compare/1.2.1...1.3.1
[1.2.1]: https://github.com/fbrehm/fb-logging/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/fbrehm/fb-logging/compare/1.1.1...1.2.0
[1.1.1]: https://github.com/fbrehm/fb-logging/compare/1.1.0...1.1.1
[1.1.0]: https://github.com/fbrehm/fb-logging/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/fbrehm/fb-logging/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/fbrehm/fb-logging/compare/0.6.2...1.0.0
[0.6.2]: https://github.com/fbrehm/fb-logging/compare/0.6.1...0.6.2
[0.6.1]: https://github.com/fbrehm/fb-logging/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/fbrehm/fb-logging/compare/0.5.5...0.6.0
[0.5.5]: https://github.com/fbrehm/fb-logging/compare/0.5.4...0.5.5
[0.5.4]: https://github.com/fbrehm/fb-logging/compare/0.5.3...0.5.4
[0.5.3]: https://github.com/fbrehm/fb-logging/compare/0.5.2...0.5.3
[0.5.2]: https://github.com/fbrehm/fb-logging/compare/0.5.1...0.5.2
[0.5.1]: https://github.com/fbrehm/fb-logging/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/fbrehm/fb-logging/compare/0.4.6...0.5.0
[0.4.6]: https://github.com/fbrehm/fb-logging/compare/0.4.5...0.4.6
[0.4.5]: https://github.com/fbrehm/fb-logging/compare/0.4.4...0.4.5
[0.4.4]: https://github.com/fbrehm/fb-logging/compare/0.4.3...0.4.4
[0.4.3]: https://github.com/fbrehm/fb-logging/compare/0.4.2...0.4.3
[0.4.2]: https://github.com/fbrehm/fb-logging/compare/0.4.1...0.4.2
[0.4.1]: https://github.com/fbrehm/fb-logging/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/fbrehm/fb-logging/compare/0.3.2...0.4.0
[0.3.2]: https://github.com/fbrehm/fb-logging/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/fbrehm/fb-logging/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/fbrehm/fb-logging/releases/tag/0.3.0
