%global i3ipc_commit a6aa7a19786bdf7b96a02900510b3b3c325c8bdf
%global xpp_commit 00165e1a6d5dd61bc153e1352b21ec07fc81245d

Name:		polybar
Version:	3.1.0
Release:	1%{?dist}
Summary:	A fast and easy-to-use tool for creating status bars

License:	MIT
URL:		https://github.com/jaagr/polybar
Source0:	https://github.com/jaagr/%{name}/archive/%{version}.tar.gz
Source1:        https://github.com/jaagr/i3ipcpp/archive/%{i3ipc_commit}.zip
Source2:        https://github.com/jaagr/xpp/archive/%{xpp_commit}.zip
Patch0:         polybar-libs.patch

BuildRequires:	cairo-devel cmake alsa-lib-devel
BuildRequires:  cairo-devel xcb-proto xcb-util-devel xcb-util-wm-devel xcb-util-image-devel xcb-util-cursor-devel
BuildRequires:  i3-ipc jsoncpp-devel pulseaudio-libs-devel wireless-tools-devel libmpdclient-devel libcurl-devel
BuildRequires:  libxcb-devel xcb-util-xrm-devel
BuildRequires:  python2
Requires:	python2

%description
Polybar aims to help users build beautiful and highly customizable
status bars for their desktop environment, without the need of
having a black belt in shell scripting.

%prep
%setup -q
%patch0 -p1
cd lib/
rmdir i3ipcpp
unzip %{_sourcedir}/%{i3ipc_commit}.zip
mv i3ipcpp-%{i3ipc_commit} i3ipcpp
rmdir xpp
unzip %{_sourcedir}/%{xpp_commit}.zip
mv xpp-%{xpp_commit} xpp
cd ../
mkdir build
cd build
%cmake ..

%build
cd build
make %{?_smp_mflags}


%install
cd build
%make_install
install -d %{buildroot}%{_libdir}
install -m 0755 -p lib/xpp/libxpp.so %{buildroot}%{_libdir}


%files
%doc README.md SUPPORT.md
%license LICENSE

%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datarootdir}/bash-completion/completions/%{name}
%{_datarootdir}/zsh/site-functions/*
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_libdir}/libxpp.so



%changelog

