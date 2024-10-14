Name:       kz
Version:    4.2.1
Release:    1
Group:      Utilities
Summary:    Installation and management scripts by Karel Zimmer
License:    CC0-1.0
BuildArch:  noarch
Requires:   psmisc, python3, python3-systemd, rsync, yum-utils, zenity

%description
Package kz contains scripts for installing and managing Red Hat and
Red Hat-based systems such as Rocky Linux.

For how to use this package see Checklist installation.

Checklist installation can be found on the site https://karelzimmer.nl/en,
under Linux.

%install
rsync --archive %{getenv:HOME}/kz-rpm/dist/etc %{buildroot}/
rsync --archive %{getenv:HOME}/kz-rpm/dist/usr %{buildroot}/

%clean

%files
/etc/*
/usr/*
