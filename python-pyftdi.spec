Name:		python-pyftdi
Version:	0.57.1
Release:	1
# pyftdi currently doesn't make source releases on pypi
#Source0:	https://files.pythonhosted.org/packages/source/p/pyftdi/pyftdi-%{version}.tar.gz
Source0:	https://github.com/eblot/pyftdi/archive/refs/tags/v%{version}.tar.gz
Summary:	FTDI device driver (pure Python)
URL:		https://pypi.org/project/pyftdi/
License:	Modified BSD
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
FTDI device driver (pure Python)

%files
%{_bindir}/*.py
%{py_sitedir}/pyftdi
%{py_sitedir}/pyftdi-*.*-info
