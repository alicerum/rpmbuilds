%global commit 2c942119c4ee340c80922ba11d14fb3b10d5e654
%global shortcommit 2c92119

Name:		mtproxy
Version:	0
Release:	rc4.%{shortcommit}%{?dist}
Summary:	Mtproto proxy for telegram

License:	GPLv2
URL:		https://github.com/TelegramMessenger/MTProxy
Source0:	https://github.com/TelegramMessenger/MTProxy/archive/%{commit}.zip

BuildRequires:	openssl-devel zlib-devel

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
%doc README.md
%license GPLv2 LGPLv2
%{_bindir}/mtproto-proxy


%changelog
* Thu Mar 14 2019 wyvie <wyvie@wyvie.org> - 0-rc4.2c92119
- Fixed PID.ip assertion

* Mon Jun 4 2018 wyvie <wyvie@wyvie.org> - 0-rc3.580909c
- Fixed PID.ip assertion

* Sat Jun 2 2018 wyvie <wyvie@wyvie.org> - 0-rc0.3ee1c5
- Initial
