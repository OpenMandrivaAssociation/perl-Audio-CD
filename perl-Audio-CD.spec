%define upstream_name    Audio-CD
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
