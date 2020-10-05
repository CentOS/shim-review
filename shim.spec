Name:           shim
Version:        15
Release:        9.el7
Summary:        First-stage UEFI bootloader

License:        BSD
URL:            http://www.codon.org.uk/~mjg59/shim/
Source0:        https://github.com/mjg59/shim/releases/download/%{version}/shim-%{version}.tar.bz2
Source1:        shim-find-debuginfo.sh

#Source100:      db.aa64.esl
#Source101:      dbx.aa64.esl
#Source200:      db.x64.esl
#Source201:      dbx.x64.esl

Source200:      centos.db.x64.esl

Patch0001: 0001-Make-some-things-dprint-instead-of-console_print.patch
Patch0002: 0002-Makefiles-ensure-m32-gets-propogated-to-our-gcc-para.patch
Patch0003: 0003-Let-MokManager-follow-a-MokTimeout-var-for-timeout-l.patch
Patch0004: 0004-httpboot-return-EFI_NOT_FOUND-when-it-fails-to-find-.patch
Patch0005: 0005-httpboot-print-more-messages-when-it-fails-to-set-IP.patch
Patch0006: 0006-httpboot-allow-the-IPv4-gateway-to-be-empty.patch
Patch0007: 0007-httpboot-show-the-error-message-for-the-ChildHandle.patch
Patch0008: 0008-Fix-typo-in-debug-path-in-shim.h.patch
Patch0009: 0009-MokManager-Stop-using-EFI_VARIABLE_APPEND_WRITE.patch
Patch0010: 0010-shim-Extend-invalid-reloc-size-warning-message.patch
Patch0011: 0011-Add-GRUB-s-PCR-Usage-to-README.tpm.patch
Patch0012: 0012-Fix-the-compile-error-of-mkdir-wrong-directory.patch
Patch0013: 0013-shim-Properly-generate-absolute-paths-from-relative-.patch
Patch0014: 0014-shim-Prevent-shim-to-set-itself-as-a-second-stage-lo.patch
Patch0015: 0015-Fix-for-Section-0-has-negative-size-error-when-loadi.patch
Patch0016: 0016-Fix-apparent-typo-in-ARM-32-on-64-code.patch
Patch0017: 0017-Makefile-do-not-run-git-on-clean-if-there-s-no-.git-.patch
Patch0018: 0018-Make.default-use-correct-flags-to-disable-unaligned-.patch
Patch0019: 0019-Cryptlib-fix-build-on-32bit-ARM.patch
Patch0020: 0020-Make-sure-that-MOK-variables-always-get-mirrored.patch
Patch0021: 0021-mok-fix-the-mirroring-of-RT-variables.patch
Patch0022: 0022-mok-consolidate-mirroring-code-in-a-helper-instead-o.patch
Patch0023: 0023-shim-only-include-shim_cert.h-in-shim.c.patch
Patch0024: 0024-mok-also-mirror-the-build-cert-to-MokListRT.patch
Patch0025: 0025-mok-minor-cleanups.patch
Patch0026: 0026-Remove-call-to-TPM2-get_event_log.patch
Patch0027: 0027-Make-EFI-variable-copying-fatal-only-on-secureboot-e.patch
Patch0028: 0028-VLogError-Avoid-NULL-pointer-dereferences-in-V-Sprin.patch
Patch0029: 0029-Once-again-try-even-harder-to-get-binaries-without-t.patch
Patch0030: 0030-shim-Rework-pause-functions-and-add-read_counter.patch
Patch0031: 0031-Hook-exit-when-shim_lock-protocol-installed.patch
Patch0032: 0032-Work-around-stuff-Waddress-of-packed-member-finds.patch
Patch0033: 0033-Fix-a-use-of-strlen-instead-of-Strlen.patch
Patch0034: 0034-MokManager-Use-CompareMem-on-MokListNode.Type-instea.patch
Patch0035: 0035-OpenSSL-always-provide-OBJ_create-with-name-strings.patch
Patch0036: 0036-Use-portable-shebangs-bin-bash-usr-bin-env-bash.patch
Patch0037: 0037-tpm-Fix-off-by-one-error-when-calculating-event-size.patch
Patch0038: 0038-tpm-Define-EFI_VARIABLE_DATA_TREE-as-packed.patch
Patch0039: 0039-MokManager-console-mode-modification-for-hi-dpi-scre.patch
Patch0040: 0040-MokManager-avoid-Werror-address-of-packed-member.patch
Patch0041: 0041-tpm-Don-t-log-duplicate-identical-events.patch
Patch0042: 0042-Slightly-better-debugging-messages.patch
Patch0043: 0043-Actually-check-for-errors-from-set_second_stage.patch
Patch0044: 0044-translate_slashes-don-t-write-to-string-literals.patch
Patch0045: 0045-shim-Update-EFI_LOADED_IMAGE-with-the-second-stage-l.patch
Patch0046: 0046-tpm-Include-information-about-PE-COFF-images-in-the-.patch
Patch0047: 0047-Fix-the-license-on-our-buildid-extractor.patch
Patch0048: 0048-Update-README.tpm.patch
Patch0049: 0049-Check-PxeReplyReceived-as-fallback-in-netboot.patch
Patch0050: 0050-Remove-a-couple-of-incorrect-license-claims.patch
Patch0051: 0051-MokManager-fix-uninitialized-value.patch
Patch0052: 0052-Fix-some-volatile-usage-gcc-whines-about.patch
Patch0053: 0053-MokManager-fix-a-wrong-allocation-failure-check.patch
Patch0054: 0054-simple_file-fix-uninitialized-variable-unchecked-ret.patch
Patch0055: 0055-Fix-a-broken-tpm-type.patch
Patch0056: 0056-Make-cert.S-not-impossible-to-read.patch
Patch0057: 0057-Add-support-for-vendor_db-built-in-shim-authorized-l.patch
Patch0058: 0058-Handle-binaries-with-multiple-signatures.patch
Patch0059: 0059-Make-openssl-accept-the-right-set-of-KU-EKUs.patch
Patch0060: 0060-Improve-debug-output-some.patch
Patch0061: 0061-Also-use-a-config-table-to-mirror-mok-variables.patch
Patch0062: 0062-Implement-lennysz-s-suggestions-for-MokListRT.patch
Patch0063: 0063-hexdump.h-fix-arithmetic-error.patch
Patch0064: 0064-Fix-some-mokmanager-stuff.patch
Patch0065: 0065-Fix-buffer-overrun-due-DEFAULT_LOADER-length-miscalc.patch

