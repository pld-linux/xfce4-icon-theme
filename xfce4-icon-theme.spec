Summary: 	Icons for Xfce
Summary(pl):	Ikony dla Xfce
Name: 		xfce4-icon-theme
Version: 	4.2.2
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:        http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	9e6bdbe92649318de671f7aa3446af58
URL: 		http://www.xfce.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for Xfce Desktop Environment.

%description -l pl
Zestaw ikon dla ¶rodowiska Xfce.

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
