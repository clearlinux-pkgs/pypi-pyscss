#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pyscss
Version  : 1.4.0
Release  : 65
URL      : https://files.pythonhosted.org/packages/92/30/64c818fd317e03138f98ca67800edb6a916f59fc07b3d7e535e84c3c333a/pyScss-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/92/30/64c818fd317e03138f98ca67800edb6a916f59fc07b3d7e535e84c3c333a/pyScss-1.4.0.tar.gz
Summary  : pyScss, a Scss compiler for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-pyscss-bin = %{version}-%{release}
Requires: pypi-pyscss-license = %{version}-%{release}
Requires: pypi-pyscss-python = %{version}-%{release}
Requires: pypi-pyscss-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pcre-dev
BuildRequires : pypi(enum34)
BuildRequires : pypi(pathlib2)
BuildRequires : pypi(six)
BuildRequires : pypi-pytest
BuildRequires : pypi-six
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==================================
        
        |build-status| |coverage|

%package bin
Summary: bin components for the pypi-pyscss package.
Group: Binaries
Requires: pypi-pyscss-license = %{version}-%{release}

%description bin
bin components for the pypi-pyscss package.


%package license
Summary: license components for the pypi-pyscss package.
Group: Default

%description license
license components for the pypi-pyscss package.


%package python
Summary: python components for the pypi-pyscss package.
Group: Default
Requires: pypi-pyscss-python3 = %{version}-%{release}

%description python
python components for the pypi-pyscss package.


%package python3
Summary: python3 components for the pypi-pyscss package.
Group: Default
Requires: python3-core
Provides: pypi(pyscss)
Requires: pypi(enum34)
Requires: pypi(pathlib2)
Requires: pypi(six)

%description python3
python3 components for the pypi-pyscss package.


%prep
%setup -q -n pyScss-1.4.0
cd %{_builddir}/pyScss-1.4.0
pushd ..
cp -a pyScss-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683046738
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
pytest --verbose || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyscss
cp %{_builddir}/pyScss-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyscss/c313f5aad9597bd831180c4a772e4c292248b00d || :
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

%files bin
%defattr(-,root,root,-)
/usr/bin/less2scss
/usr/bin/pyscss

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyscss/c313f5aad9597bd831180c4a772e4c292248b00d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
