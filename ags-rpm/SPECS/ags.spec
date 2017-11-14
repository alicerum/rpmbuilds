Name:		ags
Version:	3.4.1.9
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

%build
make --directory=Engine %{?_smp_mflags}

%install
%make_install --directory=Engine PREFIX="%{buildroot}/%{_prefix}"

%files
%{_bindir}/*

%changelog
* Tue Nov 14 2017 wyvie <irum@redhat.com> - 3.4.1.9-1
- New upstream version - 3.4.1.9

* Thu Oct 26 2017 wyvie <irum@redhat.com> - 3.4.1.7-1
- Initial version of package

