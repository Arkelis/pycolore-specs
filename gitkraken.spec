Name:           gitkraken
Version:        5.0.4
Release:        1%{?dist}
Summary:        GitKraken

License:        GitKraken End User License Agreement
URL:            https://www.gitkraken.com/
Source0:        https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz

AutoReqProv: no
Requires:       libXScrnSaver, libcurl

%description
Client graphique Git. 


%prep
%autosetup -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/gitkraken
cp -r  ./ $RPM_BUILD_ROOT/opt/gitkraken/
rm -rf gitkraken

%post
ln -s /usr/lib64/libcurl.so.4 /usr/lib64/libcurl-gnutls.so.4
cat > /usr/share/applications/gitkraken.desktop <<EOL
[Desktop Entry]
Name=GitKraken
Comment=Client graphique Git
Exec=/opt/gitkraken/gitkraken
Icon=/opt/gitkraken/gitkraken.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Utility;Development;
EOL

%files
/opt/gitkraken/

%postun
rm /usr/lib64/libcurl-gnutls.so.4
rm /usr/share/applications/gitkraken.desktop

%changelog
* Thu Dec  6 2018 builder
- 
