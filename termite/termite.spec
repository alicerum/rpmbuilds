%global util_commit 62faf9e46b8c4ab213ac42aaf6343dea9e2dfc1e
%global debug_package %{nil}

Name:		termite
Version:	13
Release:	1%{?dist}
Summary:	A keyboard-centric VTE-based terminal

License:	Unlicensed
URL:		https://github.com/thestinger/termite
Source0:	https://github.com/thestinger/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/thestinger/util/archive/%{util_commit}.zip

BuildRequires:	vte-ng-devel

%description
A keyboard-centric VTE-based terminal, aimed at use within a window manager with tiling and/or tabbing support.

%prep
%setup -q
rmdir util
unzip %{_sourcedir}/%{util_commit}.zip
mv util-%{util_commit} util
sed -i "s/-DNDEBUG/-DDEBUG/g" Makefile

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}
%{_datarootdir}/applications/%{name}.desktop
%{_mandir}/*/%{name}*
%{_datarootdir}/terminfo/x/xterm-%{name}

%changelog
* Tue Apr 17 2018 Alice Rum <wyvie@wyvie.org> 13-1
- Initial

