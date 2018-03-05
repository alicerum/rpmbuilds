Name:           mudlet
Version:        3.7.1
Release:        4%{?dist}
Summary:        Crossplatform mud client

License:        GPLv2+
Group:          Amusements/Games
URL:            http://www.mudlet.org/
Source0:	https://www.mudlet.org/download/Mudlet-%{version}.tar.xz
Patch0:         mudlet-cmake.patch
Patch1:         mudlet-lua-path.patch
Patch2:         mudlet-lua-global.patch

BuildRequires:  cmake,compat-lua-devel,libzip-devel,zlib-devel,pcre-devel,yajl-devel,hunspell-devel
BuildRequires:  qt5-qtbase-devel,qt5-qtmultimedia-devel,qt5-qttools-static,boost-devel
BuildRequires:  mesa-libGLU-devel

%description
Mudlet is a quality MUD client, designed to take mudding to a new level.

It’s a new breed of a client on the MUD scene – with an intuitive user interface, a specially designed scripting framework, and a very fast text display. Add to that cross-platform capability, an open-source development model, and you have a very likable MUD client.

%prep
%setup -c mudlet-%{version}
%patch0 -p1
%patch1
%patch2

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_datadir}/pixmaps/
install -d %{buildroot}%{_datadir}/applications/
install -m 0644 -p src/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/
install -m 0644 -p %{name}.desktop %{buildroot}%{_datadir}/applications/

%files
%doc COMPILE README.md
%license COPYING
%{_bindir}/*
%{_datadir}/mudlet
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Mar 05 2018 wyvie <irum@redhat.com> - 3.7.1-4
- fix rpm structure
- added lincense and docs

* Wed Feb 14 2018 wyvie <irum@redhat.com> - 3.7.1-3
- fix version of mudlet

* Wed Jan 31 2018 wyvie <irum@redhat.com> - 3.7.1-2
- dependencies rebuild

* Tue Dec 26 2017 wyvie <irum@redhat.com> - 3.7.1-1
- 3.7.1 release

* Sat Dec 23 2017 wyvie <irum@redhat.com> - 3.7.0-1
- 3.7.0 release

* Wed Dec 06 2017 wyvie <irum@redhat.com> - 3.6.1-2
- Hunspell 1.6.0 in rawhide

* Wed Dec 06 2017 wyvie <irum@redhat.com> - 3.6.1-1
- 3.6.1 is released

* Sun Dec 03 2017 wyvie <irum@redhat.com> - 3.6.0-1
- 3.6.0 is released

* Wed Oct 18 2017 wyvie <irum@redhat.com> - 3.5.0-1
- 3.5.0 is released

* Mon Aug 14 2017 wyvie <irum@redhat.com> - 3.4.0-1
- 3.4.0 is released

* Sat Mar 25 2017 wyvie <irum@redhat.com> - 3.0.0-20
- 3.0.0 finally released

* Thu Mar 16 2017 wyvie <irum@redhat.com> - 3.0.0-13
- Kappa preview version is now out.

* Thu May 19 2016 wyvie <irum@redhat.com>
- Made mudlet look for mudlet-lua on absolute path.

* Tue May 17 2016 wyvie <irum@redhat.com>
- Fixed dependencies of rpm package.
