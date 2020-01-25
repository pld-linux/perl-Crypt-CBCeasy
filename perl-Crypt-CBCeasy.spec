%define		pdir	Crypt
%define		pnam	CBCeasy
Summary:	Crypt::CBCeasy Perl module - makes use of Crypt::CBC simpler
Summary(pl.UTF-8):	Moduł Perla Crypt::CBCeasy - upraszczający sposób użycia Crypt::CBC
Name:		perl-Crypt-CBCeasy
Version:	0.24
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	728fb6478c2ad7b13bfcb104ba073fca
URL:		http://search.cpan.org/dist/Crypt-CBCeasy/
BuildRequires:	perl-Crypt-CBC >= 1.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Crypt::CBC) >= 1.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a helper for Crypt::CBC to make simple and usual jobs
just one-liners.

%description -l pl.UTF-8
Jest to moduł pomocniczy dla Crypt::CBC, aby uprościć wykonywanie
prostych rzeczy w jednolinijkowcach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/CBCeasy.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/CBCeasy_sock.pl
%{_examplesdir}/%{name}-%{version}/chat2new.pl
