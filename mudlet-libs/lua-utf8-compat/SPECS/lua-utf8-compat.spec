Name:     lua-utf8-compat
Version:  0.1.1
Release:  1%{?dist}
Summary:  Utf8 bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel compat-luarocks

%prep
luarocks download luautf8
luarocks unpack luautf8

%build
cd luautf8-%{version}-1/luautf8-%{version}
luarocks make --local luautf8-%{version}-1.rockspec

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f luautf8-%{version}-1/luautf8-%{version}/lua-utf8.so %{buildroot}%{_libdir}/lua/5.1/

%files
%{_libdir}/lua/5.1/*

%description
Lua utf8 library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Sat Jul 08 2017 Ilya Rum <elijahrum@gmail.com> - 1.2-1
- Initial version of the package
