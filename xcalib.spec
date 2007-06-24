Summary:        xcalib is a tiny monitor calibration loader
Name:           xcalib
Version:	0.7
Release:	%mkrel 1
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
%doc README README.profilers COPYING
%attr(755,root,root) %{_bindir}/%{name}
