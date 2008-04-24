%define _requires_exceptions libR.so\\|libRblas.so\\|libRlapack.so
%define oname rkward

Summary:	A KDE gui to R language
Name:		kde4-%{oname}
Version:	0.5.0b
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://rkward.sourceforge.net
Source0:	http://downloads.sourceforge.net/rkward/%{oname}-%{version}.tar.bz2
Buildrequires:	R-base		>= 2.6.0
BuildRequires:	kdelibs4-devel	>= 4.0.0
BuildRequires:	gcc-gfortran
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	kde4-macros
Requires:	R-base		>= 2.6.0
Requires:	php-cli
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RKWard is meant to become an easy to use, transparent frontend to the 
R-language, a very powerful, yet hard-to-get-into scripting-language with 
a strong focus on statistic functions. It will not only provide a convenient 
user-interface, however, but also take care of seamless integration with an 
office-suite. Practical statistics is not just about calculating, after all, 
but also about documenting and ultimately publishing the results.

This is a KDE4 port of %{oname}.

%prep
%setup -qn %{oname}-%{version}

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

%find_lang %{oname}

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_kde_bindir}/%{oname}*
%{_kde_datadir}/applications/kde4/rkward.desktop
%{_kde_appsdir}/rkward
%{_kde_appsdir}/katepart/*
%{_kde_docdir}/*/*/*
%{_kde_iconsdir}/*
%{_libdir}/R/*
