FROM docker.io/centos@sha256:b67d21dfe609ddacf404589e04631d90a342921e81c40aeaf3391f6717fa5322

COPY centos-7.6.1810-shim-build-deps.repo /etc/yum.repos.d/
RUN yum update -y
RUN yum install -y gcc gnu-efi gnu-efi-devel make redhat-rpm-config-9.1.0-80.el7 rpm-build yum-utils wget 
RUN mkdir -p /build/builddir/{SPECS,SOURCES}
COPY shim.spec /build/builddir/SPECS/
RUN yum-builddep -y /build/builddir/SPECS/shim.spec
COPY rpmmacros /root/.rpmmacros
COPY centos.esl /build/builddir/SOURCES/
COPY 0001-Add-vendor-esl.patch /build/builddir/SOURCES/
COPY 0002-MokListRT-Fatal.patch /build/builddir/SOURCES/
COPY shim-find-debuginfo.sh /build/builddir/SOURCES/shim-find-debuginfo.sh
WORKDIR /build
RUN wget https://github.com/rhboot/shim/releases/download/15/shim-15.tar.bz2 -O /build/builddir/SOURCES/shim-15.tar.bz2
RUN rpmbuild -ba --define 'dist .el7.centos' /build/builddir/SPECS/shim.spec --noclean
RUN sha256sum /build/builddir/BUILDROOT/shim-15-2.el7.centos.x86_64/usr/share/shim/*-15-2.el7.centos/shim*.efi

COPY shimx64.efi /
RUN hexdump -Cv /build/builddir/BUILDROOT/shim-15-2.el7.centos.x86_64/usr/share/shim/x64-15-2.el7.centos/shimx64.efi > /built.hex
RUN hexdump -Cv /shimx64.efi > /orig.hex
RUN diff -u /orig.hex /built.hex || true
RUN objdump -x /shimx64.efi | head -n 60
RUN objdump -x /build/builddir/BUILDROOT/shim-15-2.el7.centos.x86_64/usr/share/shim/x64-15-2.el7.centos/shimx64.efi | head -n 60

