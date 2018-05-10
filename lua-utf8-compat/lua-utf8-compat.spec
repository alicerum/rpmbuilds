Name:     lua-utf8-compat
Version:  0.1.1
Release:  2%{?dist}
Source0:  https://github.com/starwing/luautf8/archive/%{version}.tar.gz
Summary:  Utf8 bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel
Requires:      compat-lua-libs

%prep
%setup -q -n luautf8-%{version}

%build
gcc %{optflags} -fPIC -I/usr/include/lua-5.1 -c lutf8lib.c
gcc %{__global_ldflags} lutf8lib.o -shared -o lua-utf8.so.%{version}

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f lua-utf8.so.%{version} %{buildroot}%{_libdir}/lua/5.1/
ln -s %{_libdir}/lua/5.1/lua-utf8.so.%{version} %{buildroot}%{_libdir}/lua/5.1/lua-utf8.so

%files
%{_libdir}/lua/5.1/*

%description
Lua utf8 library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Thu May 10 2018 Alice Rum <wyvie@wyvie.com> - 0.1.1-2
- Initial version of the package
