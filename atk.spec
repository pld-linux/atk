Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - Toolkit udostępniający
Name:		atk
Version:	0.12
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/%{name}-%{version}.tar.gz
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	diffutils
BuildRequires:	glib2-devel >= 1.3.14
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libatk8

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Handy library of accessibility functions.

%description -l pl
Podręczna biblioteka funkcji udostępniających.

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki nagłówkowe i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel
Obsoletes:	libatk8-devel

%description devel
ATK - header and development documentation.

%description devel -l pl
ATK - pliki nagłówkowe i dokumentacja programisty.

%package static
Summary:	ATK static library
Summary(pl):	Biblioteka statyczna ATK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ATK static library.

%description static -l pl
Biblioteka statyczna ATK.

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
