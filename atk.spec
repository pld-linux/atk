#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library

Summary:	ATK - Accessibility Toolkit
Summary(pl.UTF-8):	ATK - biblioteka ułatwiająca niepełnosprawnym korzystanie z komputerów
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Name:		atk
Version:	2.34.0
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atk/2.34/%{name}-%{version}.tar.xz
# Source0-md5:	d2c1a54e332bef627cf4dde240a7254e
URL:		https://developer.gnome.org/atk/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.2
BuildRequires:	glib2-devel >= 1:2.38.0
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	gobject-introspection-devel >= 1.32.0
%if %{with apidocs}
BuildRequires:	gtk-doc >= 1.25
%endif
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.728
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.38.0
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
Summary(pl.UTF-8):	ATK - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.38.0
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
ATK API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API ATK.

%prep
%setup -q

%build
%meson build \
	-Ddocs=%{__true_false apidocs}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/atk}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

%find_lang atk10

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f atk10.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libatk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-1.0.so.0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-1.0.so
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
