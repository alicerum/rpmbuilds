Name:     compat-luarocks
Version:  2.4.2
Release:  2%{?dist}
Summary:  A package manager for Lua modules.
License:  GPLv3+
URL:      https://github.com/luarocks/luarocks/  
Source0:  https://github.com/luarocks/luarocks/archive/v%{version}.tar.gz

BuildRequires: compat-lua-devel compat-lua

Requires: compat-lua

%global debug_package %{nil}

%prep
%autosetup -n luarocks-%{version}

%build
./configure --prefix="/usr" --with-lua-include="/usr/include/lua-5.1"
sed -i 's@/usr/bin/env lua@/usr/bin/env lua-5.1@' src/bin/luarocks
%make_build

%install
%make_install

%files
/usr/bin/*
/usr/share/lua/5.1/luarocks/*
/etc/luarocks/config-5.1.lua

%description
It allows you to install Lua modules as self-contained packages called rocks, which also contain version dependency information.

%changelog
* Tue Mar 14 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
