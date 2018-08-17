Name:		corsix-th
Version:	0.62
Release:	1%{?dist}
Summary:	A reimplementation of the 1997 Bullfrog business sim Theme Hospital

License:	MIT
URL:		http://corsixth.com/
Source0:	https://github.com/CorsixTH/CorsixTH/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	SDL2-devel
BuildRequires:	lua-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel

Requires:	lua-filesystem
Requires:	lua-code-formatter
Requires:	lua-lpeg

%description
A reimplementation of the 1997 Bullfrog business sim Theme Hospital.
As well as faithfully recreating the original, CorsixTH adds support
for modern operating systems (Windows, Mac OSX and Linux), high resolutions and much more.

%prep
%setup -q -n CorsixTH-%{version}
mkdir build
cd build
%cmake ..

%build
cd build
make %{?_smp_mflags}

%install
cd build
%make_install


%files
%doc README.md CONTRIBUTING.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Fri Aug 17 2018 wyvie <wyvie@wyvie.org> - 0.62-1
- Initial build

