%define module networkx

Name:		python-networkx
Version:	3.6.1
Release:	1
Summary:	Creates and Manipulates Graphs and Networks
License:	BSD
URL:		https://github.com/networkx/networkx
Source0:	%{URL}/archive/%{module}-%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:  python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-gdal
BuildRequires:	python%{py_ver}dist(decorator)
BuildRequires:	python%{py_ver}dist(lxml)
BuildRequires:	python%{py_ver}dist(matplotlib)
BuildRequires:	python%{py_ver}dist(nose)
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:	python%{py_ver}dist(numpy)
BuildRequires:	python%{py_ver}dist(pandas)
BuildRequires:	python%{py_ver}dist(numpy)
BuildRequires:	python%{py_ver}dist(pillow)
BuildRequires:	python%{py_ver}dist(pyyaml)
BuildRequires:	python%{py_ver}dist(scipy)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	python%{py_ver}dist(wheel)
BuildRequires:	xdg-utils
Recommends:	python-gdal
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
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{module}-%{version}

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

