Summary: 	Icons for XFce
Summary(pl):	Ikony dla XFce
Name: 		xfce4-icon-theme
Version: 	4.1.99.2
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0aaa9f0b5e9a088560771381e272ef8a
URL: 		http://www.xfce.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for XFce 4 Desktop Environment.

%description -l pl
Zestaw ikon dla środowiska XFce 4.

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
