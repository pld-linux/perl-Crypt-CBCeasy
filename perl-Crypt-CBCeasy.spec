%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CBCeasy
Summary:	Crypt::CBCeasy Perl module - makes use of Crypt::CBC simpler
Summary(pl):	Modu³ Perla Crypt::CBCeasy - upraszczaj±cy sposób u¿ycia Crypt::CBC
Name:		perl-Crypt-CBCeasy
Version:	0.24
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Crypt-CBC >= 1.20
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl(Crypt::CBC) >= 1.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a helper for Crypt::CBC to make simple and usual jobs
just one-liners.

%description -l pl
Jest to modu³ pomocniczy dla Crypt::CBC, aby upro¶ciæ wykonywanie
prostych rzeczy w jednolinijkowcach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/CBCeasy.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/CBCeasy_sock.pl
%{_examplesdir}/%{name}-%{version}/chat2new.pl
