%define real_name Audio-CD
%define name perl-%{real_name}
%define version 0.05
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to libcdaudio
Source:		%{real_name}-%{version}.tar.bz2
URL:		http://home.wanadoo.nl/jano/disc-cover.html
License:	GPL
Group:		Sound
BuildRequires:	libcdaudio-devel
BuildRequires:	perl-devel

%description
This module was created for adding CDDB support to Xmms::shell and cd
tray eject.  Methods for a good chunk of other libcdaudio functions
were added, but the docs and glue are not complete.

NOTE: This version has been altered by J.I. van Hemert
<jvhemert@cs.leidenuniv.nl> to suit the needs of Disc-Cover. Please
start with the original package if you wish to develop something.

%prep
%setup -q -n %{real_name}-%{version}

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

