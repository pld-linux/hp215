Summary:	hp215 - HP PhotoSmart 215 digicam access utility
Summary(pl.UTF-8):	hp215 - narzędzie obsługujące aparat cyfrowy HP PhotoSmart 215
Name:		hp215
Group:		Applications
Version:	0.2.3
Release:	1
License:	GPL v2
Source0:	http://home.nwn.de/ebartels/linux/hp215/hp_photosmart215-%{version}.tar.gz
# Source0-md5:	84bf37121fd9cdfa6f97872388a5c460
URL:		http://home.nwn.de/ebartels/linux/hp215/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libusb-devel
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This commandline program with the name hp215 can read photos from the
HP Photosmart 215 camera.

%description -l pl.UTF-8
Za pomocą małego programu o nazwie hp215 można odczytać zdjęcia z
aparatu cyfrowego HP Photosmart 215.

%prep
%setup -q -n hp_photosmart215-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang hp_photosmart215

%clean
rm -rf $RPM_BUILD_ROOT

%files -f hp_photosmart215.lang
%defattr(644,root,root,755)
%doc doc/html AUTHORS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
