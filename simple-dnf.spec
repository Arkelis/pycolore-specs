Name:           simple-dnf
Version:        alpha
Release:        0.2%{?dist}
Summary:        Simple GUI for DNF

License:        GPLv3
URL:            https://hyakosm.net/articles/2018/11/27/simple-dnf.html

AutoReqProv: no
Requires:       python3-dnfdaemon

%description
Simple DNF GUI for installing or removing packages.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/python3.7/site-packages/simple_dnf
cp -r ~/simple-dnf/simple_dnf/. $RPM_BUILD_ROOT/usr/lib/python3.7/site-packages/simple_dnf
cp $RPM_BUILD_ROOT/usr/lib/python3.7/site-packages/simple_dnf/simple-dnf $RPM_BUILD_ROOT/usr/bin/simple-dnf
chmod +x $RPM_BUILD_ROOT/usr/bin/simple-dnf

%post
cat > /usr/share/applications/simple-dnf.desktop <<EOL
[Desktop Entry]
Name=Simple DNF
Comment=DNF GUI
Exec=/usr/lib/python3.7/site-packages/simple_dnf/main.py
Path=/usr/lib/python3.7/site-packages/simple_dnf/
Icon=system-software-install
Type=Application
Encoding=UTF-8
Categories=System;Settings;PackageManager;
Keywords=dnf;packages;
StarupWMClass="Simple DNF"
StartupNotify=true
EOL

%files
/usr/lib/python3.7/site-packages/simple_dnf/
/usr/bin/simple-dnf

%postun
rm /usr/share/applications/simple-dnf.desktop

%changelog
* Thu Dec  6 2018 builder
- 
