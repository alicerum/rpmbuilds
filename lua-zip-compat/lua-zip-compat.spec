Name:     lua-zip-compat
Version:  1.2.7
Release:  3%{?dist}
Source0:  https://github.com/mpeterv/luazip/archive/%{version}.tar.gz
Summary:  Zip bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel zziplib-devel
Requires:      compat-lua-libs

%prep
%setup -q -n luazip-%{version}
sed -i 's@PREFIX = /usr/local@PREFIX = /usr@' config
sed -i 's@$(PREFIX)/lib/lua/5.$(LUA_VERSION_MINOR)@%{buildroot}%{_libdir}/lua/5.1/@' config
sed -i 's@$(PREFIX)/share/lua/5.$(LUA_VERSION_MINOR)@%{buildroot}%{_datarootdir}/lua/5.1/@' config
sed -i 's@ZZLIB_INC= /usr/local/include@ZZLIB_INC= %{_prefix}/include/@' config
sed -i 's@CFLAGS=@CFLAGS=%{optflags} @' config
sed -i 's@-shared@-shared %{__global_ldflags}@' config
sed -i 's@#include "lua.h"@#include <lua.h>@' src/luazip.h
sed -i 's@LUA_INC= $(PREFIX)/include@LUA_INC= $(PREFIX)/include/lua-5.1/@' config

%build
%make_build

%install
%make_install

%files
%{_libdir}/lua/5.1/*

%description
Lua zip library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Fri Oct 20 2017 Ilya Rum <elijahrum@gmail.com> - 1.2.7-1
- 1.2.7 version

* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 1.2.6-1
- Initial version of the package
