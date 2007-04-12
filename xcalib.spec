%define name    xcalib
%define version 0.6
%define release %mkrel 1

Name:           %{name}
Summary:        xcalib is a tiny monitor calibration loader 
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-source-%{version}.tar.bz2 
URL:            http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/

Group:          System/Configuration/Hardware
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL
BuildRequires:	x11-proto-devel
BuildRequires:	libx11-devel
BuildRequires:	libxxf86vm-devel


%description
loads 'vcgt'-tag of ICC profiles to X-server like MS-Windows 
or MacOS do it to calibrate your display.
  
Versions 0.5 and higher are also usable with Microsoft Windows. 
They can be used as a free alternative to other calibration loaders.

%prep
%setup -q -a 0

%build
make icclib_xcalib

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin
cp xcalib $RPM_BUILD_ROOT/usr/bin/xcalib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root, 0755)
%doc README README.profilers COPYING
%defattr(0755,root,root)
%{_bindir}/xcalib


