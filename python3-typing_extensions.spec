#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Backported and Experimental Type Hints for Python 3.7+
Summary(pl.UTF-8):	Backportowane i eksperymentalne podpowiedzi typów dla Pythona 3.7+
Name:		python3-typing_extensions
Version:	4.14.1
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typing-extensions/
Source0:	https://files.pythonhosted.org/packages/source/t/typing-extensions/typing_extensions-%{version}.tar.gz
# Source0-md5:	da52c877660b1760771ce7553f729c5d
URL:		https://pypi.org/project/typing-extensions/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.11
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The typing_extensions module serves two related purposes:
- Enable use of new type system features on older Python versions. For
  example, typing.TypeGuard is new in Python 3.10, but
  typing_extensions allows users on previous Python versions to use it
  too.
- Enable experimentation with new type system PEPs before they are
  accepted and added to the typing module.

%description -l pl.UTF-8
Moduł typing_extensions służy dwóm celom:
- umożlwia korzystanie z nowych cech systemu typów w starszych
  wersjach Pythona - np. typing.TypeGuard pojawił się w Pythonie 3.10,
  ale typing_extensions pozwala na korzystanie z niego użytkownikom
  starszych wersji;
- pozwala na eksperymentowanie z nowymi PEP systemu typów zanim
  zostaną zaakceptowane i dodane do moduły typing.

%prep
%setup -q -n typing_extensions-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s src
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/typing_extensions.py
%{py3_sitescriptdir}/__pycache__/typing_extensions.cpython-*.py[co]
%{py3_sitescriptdir}/typing_extensions-%{version}.dist-info
