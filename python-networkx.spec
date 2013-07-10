%define module	networkx
%bcond_without	pdf_doc

Summary: 	Python package for the study of complex networks
Name: 	 	python-%{module}
Version: 	1.7
Release: 	2
Source0:	http://pypi.python.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://networkx.lanl.gov/
BuildArch: 	noarch
Requires: 	python-pygraphviz
Requires: 	python-matplotlib >= 0.73.1
Suggests:	python-pyparsing
Suggests:	python-numpy
Suggests:   python-scipy
Suggests:   python-yaml
BuildRequires: 	python-parsing
BuildRequires: 	python-setuptools
BuildRequires: 	python-sphinx
BuildRequires: 	python-matplotlib
BuildRequires: 	pkgconfig(lapack)
%{py_requires -d}
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
%py_sitedir/%{module}*


%changelog
* Fri Aug 17 2012 Lev Givon <lev@mandriva.org> 1.7-1
+ Revision: 815210
- Update to 1.7.

* Tue Nov 22 2011 Lev Givon <lev@mandriva.org> 1.6-1
+ Revision: 732412
- Update to 1.6.

* Fri Jun 10 2011 Lev Givon <lev@mandriva.org> 1.5-1
+ Revision: 684190
- Update to 1.5.

* Tue Jan 25 2011 Lev Givon <lev@mandriva.org> 1.4-1
+ Revision: 632565
- Update to 1.4.

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 1.3-2mdv2011.0
+ Revision: 599414
- rebuild for p2.7

* Sun Aug 29 2010 Lev Givon <lev@mandriva.org> 1.3-1mdv2011.0
+ Revision: 574222
- Update to 1.3.

* Fri Aug 06 2010 Lev Givon <lev@mandriva.org> 1.2-1mdv2011.0
+ Revision: 566765
- Update to 1.2.

* Thu Apr 22 2010 Lev Givon <lev@mandriva.org> 1.1-1mdv2010.1
+ Revision: 537984
- Update to 1.1.

* Tue Jan 19 2010 Lev Givon <lev@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 493748
- Update to 1.0.1.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.99-3mdv2010.0
+ Revision: 442320
- rebuild

* Wed Dec 31 2008 Adam Williamson <awilliamson@mandriva.org> 0.99-2mdv2009.1
+ Revision: 321621
- rebuild with python 2.6
- do a proper file list, clean up docs
- clean up python requires

* Sun Dec 14 2008 Lev Givon <lev@mandriva.org> 0.99-1mdv2009.1
+ Revision: 314213
- Update to 0.99.

* Mon Jul 07 2008 Lev Givon <lev@mandriva.org> 0.36-1mdv2009.0
+ Revision: 232509
- import python-networkx


* Mon Jul 7 2008 Lev Givon <lev@mandriva.org> 0.36-1mdv2008.1
- Package for Mandriva.
