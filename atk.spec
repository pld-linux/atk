Summary:	ATK - Accessibility Toolkit
Summary(pl):	ATK - 
Name:		atk
Version:	0.1
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.gtk.org/pub/gtk/v1.3/%{name}-%{version}.tar.gz
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
Summary:	ATK - header and development documentation.
Summary(pl):	Pliki naglowkowe i dokumentacj.
Group:		development/libraries
Group(pl):	programowanie/biblioteki
%description devel
%description -l pl devel

%package static
Summary:	ATK static library
Summary(pl):	Biblioteki statyczne ATK
Group:		development/libraries
Group(pl):	programowanie/biblioteki
%description static
%description -l pl static

%prep
%setup -q


#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_pkgconfigdir} install

%post
%postun

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
