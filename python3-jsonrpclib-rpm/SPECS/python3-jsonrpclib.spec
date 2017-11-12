%global srcname jsonrpclib

Name:           python3-%{srcname}
Version:        0.1.7
Release:        1%{?dist}
Summary:        JSON-RPC v2.0 client library for Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:		xmlrpc.patch
Patch1:		jsonrpcserver.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This project is an implementation of the JSON-RPC v2.0 specification
(backwards-compatible) as a client library.


%prep
%setup -q -n %{srcname}-%{version}
%patch0
%patch1


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Ihar Hrachyshka <ihrachys@redhat.com> 0.1.7-1.el7
- Update to 0.1.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.1.3-2
- Added missing python-setuptools build dependency.
- Added python macros for el6.
- Other stylistic changes.

* Thu Aug  7 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.1.3-1
- Initial package for Fedora
