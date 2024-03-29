# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       sysstat

# >> macros
# << macros

Summary:    Performance monitoring tools
Version:    12.7.5
Release:    1
Group:      Applications
License:    GPLv2
URL:        https://sysstat.github.io
Source0:    %{name}-%{version}.tar.gz
Source100:  sysstat.yaml
Source101:  sysstat-rpmlintrc
BuildRequires:  pkgconfig(systemd)

%description
Various utilities, common to many commercial Unixes, to monitor system
performance and usage activity.

This includes the cifsiostat, iostat, mpstat, pidstat, and tapestat tools.

See the "sa-tools"/"Sysstat Monitoring" package for long-term monitoring

%if "%{?vendor}" == "chum"
Title: Sysstat Tools
Type: console-application
DeveloperName: Sebastien Godard
DeveloperLogin: sysstat
PackagedBy: nephros
Categories:
 - System
 - Utility
Custom:
  Repo: "https://github.com/sysstat/sysstat"
  PackagingRepo: "https://github.com/sailfishos-chum/sysstat"
Links:
  Help: https://raw.githubusercontent.com/sysstat/sysstat/master/README.md
Screenshots:
  - https://github.com/sysstat/sysstat/raw/master/images/color_output.png
  - https://github.com/sysstat/sysstat/raw/master/images/cpugraph.jpg
  - https://github.com/sysstat/sysstat/raw/master/images/iostat.png
  - https://github.com/sysstat/sysstat/raw/master/images/loadavg-svg.png
  - https://github.com/sysstat/sysstat/raw/master/images/tcgraph.png
Donation: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=45U6F9R73ESFQ
%endif


%package sa-tools
Summary:    Performance history tools
Group:      Applications
Requires:   %{name} = %{version}-%{release}

%description sa-tools
Tools you can schedule via systemd to collect and historize
performance and activity data.

This means the sadf sar and sadc tools, and corresponding systemd units.

%if "%{?vendor}" == "chum"
Title: Sysstat Monitoring
Type: console-application
DeveloperName: Sebastien Godard
DeveloperLogin: sysstat
PackagedBy: nephros
Categories:
 - System
 - Utility
Custom:
  Repo: "https://github.com/sysstat/sysstat"
  PackagingRepo: "https://github.com/sailfishos-chum/sysstat"
Links:
  Help: https://raw.githubusercontent.com/sysstat/sysstat/master/README.md
Donation: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=45U6F9R73ESFQ
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --disable-nls \
    --disable-lto \
    --disable-compress-manpg \
    --enable-copy-only \
    --disable-file-attr \
    --disable-documentation \
    --enable-install-cron \
    --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -rf %{buildroot}%{_mandir}/*
rm -rf %{buildroot}%{_unitdir}/../system-sleep/*.sleep
# << install post

%files
%defattr(-,root,root,-)
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}*
%{_bindir}/cifsiostat
%{_bindir}/iostat
%{_bindir}/mpstat
%{_bindir}/pidstat
%{_bindir}/tapestat
# >> files
# << files

%files sa-tools
%defattr(-,root,root,-)
%{_unitdir}/*.service
%{_unitdir}/*.timer
%{_bindir}/sadf
%{_bindir}/sar
%{_libdir}/sa/sa?
%{_libdir}/sa/sadc
# >> files sa-tools
# << files sa-tools
