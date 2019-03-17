Name:     lua-yajl-compat
Version:  2.0
Release:  2%{?dist}
Source0:  https://github.com/brimworks/lua-yajl/archive/v%{version}.tar.gz
Summary:  Lrexlib with pcre bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel yajl-devel gcc
Requires:      compat-lua-libs

%prep
%setup -q -n lua-yajl-%{version}

%build
gcc %{optflags} -fPIC -llua-5.1 -I/usr/include/lua-5.1 -c lua_yajl.c
gcc %{__global_ldflags} -lyajl lua_yajl.o -shared -o yajl.so.%{version}

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f yajl.so.%{version} %{buildroot}%{_libdir}/lua/5.1/
ln -s %{_libdir}/lua/5.1/yajl.so.%{version} %{buildroot}%{_libdir}/lua/5.1/yajl.so

%files
%{_libdir}/lua/5.1/*

%description
Lua yajl lib with pcre library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.9.0-2
- Build more against fedora guidelines and without luarocks

* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
