Summary:	hp215 - HP PhotoSmart 215 digicam access utility
Summary(pl):	hp215 - Narzêdzie obs³uguj±ce aparat cyfrowy HP PhotoSmart 215
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This commandline pogramm with the name hp215 can read photos from the
HP Photosmart 215 camera.

%description -l pl
Za pomoc± ma³ego programu o nazwie hp215 mo¿na odczytaæ zdjêcia z
aparatu cyfrowego HP Photosmart 215.

%prep
%setup -q -n hp_photosmart215-%{version}

%build
cp -f %{_datadir}/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ABOUT-NLS FAQ AUTHORS INSTALL ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%{_mandir}/man1/*
