%define url_ver %(echo %{version}|cut -d. -f1,2)
%define gtkbinaryver %(pkg-config gtk+-2.0 --variable=gtk_binary_version)

Summary:	Additional themes collection for GNOME
Name:		gnome-themes-extras
Version:	3.28.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://librsvg.sourceforge.net/theme.php
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	pkgconfig(icon-naming-utils)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
# for the svg theme engine
Requires:	%{_lib}rsvg
# for the industrial theme engine
Requires:	gtk-engines2 >= 2.6
Recommends: adwaita-gtk2-theme = %{version}-%{release}
Requires: adwaita-icon-theme

%package -n adwaita-gtk2-theme
Summary: Adwaita gtk2 theme
Requires: gtk2%{_isa}

%description -n adwaita-gtk2-theme
The adwaita-gtk2-theme package contains a gtk2 theme for presenting widgets
with a GNOME look and feel.

%description
Additional themes collection for GNOME: this package contains the
Darklooks metatheme and the Foxtrot, Gion and Neu icon themes for GNOME2.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache
touch $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-2.0
cp -a $RPM_SOURCE_DIR/gtkrc $RPM_BUILD_ROOT%{_datadir}/gtk-2.0/gtkrc

%transfiletriggerin -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%files
%license LICENSE
%doc NEWS README.md
%dir %{_datadir}/icons/HighContrast
%{_datadir}/icons/HighContrast/16x16/
%{_datadir}/icons/HighContrast/22x22/
%{_datadir}/icons/HighContrast/24x24/
%{_datadir}/icons/HighContrast/32x32/
%{_datadir}/icons/HighContrast/48x48/
%{_datadir}/icons/HighContrast/256x256/
%{_datadir}/icons/HighContrast/scalable/
%{_datadir}/icons/HighContrast/index.theme
%ghost %{_datadir}/icons/HighContrast/icon-theme.cache
%{_datadir}/themes/Adwaita/gtk-3.0/
%{_datadir}/themes/Adwaita-dark/gtk-3.0/
%{_datadir}/themes/HighContrast/gtk-3.0/

%files -n adwaita-gtk2-theme
%license LICENSE
%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/gtk-2.0/gtkrc
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/gtk-2.0/
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/Adwaita-dark
%{_datadir}/themes/Adwaita-dark/gtk-2.0/
%{_datadir}/themes/Adwaita-dark/index.theme
%dir %{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrast/gtk-2.0/
%{_datadir}/themes/HighContrast/index.theme
