#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mox3
Version  : 0.14.0
Release  : 15
URL      : https://pypi.python.org/packages/source/m/mox3/mox3-0.14.0.tar.gz
Source0  : https://pypi.python.org/packages/source/m/mox3/mox3-0.14.0.tar.gz
Summary  : Mock object framework for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: mox3-python
BuildRequires : Sphinx-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : linecache2-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
Mox3 - Mock object framework for Python 3
=========================================

%package python
Summary: python components for the mox3 package.
Group: Default
Requires: fixtures-python

%description python
python components for the mox3 package.


%prep
%setup -q -n mox3-0.14.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
