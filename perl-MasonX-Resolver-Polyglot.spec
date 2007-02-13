#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MasonX
%define		pnam	Resolver-Polyglot
Summary:	MasonX::Resolver::Polyglot - component path resolver for easy internationalization
Summary(pl.UTF-8):	MasonX::Resolver::Polyglot - resolver ścieżek komponentów do łatwego umiędzynaradawiania
Name:		perl-MasonX-Resolver-Polyglot
Version:	0.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	938ed09d946569a1adbcd55a6031d921
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason >= 1.1
BuildRequires:	perl-Locale-Codes
BuildRequires:	perl(Locale::Country) >= 2.06
BuildRequires:	perl(Locale::Language) >= 2.02
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This HTML::Mason::Resolver::File::ApacheHandler subclass enables Mason
to determine the client's language preference and find the best
matching component to fulfill it.

%description -l pl.UTF-8
Ta podklasa HTML::Mason::Resolver::File::ApacheHandler umożliwia
Masonowi określanie preferowanego przez klienta języka i odnajdywania
najlepszego pasującego komponentu, aby sprostać preferencjom.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
