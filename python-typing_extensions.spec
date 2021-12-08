#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Backported and Experimental Type Hints for Python 3.5+
Summary(pl.UTF-8):	Backportowane i eksperymentalne podpowiedzi typów dla Pythona 3.5+
Name:		python-typing_extensions
Version:	3.10.0.2
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typing-extensions/
Source0:	https://files.pythonhosted.org/packages/source/t/typing-extensions/typing_extensions-%{version}.tar.gz
# Source0-md5:	ed80ecc8eac5cb15840535ca54eb43f3
URL:		https://pypi.org/project/typing-extensions/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-typing >= 3.7.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
%if "%{py3_ver}" < "3.4"
BuildRequires:	python3-typing >= 3.7.4
%endif
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The typing_extensions module contains both backports of Python typing
module changes from Python 3.6-3.7 (includes types like Text or
Coroutine) as well as experimental types that will eventually be added
to the typing module, such as Protocol or TypedDict.

%description -l pl.UTF-8
Moduł typing_extensions zawiera backporty zmian modułu Pythona typing
z wersji 3.6-3.7 (w tym typy takie jak Text czy Coroutine), a także
eksperymentalne typy, które być może zostaną dodane do modułu typing,
takie jak Protocol czy TypedDict.

%package -n python3-typing_extensions
Summary:	Backported and Experimental Type Hints for Python 3.5+
Summary(pl.UTF-8):	Backportowane i eksperymentalne podpowiedzi typów dla Pythona 3.5+
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-typing_extensions
The typing_extensions module contains both backports of Python typing
module changes from Python 3.5-3.7 (includes types like Text or
Coroutine) as well as experimental types that will eventually be added
to the typing module, such as Protocol or TypedDict.

%description -n python3-typing_extensions -l pl.UTF-8
Moduł typing_extensions zawiera backporty zmian modułu Pythona typing
z wersji 3.6-3.7 (w tym typy takie jak Text czy Coroutine), a także
eksperymentalne typy, które być może zostaną dodane do modułu typing,
takie jak Protocol czy TypedDict.

%prep
%setup -q -n typing_extensions-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s src_py2
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s src_py3
%endif
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
%doc LICENSE README.rst
%{py_sitescriptdir}/typing_extensions.py[co]
%{py_sitescriptdir}/typing_extensions-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-typing_extensions
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/typing_extensions.py
%{py3_sitescriptdir}/__pycache__/typing_extensions.cpython-*.py[co]
%{py3_sitescriptdir}/typing_extensions-%{version}-py*.egg-info
%endif
