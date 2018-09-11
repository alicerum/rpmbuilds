Name:           mudlet
Version:        3.13.0
Release:        1%{?dist}
Summary:        Crossplatform mud client

License:        GPLv2+
Group:          Amusements/Games
URL:            http://www.mudlet.org/
Source0:	https://www.mudlet.org/wp-content/files/Mudlet-%{version}.tar.xz
Patch0:         mudlet-cmake.patch
Patch1:         mudlet-lua-path.patch
Patch2:         mudlet-lua-global.patch

BuildRequires:	gcc-c++
BuildRequires:  cmake,compat-lua-devel,libzip-devel,zlib-devel,pcre-devel,yajl-devel,hunspell-devel
BuildRequires:  qt5-qtbase-devel,qt5-qtmultimedia-devel,qt5-qttools-static,boost-devel
BuildRequires:  mesa-libGLU-devel pugixml-devel

Requires:       lua-code-formatter-compat
Requires:       lua-rex-pcre-compat
Requires:       lua-sqlite3-compat
Requires:       lua-utf8-compat
Requires:       lua-zip-compat
Requires:       lua-filesystem-compat

%description
Mudlet is a quality MUD client, designed to take mudding to a new level.

It’s a new breed of a client on the MUD scene – with an intuitive user interface, a specially designed scripting framework, and a very fast text display. Add to that cross-platform capability, an open-source development model, and you have a very likable MUD client.

%prep
%setup -cq mudlet-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
* Wed Sep 5 2018 wyvie <wyvie@wyvie.org> - 3.13.0-1
- 3.13.0 release

* Mon Aug 13 2018 wyvie <wyvie@wyvie.org> - 3.12.0-1
- 3.12.0 release

* Sun Jul 15 2018 wyvie <wyvie@wyvie.org> - 3.11.0-1
- 3.11.0 release

* Tue Jun 12 2018 wyvie <wyvie@wyvie.org> - 3.10.1-1
- bugfixes

* Sun Jun 10 2018 wyvie <wyvie@wyvie.org> - 3.10.0-1
- 3.10.0 release

* Thu May 10 2018 wyvie <wyvie@wyvie.org> - 3.9.0-2
- Moved lua dependencies to same repo and strong deps

* Wed May 9 2018 wyvie <irum@redhat.com> - 3.9.0-1
- 3.9.0 release

* Sun Apr 8 2018 wyvie <irum@redhat.com> - 3.8.0-1
- 3.8.0 release

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
