# TODO: lipiDesigner (JNI+Java)
Summary:	Toolkit for creation and evaluation of recognizers for isolated shapes
Summary(pl.UTF-8):	Narzędzia do tworzenia i ewaluacji modeli rozpoznawania oddzielonych kształtów
Name:		lipi-toolkit
Version:	4.0.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://download.sourceforge.net/lipitk/%{name}%{version}-src-linux.tar.gz
# Source0-md5:	e2789ed38ca5566f46a1e98bb42914fa
URL:		http://lipitk.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toolkit for creation and evaluation of recognizers for isolated
shapes, such as handwritten gestures and characters.

%description -l pl.UTF-8
Narzędzia do tworzenia i ewaluacji modeli rozpoznawania oddzielonych
kształtów, takich jak pisane ręcznie gesty czy znaki.

%package devel
Summary:	Header files for LipiToolkit library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LipiToolkit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for LipiToolkit library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LipiToolkit.

%package doc
Summary:	Documentation for LipiToolkit library
Summary(pl.UTF-8):	Dokumentacja biblioteki LipiToolkit
Group:		Documentation
BuildArch:	noarch

%description doc
Documentation for LipiToolkit library.

%description doc -l pl.UTF-8
Dokumentacja biblioteki LipiToolkit.

%prep
%setup -q -n %{name}%{version}-src-linux

%build
%{__make} -f linux/Makefile.linux \
	LIPI_ROOT=$(pwd) \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcxxflags} -c" \
	CPPFLAGS="%{rpmcppflags} -Wno-deprecated"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/lipi-toolkit/lib,%{_includedir}/lipi-toolkit}

install lib/*.so $RPM_BUILD_ROOT%{_libdir}/lipi-toolkit/lib
cp -p src/include/*.h $RPM_BUILD_ROOT%{_includedir}/lipi-toolkit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%dir %{_libdir}/lipi-toolkit
%dir %{_libdir}/lipi-toolkit/lib
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libactivedtw.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libboxfld.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libl7.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/liblipiengine.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/liblogger.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libneuralnet.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libnn.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libnpen.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libpointfloat.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libpreproc.so
%attr(755,root,root) %{_libdir}/lipi-toolkit/lib/libsubstroke.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lipi-toolkit

%files doc
%defattr(644,root,root,755)
%doc doc/{*.cfg,*.pdf}
