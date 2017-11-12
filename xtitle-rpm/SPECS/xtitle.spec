%global debug_package %{nil}

Name:		xtitle
Version:	0.4.3
Release:	1%{?dist}
Summary:	Simple console app that outputs X window titles

License:	Unlicense
URL:		https://github.com/baskerville/xtitle
Source0:	https://github.com/baskerville/%{name}/archive/%{version}.tar.gz

BuildRequires:	libxcb-devel xcb-util-devel xcb-util-wm-devel

%description
Outputs the title of the active window and continue to output it as it changes if the snoop mode is on

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/*

%changelog
* Sun Nov 12 2017 Ilya Rum <irum@redhat.com> - 0.4.3-1
- Initial build

