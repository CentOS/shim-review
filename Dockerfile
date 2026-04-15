FROM quay.io/centos/centos:stream10

WORKDIR /root
RUN dnf -y install dnf-plugins-core rpm-build
COPY rpmmacros /root/.rpmmacros
RUN curl -kLOf https://kojihub.stream.rdu2.redhat.com/kojifiles/vol/koji02/packages/shim-unsigned-x64/16.1/1.el10.centos/src/shim-unsigned-x64-16.1-1.el10.centos.src.rpm
RUN rpm -ivh shim-unsigned-x64-16.1-1.el10.centos.src.rpm
RUN sed -i 's/linux32 -B/linux32/g' /builddir/build/SPECS/shim-unsigned-x64.spec
RUN dnf builddep -y --enablerepo=crb /builddir/build/SPECS/shim-unsigned-x64.spec
RUN rpmbuild -bb /builddir/build/SPECS/shim-unsigned-x64.spec
COPY shimx64.efi /
RUN rpm2cpio /builddir/build/RPMS/x86_64/shim-unsigned-x64-16.1-1.el10.centos.x86_64.rpm | cpio -diu
RUN ls -l /*.efi ./usr/share/shim/16.1-1.el10.centos/*/shim*.efi
RUN hexdump -Cv ./usr/share/shim/16.1-1.el10.centos/x64/shimx64.efi > built-x64.hex
RUN hexdump -Cv /shimx64.efi > orig-x64.hex
RUN objdump -h ./usr/share/shim/16.1-1.el10.centos/x64/shimx64.efi
RUN diff -u orig-x64.hex built-x64.hex
RUN pesign -h -P -i ./usr/share/shim/16.1-1.el10.centos/x64/shimx64.efi
RUN pesign -h -P -i /shimx64.efi
RUN sha256sum ./usr/share/shim/16.1-1.el10.centos/x64/shimx64.efi /shimx64.efi
