Summary:	A shout plugin for gmpc
Name:		gmpc-shout
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.8
BuildRequires:	gmpc-devel >= 0.15.98
BuildRequires:	intltool
Requires:	gmpc

%description
A shout plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%{_libdir}/gmpc/plugins/shoutplugin.so
