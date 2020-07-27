Name:             ipvsadm
Version:          1.31
Release:          2
Summary:          A utility to administer the IP virtual server services
License:          GPLv2+
URL:              https://kernel.org/pub/linux/utils/kernel/ipvsadm/
Source0:          https://kernel.org/pub/linux/utils/kernel/ipvsadm/%{name}-%{version}.tar.gz
Source1:          ipvsadm.service
Source2:          ipvsadm-config

Patch6000:        ipvsadm-use-CFLAGS-and-LDFLAGS-environment-variables.patch

BuildRequires:    gcc libnl3-devel popt-devel systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel with IP virtual server support.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%set_build_flags
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
make install BUILD_ROOT=%{buildroot}%{_prefix} SBIN=%{buildroot}%{_sbindir} MANDIR=%{buildroot}%{_mandir} MAN=%{buildroot}%{_mandir}/man8 INIT=%{buildroot}%{_sysconfdir}/rc.d/init.d
rm -f %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-config

%preun
%systemd_preun %{name}.service

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root)
%doc MAINTAINERS README
%{_sbindir}/ipvsadm*
%{_unitdir}/ipvsadm.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-config

%files help
%{_mandir}/man8/*8*

%changelog
* Mon Jul 27 2020 zhouxuodng <zhouxudong8@huawei.com> - 1.31-2
- Type: requirement
- ID: NA
- SUG: NA
- DESC: add yaml

* Mon Apr 20 2020 zhouxudong <zhouxudong8@huawei.com> - 1.31-1
- Type: requirement
- ID: NA
- SUG: NA
- DESC: update to 1.31

* Mon Mar 02 2020 wangxiaopeng <wangxiaopeng7@huawei.com> - 1.29-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:sync ipvsadm for next branch 

* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.29-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Thu Nov 7 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.29-10
- Package init for openEuler
