Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - biblioteka u³atwiaj±ca niepe³nosprawnym korzystanie z komputerów
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Name:		atk
Version:	1.0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v2.0/%{name}-%{version}.tar.bz2
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	diffutils
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libatk1.0_0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%description -l pl
Porêczna biblioteka, której stosowanie u³atwia niepe³nosprawnym
korzystanie z komputerów.

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
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel
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
Group:		Development/Libraries
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
%configure \
	--enable-static \
	--enable-shared \
	--disable-gtk-doc

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
