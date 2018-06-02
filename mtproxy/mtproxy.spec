%global commit 3ee1c47232105208dab2dbe07f78862aa7dea58b
%global shortcommit 3ee1c4

Name:		mtproxy
Version:	0
Release:	rc1.%{shortcommit}%{?dist}
Summary:	Mtproto proxy for telegram

License:	GPLv2
URL:		https://github.com/TelegramMessenger/MTProxy
Source0:	https://github.com/TelegramMessenger/MTProxy/archive/%{commit}.zip
Patch0:         pid.patch

BuildRequires:	openssl-devel

%description
This is a proxy for telegram.

%prep
%setup -q -n MTProxy-%{commit}
%patch0 -p1
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
* Sat Jun 2 2018 wyvie <wyvie@wyvie.org> - 0-rc0.3ee1c5
- Initial
