%global commit a6248105c130a56391afae9df9f9e68d00e81a1b

Name:		hsetroot
Version:	1.0.2
Release:	2%{?dist}
Summary:	imlib2-based wallpaper changer

License:	GPLv2
URL:		https://github.com/himdel/hsetroot/
Source0:	https://github.com/himdel/hsetroot/archive/%{commit}.zip

BuildRequires:	imlib2-devel
BuildRequires:  libX11-devel
BuildRequires:  gcc

%description
imlib2-based wallpaper changer

%prep
%setup -q -n hsetroot-%{commit}

%build
make CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags} -lX11 -lImlib2" CC="gcc"

%install
install -d %{buildroot}%{_bindir}
install -m 0755 -p hsetroot %{buildroot}%{_bindir}

%files
%doc Makefile README.md
%{_bindir}/hsetroot

%changelog
* Sat Aug 11 2018 wyvie <wyvie@wyvie.org> - 1.0.2-2
- fixed build for f29

* Tue Aug 7 2018 wyvie <wyvie@wyvie.org> - 1.0.2-1
- initial build

