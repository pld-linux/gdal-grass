Summary:	GRASS 6 drivers for GDAL and OGR
Summary(pl.UTF-8):	Sterowniki GRASS 6 dla bibliotek GDAL i OGR
Name:		gdal-grass
Version:	1.4.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	2bfb7640e03b4d9d012f1a5d62c0351d
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gdal.org/gdal/
BuildRequires:	gdal-devel >= 1.4.1
BuildRequires:	libstdc++-devel
BuildRequires:	grass-devel >= 6.4.0
Requires:	gdal >= 1.4.1
Requires:	grass >= 6.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRASS 6 drivers for GDAL and OGR.

%description -l pl.UTF-8
Sterowniki GRASS 6 dla bibliotek GDAL i OGR.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	CPPFLAGS="-I/usr/include/grass64" \
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
