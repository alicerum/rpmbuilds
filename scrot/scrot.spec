%global commit 974fc6b77af4abdec59568efa3e4ff57dae15453

Name:		scrot
Version:	0.9
Release:	0.rc0%{?dist}
Summary:	scrot (SCReen shOT) is a simple commandline screen capture utility

License:	GPLv3
URL:		https://github.com/dreamer/scrot
Source0:	https://github.com/dreamer/scrot/archive/%{commit}.zip

BuildRequires:	giblib-devel

%description
scrot (SCReen shOT) is a simple commandline screen capture utility
in this package it is built from master branch

%prep
%setup -n scrot-%{commit}


%build
sed -i 's|INCLUDES = -g -O3 -Wall|INCLUDES =|' src/Makefile.in
sed -i 's|CFLAGS = @CFLAGS@|CFLAGS = %{optflags} @CFLAGS@|' src/Makefile.in
sed -i 's|LDFLAGS =|LDFLAGS = %{__global_ldflags}|' src/Makefile.in

%configure
sed -i 's@docsdir = $(prefix)/doc/scrot@docsdir = $(prefix)/share/doc/scrot@g' Makefile
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_datadir}/man/man1/%{name}.1.gz



%changelog
* Fri Feb 23 2018 wyvie <irum@redhat.com> 0.9-0.rc0
- initial
