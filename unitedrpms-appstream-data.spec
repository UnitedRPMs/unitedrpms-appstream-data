Name:       unitedrpms-appstream-data
Version:    2019.09.14
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

* Sat Sep 14 2019 David Vásquez <davidva AT tuta DOT io> - 2019.09.14-1
- Updated to 2019.09.14

* Wed Jun 27 2018 David Vásquez <davidva AT tuta DOT io> - 2018.06.07-1
- Updated to 2018.06.07

* Sun Apr 15 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 2018.04.14-1
- Updated to 2018.04.14

* Sun Nov 19 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 2017.11.19-1
- Initial build
