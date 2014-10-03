Summary:	Build infrastructure and utilities
Name:		mm-common
Version:	0.9.7
Release:	1
License:	GPL v2
Group:		Development
Source0:	http://download.gnome.org/sources/mm-common/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	a8b7c11db81a72168bf38d88d97df686
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is only a required
dependency for building the C++ bindings from the gnome.org version
control repository.  An installation of mm-common is not required for
building tarball releases, unless configured to use maintainer-mode.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mm-common-prepare
%docdir %{_docdir}/mm-common
%{_docdir}/mm-common
%{_aclocaldir}/mm-*.m4
%{_datadir}/mm-common
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/mm-common-prepare.1*

