#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qstylizer
Version  : 0.2.2
Release  : 4
URL      : https://github.com/blambright/qstylizer/archive/0.2.2/qstylizer-0.2.2.tar.gz
Source0  : https://github.com/blambright/qstylizer/archive/0.2.2/qstylizer-0.2.2.tar.gz
Summary  : Stylesheet Generator for PyQt{4-5}/PySide{1-2}
Group    : Development/Tools
License  : MIT
Requires: qstylizer-license = %{version}-%{release}
Requires: qstylizer-python = %{version}-%{release}
Requires: qstylizer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(inflection)
BuildRequires : pypi(pbr)
BuildRequires : pypi(pytest)
BuildRequires : pypi(pytest_mock)
BuildRequires : pypi(pytest_runner)
BuildRequires : pypi(pytest_xdist)
BuildRequires : pypi(tinycss2)
BuildRequires : pypi-pytest

%description
*********
qstylizer
*********
.. image:: https://travis-ci.com/blambright/qstylizer.svg?branch=master
:target: https://www.travis-ci.com/blambright/qstylizer

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
%setup -q -n qstylizer-0.2.2
cd %{_builddir}/qstylizer-0.2.2
pushd ..
cp -a qstylizer-0.2.2 buildavx2
popd

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662765360
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
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
cp %{_builddir}/qstylizer-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/qstylizer/3d7f02668cb2221e10c14f91e17f8d2a9811eca5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
