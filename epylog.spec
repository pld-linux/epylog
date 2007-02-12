%include	/usr/lib/rpm/macros.perl
Summary:	New logs analyzer and parser
Summary(pl.UTF-8):   Nowy analizator i parser logów
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
BuildRequires:	perl-perldoc
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

%description -l pl.UTF-8
Epylog to nowe narzędzie do powiadamiania i analizy logów uruchamiane
regularnie z crona, przeglądające logi, przetwarzające wpisy w celu
prezentacji ich w bardziej wyczerpującym formacie, a następnie
dostarczającym wyjście. Jest napisany z myślą o dużych klastrach
sieciowych, gdzie dużo maszyn (około 50 i więcej) wysyła logi na ten
sam host przy użyciu sysloga lub syslog-ng.

%package perl
Summary:	Perl module for writing external Epylog modules
Summary(pl.UTF-8):   Moduł Perla do pisania zewnętrznych modułów Epyloga
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
This package provides a Perl module for epylog. It is useful for
writing epylog modules that use external module API. No modules
shipping with epylog by default use that API, so install this only if
you are using external Perl modules, or intend to write some of your
own.

%description perl -l pl.UTF-8
Ten pakiet dostarcza moduł Perla dla epyloga. Jest przydatny do
pisania modułów epyloga używających API dla zewnętrznych modułów.
Żaden moduł dostarczany domyślnie z epylogiem nie używa tego API, więc
pakiet należy instalować tylko jeśli używamy zewnętrznych modułów
Perla lub zamierzamy napisać jakieś własne.

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
