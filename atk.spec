Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - Toolkit udostЙpniaj╠cy
Name:		atk
Version:	0.10
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/%{name}-%{version}.tar.gz
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	diffutils
BuildRequires:	glib2-devel >= 1.3.13
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libatk8

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Handy library of accessibility functions.

%description -l pl
PodrЙczna biblioteka funkcji udostЙpniaj╠cych.

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki nagЁСwkowe i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}
Requires:	glib2-devel
Obsoletes:	libatk8-devel

%description devel
ATK - header and development documentation.

%description devel -l pl
ATK - pliki nagЁСwkowe i dokumentacja programisty.

%package static
Summary:	ATK static library
Summary(pl):	Biblioteka statyczna ATK
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
ATK static library.

%description static -l pl
Biblioteka statyczna ATK.

%prep
%setup -q

%build
%configure2_13 \
	--enable-static \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liba*.??
%{_includedir}/atk*
%{_pkgconfigdir}/atk*
%{_datadir}/gtk-doc/html/atk

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liba*.a
