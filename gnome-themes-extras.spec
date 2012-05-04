%define gtkbinaryver %(pkg-config gtk+-2.0 --variable=gtk_binary_version)

Summary: Additional themes collection for GNOME
Name: gnome-themes-extras
Version: 2.22.0
Release: %mkrel 8
License: GPL
Group: Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/%{name}-%{version}.tar.bz2
Patch: gnome-themes-extras-2.22.0-darklooks.patch
URL: http://librsvg.sourceforge.net/theme.php
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires:  libgtk+2.0-devel
BuildRequires:  gtk-engines2
BuildRequires:  perl-XML-Parser
BuildRequires:  icon-naming-utils >= 0.8.1
BuildArch: noarch
# for the svg theme engine
Requires: librsvg
# for the industrial theme engine
Requires: gtk-engines2 >= 2.6

%description
Additional themes collection for GNOME: this package contains the
Darklooks metatheme and the Foxtrot, Gion and Neu icon themes for GNOME2.

%prep
%setup -q
%patch -p1
%build

#don't use configure macro, it doesn't work
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
rm -rf %{buildroot}
%makeinstall

%find_lang gnome-themes-extras

### Remove files not to be installed
rm -rf %{buildroot}%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/{*.{a,la},libindustrial.so,libsmooth.so}
rm -rf %{buildroot}%_datadir/themes/Industrial


for dir in %buildroot%{_datadir}/icons/*; do
 touch $dir/icon-theme.cache
done

%clean
rm -rf %{buildroot}

%post
%update_icon_cache Foxtrot
%update_icon_cache Gion
%update_icon_cache Neu
%update_icon_cache gnome-alternative
%postun
%clean_icon_cache Foxtrot
%clean_icon_cache Gion
%clean_icon_cache Neu
%clean_icon_cache gnome-alternative


%files -f gnome-themes-extras.lang
%defattr(-, root, root)
%dir %{_datadir}/icons/*
%{_datadir}/icons/*/???x???
%{_datadir}/icons/*/??x??
%{_datadir}/icons/*/scalable
%_datadir/icons/Foxtrot/index.theme
%_datadir/icons/Gion/index.theme
%_datadir/icons/Neu/index.theme
%_datadir/icons/gnome-alternative/index.theme
%{_datadir}/themes/*
%doc AUTHORS MAINTAINERS ChangeLog COPYING README TODO
%ghost %{_datadir}/icons/*/icon-theme.cache

