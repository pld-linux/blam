Summary:	.NET RSS Reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		blam
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.imendio.com/pub/imendio/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3143c4408d2f60e89224ee35ffa7bab6
Patch0:		%{name}-locale-names.patch
URL:		http://micke.hallendal.net/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	dotnet-gecko-sharp-devel >= 0.5
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.0
BuildRequires:	mono-devel >= 1.0
BuildRequires:	pkgconfig
Requires(post):	GConf2 >= 2.4.0
Requires:	dotnet-gecko-sharp
Requires:	dotnet-gtk-sharp
Requires:	mono
Requires:	monodoc
Requires:	mozilla-embedded
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET RSS Reader.

%description -l pl
Program do pobierania informacji w formacie RSS wykonany w technologii
.NET.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libblam.so*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
