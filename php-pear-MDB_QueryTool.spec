%include	/usr/lib/rpm/macros.php
%define         _class          MDB
%define         _subclass       QueryTool
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - An OO-interface for easily retrieving and modifying data in a DB
Summary(pl):	%{_pearname} - obiektowy interfejs do odczytywania i modyfikowania danych w DB
Name:		php-pear-%{_pearname}
Version:	0.9.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d96ee32de31678838c91fc5909e7608b
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet to obiektowo zorientowana abstrakcja dla jêzyka zapytañ
SQL, udostêpniaj±ca metody takie jak setWhere, setOrder, setGroup,
setJoin itp. do ³atwego tworzenia zapytañ. Udostêpnia on tak¿e ³atwy
do nauczenia siê interfejs wspó³pracuj±cy z HTML-forms przy u¿yciu
tablic zawieraj±cych dane z kolumn, które maj± byæ uaktualnione/dodane
do bazy. Ten pakiet bazuje na SQL-Builderze, który pozwala na ³atwe
tworzenie i wykonywanie instrukcji SQL. Ta klasa jest portem z
oryginalnej DB_QueryTool napisanej przez Wolframa Kriesinga i Paolo
Panto (vision:produktion, wk@visionp.de).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
