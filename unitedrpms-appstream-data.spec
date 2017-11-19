Name:       unitedrpms-appstream-data
Version:    2017.11.19
Release:    1%{?dist}
Summary:    Appstream metadata for the UnitedRPMs project repository
BuildArch:  noarch

License:    MIT
URL:        https://github.com/UnitedRPMs/%{name}

Source0:    https://github.com/UnitedRPMs/%{name}/releases/download/%{version}/unitedrpms.xml.gz 
Source1:    https://github.com/UnitedRPMs/%{name}/releases/download/%{version}/unitedrpms-icons.tar.gz

BuildRequires:  libappstream-glib
Supplements:    appstream-data

%description
Appstream metadata for packages in the UnitedRPMs repository. 


%prep


%build


%install
DESTDIR=%{buildroot} appstream-util install %{S:0} %{S:1}


%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/unitedrpms.xml.gz
%{_datadir}/app-info/icons/unitedrpms/
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/xmls

%changelog

* Sun Nov 19 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 2017.11.19-1
- Initial build
