Name:           perl-Text-Autoformat
Version:        1.14.0
Release:        5%{?dist}
Summary:        Automatic text wrapping and reformatting
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Autoformat/
Source0:        http://www.cpan.org/authors/id/D/DC/DCONWAY/Text-Autoformat-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)
BuildRequires:  perl(Text::Reform) >= 1.11
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Filter out perl(Hang) and perl(NullHang) auto-provides.
Source99:       Text-Autoformat-filter-provides.sh
%global real_perl_provides %{__perl_provides}
%define __perl_provides %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)-filter-provides

%description
Text::Autoformat provides intelligent formatting of plaintext without the
need for any kind of embedded mark-up. The module recognizes Internet
quoting conventions, a wide range of bulleting and number schemes, centered
text, and block quotations, and reformats each appropriately. Other options
allow the user to adjust inter-word and inter-paragraph spacing, justify
text, and impose various capitalization schemes.

The module also supplies a re-entrant, highly configurable replacement for
the built-in Perl format() mechanism.

%prep
%setup -q -n Text-Autoformat-v%{version}
chmod a-x lib/Text/Autoformat.pm Changes README

sed -e 's,@@PERL_PROV@@,%{real_perl_provides},' %{SOURCE99} > %{__perl_provides}
chmod +x %{__perl_provides}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT %{__perl_provides}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14.0-3
- Rebuild for perl 5.10 (again)

* Wed Jan 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-2
- add BR: Test::More

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-1
- rebuild for new perl
- upstream changed license to GPL+ or Artistic

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 1.13-5
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Fri Sep 01 2006 Steven Pritchard <steve@kspei.com> 1.13-4
- Rework spec to look more like current cpanspec output.

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 1.13-3
- Minor spec cleanup.
- Add Artistic.

* Sat Aug 20 2005 Steven Pritchard <steve@kspei.com> 1.13-2
- Fix permissions (#166406).

* Tue May 24 2005 Steven Pritchard <steve@kspei.com> 1.13-1
- Update to 1.13 final.
- Filter bogus perl(Hang) and perl(NullHang) auto-provides.

* Tue May 10 2005 Steven Pritchard <steve@kspei.com> 1.13-0.3.beta
- Drop Epoch and change Release for Fedora Extras.

* Wed Feb 09 2005 Steven Pritchard <steve@kspei.com> 0:1.13-0.fdr.0.2.beta
- Minor update to 0.13beta source, from
  http://rt.cpan.org/NoAuth/Bug.html?id=8018 (pointed out by jpo@di.uminho.pt)

* Wed Jun 09 2004 Steven Pritchard <steve@kspei.com> 0:1.13-0.fdr.0.1.beta
- Specfile regenerated.
- Update to 0.13beta, which includes the upstream fix for a bug reported to
  the author.
