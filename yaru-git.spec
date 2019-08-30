%global debug_package %{nil}
%global commit        e4f61c45f69131281dbce8ad305c75673fcf4b80
%global shortcommit   %(c=%{commit}; echo ${c:0:7})
%global date          20190504
Name:           yaru-git
Version:        19.04.1
Release:        1.git%{shortcommit}%{?dist}
Summary:        Ubuntu community theme "yaru" 

License:        LGPLv3
URL:            https://github.com/ubuntu/yaru
Source0:        https://github.com/ubuntu/yaru/tarball/%{commit}#/%{name}-%{version}git%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	sassc
BuildRequires:  glib2-devel

Requires:	yaru-gnome-shell-theme-git
Requires:	yaru-icon-theme-git
Requires:	yaru-gtk2-theme-git
Requires:	yaru-gtk3-theme-git
Requires:	yaru-sound-theme-git
Provides:	communitheme = %{version}-%{release}
Conflicts:      yaru

%description
Yaru theme is the default theme for Ubuntu, entirely backed by the community. This is the theme that is shaped by the community on the Ubuntu hub, turned into the default theme starting from Ubuntu 18.10 Cosmic Cuttlefish.

#--
%package -n yaru-gnome-shell-theme-git
Summary:        GNOME Shell Ubuntu community theme "yaru"
Requires:       yaru-icon-theme-git = %{version}-%{release}
Conflicts:      yaru-gnome-shell-theme

%description -n yaru-gnome-shell-theme-git
GNOME Shell Ubuntu community theme "yaru"

#--
%package -n yaru-icon-theme-git
Summary:        Icon theme Ubuntu community theme "yaru"
Conflicts:      yaru-icon-theme

%description -n yaru-icon-theme-git
Icon theme Ubuntu community theme "yaru"

#--
%package -n yaru-gtk2-theme-git
Summary:        The GTK+ 2 parts of the Ubuntu community theme "yaru"
Conflicts:       yaru-gtk2-theme

%description -n yaru-gtk2-theme-git
The GTK+ 2 parts of the Ubuntu community theme "yaru"

#--
%package -n yaru-gtk3-theme-git
Summary:        The GTK+ 3 parts of the Ubuntu community theme "yaru"
Conflicts:      yaru-gtk3-theme

%description -n yaru-gtk3-theme-git
The GTK+ 3 parts of the Ubuntu community theme "yaru"

#--
%package -n yaru-sound-theme-git
Summary:        Sound theme Ubuntu community theme "yaru"
Conflicts:      yaru-sound-theme

%description -n yaru-sound-theme-git
Sound theme Ubuntu community theme "yaru"

%prep
%autosetup -n ubuntu-yaru-%{shortcommit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -n yaru-icon-theme-git
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%postun -n yaru-icon-theme-git
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans -n yaru-icon-theme-git
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override

%files -n yaru-gnome-shell-theme-git
%{_datadir}/gnome-shell/
%{_datadir}/wayland-sessions/Yaru-wayland.desktop
%{_datadir}/xsessions/Yaru.desktop

%files -n yaru-icon-theme-git
%{_datadir}/icons/Yaru/
%{_datadir}/themes/Yaru/index.theme

%files -n yaru-gtk2-theme-git
%{_datadir}/themes/Yaru-dark/gtk-2.0/
%{_datadir}/themes/Yaru/gtk-2.0/

%files -n yaru-gtk3-theme-git
%{_datadir}/themes/Yaru/gtk-3.0/
%{_datadir}/themes/Yaru-dark/gtk-3.0/
%{_datadir}/themes/Yaru-dark/index.theme
%{_datadir}/themes/Yaru-dark/gtk-3.20/
%{_datadir}/themes/Yaru/gtk-3.20/


%files -n yaru-sound-theme-git
%{_datadir}/sounds/Yaru/

%changelog
* Wed May 4 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> r29
- Updated to commit 9e00d5cc712dced3a0637d3ccb631715b827a040

* Wed Apr 24 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> r29
- Updated to r29 release

* Thu Nov 15 2018 David Va <davidva AT tuta DOT io> 18.10.7-3
- Updated to current commit

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 18.10.7-2
- Updated to current commit

* Mon Oct 22 2018 David Va <davidva AT tuta DOT io> 18.10.7-1
- Updated to 18.10.7

* Wed Oct 10 2018 David Va <davidva AT tuta DOT io> 18.10.6-1
- Updated to 18.10.6

* Mon Oct 01 2018 David Va <davidva AT tuta DOT io> 18.10.5-1
- Updated to 18.10.5

* Mon Sep 17 2018 David Va <davidva AT tuta DOT io> 18.10.4-1
- Updated to 18.10.4

* Fri Sep 14 2018 David Va <davidva AT tuta DOT io> 18.10.3-1
- Updated to 18.10.3

* Sun Aug 05 2018 David Va <davidva AT tuta DOT io> 18.10.1-2
- Updated to current commit

* Sun Aug 05 2018 David Va <davidva AT tuta DOT io> 18.10.1-1
- Updated to 18.10.1

* Thu Jul 26 2018 David Va <davidva AT tuta DOT io> 18.10-1
- Initial build
