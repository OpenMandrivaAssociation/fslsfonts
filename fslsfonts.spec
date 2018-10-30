Summary:	List fonts served by X font server
Name:		fslsfonts
Version:	1.0.5
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libfs)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
Fslsfonts lists the fonts that match the given pattern.

%prep
%setup -q

%build
%configure	\
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/fslsfonts
%{_mandir}/man1/fslsfonts.*

