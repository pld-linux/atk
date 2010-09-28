#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	ATK - Accessibility Toolkit
Summary(pl.UTF-8):	ATK - biblioteka ułatwiająca niepełnosprawnym korzystanie z komputerów
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Name:		atk
Version:	1.32.0
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atk/1.32/%{name}-%{version}.tar.bz2
# Source0-md5:	b9a19a3e426cd9ca930f0108c4ee343f
URL:		http://library.gnome.org/devel/atk/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.8
BuildRequires:	libtool >= 2:1.5.16
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	glib2 >= 1:2.20.0
Obsoletes:	libatk1.0_0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%description -l pl.UTF-8
Biblioteka ATK udostępnia zestaw interfejsów ułatwiających
niepełnosprawnym korzystanie z aplikacji i poszczególnych elementów
graficznego interfejsu użytkownika. Poprzez wykorzystanie interfejsów
ATK, aplikacja lub element interfejsu może być używany z takimi
narzędziami jak czytniki ekranu i narzędzia powiększające oraz
alternatywnymi urządzeniami wejściowymi.

%description -l pt_BR.UTF-8
A biblioteca ATK provê um conjunto de interfaces para adicionar
suporte a acessibilidade para aplicações e interfaces gráficas.
Suportando a interface ATK, uma aplicação ou interface gráfica pode
ser utilizada como ferramentas de leitura e aumento de tela,
dispositivos de entrada alternativos, etc.

%package devel
Summary:	ATK - header files
Summary(pl.UTF-8):	ATK - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.20.0
Obsoletes:	libatk1.0_0-devel

%description devel
ATK - header files.

%description devel -l pl.UTF-8
ATK - pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Interfaces para suporte a acessibilidade.

%package static
Summary:	ATK static library
Summary(pl.UTF-8):	Biblioteka statyczna ATK
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
ATK static library.

%description static -l pl.UTF-8
Biblioteka statyczna ATK.

%description static -l pt_BR.UTF-8
Interfaces para suporte a acessibilidade.

%package apidocs
Summary:	ATK API documentation
Summary(pl.UTF-8):	Dokumentacja API ATK
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ATK API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API ATK.

%prep
%setup -q
sed -i 's/^en@shaw//' po/LINGUAS
rm po/en@shaw.po

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang atk10

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/atk}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f atk10.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libatk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-1.0.so.0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libatk-1.0.so
%{_libdir}/libatk-1.0.la
%{_includedir}/atk-1.0
%{_pkgconfigdir}/atk.pc
%{_datadir}/gir-1.0/Atk-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatk-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atk
%endif
