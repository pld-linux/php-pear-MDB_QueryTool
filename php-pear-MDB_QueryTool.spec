%define		_status		stable
%define		_pearname	MDB_QueryTool
Summary:	%{_pearname} - an OO-interface for easily retrieving and modifying data in a DB
Summary(pl.UTF-8):	%{_pearname} - obiektowy interfejs do odczytywania i modyfikowania danych w DB
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dfe7a5502ebfbdf0ce74866cd86396da
URL:		http://pear.php.net/package/MDB_QueryTool/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1
Requires:	php-pear
Requires:	php-pear-Log >= 1.7
Requires:	php-pear-MDB
Suggests:	php-pear-MDB
Suggests:	php-pear-MDB2
Obsoletes:	php-pear-MDB_QueryTool-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(MDB.*) pear(MDB2.*)

%description
This package is an OO-abstraction to the SQL-Query language, it
provides methods such as setWhere, setOrder, setGroup, setJoin, etc.
to easily build queries. It also provides an easy to learn interface
that interacts nicely with HTML-forms using arrays that contain the
column data, that shall be updated/added in a DB. This package bases
on an SQL-Builder which lets you easily build SQL-Statements and
execute them. NB: this is just a MDB porting from the original
DB_QueryTool written by Wolfram Kriesing and Paolo Panto
(vision:produktion, wk@visionp.de).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet to obiektowo zorientowana abstrakcja dla języka zapytań
SQL, udostępniająca metody takie jak setWhere, setOrder, setGroup,
setJoin itp. do łatwego tworzenia zapytań. Udostępnia on także łatwy
do nauczenia się interfejs współpracujący z HTML-forms przy użyciu
tablic zawierających dane z kolumn, które mają być uaktualnione/dodane
do bazy. Ten pakiet bazuje na SQL-Builderze, który pozwala na łatwe
tworzenie i wykonywanie instrukcji SQL. Ta klasa jest portem z
oryginalnej DB_QueryTool napisanej przez Wolframa Kriesinga i Paolo
Panto (vision:produktion, wk@visionp.de).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB/*.php
%{php_pear_dir}/MDB/QueryTool/
