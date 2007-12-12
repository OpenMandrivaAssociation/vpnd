%define name vpnd
%define version 1.1.0
%define release %mkrel 6

Name: %{name}
Summary: The virtual private network daemon vpnd
Version: %{version}
Release: %{release}
Source: %name-%version.tar.bz2
Group: Networking/Other
URL: http://sunsite.auc.dk/vpnd/
BuildRoot: %{_tmppath}/%{name}-buildroot
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

