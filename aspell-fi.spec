Summary:	Finnish dictionary for aspell
Summary(pl.UTF-8):	Fiński słownik dla aspella
Name:		aspell-fi
Version:	0.7
%define	subv	0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/fi/aspell6-fi-%{version}-%{subv}.tar.bz2
# Source0-md5:	6d1032116982c0efab1af8fce83259c0
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Finnish dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Fiński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-fi-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
