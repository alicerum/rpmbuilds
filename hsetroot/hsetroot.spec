%global commit a6248105c130a56391afae9df9f9e68d00e81a1b

Name:		hsetroot
Version:	1.0.2
Release:	1%{?dist}
Summary:	imlib2-based wallpaper changer

License:	GPLv2
URL:		https://github.com/himdel/hsetroot/
Source0:	https://github.com/himdel/hsetroot/archive/%{commit}.zip

BuildRequires:	imlib2-devel
BuildRequires:  libX11-devel

%description
imlib2-based wallpaper changer

%prep
%setup -q -n hsetroot-%{commit}

%build
make CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags} -lX11 -lImlib2"

%install
install -d %{buildroot}%{_bindir}
install -m 0755 -p hsetroot %{buildroot}%{_bindir}

%files
%doc Makefile README.md
%{_bindir}/hsetroot

%changelog
* Tue Aug 7 2018 wyvie <wyvie@wyvie.org> - 0.1-0.rc0.gita62481
- initial build

