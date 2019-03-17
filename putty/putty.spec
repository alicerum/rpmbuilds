Name:		putty
Version:	0.70
Release:	1%{?dist}
Epoch:          1
Summary:	Free implementation of SSH and Telnet for Windows and Unix platforms, along with an xterm terminal emulator

License:	MIT
URL:		https://www.chiark.greenend.org.uk/~sgtatham/putty/
Source0:	https://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz

BuildRequires:	gcc gtk3-devel

%description
PuTTY is a free implementation of SSH and Telnet for Windows and Unix platforms, along with an xterm terminal emulator.

%prep
%setup -q


%build
%configure
sed -i 's@-Werror=format-security @-Werror=format-security -Wno-error=format-overflow -Wno-error=deprecated-declarations @' Makefile
make %{?_smp_mflags}


%install
%make_install


%files
%doc README
%license LICENCE
%{_bindir}/*
%{_mandir}/man1/*.1.gz


%changelog
* Thu Dec 6 2018 wyvie <wyvie@wyvie.org> - 0.70-1
- initial build

