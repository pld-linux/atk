Summary:	ATK - Accessibility Toolkit
Name:		atk
Version:	0.6
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
BuildRequires:	pkgconfig
BuildRequires:	glib2-devel >= 1.3.10
BuildRequires:	pango
BuildRequires:	diffutils
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Handy library of accessability functions.

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki naglowkowe i dokumentacj
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки

%description devel
ATK - header and development documentation.

%package static
Summary:	ATK static library
Summary(pl):	Biblioteki statyczne ATK
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки

%description static
ATK static library.

%description -l pl static
Biblioteki statyczne ATK.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(644,root,root) %{_includedir}/atk*
%attr(644,root,root) %{_pkgconfigdir}/atk*
%{_datadir}/gtk-doc/html/atk

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
