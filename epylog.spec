%include	/usr/lib/rpm/macros.perl
Summary:	New logs analyzer and parser
Summary(pl):	Nowy analizator i parser logów
Name:		epylog
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/epylog/download/%{name}-%{version}.tar.gz
# Source0-md5:	051ff19d4071c4e0dfd55db18c481b60
URL:		http://linux.duke.edu/projects/epylog/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	python-libxml2
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

%package perl
Summary:	Perl module for writing external Epylog modules
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
This package provides a perl module for epylog. It is useful for
writing epylog modules that use external module API. No modules
shipping with epylog by default use that API, so install this only if
you are using external perl modules, or intend to write some of your
own.

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
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/epylog/*.[cxhl]*
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/epylog/modules.d/*.conf
%{_datadir}/epylog
%{py_libdir}/site-packages/epylog
%{_mandir}/man[58]/*

%files perl
%defattr(644,root,root,755)
%{perl_vendorlib}/epylog
%{_mandir}/man3/*
