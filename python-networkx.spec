%define module	networkx
%define name	python-%{module}
%define version	1.7
%define rel		1
%if %mdkversion < 201100
%define release	%mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary: 	Python package for the study of complex networks
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0:	http://pypi.python.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://networkx.lanl.gov/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires: 	python-pygraphviz
Requires: 	python-matplotlib >= 0.73.1
Suggests:	python-pyparsing
Suggests:	python-numpy, python-scipy, python-yaml
BuildRequires: 	python-setuptools, python-sphinx, python-matplotlib
%{py_requires -d}

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

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd doc
export PYTHONPATH=`dir -d ../build/lib*`
make html
popd
rm -rf %{buildroot}%{_datadir}/doc/%{module}-%{version}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt examples/ doc/build/html
%py_sitedir/%{module}*
