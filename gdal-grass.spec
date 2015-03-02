Summary:	GRASS 6 drivers for GDAL and OGR
Summary(pl.UTF-8):	Sterowniki GRASS 6 dla bibliotek GDAL i OGR
Name:		gdal-grass
Version:	1.11.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://download.osgeo.org/gdal/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	37ea02e8ddab27a3fbae0bcefb659145
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gdal.org/gdal/
BuildRequires:	gdal-devel >= 1.11.2
BuildRequires:	libstdc++-devel
BuildRequires:	grass-devel >= 1:6.4.0
BuildRequires:	grass-devel < 1:6.5
Requires:	gdal >= 1.11.2
Requires:	grass >= 1:6.4.0
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
	--with-autoload=%{_libdir}/gdalplugins \
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
%attr(755,root,root) %{_libdir}/gdalplugins/gdal_GRASS.so
%attr(755,root,root) %{_libdir}/gdalplugins/ogr_GRASS.so
%{_datadir}/gdal/grass
