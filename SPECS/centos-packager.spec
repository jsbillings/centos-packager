Name:           centos-packager
Version:        0.5.5
Release:        2.1%{?dist}
Summary:        Tools and files necessary for building CentOS packages
Group:          Applications/Productivity

License:        GPLv2+
URL:            https://git.centos.org/centos/centos-packager
Source0:        cbs-koji.conf
Source1:        COPYING
Source2:        centos-cert

Requires:       koji
Requires:       rpm-build rpmdevtools rpmlint
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       python-centos

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
ln -sf %{_bindir}/koji %{buildroot}%{_bindir}/cbs
%{__install} -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/centos-cert

%files
%defattr(-,root,root,-)
%doc COPYING
%config /etc/koji.conf.d/cbs-koji.conf
%{_bindir}/cbs
%{_bindir}/centos-cert

%changelog
* Wed Jun 03 2020 Jonathan Billings <jsbillings@jsbillings.org> - 0.5.5-2.1
- Ported to Python 3

* Wed Jul 19 2017 brian@bstinson.com 0.5.5-2
- Bumpspec to rebuild for F26

* Mon Nov 28 2016 brian@bstinson.com 0.5.5-1
- Update more references to ACO
- Make sure Exception messages don't print credentials to the screen

* Thu Oct 20 2016 brian@bstinson.com 0.5.4-1
- Update to point at the trust ca-bundle.crt #12110
- Update the help text to mention ACO

* Tue Oct 11 2016 brian@bstinson.com 0.5.3-1
- Rebuild to fix #12011

* Tue Nov 10 2015 brian@bstinson.com 0.5.2-1
- Fix a typo pointing to the ca-bundle in the cbs koji profile

* Thu Oct 29 2015 brian@bstinson.com 0.5.1-1
- Refactor to be more friendly if the http request fails
- Move centos_cert to centos-cert

* Wed Oct 28 2015 brian@bstinson.com 0.5.0-1
- The centos-cert utility now downloads the correct certificate, and sets up the
  CA certificate properly
- Updated the koji config to point to the downloaded certificates

* Sun Jul 26 2015 brian@bstinson.com 0.2.0-1
- Added the centos_cert utility
- Remove the dep on centpkg 
- Add a dep for python-centos

* Sun Dec 14 2014 Brian Stinson <bstinson@ksu.edu> - 0.1.0-1
- initial build
