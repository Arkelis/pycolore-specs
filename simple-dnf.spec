%global pyname simple_dnf
%global debug_package %{nil}

Name:           simple-dnf
Version:        0.1.3
Release:        1%{?dist}
Summary:        Simple GUI for DNF

License:        GPLv3+
URL:            https://hyakosm.net/articles/2018/11/27/simple-dnf.html

Source0:        https://github.com/Arkelis/simple_dnf/archive/v%version.tar.gz
# The following patch generates setup.py, as poetry does not use setuptools but distutils.
# See: https://github.com/sdispater/poetry/issues/866
Patch0:         simple-dnf.patch
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

%doc README.md

%license LICENSE

%changelog
* Wed Jul 3 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> 0.1.3-1
- Some packaging fixes

* Mon May 13 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> 0.1.2-3
- Some packaging fixes

* Wed May 1 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> 0.1.2-2
- Bump to v0.1.2
