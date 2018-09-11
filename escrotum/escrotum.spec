%global pypi_name escrotum

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        UNKNOWN

License:        None
URL:            https://github.com/Roger/escrotum
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

%description
Escrotum
========

Linux screen capture using pygtk, inspired by scrot

Why?
----

Because scrot has glitches when selection is used in refreshing windows
Features
--------

* fullscreen screenshots
* partial(selection) screenshots
*
window screenshot(click to select)
* screenshot by xid
* store the image to the
clipboard

::

    Usage: escrotum [filename]

    Options:
      -h, --help
...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(setuptools) pygtk2
%description -n python2-%{pypi_name}
Escrotum
========

Linux screen capture using pygtk, inspired by scrot

Why?
----

Because scrot has glitches when selection is used in refreshing windows
Features
--------

* fullscreen screenshots
* partial(selection) screenshots
*
window screenshot(click to select)
* screenshot by xid
* store the image to the
clipboard

::

    Usage: escrotum [filename]

    Options:
      -h, --help
...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/escrotum
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Aug 31 2018 wv - 0.2.1-1
- Initial package.
