Summary:	.NET RSS Reader 
Name:		blam
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.imendio.com/pub/imendio/blam/%{name}-%{version}.tar.gz
# Source0-md5:	3143c4408d2f60e89224ee35ffa7bab6
URL:		http://micke.hallendal.net/
BuildRequires:	ORBit2-devel >= 2.8.3
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 1.0
BuildRequires:	monodoc >= 1.0
BuildRequires:	dotnet-gecko-sharp-devel >= 0.5
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info
Requires:	mono
Requires:	monodoc
Requires:	mozilla-embedded
Requires:	dotnet-gecko-sharp
Requires:	dotnet-gtk-sharp
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q
#sed -e 's/update-mime-database/-&/' -i Makefile.am

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
