Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - biblioteka u³atwiaj±ca niepe³nosprawnym korzystanie z komputerów
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Name:		atk
Version:	1.5.3
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	7cad75ba736a37e509d8f48f18afb095
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	diffutils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.3.1
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
Obsoletes:	libatk1.0_0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%description -l pl
Biblioteka ATK udostêpnia zestaw interfejsów u³atwiaj±cych
niepe³nosprawnym korzystanie z aplikacji i poszczególnych elementów
graficznego interfejsu u¿ytkownika. Poprzez wykorzystanie interfejsów
ATK, aplikacja lub element interfejsu mo¿e byæ u¿ywany z takimi
narzêdziami jak czytniki ekranu i narzêdzia powiêkszaj±ce oraz
alternatywnymi urz±dzeniami wej¶ciowymi.

%description -l pt_BR
A biblioteca ATK provê um conjunto de interfaces para adicionar
suporte a acessibilidade para aplicações e interfaces gráficas.
Suportando a interface ATK, uma aplicação ou interface gráfica pode
ser utilizada como ferramentas de leitura e aumento de tela,
dispositivos de entrada alternativos, etc.

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.3.1
Requires:	gtk-doc-common
Obsoletes:	libatk1.0_0-devel

%description devel
ATK - header and development documentation.

%description devel -l pl
ATK - pliki nag³ówkowe i dokumentacja programisty.

%description devel -l pt_BR
Interfaces para suporte a acessibilidade.

%package static
Summary:	ATK static library
Summary(pl):	Biblioteka statyczna ATK
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ATK static library.

%description static -l pl
Biblioteka statyczna ATK.

%description static -l pt_BR
Interfaces para suporte a acessibilidade.

%prep
%setup -q

%build
gtkdocize --copy
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-shared \
	--with-html-dir=%{_gtkdocdir}

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
%{_libdir}/liba*.la
%attr(755,root,root) %{_libdir}/liba*.so
%{_includedir}/atk*
%{_pkgconfigdir}/atk*
%{_gtkdocdir}/atk

%files static
%defattr(644,root,root,755)
%{_libdir}/liba*.a
