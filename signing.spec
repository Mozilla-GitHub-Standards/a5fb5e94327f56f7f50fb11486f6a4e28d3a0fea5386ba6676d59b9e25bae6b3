%define pyver 26
%define name python%{pyver}-receiptsigner
%define pythonname signing
%define version 0.1
%define release 1

Summary: Receipt Signing App
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{version}.tar.gz
License: MPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Services team <services-dev@mozilla.org>
Requires: python%{pyver} python%{pyver}-setuptools python%{pyver}-webob
Requires: python%{pyver}-paste python%{pyver}-pastedeploy python%{pyver}-pyramid
Requires: python%{pyver}-simplejson python%{pyver}-m2crypto python%{pyver}-cef
Requires: python%{pyver}-jwt

Url: https://github.com/rtilder/signing

%description
See README

%package certifier
Requires: python%{pyver} python%{pyver}-simplejson python%{pyver}-m2crypto
Requires: python%{pyver}-cef python%{pyver}-jwt python%{pyver}-requests
Requires: python%{pyver}-argparse

%description certifier
Scripts to run on the machine with the HSM that does key generation and
certification

%prep
%setup -n %{pythonname}-%{version} -n %{pythonname}-%{version}

%build
python2.6 setup.py build

%install
python2.6 setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES

%defattr(-,root,root)