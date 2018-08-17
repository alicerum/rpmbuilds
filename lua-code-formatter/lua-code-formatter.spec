Name:      lua-code-formatter
Version:   5.3.4
Release:   1%{?dist}
Source0:   https://github.com/martin-eden/lua_code_formatter/archive/5.3-4.tar.gz
Summary:   Lua code formatter for lua-5.1
License:   GPLv3+
BuildArch: noarch

Requires: lua

BuildRequires: unzip

%prep
%setup -q -n lua_code_formatter-5.3-4

%install
mkdir -p %{buildroot}%{_datarootdir}/lua/5.3/lcf

cp -r get_ast %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp    get_ast.lua %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp -r get_formatter_ast %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp    get_formatter_ast.lua %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp -r reformat %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp    reformat.lua %{buildroot}%{_datarootdir}/lua/5.3/lcf/
cp -r workshop %{buildroot}%{_datarootdir}/lua/5.3/lcf/

%files
%{_datarootdir}/lua/5.3/*

%description
Lua code formatter built for lua-5.3.

%changelog
* Fri Aug 17 2018 wyvie <wyvie@wyvie.org> - 5.3.4-1
- Initial build

