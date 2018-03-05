%global debug_package %{nil}

Name:		compton
Version:	0.1
Release:	1%{?dist}
Summary:	Compositor for X

License:	GPLv2
URL:		https://github.com/chjj/compton
Source0:	https://github.com/chjj/compton/archive/master.zip

BuildRequires:	libX11-devel libXcomposite-devel libXdamage-devel
BuildRequires:  libXfixes-devel libXext-devel libXrender-devel
BuildRequires:  libXrandr-devel libXinerama-devel
BuildRequires:  pcre-devel libconfig-devel libdrm-devel mesa-libGL-devel 
BuildRequires:  dbus-devel asciidoc

%description

%prep
%setup -n compton-master

%build
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
/usr/share/applications/*
/usr/share/icons/hicolor/48x48/apps/*
/usr/share/icons/hicolor/scalable/apps/*
%{_mandir}/man1/*

%changelog
* Sun Oct 22 2017 Ilya Rum <elijahrum@gmail.com> - 0.1-1
- Initial version of the package
