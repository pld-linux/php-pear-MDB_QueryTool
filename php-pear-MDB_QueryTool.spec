%include	/usr/lib/rpm/macros.php
%define		_class		MDB
%define		_subclass	QueryTool
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an OO-interface for easily retrieving and modifying data in a DB
Summary(pl):	%{_pearname} - obiektowy interfejs do odczytywania i modyfikowania danych w DB
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ef9b19407ef62ea27695d2bcabe30dd0
URL:		http://pear.php.net/package/MDB_QueryTool/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1
Requires:	php-pear
Requires:	php-pear-MDB
Requires:	php-pear-Log >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Ten pakiet to obiektowo zorientowana abstrakcja dla j�zyka zapyta�
SQL, udost�pniaj�ca metody takie jak setWhere, setOrder, setGroup,
setJoin itp. do �atwego tworzenia zapyta�. Udost�pnia on tak�e �atwy
do nauczenia si� interfejs wsp�pracuj�cy z HTML-forms przy u�yciu
tablic zawieraj�cych dane z kolumn, kt�re maj� by� uaktualnione/dodane
do bazy. Ten pakiet bazuje na SQL-Builderze, kt�ry pozwala na �atwe
tworzenie i wykonywanie instrukcji SQL. Ta klasa jest portem z
oryginalnej DB_QueryTool napisanej przez Wolframa Kriesinga i Paolo
Panto (vision:produktion, wk@visionp.de).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
