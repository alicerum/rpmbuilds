Name:     lua-sqlite3-compat
Version:  2.3.0
Release:  4%{?dist}
Summary:  Sqlite3 bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel compat-luarocks libsq3-devel

%prep
luarocks download luasql-sqlite3
luarocks unpack luasql-sqlite3

%build
cd luasql-sqlite3-%{version}-1/luasql
luarocks make --local luasql-sqlite3-%{version}-1.rockspec

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/luasql
cp -f luasql-sqlite3-%{version}-1/luasql/luasql/sqlite3.so %{buildroot}%{_libdir}/lua/5.1/luasql/

%files
%{_libdir}/lua/5.1/*

%description
Lua libraries built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
