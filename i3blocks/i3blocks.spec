Name:     i3blocks
Version:  1.4
Release:  5%{?dist}
Summary:  Highly flexible status line for the i3 window manager
License:  GPLv3+
URL:      https://github.com/vivien/i3blocks/  
Source0:  https://github.com/vivien/i3blocks/releases/download/%{version}/i3blocks-%{version}.tar.gz

%description
i3blocks is a highly flexible status line for the i3 window manager.
It handles clicks, signals and language-agnostic user scripts.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags} -Iinclude" LDFLAGS="%{__global_ldflags}" PREFIX="%{_prefix}"

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.md CHANGELOG.md
%license COPYING

%{_bindir}/%{name}
%{_sysconfdir}/%{name}.conf
%{_libexecdir}/i3blocks
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Feb 26 2018 Alice Rum <irum@redhat.com> - 1.4-1
- Initial version of the package
