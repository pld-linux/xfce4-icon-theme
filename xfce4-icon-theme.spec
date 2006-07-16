Summary: 	Icons for Xfce
Summary(pl):	Ikony dla Xfce
Name: 		xfce4-icon-theme
Version: 	4.3.90.2
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a0649d25b1ee231f9563492c17b3bac1
URL: 		http://www.xfce.org/
BuildRequires:	perl-modules
Requires(post,postun):	gtk+2 >= 2:2.10.0
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

%post
gtk-update-icon-cache -qf %{_datadir}/icons/Rodent

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/Rodent

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_iconsdir}/Rodent
%dir %{_datadir}/xfce4/mime
%{_datadir}/xfce4/mime/Rodent.mime.xml
%{_pkgconfigdir}/xfce4-icon-theme-1.0.pc
