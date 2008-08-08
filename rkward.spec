%define _requires_exceptions libR.so\\|libRblas.so\\|libRlapack.so

Summary:	A KDE gui to R language
Name:		rkward
Version:	0.5.0b
Release:	%mkrel 5
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://rkward.sourceforge.net
Source0:	http://downloads.sourceforge.net/rkward/%{name}-%{version}.tar.bz2
Buildrequires:	R-base		>= 2.6.0
BuildRequires:	kdelibs4-devel	>= 4.0.0
BuildRequires:	gcc-gfortran
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	kde4-macros
Requires:	R-base		>= 2.6.0
Requires:	php-cli
Obsoletes:      kde4-%{name} <= 0.5.0b
Provides:       kde4-%{name} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%cmake_kde4

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

pushd build
%makeinstall_std
popd

#(tpg) provide by R-base
rm -rf %{buildroot}%{_libdir}/R/lib/R.css

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_kde_bindir}/%{name}*
%{_kde_datadir}/applications/kde4/rkward.desktop
%{_kde_appsdir}/rkward
%{_kde_appsdir}/katepart/*
%{_kde_docdir}/*/*/*
%{_kde_iconsdir}/*
%{_libdir}/R/*
