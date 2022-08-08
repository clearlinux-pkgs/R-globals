#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-globals
Version  : 0.16.0
Release  : 46
URL      : https://cran.r-project.org/src/contrib/globals_0.16.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/globals_0.16.0.tar.gz
Summary  : Identify Global Objects in R Expressions
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : buildreq-R

%description
by code inspection using various strategies (ordered, liberal, or
    conservative).  The objective of this package is to make it as simple as
    possible to identify global objects for the purpose of exporting them in
    parallel, distributed compute environments.

%prep
%setup -q -c -n globals
cd %{_builddir}/globals

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659973949

%install
export SOURCE_DATE_EPOCH=1659973949
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library globals
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library globals
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library globals
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc globals || :


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
