Name:		vte-ng
Version:	0.50.2.a
Release:	2%{?dist}
Summary:	A library implementing a terminal emulator widget for GTK+

License:	LGPLv2.1
URL:		https://github.com/thestinger/vte-ng
Source0:	https://github.com/thestinger/%{name}/archive/%{version}.tar.gz

Provides:       vte291 = 0.52.1
Obsoletes:      vte291 <= 0.52.1
Provides:       vte-profile = 0.52.1
Obsoletes:      vte-profile <= 0.52.1

BuildRequires:	gtk-doc autoconf automake libtool intltool
BuildRequires:  glib2-devel
BuildRequires:  pango-devel
BuildRequires:  gtk3-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala-devel
BuildRequires:  gperf gperftools-devel

%description
VTE is a library (libvte) implementing a terminal emulator widget for GTK+,
and a minimal sample application (vte) using that.  Vte is mainly used in
gnome-terminal, but can also be used to embed a console/terminal in games,
editors, IDEs, etc.

%package devel
Requires: %{name}
Summary:  vte-ng development files

%description devel
This is a vte-ng development package

%prep
%setup -q
./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README NEWS
%license COPYING

%{_sysconfdir}/profile.d/*.sh
%{_libdir}/*so*
%{_bindir}/*
%{_libdir}/girepository-1.0/*.typelib

%{_datarootdir}/locale/*/LC_MESSAGES/*.mo

%files devel
%{_includedir}/*/*/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_datarootdir}/vala/vapi/*.vapi
%{_datarootdir}/gir-1.0/*.gir



%changelog
* Tue Apr 17 2018 Alice Rum <wyvie@wyvie.org> 0.50.2.a-1
- Initial
