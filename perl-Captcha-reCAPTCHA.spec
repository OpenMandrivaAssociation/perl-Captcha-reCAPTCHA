%define upstream_name    Captcha-reCAPTCHA
%define upstream_version 0.97

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.97
Release:	1

Summary:	A Perl implementation of the reCAPTCHA API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Captcha/Captcha-reCAPTCHA-0.97.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.940.0-2mdv2011.0
+ Revision: 658736
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-1mdv2011.0
+ Revision: 553063
- update to 0.94

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.1
+ Revision: 471170
- import perl-Captcha-reCAPTCHA


* Sun Nov 29 2009 cpan2dist 0.92-1mdv
- initial mdv release, generated with cpan2dist

