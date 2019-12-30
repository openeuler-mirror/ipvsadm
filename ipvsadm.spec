Name:             ipvsadm
Version:          1.29
Release:          11
Summary:          A utility to administer the IP virtual server services
License:          GPLv2+
URL:              https://kernel.org/pub/linux/utils/kernel/ipvsadm/
Source0:          https://kernel.org/pub/linux/utils/kernel/ipvsadm/%{name}-%{version}.tar.gz
Source1:          ipvsadm.service

Patch6000:        ipvsadm-catch-the-original-errno-from-netlink-answer.patch
Patch6001:        libipvs-discrepancy-with-libnl-genlmsg_put.patch
Patch6002:        ipvsadm-use-CFLAGS-and-LDFLAGS-environment-variables.patch

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

%files help
%{_mandir}/man8/*8*

%changelog
* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.29-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Thu Nov 7 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.29-10
- Package init for openEuler
