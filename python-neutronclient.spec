#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	CLI and Client Library for OpenStack Networking
Name:		python-neutronclient
Version:	6.5.0
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-neutronclient/%{name}-%{version}.tar.gz
# Source0-md5:	84b65efa068a64134a4a6e6864a12ba3
URL:		https://pypi.python.org/pypi/python-neutronclient
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-cliff >= 2.8.0
Requires:	python-debtcollector >= 1.2.0
Requires:	python-iso8601 >= 0.1.11
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-keystoneclient >= 3.8.0
Requires:	python-netaddr >= 0.7.13
Requires:	python-os-client-config >= 1.28.0
Requires:	python-osc-lib >= 1.7.0
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-oslo.serialization >= 1.10.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-requests >= 2.14.2
Requires:	python-simplejson >= 2.2.0
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a client library for Neutron built on the Neutron API. It
provides a Python API (the neutronclient module), the a command-line
tool (neutron) is provided in the 'neutronclient' package.

%package -n python3-neutronclient
Summary:	CLI and Client Library for OpenStack Networking
Group:		Libraries/Python
Requires:	python3-babel >= 2.3.4
Requires:	python3-cliff >= 2.8.0
Requires:	python3-debtcollector >= 1.2.0
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-keystoneauth1 >= 3.0.1
Requires:	python3-keystoneclient >= 3.8.0
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-os-client-config >= 1.28.0
Requires:	python3-osc-lib >= 1.7.0
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-oslo.serialization >= 1.10.0
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-requests >= 2.14.2
Requires:	python3-simplejson >= 2.2.0
Requires:	python3-six >= 1.9.0

%description -n python3-neutronclient
This is a client library for Neutron built on the Neutron API. It
provides a Python API (the neutronclient module), the a command-line
tool (neutron) is provided in the 'neutronclient' package.

%package -n neutronclient
Summary:	CLI Client for OpenStack Networking
Group:		Libraries/Python
%if %{with python3}
Requires:	python3-neutronclient = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n neutronclient
This is a client for Neutron built on the Neutron API.

%package apidocs
Summary:	API documentation for Python neutronclient module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona neutronclient
Group:		Documentation

%description apidocs
API documentation for Pythona neutronclient module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona neutronclient.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/neutronclient
%{py_sitescriptdir}/python_neutronclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-neutronclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/neutronclient
%{py3_sitescriptdir}/python_neutronclient-%{version}-py*.egg-info
%endif

%files -n neutronclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/neutron

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
