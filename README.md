-------------------------------------------------------------------------------
What organization or people are asking to have this signed:
-------------------------------------------------------------------------------
Red Hat, Inc.

-------------------------------------------------------------------------------
What product or service is this for:
-------------------------------------------------------------------------------
CentOS Linux 8.0.1905

-------------------------------------------------------------------------------
What's the justification that this really does need to be signed for the whole world to be able to boot it:
-------------------------------------------------------------------------------
CentOS Linux is deployed on a high number of nodes already using it in SecureBoot mode enabled

-------------------------------------------------------------------------------
Who is the primary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Fabian Arrotin
- Position: System Administrator
- Email address: arrfab@redhat.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: https://github.com/centos/shim-review/blob/8.0.1905/arrfab.pub

-------------------------------------------------------------------------------
Who is the secondary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Jim Perrin
- Position: Manager
- Email address: jperrin@redhat.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: https://github.com/centos/shim-review/blob/8.0.1905/jperrin.pub

-------------------------------------------------------------------------------
What upstream shim tag is this starting from:
-------------------------------------------------------------------------------
https://github.com/rhboot/shim/tree/15

-------------------------------------------------------------------------------
URL for a repo that contains the exact code which was built to get this binary:
-------------------------------------------------------------------------------
https://github.com/rhboot/shim/tree/15

-------------------------------------------------------------------------------
What patches are being applied and why:
-------------------------------------------------------------------------------
There are five patches from the shim-16 development branch included.

-------------------------------------------------------------------------------
What OS and toolchain must we use to reproduce this build?  Include where to find it, etc.  We're going to try to reproduce your build as close as possible to verify that it's really a build of the source tree you tell us it is, so these need to be fairly thorough. At the very least include the specific versions of gcc, binutils, and gnu-efi which were used, and where to find those binaries.
-------------------------------------------------------------------------------
It's done on something very close to the RHEL 8 public beta.  It can be built
from the docker image at http://pjones.fedorapeople.org/rhel-8-beta.tar.bz2
plus the yum repo at https://koji.mbox.centos.org/kojifiles/repos/dist-c8-build/latest/x86_64/ .

For your convenience, a Dockerfile has been supplied at
https://github.com/centos/shim-review/blob/8.0.1905/Dockerfile that can be
used to reproduce the entire build using the release tarball from github.  Use
it like this:
`
$ sudo su -
# docker import https://pjones.fedorapeople.org/rhel-8-beta.img rhel-8-beta:latest
# docker build - Dockerfile -t centos-8.0.1905-shim-review .
`

-------------------------------------------------------------------------------
Which files in this repo are the logs for your build?   This should include logs for creating the buildroots, applying patches, doing the build, creating the archives, etc.
-------------------------------------------------------------------------------
https://github.com/centos/shim-review/blob/8.0.1905/root.log
https://github.com/centos/shim-review/blob/8.0.1905/build.log

-------------------------------------------------------------------------------
Add any additional information you think we may need to validate this shim
-------------------------------------------------------------------------------
