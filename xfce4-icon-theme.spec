Summary: 	Icons for Xfce
Summary(pl):	Ikony dla Xfce
Name: 		xfce4-icon-theme
Version: 	4.3.90.1
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8f8f2f899d819ef6bec5360cf49a125d
URL: 		http://www.xfce.org/
BuildRequires:	perl-modules
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
%{_pkgconfigdir}/xfce4-icon-theme-1.0.pc
