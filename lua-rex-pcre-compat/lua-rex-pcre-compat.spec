Name:     lua-rex-pcre-compat
Version:  2.9.0
Release:  4%{?dist}
Source0:  https://github.com/rrthomas/lrexlib/archive/rel-2-9-0.tar.gz
Summary:  Lrexlib with pcre bindings for lua-5.1
License:  GPLv3+

BuildRequires: compat-lua-devel pcre-devel gcc
Requires:      compat-lua-libs

%prep
%setup -q -n lrexlib-rel-2-9-0
cd src
sed -i 's@"lua.h"@<lua.h>@' common.c
sed -i 's@"lua.h"@<lua.h>@' common.h
sed -i 's@#define REX_VERSION@#define VERSION "2.9.0"\n#define REX_VERSION@' algo.h
sed -i 's@"lua.h"@<lua.h>@' pcre/lpcre.c
sed -i 's@"lua.h"@<lua.h>@' pcre/lpcre_f.c

%build
cd src
gcc %{optflags} -fPIC -llua-5.1 -I/usr/include/lua-5.1 -c common.c
gcc %{optflags} -fPIC -llua-5.1 -I/usr/include/lua-5.1 -c pcre/lpcre.c
gcc %{optflags} -fPIC -llua-5.1 -I/usr/include/lua-5.1 -c pcre/lpcre_f.c
gcc %{__global_ldflags} -lpcre lpcre.o lpcre_f.o common.o -shared -o rex_pcre.so.%{version}

%install
cd src
mkdir -p %{buildroot}%{_libdir}/lua/5.1/
cp -f rex_pcre.so.%{version} %{buildroot}%{_libdir}/lua/5.1/
ln -s %{_libdir}/lua/5.1/rex_pcre.so.%{version} %{buildroot}%{_libdir}/lua/5.1/rex_pcre.so

%files
%{_libdir}/lua/5.1/*

%description
Lua lrexlib with pcre library built for lua-5.1 (compat-lua in fedora) needed by mudlet.

%changelog
* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.9.0-2
- Build more against fedora guidelines and without luarocks

* Wed Mar 15 2017 Ilya Rum <elijahrum@gmail.com> - 2.4.2-1
- Initial version of the package
