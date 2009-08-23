#
%include	 /usr/lib/rpm/macros.mono
Summary:	.NET RSS Reader
Summary(pl.UTF-8):	Program do pobierania informacji w formacie RSS
Name:		blam
Version:	1.8.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.cmartin.tk/blam/%{name}-%{version}.tar.bz2
# Source0-md5:	ecb4af421c93ae8e58087de4b00e6b35
Patch0:		%{name}-desktop.patch
URL:		http://micke.hallendal.net/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gecko-sharp2-devel >= 0.11
BuildRequires:	dotnet-gnome-sharp-devel >= 2.15.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.9.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xulrunner-devel
Requires(post,preun):	GConf2 >= 2.4.0
%requires_eq	xulrunner
ExcludeArch:	alpha i386 sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET RSS Reader.

%description -l pl.UTF-8
Program do pobierania informacji w formacie RSS wykonany w technologii
.NET.

%prep
%setup -q
%patch0 -p1

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install blam.schemas

%preun
%gconf_schema_uninstall blam.schemas

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_prefix}/lib/%{name}
%attr(755,root,root) %{_prefix}/lib/%{name}/*.exe
%{_prefix}/lib/%{name}/blam.exe.config
%{_prefix}/lib/%{name}/*.dll
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_sysconfdir}/gconf/schemas/blam.schemas
%{_iconsdir}/hicolor/16x16/apps/blam.png
%{_iconsdir}/hicolor/22x22/apps/blam.png
%{_iconsdir}/hicolor/24x24/apps/blam.png
%{_iconsdir}/hicolor/32x32/apps/blam.png
%{_iconsdir}/hicolor/48x48/apps/blam.png
%{_iconsdir}/hicolor/scalable/apps/blam.svg
%{_mandir}/man1/blam.1*
