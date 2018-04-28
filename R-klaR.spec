#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-klaR
Version  : 0.6.14
Release  : 10
URL      : https://cran.r-project.org/src/contrib/klaR_0.6-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/klaR_0.6-14.tar.gz
Summary  : Classification and Visualization
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ClustVarLV
Requires: R-clustMixType
Requires: R-combinat
Requires: R-questionr
Requires: R-scatterplot3d
Requires: R-som
BuildRequires : R-ClustVarLV
BuildRequires : R-clustMixType
BuildRequires : R-combinat
BuildRequires : R-questionr
BuildRequires : R-scatterplot3d
BuildRequires : R-som
BuildRequires : clr-R-helpers

%description
e.g. regularized discriminant analysis, sknn() kernel-density naive Bayes, 
	 an interface to 'svmlight' and stepclass() wrapper variable selection 
   	 for supervised classification, partimat() visualization of classification rules 
         and shardsplot() of cluster results as well as kmodes() clustering for categorical data, 
	 corclust() variable clustering, variable extraction from different variable clustering models 
         and weight of evidence preprocessing.

%prep
%setup -q -c -n klaR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523311556

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523311556
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library klaR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library klaR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library klaR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library klaR|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/klaR/CITATION
/usr/lib64/R/library/klaR/DESCRIPTION
/usr/lib64/R/library/klaR/INDEX
/usr/lib64/R/library/klaR/Meta/Rd.rds
/usr/lib64/R/library/klaR/Meta/data.rds
/usr/lib64/R/library/klaR/Meta/features.rds
/usr/lib64/R/library/klaR/Meta/hsearch.rds
/usr/lib64/R/library/klaR/Meta/links.rds
/usr/lib64/R/library/klaR/Meta/nsInfo.rds
/usr/lib64/R/library/klaR/Meta/package.rds
/usr/lib64/R/library/klaR/NAMESPACE
/usr/lib64/R/library/klaR/NEWS
/usr/lib64/R/library/klaR/R/klaR
/usr/lib64/R/library/klaR/R/klaR.rdb
/usr/lib64/R/library/klaR/R/klaR.rdx
/usr/lib64/R/library/klaR/data/B3.RData
/usr/lib64/R/library/klaR/data/GermanCredit.RData
/usr/lib64/R/library/klaR/data/countries.RData
/usr/lib64/R/library/klaR/help/AnIndex
/usr/lib64/R/library/klaR/help/aliases.rds
/usr/lib64/R/library/klaR/help/klaR.rdb
/usr/lib64/R/library/klaR/help/klaR.rdx
/usr/lib64/R/library/klaR/help/paths.rds
/usr/lib64/R/library/klaR/html/00Index.html
/usr/lib64/R/library/klaR/html/R.css
