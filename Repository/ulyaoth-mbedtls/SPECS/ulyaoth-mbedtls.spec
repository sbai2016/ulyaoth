Summary: mbed TLS is an open source and commercial SSL library licensed by ARM Limited.. mbed TLS used to be called PolarSSL,
Name: ulyaoth-mbedtls
Version: 1.3.10
Release: 1%{?dist}
BuildArch: x86_64
Vendor: ARM Limited.
URL: https://tls.mbed.org/
Packager: Sjir Bagmeijer <sbagmeijer@ulyaoth.co.kr>

Source0: https://tls.mbed.org/download/start/mbedtls-1.3.10-gpl.tgz

License: GPLv2 or proprietary

BuildRoot: %{_tmppath}/mbedtls-%{version}-%{release}-root
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: openssl-devel

Provides: mbedtls
Provides: ulyaoth-mbedtls

%description
mbed TLS (formerly known as PolarSSL) makes it trivially easy for developers to include cryptographic and SSL/TLS capabilities in their (embedded) products, facilitating this functionality with a minimal coding footprint.

%prep
%setup -q -n mbedtls-%{version}

%build
%cmake -D CMAKE_BUILD_TYPE:String="Release" -D USE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE -DENABLE_ZLIB_SUPPORT:BOOL=TRUE USE_PKCS11_HELPER_LIBRARY:BOOL=TRUE .
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)


%pre

%post
# Register the monkey service
    # print site info
    cat <<BANNER
----------------------------------------------------------------------

Thanks for using ulyaoth-mbedtls!

Please find the official documentation for mbedtls here:
* https://tls.mbed.org

For any additional help please visit my forum at:
* http://www.ulyaoth.net

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Sun May 3 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.co.kr> 1.3.10-1
- Initial release.