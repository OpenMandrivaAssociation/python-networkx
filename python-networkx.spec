%global srcname networkx

Name:           python-%{srcname}
Version:        2.3
Release:        3%{?dist}
Summary:        Creates and Manipulates Graphs and Networks
License:        BSD
URL:            http://networkx.github.io/
Source0:        https://github.com/networkx/networkx/archive/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(gdal)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  xdg-utils

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-%{srcname}
Summary:        Creates and Manipulates Graphs and Networks
Recommends:     python3dist(gdal)
Recommends:     python3dist(lxml)
Recommends:     python3dist(matplotlib)
Recommends:     python3dist(numpy)
Recommends:     python3dist(pillow)
Recommends:     python3dist(pyparsing)
Recommends:     python3dist(pyyaml)
Recommends:     xdg-utils
Provides:	python-%{srcname} = %{EVRD}

%description -n python3-%{srcname}
NetworkX is a Python 3 package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%prep
%autosetup -p0 -n %{srcname}-%{srcname}-%{version}

# Do not use env
for f in $(grep -FRl %{_bindir}/env .); do
  sed -e 's,%{_bindir}/env python,%{__python3},' \
      -e 's,%{_bindir}/env ,%{_bindir},' \
      -i.orig $f
  touch -r $f.orig $f
  rm $f.orig
done

# The football example requires network access, and the parallel betweenness
# example has a function that cannot be pickled.
sed -i "/expected_failing_examples/s|]|,'../examples/advanced/plot_parallel_betweenness.py','../examples/graph/plot_football.py'&|" doc/conf.py

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_docdir}/networkx-%{version} ./installed-docs
rm -f installed-docs/INSTALL.txt

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
grep -rlZ '^#!' %{buildroot}%{python3_sitelib}/networkx | xargs -0 chmod a+x

# Temporarily disabled until a bug in graphviz > 2.38 is fixed that causes
# multigraphs to not work.  (Adding the same edge with multiple keys yields
# only the initial edge; see bz 1703571).  This is slated to be fixed in
# graphviz 2.42.  Once that is built for Fedora, we can reenable the tests.
#%%check
#nosetests-3 -v

%files -n python3-networkx
%doc README.rst installed-docs/*
%license LICENSE.txt
%{python3_sitelib}/networkx*
