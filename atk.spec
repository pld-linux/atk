#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	ATK - Accessibility Toolkit
Summary(pl.UTF-8):   ATK - biblioteka ułatwiająca niepełnosprawnym korzystanie z komputerów
Summary(pt_BR.UTF-8):   Interfaces para suporte a acessibilidade
Name:		atk
Version:	1.12.4
Release:	2
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/atk/1.12/%{name}-%{version}.tar.bz2
# Source0-md5:	0a2c6a7bbc380e3a3d94e9061f76a849
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	diffutils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	gtk-doc-automake >= 1.7
BuildRequires:	libtool >= 2:1.5.16
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	glib2 >= 1:2.12.4
Obsoletes:	libatk1.0_0
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
Summary(pl.UTF-8):   ATK - pliki nagłówkowe
Summary(pt_BR.UTF-8):   Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.12.4
Obsoletes:	libatk1.0_0-devel

%description devel
ATK - header files.

%description devel -l pl.UTF-8
ATK - pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Interfaces para suporte a acessibilidade.

%package static
Summary:	ATK static library
Summary(pl.UTF-8):   Biblioteka statyczna ATK
Summary(pt_BR.UTF-8):   Interfaces para suporte a acessibilidade
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
Summary(pl.UTF-8):   Dokumentacja API ATK
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ATK API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API ATK.

%prep
%setup -q

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang atk10

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f atk10.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/atk*
%{_pkgconfigdir}/atk*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atk
%endif