BuildRequires: git openssl-devel openssl
BuildRequires: pesign >= 0.106-1
BuildRequires: gnu-efi >= 1:3.0.5-6.el7, gnu-efi-devel >= 1:3.0.5-6.el7

# for xxd
BuildRequires: vim-common

# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI is not
# compatible with SysV (there's no red zone under UEFI) and there isn't a
# POSIX-style C library.
Provides: bundled(openssl) = 1.0.2j

# Shim is only required on platforms implementing the UEFI secure boot
# protocol. The only one of those we currently wish to support is 64-bit x86.
# Adding further platforms will require adding appropriate relocation code.
ExclusiveArch: x86_64 aarch64

%ifarch x86_64
%global efiarch x64
%endif
%ifarch aarch64
%global efiarch aa64
%endif

# Figure out the right file path to use
%global efidir %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))

%define debug_package %{nil}
%global __debug_package 1

%global _binaries_in_noarch_packages_terminate_build 0

%description
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments.

%package -n shim-unsigned-%{efiarch}
Summary: First-stage UEFI bootloader (unsigned data)

%description -n shim-unsigned-%{efiarch}
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments.

%package -n shim-unsigned-%{efiarch}-debuginfo
Obsoletes: shim-debuginfo < 0.9
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
BuildArch: noarch

%description -n shim-unsigned-%{efiarch}-debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%ifarch x86_64
%package -n shim-unsigned-ia32
Summary: First-stage UEFI bootloader (unsigned data)

%description -n shim-unsigned-ia32
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments.

%package -n shim-unsigned-ia32-debuginfo
Obsoletes: shim-debuginfo < 0.9
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
BuildArch: noarch

%description -n shim-unsigned-ia32-debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.
%endif

%prep
%setup -T -n %{name}-%{version}-%{release} -c
%{__tar} -xo -f %{SOURCE0}
mv %{name}-%{version} %{name}-%{version}-%{efiarch}
cd %{name}-%{version}-%{efiarch}
git init
git config user.email "example@example.com"
git config user.name "rpmbuild -bp"
git add .
git commit -a -q -m "%{version} baseline."
git am --ignore-whitespace %{patches} </dev/null
git config --unset user.email
git config --unset user.name

