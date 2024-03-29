%define major 3

#define snapshot 20220106
%define libname %mklibname MauiKitDocuments
%define devname %mklibname -d MauiKitDocuments

Name:		mauikit-documents
Version:	3.1.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	MauiKit QtQuick plugins for text editing
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-documents/-/archive/%{?snapshot:master/mauikit-documents-master.tar.bz2#/mauikit-documents-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-documents-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit3)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:  cmake(Qt5PacketProtocol)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
Requires:	%{libname} = %{EVRD}

%description
Library for developing MAUI applications text editing

%package -n %{libname}
Summary:	Library files for mauikit-documents
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for mauikit-documents

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{devname}
Summary:	Development files for mauikit-documents
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for mauikit-documents

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.


%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang mauikitdocuments

%files -f mauikitdocuments.lang

%files -n %{libname}
%{_libdir}/libMauiKitDocuments3.so*
%{_libdir}/qt5/qml/org/mauikit/documents/

%files -n %{devname}
%{_includedir}/MauiKit3/Documents/
%{_libdir}/cmake/MauiKitDocuments3/
