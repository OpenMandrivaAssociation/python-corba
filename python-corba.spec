Summary:	Python bindings for CORBA
Name:		python-corba
Version:	1.2.0
Release:	1
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
#Patch0:		pyorbit-2.24.0-linkage.patch

BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:	pkgconfig(MateCORBA-2.0)
BuildRequires:	pkgconfig(python)

Requires:	CORBA

%description
pyorbit is an extension module for python that gives you access
to the CORBA ORB.

%package devel
Summary:	Files needed to build wrappers for CORBA addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%release

%description devel
This package contains files required to build wrappers for CORBA addon
libraries so that they interoperate with pyorbit

%prep
%setup -q
#patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -name "*.la" -exec rm {} \;

%files
%doc AUTHORS NEWS README ChangeLog
%{py_platsitedir}/*

%files devel
%dir %{_includedir}/pymatecorba-2
%{_includedir}/pymatecorba-2/*.h
%{_libdir}/pkgconfig/*.pc
