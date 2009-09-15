%define module	networkx
%define name	python-%{module}
%define version	0.99
%define release	%mkrel 3

Summary: 	Python package for the study of complex networks
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.zip
License: 	LGPLv2.1
Group: 	 	Development/Python
Url: 	 	https://networkx.lanl.gov/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-pygraphviz
Requires: 	python-matplotlib >= 0.73.1
%{py_requires -d}
BuildRequires: 	python-setuptools
BuildArch: 	noarch

%description
NetworkX (NX) is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

Features:
* Includes standard graph-theoretic and statistical physics functions
* Easy exchange of network algorithms between applications, disciplines, 
  and platforms
* Includes many classic graphs and synthetic networks
* Nodes and edges can be "anything" (e.g. time-series, text, images, 
  XML records)
* Exploits existing code from high-quality legacy software in C, C++, 
  Fortran, etc.
* Open source (encourages community input)
* Unit-tested

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}
rm -rf %{buildroot}%{_docdir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}-py%{pyver}.egg-info
%doc doc/* examples/

