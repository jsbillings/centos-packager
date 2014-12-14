Name:           centos-packager
Version:        0.1.0
Release:        1%{?dist}
Summary:        Tools and files necessary for building CentOS packages
Group:          Applications/Productivity

License:        GPLv2+
URL:            http://www.centos.org
Source0:        cbs-koji.conf
Source1:        COPYING

Requires:       koji
Requires:       rpm-build rpmdevtools rpmlint
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       centpkg

BuildArch:      noarch

%description
Tools to help set up a CentOS packaging environment


%prep
cp %{SOURCE1} .

%build
# Nothing here

%install
%{__mkdir_p} %{buildroot}/etc/koji.conf.d/
%{__install} -m 0644 %{SOURCE0} %{buildroot}/etc/koji.conf.d/cbs-koji.conf

%{__mkdir_p} %{buildroot}/%{_bindir}
ln -sf %{_bindir}/koji %{buildroot}/%{_bindir}/cbs

%files
%defattr(-,root,root,-)
%doc COPYING
%config /etc/koji.conf.d/cbs-koji.conf
%{_bindir}/cbs

%changelog
* Sun Dec 14 2014 Brian Stinson <bstinson@ksu.edu> - 0.1.0-1
- initial build
