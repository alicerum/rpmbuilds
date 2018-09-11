# Created by pyp2rpm-3.2.1
%global pypi_name notify2

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        2%{?dist}
Summary:        Python interface to DBus notifications

License:        TODO
URL:            https://bitbucket.org/takluyver/pynotify2
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  dbus-python

%description
This is a purepython replacement for notifypython, using pythondbus to
communicate with the notifications server directly. It's compatible with Python
2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.To use it,
first call notify2.init('app name'), then create and show notifications:: n
notify2.Notification("Summary", "Some body text", "notificationmessageim" Icon
name ) ...

%package -n     python2-%{pypi_name}
Requires:	python2-dbus
Summary:        Python interface to DBus notifications
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This is a purepython replacement for notifypython, using pythondbus to
communicate with the notifications server directly. It's compatible with Python
2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.To use it,
first call notify2.init('app name'), then create and show notifications:: n
notify2.Notification("Summary", "Some body text", "notificationmessageim" Icon
name ) ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%define _unpackaged_files_terminate_build 0
%doc 

%{python2_sitelib}/%{pypi_name}.py
%{python2_sitelib}/%{pypi_name}.pyc
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sat Mar 11 2017 wyvie <wyvie@wyvie.org> - 0.3.1-2
- Added runtime dependency to dbus

* Sat Mar 11 2017 wyvie <wyvie@wyvie.org> - 0.3.1-1
- Initial package
