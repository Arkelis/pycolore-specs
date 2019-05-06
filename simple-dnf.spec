%global pyname simple_dnf
%global debug_package %{nil}

Name:           simple-dnf
Version:        0.1.2
Release:        2%{?dist}
Summary:        Simple GUI for DNF

License:        GPLv3+
URL:            https://hyakosm.net/articles/2018/11/27/simple-dnf.html

Source0:        https://github.com/Arkelis/simple_dnf/archive/v%version.tar.gz
Patch0:         simple-dnf.patch
AutoReqProv:    no
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
Requires:       python3-dnfdaemon
BuildArch:      noarch

%description
Simple DNF GUI for installing or removing packages.

%prep
%setup -q -n %pyname-%{version}
%patch0 -p1

%build
%py3_build

%install
cat > %name.desktop <<EOL
[Desktop Entry]
Name=Simple DNF
Comment=DNF GUI
Exec=simple-dnf
Icon=system-software-install
Type=Application
Encoding=UTF-8
Categories=System;Settings;PackageManager;
Keywords=dnf;packages;
X-StarupWMClass="Simple DNF"
StartupNotify=true
EOL
%py3_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %name.desktop

%files
%{python3_sitelib}/%{pyname}-*.egg-info/
%{python3_sitelib}/%{pyname}/
%{_bindir}/simple-dnf
%{_datadir}/applications/%name.desktop

%changelog
* Wed May 1 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> 0.1.2
- Bump to v0.1.2
