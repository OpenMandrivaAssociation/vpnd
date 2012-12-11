%define name vpnd
%define version 1.1.2
%define release %mkrel 1

Name: %{name}
Summary: The virtual private network daemon vpnd
Version: %{version}
Release: %{release}
Source: %name-%version.tar.bz2
Group: Networking/Other
URL: http://sunsite.auc.dk/vpnd/
License: GPL/LGPL

%description
The virtual private network daemon vpnd is a daemon which connects two
networks on network level either via TCP/IP or a (virtual) leased line attached
to a serial interface. All data transfered between the two networks are
encrypted using the unpatented free Blowfish encryption algorithm.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n vpnd

%build
%configure
%make

%install
install -m 775 -d $RPM_BUILD_ROOT%{_sbindir}
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}
install -m 755 vpnd $RPM_BUILD_ROOT%{_sbindir}
install -m 644 vpnd.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 vpnd.chat $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VERSIONS SPEED.TXT README dynamic-ip-client samples
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vpnd.chat
%config(noreplace) %{_sysconfdir}/vpnd.conf
%{_sbindir}/*



%changelog
* Tue Dec 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.1.2-1mdv2008.1
+ Revision: 132021
- New release

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import vpnd


* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.1.0-6mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-5mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-4mdk
- rebuild

* Tue Oct 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-3mdk
- rebuild

* Thu Sep 06 2001 Etienne Faure <etienne@mandrakesoft.com> 1.1.0-2mdk
- Version 1.1.0

* Wed Feb 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-1mdk
- updated to 1.1.0

* Tue Sep 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.8-3mdk 
- bm & macros

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.8-2mdk
- fix group
- fix files section

* Wed Nov 03 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptations / New in contribs 

* Tue Oct 05 1999 Sean P. Kane <kane@ca.metsci.com>
- Created first VPND RPM - version 1.0.8 - for Mandrake

* Fri Aug 06 1999 Stefan Siegel <siegel@informatik.uni-kl.de>
- Added "config" tag for files containing /etc or /config
- Added compression for perl- and localized man-pages

* Sat Jun 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- create (more or less) generic spec file...
