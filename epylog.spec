%include	/usr/lib/rpm/macros.perl
Summary:	New logs analyzer and parser
Summary(pl):	Nowy analizator i parser log�w
Name:		epylog
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/epylog/download/%{name}-%{version}.tar.gz
# Source0-md5:	6beedd62e0d59d6309ae1f537fc75772
URL:		http://linux.duke.edu/projects/epylog/
BuildRequires:	python-libxml2
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	python-libxml2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epylog is a new log notifier and parser which runs periodically out of
cron, looks at your logs, processes the entries in order to present
them in a more comprehensive format, and then provides you with the
output. It is written specifically with large network clusters in mind
where a lot of machines (around 50 and upwards) log to the same
loghost using syslog or syslog-ng.

%description -l pl
Epylog to nowe narz�dzie do powiadamiania i analizy log�w uruchamiane
regularnie z crona, przegl�daj�ce logi, przetwarzaj�ce wpisy w celu
prezentacji ich w bardziej wyczerpuj�cym formacie, a nast�pnie
dostarczaj�cym wyj�cie. Jest napisany z my�l� o du�ych klastrach
sieciowych, gdzie du�o maszyn (oko�o 50 i wi�cej) wysy�a logi na ten
sam host przy u�yciu sysloga lub syslog-ng.

%package perl
Summary:	Perl module for writing external Epylog modules
Summary(pl):	Modu� Perla do pisania zewn�trznych modu��w Epyloga
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
This package provides a Perl module for epylog. It is useful for
writing epylog modules that use external module API. No modules
shipping with epylog by default use that API, so install this only if
you are using external Perl modules, or intend to write some of your
own.

%description perl -l pl
Ten pakiet dostarcza modu� Perla dla epyloga. Jest przydatny do
pisania modu��w epyloga u�ywaj�cych API dla zewn�trznych modu��w.
�aden modu� dostarczany domy�lnie z epylogiem nie u�ywa tego API, wi�c
pakiet nale�y instalowa� tylko je�li u�ywamy zewn�trznych modu��w
Perla lub zamierzamy napisa� jakie� w�asne.

%prep
%setup -q

%build
%configure \
	--with-python=%{_bindir}/python \
	--with-lynx=%{_bindir}/lynx \
	--with-site-perl=%{perl_vendorlib}/epylog

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
%attr(700,root,root) /etc/cron.daily/*.*
%attr(750,root,root) %dir %{_sysconfdir}/epylog
%dir %{_sysconfdir}/epylog/modules.d
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/epylog/*.[cxhl]*
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/epylog/modules.d/*.conf
%{_datadir}/epylog
%{py_sitedir}/epylog
%{_mandir}/man[58]/*
%attr(750,root,root) %dir %{_var}/lib/epylog

%files perl
%defattr(644,root,root,755)
%{perl_vendorlib}/epylog
%{_mandir}/man3/*
