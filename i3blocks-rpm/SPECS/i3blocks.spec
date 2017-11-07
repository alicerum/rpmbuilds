%global debug_package %{nil}

Name:     i3blocks
Version:  1.4
Release:  4%{?dist}
Summary:  Highly flexible status line for the i3 window manager
License:  GPLv3+
URL:      https://github.com/vivien/i3blocks/  
Source0:  https://github.com/vivien/i3blocks/releases/download/%{version}/i3blocks-%{version}.tar.gz

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX="/usr"

%files
%{_sysconfdir}/*
%{_bindir}/*
%{_libexecdir}/i3blocks/*
%{_mandir}/man1/*

%description
i3blocks is a highly flexible status line for the i3 window manager. It handles clicks, signals and language-agnostic user scripts.

%changelog
* Sat Mar 11 2017 Ilya Rum <elijahrum@gmail.com> - 1.4-3
- Moved scripts from /usr/lib to /usr/libexec

* Sat Mar 11 2017 Ilya Rum <elijahrum@gmail.com> - 1.4-2
- Fixed package description to be less robust

* Sat Mar 11 2017 Ilya Rum <elijahrum@gmail.com> - 1.4-1
- Initial version of the package
