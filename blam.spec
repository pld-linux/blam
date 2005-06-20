Summary:	.NET RSS Reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		blam
Version:	1.8.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.imendio.com/pub/imendio/blam/src/%{name}-%{version}.tar.gz
# Source0-md5:	8cb05faedf60d895d94a5ecf9d10eb8f
Patch0:		%{name}-mozilla.patch
Patch1:		%{name}-mozilla_includes.patch
Patch2:		%{name}-desktop.patch
URL:		http://micke.hallendal.net/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gecko-sharp-devel >= 0.6
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 1.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
Requires(post,preun):	GConf2 >= 2.4.0
Requires:	dotnet-gecko-sharp
Requires:	dotnet-gtk-sharp
Requires:	mono
Requires:	monodoc
Requires:	mozilla-embedded
# TODO: recheck alpha
ExcludeArch:	%{x8664}
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
%gconf_schema_install blam.schemas

%preun
%gconf_schema_uninstall blam.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libblam.so*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/blam.exe.config
%{_libdir}/%{name}/*.dll
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
