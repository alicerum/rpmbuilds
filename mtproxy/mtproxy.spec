%global commit 580909cbca12a2f8529dbb387edf8e9bc5bd4e3a
%global shortcommit 580909c

Name:		mtproxy
Version:	0
Release:	rc3.%{shortcommit}%{?dist}
Summary:	Mtproto proxy for telegram

License:	GPLv2
URL:		https://github.com/TelegramMessenger/MTProxy
Source0:	https://github.com/TelegramMessenger/MTProxy/archive/%{commit}.zip

BuildRequires:	openssl-devel

%description
This is a proxy for telegram.

%prep
%setup -q -n MTProxy-%{commit}
sed -i 's@CFLAGS =@CFLAGS = %{optflags}@' Makefile
sed -i 's@LDFLAGS =@LDFLAGS = %{__global_ldflags}@' Makefile
sed -i 's@-Werror=format-security @@' Makefile


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
cp objs/bin/mtproto-proxy %{buildroot}%{_bindir}

%files
%doc README
%license GPLv2 LGPLv2
%{_bindir}/mtproto-proxy


%changelog
* Tue Jun 4 2018 wyvie <wyvie@wyvie.org> - 0-rc3.580909c
- Fixed PID.ip assertion

* Sat Jun 2 2018 wyvie <wyvie@wyvie.org> - 0-rc0.3ee1c5
- Initial
