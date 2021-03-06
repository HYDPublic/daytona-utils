Name:           dfu-programmer
Version:        0.5.2
Release:        1%{?dist}
Summary:        A Device Firmware Update based USB programmer for Atmel chips

Group:          Development/Tools
License:        GPLv2+
URL:            http://dfu-programmer.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libusb-devel >= 0.1.10a

%description 
A linux based command-line programmer for Atmel chips with a USB
bootloader supporting ISP. This is a mostly Device Firmware Update
(DFU) 1.0 compliant user-space application. Supports all DFU enabled
Atmel chips with USB support.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install 

%{__install} -d %{buildroot}%{_datadir}/hal/fdi/information/20thirdparty
%{__install} -pm 644 fedora/10-dfu-programmer.fdi %{buildroot}%{_datadir}/hal/fdi/information/20thirdparty/10-dfu-programmer.fdi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/hal/fdi/information/20thirdparty/10-dfu-programmer.fdi

%changelog

* Sat Aug 22 2009 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.2-1
- added ability to read from STDIN
- added ability to configure AVR32 fuses
- Applied a number of bug fixes
- Fixed AVR device support
* Wed Dec 10 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.1-1
- add new flag to surpress bootloader memory checking
* Wed Dec 03 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.0-1
- update the description
- fix the broken hal rules
* Fri Aug 29 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.6-1
- change udev rules and permissions to be hal based
* Wed Aug 20 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.5-1
- added 4K bootloader support
- added eeprom-dump and eeprom-flash support
- fixed the Source0 url
* Mon Nov 19 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.4-1
- added reset command
- added udev rules and permissions
* Sun Aug 15 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.3-2
- updated the license tag
* Sun Aug 12 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.3-1
- see NEWS for details about this release
* Fri Jul 20 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.2-2
- updated the release to include the dist, and remove the runtime lib req.
* Fri Jul 06 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.2-1
- updating the release and other information to be ready to be part of fedora
* Tue May 08 2007 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.1-1
- fixint the changelog and Source0 URL
* Wed Oct 21 2006 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.3.1-1
- updated the release to get ready to be part of the fedora extras
* Wed May 07 2006 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.3.0-1
- updated the release to Fedora Core 5 & the email address
* Wed Aug 31 2005 Weston Schmidt <weston_schmidt at yahoo.com>
- initial creation
