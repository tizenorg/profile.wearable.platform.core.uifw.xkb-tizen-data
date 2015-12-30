Name:          xkb-tizen-data
Version:       0.0.2
Release:       0
BuildArch:     noarch
Summary:       Xkb data files
Group:         Graphics & UI Framework/Other
License:       MIT
Source0:       %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest

%description
Data files for Xkb keymap

%prep
%setup -q
cp -a %{SOURCE1001} .

%build
%autogen
%configure

make

%install
rm -rf %{buildroot}

# install service
%__mkdir_p %{buildroot}/usr/share/X11/xkb
%__cp -f xkb/tizen_key_layout.txt %{buildroot}/usr/share/X11/xkb/tizen_key_layout.txt

%pre

%postun

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
/usr/share/X11/xkb/tizen_key_layout.txt
