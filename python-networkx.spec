%{?python_enable_dependency_generator}

Name:		python-networkx
Version:	3.5
Release:	2
Summary:	Creates and Manipulates Graphs and Networks
License:	BSD
URL:		https://networkx.org
#Source0:	https://github.com/networkx/networkx/archive/networkx-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/n/networkx/networkx-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{py_ver}dist(decorator)
BuildRequires:	python%{py_ver}dist(gdal)
BuildRequires:	python%{py_ver}dist(lxml)
BuildRequires:	python%{py_ver}dist(matplotlib)
BuildRequires:	python%{py_ver}dist(nose)
BuildRequires:	python%{py_ver}dist(numpy)
BuildRequires:	python%{py_ver}dist(numpydoc)
BuildRequires:	python%{py_ver}dist(pillow)
BuildRequires:	python%{py_ver}dist(pyyaml)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	xdg-utils
Recommends:	python%{py_ver}dist(gdal)
Recommends:	python%{py_ver}dist(lxml)
Recommends:	python%{py_ver}dist(matplotlib)
Recommends:	python%{py_ver}dist(numpy)
Recommends:	python%{py_ver}dist(pillow)
Recommends:	python%{py_ver}dist(pyparsing)
Recommends:	python%{py_ver}dist(pyyaml)
Recommends:	xdg-utils

#Provides:	python-networkx = %{EVRD}

%description
NetworkX is a Python 3 package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/networkx*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n networkx-%{version}

# Do not use env
for f in $(grep -FRl %{_bindir}/env .); do
  sed -e 's,%{_bindir}/env python,%{__python},' \
      -e 's,%{_bindir}/env ,%{_bindir},' \
      -i.orig $f
  touch -r $f.orig $f
  rm $f.orig
done

# The football example requires network access, and the parallel betweenness
# example has a function that cannot be pickled.
sed -i "/expected_failing_examples/s|]|,'../examples/advanced/plot_parallel_betweenness.py','../examples/graph/plot_football.py'&|" doc/conf.py

%build
%py_build

%install
%py_install

# Repack uncompressed zip archives
for fil in $(find doc/build -name \*.zip); do
  mkdir zip
  cd zip
  unzip ../$fil
  zip -9r ../$fil .
  cd ..
  rm -fr zip
done

# The tests have shebangs, so mark them as executable
#grep -rlZ '^#!' %{buildroot}%{python_sitelib}/networkx | xargs -0 chmod a+x

# Temporarily disabled until a bug in graphviz > 2.38 is fixed that causes
# multigraphs to not work.  (Adding the same edge with multiple keys yields
# only the initial edge; see bz 1703571).  This is slated to be fixed in
# graphviz 2.42.  Once that is built for Fedora, we can reenable the tests.
#%%check
#nosetests-3 -v

