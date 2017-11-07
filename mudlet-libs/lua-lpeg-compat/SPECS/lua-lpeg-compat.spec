Name:     lua-lpeg-compat
Version:  1.0.1
Release:  2%{?dist}
Summary:  Lpeg bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel compat-luarocks

%prep
luarocks download lpeg
luarocks unpack lpeg

%build
cd lpeg-%{version}-1/lpeg-%{version}
luarocks make --local lpeg-%{version}-1.rockspec

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f lpeg-%{version}-1/lpeg-%{version}/lpeg.so %{buildroot}%{_libdir}/lua/5.1/

%files
%{_libdir}/lua/5.1/*

%description
Lua lrexlib with pcre library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
