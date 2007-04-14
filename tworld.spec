#
# TODO: icon in games menu
#

Summary:	Chip's Challenge game emulation
Summary(pl.UTF-8):	Emulator gry Chip's Challenge
Name:		tworld
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.muppetlabs.com/~breadbox/pub/software/tworld/%{name}-%{version}-CCLP2.tar.gz
# Source0-md5:	100311f324b00a13649148448a20dc29
URL:		http://www.muppetlabs.com/~breadbox/software/tworld/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tile World is an emulation of the game "Chip's Challenge".

%description -l pl.UTF-8
Tile World jest emulacją silnika gry "Chip's Challenge".

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{res,data,sets}} $RPM_BUILD_ROOT%{_desktopdir}

install tworld $RPM_BUILD_ROOT%{_bindir}/tworld
install res/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/res
install data/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install sets/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/sets

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF

WARNING!
 If You want to play original Chip's Challenge levelset.
 Save file chips.dat to /usr/share/tworld/data

EOF

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
#%{_pixmapsdir}/tworld.png
#%{_desktopdir}/*.desktop
