Name:		python-pyftdi
Version:	0.54.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pyftdi/pyftdi-%{version}.tar.gz
Summary:	FTDI device driver (pure Python)
URL:		https://pypi.org/project/pyftdi/
License:	Modified BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
FTDI device driver (pure Python)

%prep
%autosetup -p1 -n pyftdi-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/*.py
%{py_sitedir}/pyftdi
%{py_sitedir}/pyftdi-*.*-info
