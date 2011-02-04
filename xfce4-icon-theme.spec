Summary:	Icons for Xfce
Summary(pl.UTF-8):	Ikony dla Xfce
Name:		xfce4-icon-theme
Version:	4.4.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	73ce2977b84f634a6a6c5d9c27e336db
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-update-icon-cache
BuildRequires:	intltool >= 0.31
BuildRequires:	perl-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for Xfce Desktop Environment.

%description -l pl.UTF-8
Zestaw ikon dla środowiska Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
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
