%define module	networkx
%bcond_without	pdf_doc

Summary: 	Python package for the study of complex networks
Name: 	 	python-%{module}
Version: 	1.9
Release: 	1
Source0:	http://pypi.python.org/packages/source/n/networkx/networkx-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://networkx.lanl.gov/
BuildArch: 	noarch
Requires: 	python-pygraphviz
Requires: 	python-matplotlib >= 0.73.1
Suggests:	python-parsing
Suggests:	python-numpy
Suggests:   python-scipy
Suggests:   python-yaml

# FIXME not a proper build breakage solution but good until properly
# fixed in python-matplotib
BuildRequires:	fonts-ttf-dejavu

BuildRequires: 	python-parsing
BuildRequires: 	python-setuptools
BuildRequires: 	python-sphinx
BuildRequires: 	python-matplotlib
BuildRequires: 	pkgconfig(lapack)
BuildRequires: 	python-devel

%if %{with_pdf_doc}
BuildRequires:	texlive
BuildRequires:	zip
%endif

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd doc
export PYTHONPATH=`dir -d ../build/lib*`
%if %{with_pdf_doc}
make dist
%else
make html
%endif
find . -name .buildinfo | xargs rm
popd
rm -rf %{buildroot}%{_datadir}/doc/%{module}-%{version}

%files
%doc *.txt examples/
%if %{with_pdf_doc}
%doc doc/build/dist
%else
%doc doc/build/html
%endif
%{py_puresitedir}/%{module}*