%ifarch x86_64
cd ..
%{__tar} -xo -f %{SOURCE0}
mv %{name}-%{version} %{name}-%{version}-ia32
cd %{name}-%{version}-ia32
git init
git config user.email "example@example.com"
git config user.name "rpmbuild -bp"
git add .
git commit -a -q -m "%{version} baseline."
git am --ignore-whitespace %{patches} </dev/null
git config --unset user.email
git config --unset user.name
%endif

%build
COMMIT_ID=$(cat %{name}-%{version}-%{efiarch}/commit)
MAKEFLAGS="RELEASE=%{release} ENABLE_HTTPBOOT=true COMMIT_ID=${COMMIT_ID}"
%ifarch aarch64
if [ -s "%{SOURCE100}" ]; then
        MAKEFLAGS="$MAKEFLAGS VENDOR_DB_FILE=%{SOURCE100}"
fi
if [ -s "%{SOURCE101}" ]; then
        MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE101}"
fi
%else
if [ -s "%{SOURCE200}" ]; then
        MAKEFLAGS="$MAKEFLAGS VENDOR_DB_FILE=%{SOURCE200}"
fi
if [ -s "%{SOURCE201}" ]; then
        MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE201}"
fi
%endif
cd %{name}-%{version}-%{efiarch}
make 'DEFAULT_LOADER=\\\\grub%{efiarch}.efi' ${MAKEFLAGS} shim%{efiarch}.efi mm%{efiarch}.efi fb%{efiarch}.efi

%ifarch x86_64
cd ../%{name}-%{version}-ia32
setarch linux32 make 'DEFAULT_LOADER=\\\\grubia32.efi' ARCH=ia32 ${MAKEFLAGS} shimia32.efi mmia32.efi fbia32.efi
cd ../%{name}-%{version}-%{efiarch}
%endif

%install
cd %{name}-%{version}-%{efiarch}
pesign -h -P -i shim%{efiarch}.efi -h > shim%{efiarch}.hash
install -D -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/
install -m 0644 shim%{efiarch}.hash $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/shim%{efiarch}.hash
for x in shim%{efiarch} mm%{efiarch} fb%{efiarch} ; do
        install -m 0644 $x.efi $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/
        install -m 0644 $x.so $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/
done

%ifarch x86_64
cd ../%{name}-%{version}-ia32
pesign -h -P -i shimia32.efi -h > shimia32.hash
install -D -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/shim/ia32-%{version}-%{release}/
install -m 0644 shimia32.hash $RPM_BUILD_ROOT%{_datadir}/shim/ia32-%{version}-%{release}/shimia32.hash
for x in shimia32 mmia32 fbia32 ; do
        install -m 0644 $x.efi $RPM_BUILD_ROOT%{_datadir}/shim/ia32-%{version}-%{release}/
        install -m 0644 $x.so $RPM_BUILD_ROOT%{_datadir}/shim/ia32-%{version}-%{release}/
done
cd ../%{name}-%{version}-%{efiarch}
%endif

