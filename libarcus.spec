%define oname Arcus
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 3
%define liboldver 1.1.0
%define libname %mklibname %{lname} %{major}
%define devname %mklibname %{lname} -d

%define pyname python-%{lname}

Summary:	Communication library between internal components for Ultimaker software
Name:		lib%{lname}
Version:	2.3.1
Release:	1
Group:		Development/Other
License:	AGPLv3+
URL:		https://github.com/Ultimaker/libArcus
Source0:	https://github.com/Ultimaker/libArcus/archive/%{version}/lib%{oname}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	protobuf-compiler > 3.0.0
BuildRequires:	pkgconfig(protobuf) > 3.0.0
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(protobuf) > 3.0.0
BuildRequires:	python-sip

%description
%{oname} library contains C++ code and Python3 bindings for creating a socket
in a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Communication library between internal components for Ultimaker software
License:	Apache License
Group:		System/Libraries
Provides:	%{lname} = %{version}-%{release}
Provides:	%{oname} = %{version}-%{release}

%description -n %{libname}
Arcus library contains C++ code and Python3 bindings for creating a socket
in a thread and using this socket to send and receive messages based on the
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
Provides:	%{lname}-devel = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
Arcus contains C++ code and Python3 bindings for creating a socket in a
thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

This package provides development files for %{oname} library.

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
%setup -q -n lib%{oname}-%{version}

%build
%cmake \
	-DBUILD_STATIC:BOOL=OFF \
	-DBUILD_PYTHON:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DPYTHON_SITE_PACKAGES_DIR=%{py_platsitedir} \
	%{nil}
%make

%install
%makeinstall_std -C build

