Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - 
Name:		atk
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	glib-devel
BuildRequires:	pango
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define _pkgconfigdir /usr/lib/pkgconfig

%description

%description -l pl

%package devel
Summary:	ATK - header and development documentation
Summary(pl):	Pliki naglowkowe i dokumentacj

%description devel

%description -l pl devel

%package static
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Summary:	ATK static library
Summary(pl):	Biblioteki statyczne ATK

%description static

%description -l pl static

%prep
%setup -q

%build
%onfigure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_pkgconfigdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc
%attr(755,root,root) %{_libdir}/libatk.so.0.*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libatk*so
%attr(644,root,root) %{_libdir}/libatk*so.0
%dir %{_includedir}/atk*
%attr(644,root,root) %{_includedir}/atk*/atk/*
%attr(644,root,root) %{_pkgconfigdir}/atk*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.la
