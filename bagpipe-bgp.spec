%global pypi_name bagpipe-bgp

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Lightweight implementation of BGP IP VPN and E-VPN

License:        ASL 2.0
URL:            https://github.com/Orange-OpenSource/bagpipe-bgp
Source0:        https://<remove>files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

%description
BaGPipe BGP BaGPipe BGP is a lightweight implementation of BGP VPNs (IP VPNs
and EVPNs), targeting deployments on servers hosting VMs, in particular for
Openstack/KVM platforms.The goal is *not* to fully implement BGP
specifications, but only the subset of specifications required to implement IP
VPN VRFs and EVPN EVIs (RFC4364 < a.k.a RFC2547bis, RFC7432 < < and RFC4684 <
BGP is designed to...

%package -n     python2-%{pypi_name}
Summary:        Lightweight implementation of BGP IP VPN and E-VPN
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-pbr >= 1.6
Requires:       python-bottle
Requires:       python-daemon
Requires:       python-netaddr >= 0.7.7
Requires:       python-networking-bagpipe
Requires:       python-twisted >= 13.2
Requires:       python-setuptools

%description -n python2-%{pypi_name}
BaGPipe BGP BaGPipe BGP is a lightweight implementation of BGP VPNs (IP VPNs
and EVPNs), targeting deployments on servers hosting VMs, in particular for
Openstack/KVM platforms.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install
cp %{buildroot}/%{_bindir}/bagpipe-bgp-cleanup %{buildroot}/%{_bindir}/bagpipe-bgp-cleanup-2
ln -sf %{_bindir}/bagpipe-bgp-cleanup-2 %{buildroot}/%{_bindir}/bagpipe-bgp-cleanup-%{python2_version}
cp %{buildroot}/%{_bindir}/bagpipe-looking-glass %{buildroot}/%{_bindir}/bagpipe-looking-glass-2
ln -sf %{_bindir}/bagpipe-looking-glass-2 %{buildroot}/%{_bindir}/bagpipe-looking-glass-%{python2_version}
cp %{buildroot}/%{_bindir}/bagpipe-bgp %{buildroot}/%{_bindir}/bagpipe-bgp-2
ln -sf %{_bindir}/bagpipe-bgp-2 %{buildroot}/%{_bindir}/bagpipe-bgp-%{python2_version}
cp %{buildroot}/%{_bindir}/bagpipe-fakerr %{buildroot}/%{_bindir}/bagpipe-fakerr-2
ln -sf %{_bindir}/bagpipe-fakerr-2 %{buildroot}/%{_bindir}/bagpipe-fakerr-%{python2_version}
cp %{buildroot}/%{_bindir}/bagpipe-rest-attach %{buildroot}/%{_bindir}/bagpipe-rest-attach-2
ln -sf %{_bindir}/bagpipe-rest-attach-2 %{buildroot}/%{_bindir}/bagpipe-rest-attach-%{python2_version}


%files -n python2-%{pypi_name}
/etc/bagpipe-bgp/bgp.conf.template
/etc/bagpipe-bgp/log.conf.template
/etc/init.d/bagpipe-bgp
/etc/init.d/bagpipe-fakerr
%license LICENSE
%doc README.rst README.exabgp
%{_bindir}/bagpipe-bgp-cleanup
%{_bindir}/bagpipe-bgp-cleanup-2
%{_bindir}/bagpipe-bgp-cleanup-%{python2_version}
%{_bindir}/bagpipe-looking-glass
%{_bindir}/bagpipe-looking-glass-2
%{_bindir}/bagpipe-looking-glass-%{python2_version}
%{_bindir}/bagpipe-bgp
%{_bindir}/bagpipe-bgp-2
%{_bindir}/bagpipe-bgp-%{python2_version}
%{_bindir}/bagpipe-fakerr
%{_bindir}/bagpipe-fakerr-2
%{_bindir}/bagpipe-fakerr-%{python2_version}
%{_bindir}/bagpipe-rest-attach
%{_bindir}/bagpipe-rest-attach-2
%{_bindir}/bagpipe-rest-attach-%{python2_version}
%{python2_sitelib}/bagpipe
%{python2_sitelib}/bagpipe_bgp-%{version}-py?.?.egg-info

%changelog
* Thu Feb 02 2017 Luke Hinds - 1.80.0
- Initial package.
