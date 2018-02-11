Name:		tagainijisho
Version:	1.0.3
Release:	100%{?dist}
Summary:	Free opensource japanese dictionary

License:	GPLv3
URL:		https://www.tagaini.net/
Source0:	https://github.com/Gnurou/tagainijisho/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	qt-devel cmake

%description
Tagaini Jisho is designed to help you remember Japanese vocabulary and kanji (later referred as 'entries') by presenting them in a way that makes it easy to create connections between them. It does so by keeping track of all the entries you already know and want to study, and letting you tag and annote them, in addition to providing easy navigation between related entries. A powerful search engine also allows you to search for entries very precisely. Finally, Tagaini let you produce printed material (including a handy foldable pocket book) so let you study anywhere.

%prep
%setup -q


%build
%cmake .

%install
%make_install


%files
%{_bindir}/%{name}
%{_datadir}/applications/*

%{_datadir}/icons/hicolor/128x128/apps/tagainijisho.png
%{_datadir}/icons/hicolor/16x16/apps/tagainijisho.png
%{_datadir}/icons/hicolor/22x22/apps/tagainijisho.png
%{_datadir}/icons/hicolor/32x32/apps/tagainijisho.png
%{_datadir}/icons/hicolor/48x48/apps/tagainijisho.png
%{_datadir}/icons/hicolor/64x64/apps/tagainijisho.png

%{_datadir}/%{name}/*


%changelog
* Sun Feb 11 2018 wyvie <irum@redhat.com> - 1.0.3-100
- Initial package
