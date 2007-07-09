Summary:	GRASS 6 drivers for GDAL and OGR
Summary(pl.UTF-8):	Sterowniki GRASS 6 dla bibliotek GDAL i OGR
Name:		gdal-grass
Version:	1.4.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	05403a06e8918763bd0fbce2988d43d4
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gdal.org/gdal/
BuildRequires:	gdal-devel >= 1.4.1
BuildRequires:	libstdc++-devel
BuildRequires:	grass-devel >= 6.2.0
Requires:	gdal >= 1.4.1
Requires:	grass >= 6.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRASS 6 drivers for GDAL and OGR.

%description -l pl.UTF-8
Sterowniki GRASS 6 dla bibliotek GDAL i OGR.

%prep
%setup -q
%patch0 -p1

rm -rf autom4te.cache

%build
%configure \
	CPPFLAGS="-I/usr/include/grass62" \
	--with-grass=`echo /usr/%{_lib}/grass-*`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
# XXX: this dir could be owned by gdal
%dir %{_libdir}/gdalplugins
%attr(755,root,root) %{_libdir}/gdalplugins/gdal_GRASS.so
%attr(755,root,root) %{_libdir}/gdalplugins/ogr_GRASS.so
%{_datadir}/gdal/grass