%ifarch x86_64
%global __debug_install_post                                            \
        bash %{SOURCE1}                                                 \\\
                %{?_missing_build_ids_terminate_build:--strict-build-id}\\\
                %{?_find_debuginfo_opts}                                \\\
                "%{_builddir}/%{?buildsubdir}/%{name}-%{version}-%{efiarch}" \
        rm -f $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/*.so \
        mv debugfiles.list ../debugfiles-%{efiarch}.list                \
        cd ..                                                           \
        cd %{name}-%{version}-ia32                                      \
        bash %{SOURCE1}                                                 \\\
                %{?_missing_build_ids_terminate_build:--strict-build-id}\\\
                %{?_find_debuginfo_opts}                                \\\
                "%{_builddir}/%{?buildsubdir}/%{name}-%{version}-ia32"  \
        rm -f $RPM_BUILD_ROOT%{_datadir}/shim/ia32-%{version}-%{release}/*.so \
        mv debugfiles.list ../debugfiles-ia32.list                      \
        cd ..                                                           \
        %{nil}
%else
%global __debug_install_post                                            \
        bash %{SOURCE1}                                                 \\\
                %{?_missing_build_ids_terminate_build:--strict-build-id}\\\
                %{?_find_debuginfo_opts}                                \\\
                "%{_builddir}/%{?buildsubdir}/%{name}-%{version}-%{efiarch}" \
        rm -f $RPM_BUILD_ROOT%{_datadir}/shim/%{efiarch}-%{version}-%{release}/*.so \
        mv debugfiles.list ../debugfiles-%{efiarch}.list                \
        cd ..                                                           \
        %{nil}
%endif

%files -n shim-unsigned-%{efiarch}
%dir %{_datadir}/shim
%dir %{_datadir}/shim/%{efiarch}-%{version}-%{release}/
%{_datadir}/shim/%{efiarch}-%{version}-%{release}/*.efi
%{_datadir}/shim/%{efiarch}-%{version}-%{release}/*.hash

%files -n shim-unsigned-%{efiarch}-debuginfo -f debugfiles-%{efiarch}.list
%defattr(-,root,root)

%ifarch x86_64
%files -n shim-unsigned-ia32
%dir %{_datadir}/shim
%dir %{_datadir}/shim/ia32-%{version}-%{release}/
%{_datadir}/shim/ia32-%{version}-%{release}/*.efi
%{_datadir}/shim/ia32-%{version}-%{release}/*.hash

%files -n shim-unsigned-ia32-debuginfo -f debugfiles-ia32.list
%defattr(-,root,root)
%endif

%changelog
* Wed Sep 09 2020 Peter Jones <pjones@redhat.com> - 15-9.el7
- Fix an incorrect allocation size.
  Related: rhbz#1875486

* Thu Jul 30 2020 Peter Jones <pjones@redhat.com> - 15-8.el7
- Fix a load-address-dependent forever loop.
  Resolves: rhbz#1862045
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311
  Related: CVE-2020-15705
  Related: CVE-2020-15706
  Related: CVE-2020-15707

* Sat Jul 25 2020 Peter Jones <pjones@redhat.com> - 15-7
- Implement Lenny's workaround.
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311

* Thu Jul 23 2020 Peter Jones <pjones@redhat.com> - 15-6
- Rebuild for bug fixes and new signing keys
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311

* Mon Mar 18 2019 Peter Jones <pjones@redhat.com> - 15-5
- Fix a couple more things that are breaking reproducability, and thus
  breaking external review.
  Related: rhbz#1649270

* Fri Mar 15 2019 Peter Jones <pjones@redhat.com> - 15-4
- Fight with binutils to try to get a binary without timestamps in it.
  Again, but without breaking aarch64 this time.
  Related: rhbz#1649270

* Fri Mar 15 2019 Peter Jones <pjones@redhat.com> - 15-3
- Fight with binutils to try to get a binary without timestamps in it.  Again.
  Related: rhbz#1649270

* Tue Feb 12 2019 Peter Jones <pjones@redhat.com> - 15-2
- Fix MoK mirroring issue which breaks kdump without intervention
  Related: rhbz#1649270

* Mon Jun 18 2018 Peter Jones <pjones@redhat.com> - 15-1
- Update to shim 15
  Resolves: rhbz#1589961

* Thu Apr 27 2017 Peter Jones <pjones@redhat.com> - 12-1
- Update to 12-1 to work around a signtool.exe bug
  Related: rhbz#1445393

* Mon Apr 03 2017 Peter Jones <pjones@redhat.com> - 11-1
- Update to 11-1
  Related: rhbz#1310766
- Fix regression in PE loader
  Related: rhbz#1310766
- Fix case where BDS invokes us wrong and we exec shim again as a result
  Related: rhbz#1310766

* Tue Mar 21 2017 Peter Jones <pjones@redhat.com> - 10-1
- Update to 10-1
- Support ia32
  Resolves: rhbz#1310766
- Handle various different load option implementation differences
- TPM 1 and TPM 2 support.
- Update to OpenSSL 1.0.2k

* Mon Jun 22 2015 Peter Jones <pjones@redhat.com> - 0.9-1
- Update to 0.9-1
- Fix early call to BS->Exit()
  Resolves: rhbz#1115843
- Implement shim on aarch64
  Resolves: rhbz#1100048
  Resolves: rhbz#1190191

* Mon Jun 22 2015 Peter Jones <pjones@redhat.com> - 0.7-14
- Excise mokutil.
  Related: rhbz#1100048

* Mon Jun 22 2015 Peter Jones <pjones@redhat.com> - 0.7-13
- Do a build for Aarch64 to make the tree composable.
  Related: rhbz#1100048

* Wed Feb 25 2015 Peter Jones <pjones@redhat.com> - 0.7-10
- Fix a couple more minor bugs aavmf has found in fallback.
  Related: rhbz#1190191
- Build lib/ with the right CFLAGS
  Related: rhbz#1190191

* Tue Feb 24 2015 Peter Jones <pjones@redhat.com> - 0.7-9
- Fix aarch64 section loading.
  Related: rhbz#1190191

* Tue Sep 30 2014 Peter Jones <pjones@redhat.com> - 0.7-8
- Build -8 for arm as well.
  Related: rhbz#1100048
- out-of-bounds memory read flaw in DHCPv6 packet processing
  Resolves: CVE-2014-3675
- heap-based buffer overflow flaw in IPv6 address parsing
  Resolves: CVE-2014-3676
- memory corruption flaw when processing Machine Owner Keys (MOKs)
  Resolves: CVE-2014-3677

* Tue Sep 23 2014 Peter Jones <pjones@redhat.com> - 0.7-7
- Use the right key for ARM Aarch64.

* Sun Sep 21 2014 Peter Jones <pjones@redhat.com> - 0.7-6
- Preliminary build for ARM Aarch64.

* Tue Feb 18 2014 Peter Jones <pjones@redhat.com> - 0.7-5
- Update for production signing
  Resolves: rhbz#1064424
  Related: rhbz#1064449

* Thu Nov 21 2013 Peter Jones <pjones@redhat.com> - 0.7-4
- Make dhcpv4 paths work better when netbooting.
  Resolves: rhbz#1032583

* Thu Nov 14 2013 Peter Jones <pjones@redhat.com> - 0.7-3
- Make lockdown include UEFI and other KEK/DB entries.
  Resolves: rhbz#1030492

* Fri Nov 08 2013 Peter Jones <pjones@redhat.com> - 0.7-2
- Update lockdown to reflect SetupMode better as well
  Related: rhbz#996863

* Wed Nov 06 2013 Peter Jones <pjones@redhat.com> - 0.7-1
- Fix logic to handle SetupMode efi variable.
  Related: rhbz#996863

* Thu Oct 31 2013 Peter Jones <pjones@redhat.com> - 0.6-1
- Fix a FreePool(NULL) call on machines too old for SB

* Fri Oct 04 2013 Peter Jones <pjones@redhat.com> - 0.5-1
- Update to 0.5

* Tue Aug 06 2013 Peter Jones <pjones@redhat.com> - 0.4-3
- Build with early RHEL test keys.
  Related: rhbz#989442

* Thu Jul 25 2013 Peter Jones <pjones@redhat.com> - 0.4-2
- Fix minor RHEL 7.0 build issues
  Resolves: rhbz#978766
- Be less verbose by default

* Tue Jun 11 2013 Peter Jones <pjones@redhat.com> - 0.4-1
- Update to 0.4

* Fri Jun 07 2013 Peter Jones <pjones@redhat.com> - 0.3-2
- Require gnu-efi-3.0q for now.
- Don't allow mmx or sse during compilation.
- Re-organize this so all real signing happens in shim-signed instead.
- Split out mokutil

* Wed Dec 12 2012 Peter Jones <pjones@redhat.com> - 0.2-3
- Fix mokutil's idea of signature sizes.

* Wed Nov 28 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-2
- Fix secure_mode() always returning true

* Mon Nov 26 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-1
- Update shim
- Include mokutil
- Add debuginfo package since mokutil is a userspace executable

* Mon Oct 22 2012 Peter Jones <pjones@redhat.com> - 0.1-4
- Produce an unsigned shim

* Tue Aug 14 2012 Peter Jones <pjones@redhat.com> - 0.1-3
- Update how embedded cert and signing work.

* Mon Aug 13 2012 Josh Boyer <jwboyer@redhat.com> - 0.1-2
- Add patch to fix image size calculation

* Mon Aug 13 2012 Matthew Garrett <mjg@redhat.com> - 0.1-1
- initial release
