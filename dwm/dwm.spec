Name:		dwm
Version:	6.1
Release:	4%{?dist}
Epoch:		2
Summary:	A tiling window manager

License:	MIT
URL:		https://dwm.suckless.org/
Source0:	https://github.com/wyvie/dwm/archive/master.zip
Source1:	dwm.desktop

BuildRequires:	libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel
BuildRequires:  freetype-devel
BuildRequires:  clang

%description
Dynamic window manager with patches by wyvie

%prep
%setup -q -n dwm-master
sed -i 's@dwm-"VERSION@dwm-%{version}"@' dwm.c

%build
make %{?_smp_mflags} \
	CFLAGS="%{optflags} -I/usr/include/freetype2 -DXINERAMA" \
	LDFLAGS="%{__global_ldflags} -lXft -lXinerama -lX11 -lfreetype -lfontconfig" \
	CC="gcc"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/xsessions
install -m 0755 %{name} %{buildroot}%{_bindir}
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions

%files
%doc README TODO
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Tue Aug 14 2018 wyvie <wyvie@wyvie.org> - 6.1-4
- turn on xinerama

* Mon Aug 13 2018 wyvie <wyvie@wyvie.org> - 6.1-3
- removed windows restack warping

* Sat Aug 11 2018 wyvie <wyvie@wyvie.org> - 6.1-2
- changed terminal

* Sat Aug 11 2018 wyvie <wyvie@wyvie.org> - 6.1-1
- initial build

