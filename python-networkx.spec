%define module	networkx
%bcond_without	pdf_doc

Summary: 	Python package for the study of complex networks
Name: 	 	python2-%{module}
Version: 	1.8.1
Release: 	3
Source0:	http://pypi.python.org/packages/source/n/networkx/networkx-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://networkx.lanl.gov/
BuildArch: 	noarch
Requires: 	python2-pygraphviz
Requires: 	python2-matplotlib >= 0.73.1
Suggests:	python2-parsing
Suggests:	python2-numpy
Suggests:   python2-scipy
Suggests:   python2-yaml
%rename 	python-networkx

# FIXME not a proper build breakage solution but good until properly
# fixed in python-matplotib
BuildRequires:	fonts-ttf-dejavu

BuildRequires: 	python2-parsing
BuildRequires: 	python2-setuptools
BuildRequires: 	python2-sphinx
BuildRequires: 	python2-matplotlib
BuildRequires: 	pkgconfig(lapack)
BuildRequires: 	python2-devel

%if %{with pdf_doc}
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

sed -i 's#python#python2#' doc/Makefile doc/*.py

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
pushd doc
export PYTHONPATH=`dir -d ../build/lib*`
export PYTHON=%__python2
%if %{with pdf_doc}
make dist SPHINXBUILD=sphinx-build2
%else
SPHINXBUILD=sphinx-build2 make html
%endif
find . -name .buildinfo | xargs rm
popd
rm -rf %{buildroot}%{_datadir}/doc/%{module}-%{version}

%files
%doc *.txt examples/
%if %{with pdf_doc}
%doc doc/build/dist
%else
%doc doc/build/html
%endif
%{py2_puresitedir}/%{module}*

