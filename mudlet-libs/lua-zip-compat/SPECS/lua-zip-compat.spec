Name:     lua-zip-compat
Version:  1.2.7
Release:  1%{?dist}
Summary:  Zip bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel compat-luarocks zziplib-devel

%prep
luarocks download LuaZip
luarocks unpack LuaZip

%build
cd luazip-%{version}-1/luazip
luarocks make --local luazip-%{version}-1.rockspec

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f luazip-%{version}-1/luazip/zip.so %{buildroot}%{_libdir}/lua/5.1/

%files
%{_libdir}/lua/5.1/*

%description
Lua zip library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Fri Oct 20 2017 Ilya Rum <elijahrum@gmail.com> - 1.2.7-1
- 1.2.7 version

* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 1.2.6-1
- Initial version of the package
