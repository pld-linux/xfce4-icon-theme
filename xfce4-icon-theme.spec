Summary: 	Icons for Xfce
Summary(pl):	Ikony dla Xfce
Name: 		xfce4-icon-theme
Version: 	4.3.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ccdcd6aa7e03732347d785a826c81f84
URL: 		http://www.xfce.org/
BuildRequires:	gtk+2 >= 2:2.10.0
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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir='%{_datadir}/pkgconfig'

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/Rodent

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_iconsdir}/Rodent
%dir %{_datadir}/xfce4/mime
%{_datadir}/pkgconfig/xfce4-icon-theme-1.0.pc
%{_datadir}/xfce4/mime/Rodent.mime.xml
