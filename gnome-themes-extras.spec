%define url_ver %(echo %{version}|cut -d. -f1,2)
%define gtkbinaryver %(pkg-config gtk+-2.0 --variable=gtk_binary_version)

Summary:	Additional themes collection for GNOME
Name:		gnome-themes-extras
Version:	2.22.0
Release:	17
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://librsvg.sourceforge.net/theme.php
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		gnome-themes-extras-2.22.0-darklooks.patch
BuildArch:	noarch

BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	pkgconfig(icon-naming-utils)
# for the svg theme engine
Requires:	librsvg
# for the industrial theme engine
Requires:	gtk-engines2 >= 2.6

%description
Additional themes collection for GNOME: this package contains the
Darklooks metatheme and the Foxtrot, Gion and Neu icon themes for GNOME2.

%prep
%setup -q
%apply_patches
%build

#don't use configure macro, it doesn't work
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%make

%install
%makeinstall

%find_lang gnome-themes-extras

### Remove files not to be installed
rm -rf %{buildroot}%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/{*.{a,la},libindustrial.so,libsmooth.so}
rm -rf %{buildroot}%_datadir/themes/Industrial

for dir in %buildroot%{_iconsdir}/*; do
 touch $dir/icon-theme.cache
done

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
%doc AUTHORS MAINTAINERS ChangeLog COPYING README TODO
%dir %{_iconsdir}/*
%{_datadir}/themes/*
%{_iconsdir}/*/???x???
%{_iconsdir}/*/??x??
%{_iconsdir}/*/scalable
%{_iconsdir}/Foxtrot/index.theme
%{_iconsdir}/Gion/index.theme
%{_iconsdir}/Neu/index.theme
%{_iconsdir}/gnome-alternative/index.theme
%ghost %{_iconsdir}/*/icon-theme.cache

