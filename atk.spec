Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - biblioteka u�atwiaj�ca niepe�nosprawnym korzystanie z komputer�w
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Name:		atk
%define		_major_ver	1.6
%define		_minor_ver	1
Epoch:		1
Version:	%{_major_ver}.%{_minor_ver}
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{_major_ver}/%{name}-%{version}.tar.bz2
# Source0-md5:	f77be7e128c957bd3056c2e270b5f283
Patch0:		%{name}-locale-names.patch
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	diffutils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
Requires:	glib2 >= 1:2.4.0
Obsoletes:	libatk1.0_0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%description -l pl
Biblioteka ATK udost�pnia zestaw interfejs�w u�atwiaj�cych
niepe�nosprawnym korzystanie z aplikacji i poszczeg�lnych element�w
graficznego interfejsu u�ytkownika. Poprzez wykorzystanie interfejs�w
ATK, aplikacja lub element interfejsu mo�e by� u�ywany z takimi
narz�dziami jak czytniki ekranu i narz�dzia powi�kszaj�ce oraz
alternatywnymi urz�dzeniami wej�ciowymi.

%description -l pt_BR
A biblioteca ATK prov� um conjunto de interfaces para adicionar
suporte a acessibilidade para aplica��es e interfaces gr�ficas.
Suportando a interface ATK, uma aplica��o ou interface gr�fica pode
ser utilizada como ferramentas de leitura e aumento de tela,
dispositivos de entrada alternativos, etc.

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki nag��wkowe i dokumentacja
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0
Requires:	gtk-doc-common
Obsoletes:	libatk1.0_0-devel

%description devel
ATK - header and development documentation.

%description devel -l pl
ATK - pliki nag��wkowe i dokumentacja programisty.

%description devel -l pt_BR
Interfaces para suporte a acessibilidade.

%package static
Summary:	ATK static library
Summary(pl):	Biblioteka statyczna ATK
Summary(pt_BR):	Interfaces para suporte a acessibilidade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
ATK static library.

%description static -l pl
Biblioteka statyczna ATK.

%description static -l pt_BR
Interfaces para suporte a acessibilidade.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

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
	--enable-gtk-doc \
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/atk*
%{_pkgconfigdir}/atk*
%{_gtkdocdir}/atk

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
