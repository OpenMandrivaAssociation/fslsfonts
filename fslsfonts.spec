Name:		fslsfonts
Version:	1.0.4
Release:	1
Summary:	List fonts served by X font server
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
Patch0:		fslsfonts-aarch64.patch

BuildRequires:	libfs-devel >= 1.0.0
BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
Fslsfonts lists the fonts that match the given pattern.

%prep
%setup -q
%apply_patches

%build
%configure2_5x	\
		--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/fslsfonts
%{_mandir}/man1/fslsfonts.*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 664389
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592588
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2010.1
+ Revision: 522673
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-3mdv2010.0
+ Revision: 424481
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2009.0
+ Revision: 264513
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 211788
- New version

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2008.1
+ Revision: 150086
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 45341
- rebuild for 2008


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:24:00 (27460)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

