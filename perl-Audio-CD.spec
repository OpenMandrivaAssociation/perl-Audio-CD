%define upstream_name    Audio-CD
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl interface to libcdaudio
License:	GPL
Group:		Sound
Url:		http://home.wanadoo.nl/jano/disc-cover.html
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	libcdaudio-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module was created for adding CDDB support to Xmms::shell and cd
tray eject.  Methods for a good chunk of other libcdaudio functions
were added, but the docs and glue are not complete.

NOTE: This version has been altered by J.I. van Hemert
<jvhemert@cs.leidenuniv.nl> to suit the needs of Disc-Cover. Please
start with the original package if you wish to develop something.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

chmod 644 README

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Audio
%{perl_vendorarch}/auto/Audio
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.50.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.50.0-3
+ Revision: 680481
- mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 555422
- rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 406836
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.05-10mdv2009.0
+ Revision: 255344
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.05-8mdv2008.1
+ Revision: 151831
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-7mdv2008.0
+ Revision: 85919
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:27:51 (58375)
- mkrel

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:25:03 (58374)
Import perl-Audio-CD

* Sun Jun 26 2005 Götz Waschk <waschk@mandriva.org> 0.05-5mdk
- rebuild to fix bug #16551

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.05-4mdk
- rebuild for new perl

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.05-3mdk
- own dir

* Thu Jan 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-2mdk
- rebuild
- drop patch, new version already carries modifications

* Fri Nov 28 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-1mdk
- new version

* Thu Oct 23 2003 Götz Waschk <waschk@linux-mandrake.com> 0.04-11mdk
- fix deps
- rebuild with fixed gcc (bug #6192)

