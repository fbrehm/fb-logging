%define version @@@Version@@@
%define builddir %{_builddir}/python%{python3_pkgversion}-fb-logging-%{version}

Name:           python%{python3_pkgversion}-fb-logging
Version:        %{version}
Release:        @@@Release@@@%{?dist}
Summary:        Python modules to extend the logging mechanism in Python.

Group:          Development/Languages/Python
License:        LGPL-3
Distribution:   Frank Brehm
URL:            https://github.com/fbrehm/fb-logging
Source0:        fb-logging.%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-semver
BuildRequires:  pyproject-rpm-macros
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-libs
Requires:       python%{python3_pkgversion}-semver
BuildArch:      noarch

%description
Python modules to extend the logging mechanism in Python.

This package provides the following script:
 * dch2speclog - converting a Debian changelog into log entries of a RPM spec file.
 * check-changelog - checking a CHANGELOG.md for syntax errors and prints some information about.

This is the Python@@@py_version_nodot@@@ version.

%prep
echo "Preparing '${builddir}' ..."
echo "Pwd: $( pwd )"
%autosetup -p1 -v

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fb_logging

echo "Whats in '%{builddir}':"
ls -lA '%{builddir}'

echo "Whats in '%{buildroot}':"
ls -lA '%{buildroot}'

%files -f %{pyproject_files}
%defattr(-,root,root,-)
%license LICENSE
%doc CHANGELOG.md LICENSE README.md pyproject.toml debian/changelog
%{_bindir}/*
%{_mandir}/*

%changelog
