Name:		utimer
Version:	0.4
Release:	1%{?dist}
Summary:	Simple console timer application

License:	GPLv2
URL:		https://sourceforge.net/projects/utimer/
Source0:	https://downloads.sourceforge.net/project/utimer/utimer-%{version}.tar.gz

BuildRequires:	gcc glib-devel glib2-devel intltool

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/utimer*.1*

%changelog
* Mon Nov 06 2017 Ilya Rum <irum@redhat.com> - 0.4-1
- Initial Version
