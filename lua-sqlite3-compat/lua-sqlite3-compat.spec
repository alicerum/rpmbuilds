Name:     lua-sqlite3-compat
Version:  2.3.5
Release:  3%{?dist}
Source0:  https://github.com/keplerproject/luasql/archive/v%{version}.tar.gz
Summary:  Sqlite3 bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel sqlite-devel
Requires:      compat-lua-libs

%prep
%setup -q -n luasql-%{version}
sed -i 's@#include "lua.h"@#include <lua.h>@' src/luasql.c
sed -i 's@#include "lua.h"@#include <lua.h>@' src/ls_sqlite3.c
sed -i 's@#include "sqlite3.h"@#include <sqlite3.h>@' src/ls_sqlite3.c
sed -i 's@LUA_SYS_VER ?= 5.2@LUA_SYS_VER ?= 5.1@' config
sed -i 's@LUA_INC ?= $(PREFIX)/include/lua$(LUA_SYS_VER)@LUA_INC ?= $(PREFIX)/include/lua-$(LUA_SYS_VER)@' config
sed -i 's@LUA_INC ?= $(PREFIX)/share/lua$(LUA_SYS_VER)@LUA_INC ?= $(PREFIX)/share/lua-$(LUA_SYS_VER)@' config
sed -i 's@CFLAGS = @CFLAGS = %{optflags} @' config
sed -i 's@LUA_LIBDIR ?= $(PREFIX)/lib/lua/$(LUA_SYS_VER)@LUA_LIBDIR ?= %{buildroot}%{_libdir}/lua/$(LUA_SYS_VER)/@' config
sed -i 's@LIB_OPTION ?= -shared@LIB_OPTION ?= -shared %{__global_ldflags} @' config

%build
%make_build sqlite3

%install
%make_install

%files
%{_libdir}/lua/5.1/*

%description
Lua libraries built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed May 9 2018 Alice Rum <wyvie@wyvie.org> - 2.3.5-1
- Built without luarocks
