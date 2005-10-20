Summary:	GRASS 6 drivers for GDAL and OGR
Summary(pl):	Sterowniki GRASS 6 dla bibliotek GDAL i OGR
Name:		gdal-grass
Version:	1.3.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	4297d174ecd23ad2aa919e89e5759b66
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.remotesensing.org/gdal/
BuildRequires:	gdal-devel
BuildRequires:	libstdc++-devel
BuildRequires:	grass-devel >= 5.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRASS 6 drivers for GDAL and OGR.

%description -l pl
Sterowniki GRASS 6 dla bibliotek GDAL i OGR.

%prep
%setup -q
%patch0 -p1

rm -rf autom4te.cache

%build
%configure \
	CPPFLAGS="-I/usr/include/grass60" \
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
