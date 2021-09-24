#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qstylizer
Version  : 0.2.1
Release  : 1
URL      : https://github.com/blambright/qstylizer/archive/0.2.1/qstylizer-0.2.1.tar.gz
Source0  : https://github.com/blambright/qstylizer/archive/0.2.1/qstylizer-0.2.1.tar.gz
Summary  : Stylesheet Generator for PyQt{4-5}/PySide{1-2}
Group    : Development/Tools
License  : MIT
Requires: qstylizer-license = %{version}-%{release}
Requires: qstylizer-python = %{version}-%{release}
Requires: qstylizer-python3 = %{version}-%{release}
Requires: inflection
Requires: tinycss2
BuildRequires : buildreq-distutils3
BuildRequires : inflection
BuildRequires : pbr
BuildRequires : pytest
BuildRequires : pytest-mock
BuildRequires : pytest-runner
BuildRequires : pytest-xdist
BuildRequires : tinycss2

%description
*********
qstylizer
*********
.. image:: https://www.travis-ci.org/blambright/qstylizer.svg?branch=master
:target: https://www.travis-ci.org/blambright/qstylizer

%package license
Summary: license components for the qstylizer package.
Group: Default

%description license
license components for the qstylizer package.


%package python
Summary: python components for the qstylizer package.
Group: Default
Requires: qstylizer-python3 = %{version}-%{release}

%description python
python components for the qstylizer package.


%package python3
Summary: python3 components for the qstylizer package.
Group: Default
Requires: python3-core
Provides: pypi(qstylizer)
Requires: pypi(inflection)
Requires: pypi(tinycss2)

%description python3
python3 components for the qstylizer package.


%prep
%setup -q -n qstylizer-0.2.1
cd %{_builddir}/qstylizer-0.2.1

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632448035
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])")
pytest --verbose
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export PBR_VERSION=%{version}
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/qstylizer
cp %{_builddir}/qstylizer-0.2.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/qstylizer/3d7f02668cb2221e10c14f91e17f8d2a9811eca5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qstylizer/3d7f02668cb2221e10c14f91e17f8d2a9811eca5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
