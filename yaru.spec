%global debug_package %{nil}

Name:           yaru
Version:        19.10.1
Release:        1%{?dist}
Summary:        Ubuntu community theme "yaru" 

License:        LGPLv3
URL:            https://github.com/ubuntu/yaru
Source0:	https://github.com/ubuntu/yaru/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	sassc
BuildRequires:  glib2-devel

Requires:	yaru-gnome-shell-theme 
Requires:	yaru-icon-theme 
Requires:	yaru-gtk2-theme 
Requires:	yaru-gtk3-theme 
Requires:	yaru-sound-theme
Provides:	communitheme = %{version}-%{release}

%description
Yaru theme is the default theme for Ubuntu, entirely backed by the community. This is the theme that is shaped by the community on the Ubuntu hub, turned into the default theme starting from Ubuntu 18.10 Cosmic Cuttlefish.

#--
%package gnome-shell-theme
Summary:        GNOME Shell Ubuntu community theme "yaru"
Requires:       %{name}-icon-theme = %{version}-%{release}

%description gnome-shell-theme
GNOME Shell Ubuntu community theme "yaru"

#--
%package icon-theme
Summary:        Icon theme Ubuntu community theme "yaru"

%description icon-theme
Icon theme Ubuntu community theme "yaru"

#--
%package gtk2-theme
Summary:        The GTK+ 2 parts of the Ubuntu community theme "yaru"

%description gtk2-theme
The GTK+ 2 parts of the Ubuntu community theme "yaru"

#--
%package gtk3-theme
Summary:        The GTK+ 3 parts of the Ubuntu community theme "yaru"

%description gtk3-theme
The GTK+ 3 parts of the Ubuntu community theme "yaru"

#--
%package sound-theme
Summary:        Sound theme Ubuntu community theme "yaru"

%description sound-theme
Sound theme Ubuntu community theme "yaru"

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post icon-theme
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%postun icon-theme
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans icon-theme
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override

%files gnome-shell-theme
%{_datadir}/gnome-shell/
%{_datadir}/wayland-sessions/Yaru-wayland.desktop
%{_datadir}/xsessions/Yaru.desktop

%files icon-theme
%{_datadir}/icons/Yaru/
%{_datadir}/themes/Yaru/index.theme

%files gtk2-theme
%{_datadir}/themes/Yaru-dark/gtk-2.0/
%{_datadir}/themes/Yaru/gtk-2.0/

%files gtk3-theme
%{_datadir}/themes/Yaru/gtk-3.0/
%{_datadir}/themes/Yaru-dark/gtk-3.0/
%{_datadir}/themes/Yaru-dark/index.theme
%{_datadir}/themes/Yaru-dark/gtk-3.20/
%{_datadir}/themes/Yaru/gtk-3.20/


%files sound-theme
%{_datadir}/sounds/Yaru/

%changelog
* Fri Aug 30 2019 Guillaume Fayard <guillaume DOT fayard AT pycolore DOT fr> 19.10.1-1

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
