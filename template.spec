%define version @@@Version@@@
%define builddir python@@@py_version_nodot@@@_fb_logging-%{version}

Name:           python@@@py_version_nodot@@@-fb-logging
Version:        %{version}
Release:        @@@Release@@@%{?dist}
Summary:        Python modules to extend the logging mechanism in Python.

Group:          Development/Languages/Python
License:        LGPL-3
Distribution:   Frank Brehm
URL:            https://github.com/fbrehm/fb-logging
Source0:        fb_logging.%{version}.tar.gz

BuildRequires:  python@@@py_version_nodot@@@
BuildRequires:  python@@@py_version_nodot@@@-libs
BuildRequires:  python@@@py_version_nodot@@@-devel
BuildRequires:  python@@@py_version_nodot@@@-setuptools
Requires:       python@@@py_version_nodot@@@
Requires:       python@@@py_version_nodot@@@-libs
BuildArch:      noarch

%description
Python modules to extend the logging mechanism in Python.

This package provides the following script:
 * dch2speclog - converting a Debian changelog into log entries of a RPM spec file.

This is the Python@@@py_version_nodot@@@ version.

%prep
echo "Preparing '${builddir}-' ..."
%setup -n %{builddir}

%build
cd ../%{builddir}
python@@@py_version_dot@@@ setup.py build

%install
cd ../%{builddir}
echo "Buildroot: %{buildroot}"
python@@@py_version_dot@@@ setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%doc LICENSE README.md requirements.txt debian/changelog
%{_bindir}/*
%{python3_sitelib}/*

%changelog
