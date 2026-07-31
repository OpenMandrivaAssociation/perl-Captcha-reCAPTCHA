%define upstream_name    Captcha-reCAPTCHA
%define upstream_version 0.98
Name:		perl-%{upstream_name}
Version:	0.98
Release:	5

Summary:	A Perl implementation of the reCAPTCHA API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Captcha-reCAPTCHA
Source0:	https://cpan.metacpan.org/authors/id/S/SU/SUNNYP/Captcha-reCAPTCHA-0.98.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Tiny)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
reCAPTCHA is a hybrid mechanical turk and captcha that allows visitors who
complete the captcha to assist in the digitization of books.

From the http://recaptcha.net/learnmore.html manpage:

    reCAPTCHA improves the process of digitizing books by sending words that
    cannot be read by computers to the Web in the form of CAPTCHAs for
    humans to decipher. More specifically, each word that cannot be read
    correctly by OCR is placed on an image and used as a CAPTCHA. This is
    possible because most OCR programs alert you when a word cannot be read
    correctly.

%prep
%setup -q -n .

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
%make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

