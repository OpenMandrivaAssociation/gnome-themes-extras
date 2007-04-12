%define gtkbinaryver %(pkg-config gtk+-2.0 --variable=gtk_binary_version)

Summary: Additional themes collection for GNOME
Name: gnome-themes-extras
Version: 0.9.0
Release: %mkrel 4
License: GPL
Group: Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/%{name}-%{version}.tar.bz2
URL: http://www.gnome.org/~uraeus/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires:  libgtk+2.0-devel
BuildRequires: gtk-engines2
BuildRequires:  perl-XML-Parser
BuildRequires: automake1.7
BuildArch: noarch
# for the svg theme engine
Requires: librsvg
# for the industrial theme engine
Requires: gtk-engines2 >= 2.6


%description
Additional themes collection for GNOME: this package contains the
BlueSphere, Gorilla, Lush, Nuvola and  Wasp themes for GNOME2.

%prep
%setup -q
%build

#don't use configure macro, it doesn't work
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%find_lang gnome-themes-extras

### Remove files not to be installed
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/{*.{a,la},libindustrial.so,libsmooth.so}
rm -rf $RPM_BUILD_ROOT%_datadir/themes/Industrial

#add symlinks for missing icons
ln -s gnome-audio2.svg %buildroot%_datadir/icons/Wasp/scalable/apps/gnome-audio.svg
ln -s ../stock/stock_lockscreen.svg %buildroot%_datadir/icons/Wasp/scalable/apps/gnome-lockscreen.svg
ln -s ../stock/stock_logout.svg %buildroot%_datadir/icons/Wasp/scalable/apps/gnome-logout.png

for dir in %buildroot%{_datadir}/icons/*; do
 touch $dir/icon-theme.cache
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%update_icon_cache Amaranth
%update_icon_cache Gorilla
%update_icon_cache Lush
%update_icon_cache Nuvola
%update_icon_cache Wasp

%postun
%clean_icon_cache Amaranth
%clean_icon_cache Gorilla
%clean_icon_cache Lush
%clean_icon_cache Nuvola
%clean_icon_cache Wasp

%files -f gnome-themes-extras.lang
%defattr(-, root, root)
%dir %{_datadir}/icons/*
%{_datadir}/icons/*/??x??
%{_datadir}/icons/*/scalable
%_datadir/icons/Amaranth/index.theme
%_datadir/icons/Gorilla/index.theme
%_datadir/icons/Lush/index.theme
%_datadir/icons/Nuvola/index.theme
%_datadir/icons/Wasp/index.theme
%{_datadir}/themes/*
%doc AUTHORS MAINTAINERS ChangeLog COPYING README license_dsg license_lgpl license_gpl TODO
%ghost %{_datadir}/icons/*/icon-theme.cache

