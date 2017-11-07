Name:     lua-rex-pcre-compat
Version:  2.8.0
Release:  2%{?dist}
Summary:  Lrexlib with pcre bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel compat-luarocks pcre-devel

%prep
luarocks download lrexlib-pcre
luarocks unpack lrexlib-pcre

%build
cd lrexlib-pcre-%{version}-1/lrexlib
luarocks make --local lrexlib-pcre-%{version}-1.rockspec

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f lrexlib-pcre-%{version}-1/lrexlib/rex_pcre.so %{buildroot}%{_libdir}/lua/5.1/

%files
%{_libdir}/lua/5.1/*

%description
Lua lrexlib with pcre library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
