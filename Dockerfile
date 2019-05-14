FROM rhel-8-beta:latest

RUN /bin/rm /etc/yum.repos.d/*.repo
COPY centos-8.0.1905-shim-build-deps.repo /etc/yum.repos.d/
#RUN yum update -y --skip-broken
RUN yum install -y binutils gcc gnu-efi gnu-efi-devel make redhat-rpm-config rpm-build yum-utils wget
COPY shim-unsigned-x64.spec /builddir/build/SPECS/
COPY shimx64.efi /
RUN yum-builddep -y /builddir/build/SPECS/shim-unsigned-x64.spec
COPY rpmmacros /root/.rpmmacros
COPY centossecureboot001.der /builddir/build/SOURCES/
COPY shim-find-debuginfo.sh /builddir/build/SOURCES/shim-find-debuginfo.sh
COPY dbx.esl *.patch /builddir/build/SOURCES/
WORKDIR /build
RUN wget https://github.com/rhboot/shim/releases/download/15/shim-15.tar.bz2 -O /builddir/build/SOURCES/shim-15.tar.bz2
RUN rpmbuild -ba /builddir/build/SPECS/shim-unsigned-x64.spec --noclean --define 'dist .el8'
RUN find /builddir/build/ -name 'shim*.efi'
RUN sha256sum /builddir/build/BUILDROOT/shim*/usr/share/shim/*/*/shim*.efi
RUN sha256sum /shimx64.efi
#RUN hexdump -Cv /build/builddir/BUILDROOT/shim*/usr/share/shim/*/*/shim*.efi > /built.hex
RUN hexdump -Cv /builddir/build/BUILDROOT/shim*/usr/share/shim/*/*/shimx64.efi > /built.hex
RUN hexdump -Cv /shimx64.efi > /orig.hex
RUN diff -u /orig.hex /built.hex || true
#RUN objdump -x /shimx64.efi | head -n 60
#RUN objdump -x /build/builddir/BUILDROOT/shim*/usr/share/shim/*/*/shim*.efi | head -n 60

