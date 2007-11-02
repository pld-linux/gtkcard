Summary:	A simple GUI application for using smart cards
Summary(pl.UTF-8):	Prosta aplikacja do używania kart procesorowych z graficznym interfejsem 
Name:		gtkcard
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.opensc-project.org/files/gtkcard/testing/%{name}-%{version}.tar.gz
# Source0-md5:	ed6454d6d076202e0849b0ba682b3e0a
URL:		http://www.opensc-project.org/gtkcard/
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	opensc
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 1:2.0.3
Requires:	opensc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple GUI application for using smart cards.

%description -l pl.UTF-8
Prosta aplikacja do używania kart procesorowych z graficznym
interfejsem użytkownika.

%prep
%setup -q

%build
%configure \
	--enable-pkcs11=%{_libdir}/opensc-pkcs11.so

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/GTKCard
