Summary:        Tiny monitor calibration loader
Name:           xcalib
Version:	0.8
Release:	%mkrel 7
License:	GPL
Group:		System/Configuration/Hardware
URL:		http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib
Source0:	http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/%{name}-source-%{version}.tar.bz2
BuildRequires:	x11-proto-devel
BuildRequires:	libx11-devel
BuildRequires:	libxxf86vm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
xcalib is a tiny monitor calibration loader for XFree86 (or X.org) 

%prep
%setup -q

%build
%make xcalib CFLAGS="%{optflags}" XLIBDIR=%{_libdir} XINCLUDEDIR=%{_includedir}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
cp xcalib %{buildroot}%{_bindir}/xcalib

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README README.profilers COPYING *.icc *.icm
%attr(755,root,root) %{_bindir}/%{name}


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8-7mdv2010.0
+ Revision: 435054
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-6mdv2009.0
+ Revision: 262277
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-5mdv2009.0
+ Revision: 256635
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-3mdv2008.1
+ Revision: 168511
- rebuild
- fix summary
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.8-2mdv2008.1
+ Revision: 120422
- Add ICC and ICM profiles from upstream to doc directory

* Tue Sep 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.8-1mdv2008.0
+ Revision: 79514
- New version

* Sun Jun 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7-1mdv2008.0
+ Revision: 43675
- new version
- update description
- pass correct variables to the makefile
- spec file clean


* Sun Jan 07 2007 Emmanuel Andry <eandry@mandriva.org> 0.6-1mdv2007.0
+ Revision: 105236
- fix buildrequires
- buildrequires libxxf86vm1-devel
- fix buildrequires
- fix buildrequires
- buildrequires libiv3-devel
- Import xcalib

* Sat Jan 06 2007 Kjetil Skjønberg <kjetil84@gmail.com> 0.6
- Initial package

