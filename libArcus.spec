%define oname Arcus
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 3
%define liboldver 1.1.0
%define libname %mklibname %{oname} %{major}
%define devname %mklibname %{oname} -d

%define pyname python-%{oname}

Summary:	Communication library between internal components for Ultimaker software
Name:		lib%{oname}
Version:	2.5.0
Release:	0
Group:		Development/Other
License:	AGPLv3+
URL:		https://github.com/Ultimaker/libArcus
Source0:	https://github.com/Ultimaker/libArcus/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.5.0-CMakeLists.patch

BuildRequires:	cmake
BuildRequires:	protobuf-compiler > 3.0.0
BuildRequires:	pkgconfig(protobuf) > 3.0.0
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(protobuf) > 3.0.0
BuildRequires:	python3-sip
 
%description
libArcus contains C++ code and Python3 bindings for creating a socket in a
thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Communication library between internal components for Ultimaker software
License:	Apache License
Group:		System/Libraries
Provides:	%{oname} = %{version}-%{release}

%description -n %{libname}
Arcus contains C++ code and Python3 bindings for creating a socket in a
thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%files -n %{libname}
%{_libdir}/lib%{oname}.so.%{major}
%{_libdir}/lib%{oname}.so.%{liboldver}
%doc LICENSE

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and docs for the %{oname} library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Arcus contains C++ code and Python3 bindings for creating a socket in a
thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

This package provides development files for %{name} library.

%files -n %{devname}
%{_includedir}/%{oname}
%{_libdir}/cmake/%{oname}
%{_libdir}/lib%{oname}.so
%docdir examples/
%doc examples/example.cpp
%doc examples/example.proto
%doc examples/example.py
%doc examples/example_py.sh
%doc README.md
%doc TODO.md
%doc LICENSE

#----------------------------------------------------------------------------

%package -n %{pyname}
Summary:	Python binding fpor %{oname} library
Group:		Development/Python

Requires:	python
Requires:	%{libname} = %{version}-%{release}

%description -n %{pyname}
Arcus contains C++ code and Python3 bindings for creating a socket in a
thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

This package provides the Python3 binding for %{oname}.

%files -n %{pyname}
%{py_platsitedir}/%{oname}.so
%doc LICENSE

#----------------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig

%build
%cmake \
	-DBUILD_STATIC:BOOL=OFF \
	-DBUILD_PYTHON:BOOL=ON \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DPYTHON_SITE_PACKAGES_DIR=%{py_platsitedir} \
	%{nil}
%make

%install
%makeinstall_std -C build

