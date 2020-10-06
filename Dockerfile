FROM docker.io/centos@sha256:9b4ebb48de8dbb85a3d9fbdec4d28a3e2e14912f27b7234c10c1658a05c320a5
COPY c7.2009.00.buildlogs.x86_64.repo /etc/yum.repos.d/
RUN yum-config-manager --enable c7.2009.00.buildlogs 
RUN yum update -y 
RUN yum install -y gcc gnu-efi gnu-efi-devel make redhat-rpm-config-9.1.0-88.el7.centos rpm-build yum-utils wget 
RUN mkdir -p /build/builddir/{SPECS,SOURCES}
COPY shim.spec /build/builddir/SPECS/
RUN yum-builddep -y /build/builddir/SPECS/shim.spec
COPY rpmmacros /root/.rpmmacros
COPY centos.db.x64.esl /build/builddir/SOURCES/
COPY 0001-Make-some-things-dprint-instead-of-console_print.patch /build/builddir/SOURCES/
COPY 0002-Makefiles-ensure-m32-gets-propogated-to-our-gcc-para.patch /build/builddir/SOURCES/
COPY 0003-Let-MokManager-follow-a-MokTimeout-var-for-timeout-l.patch /build/builddir/SOURCES/
COPY 0004-httpboot-return-EFI_NOT_FOUND-when-it-fails-to-find-.patch /build/builddir/SOURCES/
COPY 0005-httpboot-print-more-messages-when-it-fails-to-set-IP.patch /build/builddir/SOURCES/
COPY 0006-httpboot-allow-the-IPv4-gateway-to-be-empty.patch /build/builddir/SOURCES/
COPY 0007-httpboot-show-the-error-message-for-the-ChildHandle.patch /build/builddir/SOURCES/
COPY 0008-Fix-typo-in-debug-path-in-shim.h.patch /build/builddir/SOURCES/
COPY 0009-MokManager-Stop-using-EFI_VARIABLE_APPEND_WRITE.patch /build/builddir/SOURCES/
COPY 0010-shim-Extend-invalid-reloc-size-warning-message.patch /build/builddir/SOURCES/
COPY 0011-Add-GRUB-s-PCR-Usage-to-README.tpm.patch /build/builddir/SOURCES/
COPY 0012-Fix-the-compile-error-of-mkdir-wrong-directory.patch /build/builddir/SOURCES/
COPY 0013-shim-Properly-generate-absolute-paths-from-relative-.patch /build/builddir/SOURCES/
COPY 0014-shim-Prevent-shim-to-set-itself-as-a-second-stage-lo.patch /build/builddir/SOURCES/
COPY 0015-Fix-for-Section-0-has-negative-size-error-when-loadi.patch /build/builddir/SOURCES/
COPY 0016-Fix-apparent-typo-in-ARM-32-on-64-code.patch /build/builddir/SOURCES/
COPY 0017-Makefile-do-not-run-git-on-clean-if-there-s-no-.git-.patch /build/builddir/SOURCES/
COPY 0018-Make.default-use-correct-flags-to-disable-unaligned-.patch /build/builddir/SOURCES/
COPY 0019-Cryptlib-fix-build-on-32bit-ARM.patch /build/builddir/SOURCES/
COPY 0020-Make-sure-that-MOK-variables-always-get-mirrored.patch /build/builddir/SOURCES/
COPY 0021-mok-fix-the-mirroring-of-RT-variables.patch /build/builddir/SOURCES/
COPY 0022-mok-consolidate-mirroring-code-in-a-helper-instead-o.patch /build/builddir/SOURCES/
COPY 0023-shim-only-include-shim_cert.h-in-shim.c.patch /build/builddir/SOURCES/
COPY 0024-mok-also-mirror-the-build-cert-to-MokListRT.patch /build/builddir/SOURCES/
COPY 0025-mok-minor-cleanups.patch /build/builddir/SOURCES/
COPY 0026-Remove-call-to-TPM2-get_event_log.patch /build/builddir/SOURCES/
COPY 0027-Make-EFI-variable-copying-fatal-only-on-secureboot-e.patch /build/builddir/SOURCES/
COPY 0028-VLogError-Avoid-NULL-pointer-dereferences-in-V-Sprin.patch /build/builddir/SOURCES/
COPY 0029-Once-again-try-even-harder-to-get-binaries-without-t.patch /build/builddir/SOURCES/
COPY 0030-shim-Rework-pause-functions-and-add-read_counter.patch /build/builddir/SOURCES/
COPY 0031-Hook-exit-when-shim_lock-protocol-installed.patch /build/builddir/SOURCES/
COPY 0032-Work-around-stuff-Waddress-of-packed-member-finds.patch /build/builddir/SOURCES/
COPY 0033-Fix-a-use-of-strlen-instead-of-Strlen.patch /build/builddir/SOURCES/
COPY 0034-MokManager-Use-CompareMem-on-MokListNode.Type-instea.patch /build/builddir/SOURCES/
COPY 0035-OpenSSL-always-provide-OBJ_create-with-name-strings.patch /build/builddir/SOURCES/
COPY 0036-Use-portable-shebangs-bin-bash-usr-bin-env-bash.patch /build/builddir/SOURCES/
COPY 0037-tpm-Fix-off-by-one-error-when-calculating-event-size.patch /build/builddir/SOURCES/
COPY 0038-tpm-Define-EFI_VARIABLE_DATA_TREE-as-packed.patch /build/builddir/SOURCES/
COPY 0039-MokManager-console-mode-modification-for-hi-dpi-scre.patch /build/builddir/SOURCES/
COPY 0040-MokManager-avoid-Werror-address-of-packed-member.patch /build/builddir/SOURCES/
COPY 0041-tpm-Don-t-log-duplicate-identical-events.patch /build/builddir/SOURCES/
COPY 0042-Slightly-better-debugging-messages.patch /build/builddir/SOURCES/
COPY 0043-Actually-check-for-errors-from-set_second_stage.patch /build/builddir/SOURCES/
COPY 0044-translate_slashes-don-t-write-to-string-literals.patch /build/builddir/SOURCES/
COPY 0045-shim-Update-EFI_LOADED_IMAGE-with-the-second-stage-l.patch /build/builddir/SOURCES/
COPY 0046-tpm-Include-information-about-PE-COFF-images-in-the-.patch /build/builddir/SOURCES/
COPY 0047-Fix-the-license-on-our-buildid-extractor.patch /build/builddir/SOURCES/
COPY 0048-Update-README.tpm.patch /build/builddir/SOURCES/
COPY 0049-Check-PxeReplyReceived-as-fallback-in-netboot.patch /build/builddir/SOURCES/
COPY 0050-Remove-a-couple-of-incorrect-license-claims.patch /build/builddir/SOURCES/
COPY 0051-MokManager-fix-uninitialized-value.patch /build/builddir/SOURCES/
COPY 0052-Fix-some-volatile-usage-gcc-whines-about.patch /build/builddir/SOURCES/
COPY 0053-MokManager-fix-a-wrong-allocation-failure-check.patch /build/builddir/SOURCES/
COPY 0054-simple_file-fix-uninitialized-variable-unchecked-ret.patch /build/builddir/SOURCES/
COPY 0055-Fix-a-broken-tpm-type.patch /build/builddir/SOURCES/
COPY 0056-Make-cert.S-not-impossible-to-read.patch /build/builddir/SOURCES/
COPY 0057-Add-support-for-vendor_db-built-in-shim-authorized-l.patch /build/builddir/SOURCES/
COPY 0058-Handle-binaries-with-multiple-signatures.patch /build/builddir/SOURCES/
COPY 0059-Make-openssl-accept-the-right-set-of-KU-EKUs.patch /build/builddir/SOURCES/
COPY 0060-Improve-debug-output-some.patch /build/builddir/SOURCES/
COPY 0061-Also-use-a-config-table-to-mirror-mok-variables.patch /build/builddir/SOURCES/
COPY 0062-Implement-lennysz-s-suggestions-for-MokListRT.patch /build/builddir/SOURCES/
COPY 0063-hexdump.h-fix-arithmetic-error.patch /build/builddir/SOURCES/
COPY 0064-Fix-some-mokmanager-stuff.patch /build/builddir/SOURCES/
COPY 0065-Fix-buffer-overrun-due-DEFAULT_LOADER-length-miscalc.patch /build/builddir/SOURCES/
COPY shim-find-debuginfo.sh /build/builddir/SOURCES/shim-find-debuginfo.sh
WORKDIR /build
RUN wget https://github.com/rhboot/shim/releases/download/15/shim-15.tar.bz2 -O /build/builddir/SOURCES/shim-15.tar.bz2
RUN rpmbuild -ba --define 'dist .el7' /build/builddir/SPECS/shim.spec --noclean
RUN sha256sum /build/builddir/BUILDROOT/shim-15-9.el7.x86_64/usr/share/shim/*-15-9.el7/shim*.efi

COPY shimx64.efi /
RUN hexdump -Cv /build/builddir/BUILDROOT/shim-15-9.el7.x86_64/usr/share/shim/x64-15-9.el7/shimx64.efi > /built.hex
RUN hexdump -Cv /shimx64.efi > /orig.hex
RUN diff -u /orig.hex /built.hex || true
RUN objdump -x /shimx64.efi | head -n 60
RUN objdump -x /build/builddir/BUILDROOT/shim-15-9.el7.x86_64/usr/share/shim/x64-15-9.el7/shimx64.efi | head -n 60

