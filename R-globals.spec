#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-globals
Version  : 0.16.3
Release  : 58
URL      : https://cran.r-project.org/src/contrib/globals_0.16.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/globals_0.16.3.tar.gz
Summary  : Identify Global Objects in R Expressions
Group    : Development/Tools
License  : LGPL-2.1+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
by code inspection using various strategies (ordered, liberal, or
    conservative).  The objective of this package is to make it as simple as
    possible to identify global objects for the purpose of exporting them in
    parallel, distributed compute environments.

%prep
%setup -q -n globals
pushd ..
cp -a globals buildavx2
popd
pushd ..
cp -a globals buildavx512
popd
pushd ..
cp -a globals buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740093805

%install
export SOURCE_DATE_EPOCH=1740093805
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/globals/DESCRIPTION
/usr/lib64/R/library/globals/INDEX
/usr/lib64/R/library/globals/Meta/Rd.rds
/usr/lib64/R/library/globals/Meta/features.rds
/usr/lib64/R/library/globals/Meta/hsearch.rds
/usr/lib64/R/library/globals/Meta/links.rds
/usr/lib64/R/library/globals/Meta/nsInfo.rds
/usr/lib64/R/library/globals/Meta/package.rds
/usr/lib64/R/library/globals/NAMESPACE
/usr/lib64/R/library/globals/NEWS.md
/usr/lib64/R/library/globals/R/globals
/usr/lib64/R/library/globals/R/globals.rdb
/usr/lib64/R/library/globals/R/globals.rdx
/usr/lib64/R/library/globals/WORDLIST
/usr/lib64/R/library/globals/help/AnIndex
/usr/lib64/R/library/globals/help/aliases.rds
/usr/lib64/R/library/globals/help/globals.rdb
/usr/lib64/R/library/globals/help/globals.rdx
/usr/lib64/R/library/globals/help/paths.rds
/usr/lib64/R/library/globals/html/00Index.html
/usr/lib64/R/library/globals/html/R.css
/usr/lib64/R/library/globals/tests/Globals.R
/usr/lib64/R/library/globals/tests/cleanup.R
/usr/lib64/R/library/globals/tests/conservative.R
/usr/lib64/R/library/globals/tests/dotdotdot.R
/usr/lib64/R/library/globals/tests/findGlobals.R
/usr/lib64/R/library/globals/tests/formulas.R
/usr/lib64/R/library/globals/tests/globalsByName.R
/usr/lib64/R/library/globals/tests/globalsOf,locals.R
/usr/lib64/R/library/globals/tests/globalsOf.R
/usr/lib64/R/library/globals/tests/incl/end.R
/usr/lib64/R/library/globals/tests/incl/globals.R
/usr/lib64/R/library/globals/tests/incl/start,load-only.R
/usr/lib64/R/library/globals/tests/incl/start.R
/usr/lib64/R/library/globals/tests/liberal.R
/usr/lib64/R/library/globals/tests/utils.R
/usr/lib64/R/library/globals/tests/walkAST.R
/usr/lib64/R/library/globals/tests/zzz.R
