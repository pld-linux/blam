#
%include	 /usr/lib/rpm/macros.mono
Summary:	.NET RSS Reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		blam
Version:	1.8.2
Release:	3.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.imendio.com/pub/imendio/blam/src/%{name}-%{version}.tar.gz
# Source0-md5:	8cb05faedf60d895d94a5ecf9d10eb8f
Patch0:		%{name}-mozilla.patch
Patch1:		%{name}-mozilla_includes.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-install.patch
Patch4:		%{name}-dotnet2.patch
Patch5:		%{name}-include.patch
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
BuildRequires:	xulrunner-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
Requires(post,preun):	GConf2 >= 2.4.0
%requires_eq	xulrunner
ExcludeArch:	alpha i386 sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET RSS Reader.

%description -l pl
Program do pobierania informacji w formacie RSS wykonany w technologii
.NET.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__autoheader}
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
%attr(755,root,root) %{_libdir}/libblam.so*
%attr(755,root,root) %{_prefix}/lib/%{name}/*.exe
%{_prefix}/lib/%{name}/blam.exe.config
%{_prefix}/lib/%{name}/*.dll
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/blam.schemas
