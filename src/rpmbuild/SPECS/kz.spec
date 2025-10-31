Name:       kz
Version:    4.2.1
Release:    1
Group:      Utilities
Summary:    Installation and management scripts by Karel Zimmer
License:    CC0-1.0
BuildArch:  noarch
Requires:   epel-release, psmisc, python3-systemd, rsync, zenity

%description
Package kz contains scripts for installing and managing Red Hat and Red Hat-based systems such as Rocky Linux.

For how to use this package see Checklist installation.

Checklist installation can be found on the site https://karelzimmer.nl/en,
under Linux.

%install
rsync --archive kz-rpm/dist/etc %{buildroot}/
rsync --archive kz-rpm/dist/usr %{buildroot}/

%clean

%files
/etc/firefox/policies/policies.json
/etc/opt/chrome/policies/managed/policies.json
/etc/opt/edge/policies/managed/MSEDGE-GLOBAL.json
/usr/bin/*
/usr/share/applications/*
/usr/share/bash-completion/completions/*
/usr/share/doc/kz/build.id
/usr/share/doc/kz/copyright
/usr/share/doc/kz/README
/usr/share/gettext/its/kz-policy.its
/usr/share/gettext/its/kz-policy.loc
/usr/share/kz/kz-public-key.gpg
/usr/share/locale/nl/LC_MESSAGES/kz.mo
/usr/share/man/man1/*
/usr/share/man/man5/*
/usr/share/man/nl/man1/*
/usr/share/man/nl/man5/*
/usr/share/pixmaps/*
/usr/share/polkit-1/actions/nl.karelzimmer.kz_common.policy
/usr/share/polkit-1/actions/nl.karelzimmer.kz-install.policy
/usr/share/polkit-1/actions/nl.karelzimmer.kz-wifi.policy
