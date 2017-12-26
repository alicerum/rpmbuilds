Name:           mudlet
Version:        3.7.1
Release:        1%{?dist}
Summary:        Crossplatform mud client

License:        GPLv2+
Group:          Amusements/Games
URL:            http://www.mudlet.org/
Source0:	https://www.mudlet.org/download/Mudlet-%{version}.tar.xz
Patch0:         mudlet-%{version}-cmake.patch
Patch1:         mudlet-3.0.0-ctelnet.patch
Patch2:         mudlet-%{version}-lua-path.patch
Patch3:         mudlet-%{version}-lua-global.patch
Patch4:         mudlet-3.0.0-hunspell.patch

BuildRequires:  cmake,compat-lua-devel,libzip-devel,zlib-devel,pcre-devel,yajl-devel,hunspell-devel
BuildRequires:  qt5-qtbase-devel,qt5-qtmultimedia-devel,qt5-qttools-static,boost-devel
BuildRequires:  mesa-libGLU-devel

%description
Mudlet is a quality MUD client, designed to take mudding to a new level.

It’s a new breed of a client on the MUD scene – with an intuitive user interface, a specially designed scripting framework, and a very fast text display. Add to that cross-platform capability, an open-source development model, and you have a very likable MUD client.

%prep
%setup -c mudlet-%{version}
%patch0 -p1
%patch2
%patch3

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
mkdir -pv %{buildroot}/usr/share/pixmaps/
cp src/icons/mudlet.png %{buildroot}/usr/share/pixmaps/
mkdir -pv %{buildroot}/usr/share/applications/
cp mudlet.desktop %{buildroot}/usr/share/applications/

%files
/usr/bin/*
/usr/share/mudlet
/usr/share/pixmaps/*
/usr/share/applications/*

%changelog
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
