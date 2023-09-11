%if %{_use_internal_dependency_generator}
%define __noautoreq 'libR\\.so|libRblas\\.so|libRlapack\\.so'
%else
%define _requires_exceptions libR.so\\|libRblas.so\\|libRlapack.so
%endif

Summary:	A KDE gui to R language
Name:		rkward
Version:	0.7.5
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://rkward.sourceforge.net
Source0:	http://download.kde.org/stable/rkward/%{version}/src/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libR)
BuildRequires:	gcc-gfortran
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets) cmake(Qt5Core) cmake(Qt5Xml) cmake(Qt5Network) cmake(Qt5WebKitWidgets) cmake(Qt5Script) cmake(Qt5PrintSupport) cmake(Qt5Test)
BuildRequires:  cmake(KF5CoreAddons) cmake(KF5DocTools) cmake(KF5I18n) cmake(KF5XmlGui) cmake(KF5TextEditor) cmake(KF5WidgetsAddons) cmake(KF5WebKit) cmake(KF5Parts) cmake(KF5Config) cmake(KF5Notifications) cmake(KF5WindowSystem) cmake(KF5Crash)

Requires:	R-base
Requires:	php-cli
Suggests:	katepart
Obsoletes:	kde4-%{name} < 0.5.1
Provides:	kde4-%{name} = %{version}

%description
RKWard is meant to become an easy to use, transparent frontend to the
R-language, a very powerful, yet hard-to-get-into scripting-language with
a strong focus on statistic functions. It will not only provide a convenient
user-interface, however, but also take care of seamless integration with an
office-suite. Practical statistics is not just about calculating, after all,
but also about documenting and ultimately publishing the results.

%prep
%setup -qn %{name}-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

#(tpg) provide by R-base
rm -rf %{buildroot}%{_libdir}/R/lib/R.css

# provided by katepart
rm -f %{buildroot}%{_kde_appsdir}/katepart/syntax/r.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}*
%{_datadir}/kservices5/rkward.protocol
%{_datadir}/applications/*.desktop
%{_datadir}/rkward
#{_datadir}/kxmlgui5/rkward
%{_datadir}/mime/packages/*
%{_docdir}/*/*/*
%{_iconsdir}/*
%{_libdir}/libexec/%{name}.*
%{_mandir}/man1/%{name}.1*
#{_libdir}/R/*
%{_datadir}/org.kde.syntax-highlighting/syntax/*
