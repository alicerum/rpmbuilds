Name:      lua-code-formatter-compat
Version:   5.1.2
Release:   2%{?dist}
Source0:   https://github.com/martin-eden/lua_code_formatter/archive/5.1-2.tar.gz
Summary:   Lua code formatter for lua-5.1
License:   GPLv3+
BuildArch: noarch

Requires: compat-lua-libs

BuildRequires: unzip

%prep
%setup -q -n lua_code_formatter-5.1-2

%install
mkdir -p %{buildroot}%{_datarootdir}/lua/5.1/lcf

cp -r get_ast %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp    get_ast.lua %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp -r get_formatter_ast %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp    get_formatter_ast.lua %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp -r reformat %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp    reformat.lua %{buildroot}%{_datarootdir}/lua/5.1/lcf/
cp -r workshop %{buildroot}%{_datarootdir}/lua/5.1/lcf/

%files
%{_datarootdir}/lua/5.1/*

%description
Lua code formatter built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Fri Aug 17 2018 wyvie <wyvie@wyvie.org> - 5.1-2
- Dependency to compat-lua-libs

* Sun Dec 03 2017 wyvie <wyvie@wyvie.org> - 5.1-1
- Initial version of the package
