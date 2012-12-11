%if %{_use_internal_dependency_generator}
%define __noautoreq 'libR\\.so|libRblas\\.so|libRlapack\\.so'
%else
%define _requires_exceptions libR.so\\|libRblas.so\\|libRlapack.so
%endif

Summary:	A KDE gui to R language
Name:		rkward
Version:	0.6.0
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://rkward.sourceforge.net
Source0:	http://downloads.sourceforge.net/rkward/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libR)
BuildRequires:	kdelibs4-devel
BuildRequires:	gcc-gfortran
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
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
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

#(tpg) provide by R-base
rm -rf %{buildroot}%{_libdir}/R/lib/R.css

# provided by katepart
rm -f %{buildroot}%{_kde_appsdir}/katepart/syntax/r.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_kde_bindir}/%{name}*
%{_kde_datadir}/applications/kde4/rkward.desktop
%{_kde_appsdir}/rkward
%{_kde_appsdir}/katepart/*
%{_kde_docdir}/*/*/*
%{_kde_iconsdir}/*
%{_kde_libdir}/kde4/libexec/%{name}.*
%{_kde_mandir}/man1/%{name}.1*
%{_libdir}/R/*

