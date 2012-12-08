%define gtkbinaryver %(pkg-config gtk+-2.0 --variable=gtk_binary_version)

Summary:	Additional themes collection for GNOME
Name:		gnome-themes-extras
Version:	2.22.0
Release:	8
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://librsvg.sourceforge.net/theme.php
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/%{name}-%{version}.tar.bz2
Patch:		gnome-themes-extras-2.22.0-darklooks.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	perl-XML-Parser
BuildRequires:	icon-naming-utils >= 0.8.1
BuildArch:	noarch
# for the svg theme engine
Requires:	librsvg
# for the industrial theme engine
Requires:	gtk-engines2 >= 2.6

%description
Additional themes collection for GNOME: this package contains the
Darklooks metatheme and the Foxtrot, Gion and Neu icon themes for GNOME2.

%prep
%setup -q
%patch -p1
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


for dir in %buildroot%{_datadir}/icons/*; do
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
%dir %{_datadir}/icons/*
%{_datadir}/icons/*/???x???
%{_datadir}/icons/*/??x??
%{_datadir}/icons/*/scalable
%_datadir/icons/Foxtrot/index.theme
%_datadir/icons/Gion/index.theme
%_datadir/icons/Neu/index.theme
%_datadir/icons/gnome-alternative/index.theme
%{_datadir}/themes/*
%ghost %{_datadir}/icons/*/icon-theme.cache



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.22.0-7mdv2011.0
+ Revision: 664888
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.22.0-6mdv2011.0
+ Revision: 605475
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.22.0-5mdv2010.1
+ Revision: 521493
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.22.0-4mdv2009.1
+ Revision: 351218
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-3mdv2009.0
+ Revision: 264572
- rebuild early 2009.0 package (before pixel changes)

* Sun May 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 211279
- fix darklooks gtk theme (bug #41041)

* Wed Apr 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 191908
- new version
- add new icon theme

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.20-2mdv2008.1
+ Revision: 150197
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20-1mdv2008.0
+ Revision: 89467
- new version

* Tue Jul 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56984
- fix buildrequires
- new version
- fix file list
- fix installation
- update description

* Wed Jul 04 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.0-5mdv2008.0
+ Revision: 47846
- drop bogus automake buildrequire, rebuild for 2008


* Fri Sep 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.0-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Wed Aug 30 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-3mdv2007.0
- fix uninstallation

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-2mdv2007.0
- rebuild

* Wed Dec 07 2005 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdk
- drop merged patch
- New release 0.9.0
- use mkrel

* Wed Oct 05 2005 Frederic Crozat <fcrozat@mandriva.com> 0.8.1-5mdk
- Remove clearlooks, now in gnome-themes

* Fri Jul 15 2005 Götz Waschk <waschk@mandriva.org> 0.8.1-4mdk
- add Clearlooks themes, except for the engine

* Fri Jun 24 2005 Götz Waschk <waschk@mandriva.org> 0.8.1-3mdk
- add the Clearlooks metacity theme (John Keller)

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 0.8.1-2mdk
- fix buildrequires

* Mon Apr 25 2005 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdk
- drop patch 1
- New release 0.8.1

* Tue Dec 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.0-4mdk
- don't depend on ximian-artwork

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.0-3mdk
- make it a noarch package
- Don't ship smooth engine, it is now in gnome-themes

* Thu Sep 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.0-2mdk
- fix buildrequires

* Wed Sep 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.0-1mdk
- don't remove the icon symlinks, they aren't broken anymore
- reenable libtoolize
- New release 0.8

* Tue Apr 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- remove broken symlinks
- fix locale file list
- fix source location
- new version

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com 0.6-3mdk
- Patch1 : don't disable deprecated API in Smooth theme

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-2mdk
- do not hardcode gtk+ version
- rebuild for gtk+-2.4 (because of theme engine path)

* Mon Jan 12 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- new version

* Fri Dec 12 2003 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- fix missing icons in the Wasp theme

* Sat Dec 06 2003 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- fix more broken symlinks
- new version

* Wed Oct 01 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-1mdk
- clean some more broken symlinks
- remove Wasp patch 
- don't libtoolize
- new version

* Tue Sep 16 2003 Götz Waschk <waschk@linux-mandrake.com> 0.3-3mdk
- fix Wasp icon theme

