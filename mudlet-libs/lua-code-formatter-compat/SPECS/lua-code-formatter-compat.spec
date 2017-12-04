Name:      lua-code-formatter-compat
Version:   5.1
Release:   1%{?dist}
Summary:   Lua code formatter for lua-5.1
License:   GPLv3+
BuildArch: noarch

BuildRequires: compat-luarocks unzip

%prep
luarocks unpack lcf

%build
cd lcf-%{version}-1/lua_code_formatter/

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/lcf

cp -r lcf-%{version}-1/lua_code_formatter/get_ast %{buildroot}%{_libdir}/lua/5.1/lcf/
cp    lcf-%{version}-1/lua_code_formatter/get_ast.lua %{buildroot}%{_libdir}/lua/5.1/lcf/
cp -r lcf-%{version}-1/lua_code_formatter/get_formatter_ast %{buildroot}%{_libdir}/lua/5.1/lcf/
cp    lcf-%{version}-1/lua_code_formatter/get_formatter_ast.lua %{buildroot}%{_libdir}/lua/5.1/lcf/
cp -r lcf-%{version}-1/lua_code_formatter/reformat %{buildroot}%{_libdir}/lua/5.1/lcf/
cp    lcf-%{version}-1/lua_code_formatter/reformat.lua %{buildroot}%{_libdir}/lua/5.1/lcf/
cp -r lcf-%{version}-1/lua_code_formatter/workshop %{buildroot}%{_libdir}/lua/5.1/lcf/

%files
%{_libdir}/lua/5.1/*

%description
Lua code formatter built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Sun Dec 03 2017 Ilya Rum <elijahrum@gmail.com> - 5.1-1
- Initial version of the package
