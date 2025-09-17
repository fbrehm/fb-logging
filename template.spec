%define version @@@Version@@@
%define builddir python@@@py_version_nodot@@@_fb-logging-%{version}

Name:           python@@@py_version_nodot@@@-fb-logging
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
BuildRequires:  pyproject-rpm-macros
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-libs
BuildArch:      noarch

%description
Python modules to extend the logging mechanism in Python.

This package provides the following script:
 * dch2speclog - converting a Debian changelog into log entries of a RPM spec file.

This is the Python@@@py_version_nodot@@@ version.

%prep
echo "Preparing '${builddir}-' ..."
echo "Pwd: $( pwd )"
%autosetup -p1 -v

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fb_logging

# cd ../%{builddir}
# echo "Pwd: $( pwd )"
# echo "Buildroot: %{buildroot}"
# pip3 install --user -v . --no-deps --root %{buildroot} --use-pep517
# # python@@@py_version_dot@@@ setup.py install --prefix=%{_prefix} --root=%{buildroot}
# ls -l %{buildroot}

%files -f %{pyproject_files}
%defattr(-,root,root,-)
%license LICENSE
%doc LICENSE README.md requirements.txt debian/changelog
%{_bindir}/*

%changelog
