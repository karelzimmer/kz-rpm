Name:       kz
Version:    4.2.1
Release:    1
Group:      Utilities
Summary:    Installation and management scripts by Karel Zimmer
License:    CC0-1.0
BuildArch:  noarch
Requires:   epel-release, psmisc, python3, python3-systemd, rsync, yum-utils, zenity

%description
Package kz contains scripts for installing and managing Red Hat-based systems such as AlmaLinux and Rocky Linux.

For how to use this package see Checklist installation.

Checklist installation can be found on the site https://karelzimmer.nl/en,
under Linux.

%install
rsync --archive kz-rpm/dist/etc %{buildroot}/
rsync --archive kz-rpm/dist/usr %{buildroot}/

%clean

%files
/etc/firefox/policies/*
/etc/opt/chrome/policies/managed/*
/usr/bin/*
/usr/share/applications/*
/usr/share/bash-completion/completions/*
/usr/share/doc/kz/*
/usr/share/kz/*
/usr/share/locale/nl/LC_MESSAGES/*
/usr/share/man/man1/*
/usr/share/man/man7/*
/usr/share/man/nl/man1/*
/usr/share/man/nl/man7/*
/usr/share/pixmaps/*
/usr/share/polkit-1/actions/*
