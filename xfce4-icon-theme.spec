Summary: 	Icons for XFce
Summary(pl):	Ikony dla XFce
Name: 		xfce4-icon-theme
Version: 	4.1.90
Release: 	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	73e7f7fd220d085f4744f2577808c766
URL: 		http://www.xfce.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for XFce 4 Desktop Environment.

%description -l pl
Zestaw ikon dla ¶rodowiska XFce 4.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog NEWS README
%{_iconsdir}/*
%{_datadir}/xfce4/mime/Rodent.mime.xml
