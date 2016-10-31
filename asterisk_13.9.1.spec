#
# spec file for package asterisk
#
# Copyright (c) 2016 Venkatesh Macha.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://sillycodes.org/
#

Name:           asterisk
Version:        13.9.1
Release:        1%{?dist}
Summary:        Asterisk call server

Group:          Applications/Communications
License:        GPL
URL:            http://www.asterisk.org/
Source:         %name-%version.tar.gz
#Source:         http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13.7.2.tar.gz

#requires: jansson >= 2.6, pjproject >= 2.3-5, mysql >= 5.1.73, unixODBC  >= 2.2.14, libsrtp >= 1.4.4-10, gsm >= 1.0.13-4, speex >= 1.2, mysql-connector-odbc >= 5.1.5r1144

requires:  jansson, libuuid-devel, sqlite-devel, mariadb, mariadb-devel, mariadb-server, mariadb-libs, gsm >= 1.0.13-4, speex >= 1.2

%description
The Asterisk call server with Call Center support.


%package devel
Summary:  Asterisk development files
Group:    Applications/Communications
Provides: aterisk-devel

%description devel
The Asterisk development headers

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --libdir=/usr/lib64 --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc
make menuselect.makeopts
make -j2 %{?_smp_mflags}


%install
b="%buildroot"
%make_install
mkdir -p /var/lib/asterisk/
make samples DESTDIR="$b"


%files
%defattr(-,root,root)
/etc/asterisk/*
/usr/sbin/*
/usr/share/man/man8/*
/usr/lib64/asterisk
/usr/lib64/libasteriskssl.so
/usr/lib64/libasteriskssl.so.1
/var/lib/asterisk
/var/log/asterisk
/var/spool/asterisk

%files devel
/usr/include/asterisk.h
/usr/include/asterisk

%changelog

%clean
rm -rf %{buildroot}
