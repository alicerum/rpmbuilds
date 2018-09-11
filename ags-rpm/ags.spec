Name:		ags
Version:	3.4.1.14
Release:	1%{?dist}
Summary:	Visual adventure game engine

License:	Artistic
URL:		http://www.adventuregamestudio.co.uk/
Source0:	https://github.com/adventuregamestudio/ags/archive/v.%{version}.tar.gz

BuildRequires:	allegro-devel dumb-devel freetype-devel libogg-devel libtheora-devel libvorbis-devel
BuildRequires:	libXext-devel libXxf86vm-devel

%description
AGS provides everything you need from within one easy-to-use application. Create, test and debug your game, all in one place.

%prep
%setup -n %{name}-v.%{version}
sed -i.bak 's@CFLAGS := -O2 -g -fsigned-char -Wfatal-errors@CFLAGS := %{optflags}@' Engine/Makefile-defs.linux
sed -i.bak 's@LDFLAGS  += -Wl,--as-needed@LDFLAGS  += %{__global_ldflags}@' Engine/Makefile-defs.linux

%build
make --directory=Engine

%install
%make_install --directory=Engine PREFIX="%{buildroot}/%{_prefix}"

%files
%license License.txt
%doc README.md
%{_bindir}/*

%changelog
* Wed Aug 29 2018 wyvie <wyvie@wyvie.org> - 3.4.1.14-1
- New upstream version - 3.4.1.14

* Sun Jan 28 2018 wyvie <wyvie@wyvie.org> - 3.4.1.12-1
- New upstream version - 3.4.1.12

* Tue Dec 26 2017 wyvie <wyvie@wyvie.org> - 3.4.1.11-1
- New upstream version - 3.4.1.11

* Wed Dec 13 2017 wyvie <wyvie@wyvie.org> - 3.4.1.10-1
- New upstream version - 3.4.1.10

* Tue Nov 14 2017 wyvie <wyvie@wyvie.org> - 3.4.1.9-1
- New upstream version - 3.4.1.9

* Thu Oct 26 2017 wyvie <wyvie@wyvie.org> - 3.4.1.7-1
- Initial version of package

