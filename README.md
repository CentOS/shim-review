-------------------------------------------------------------------------------
What organization or people are asking to have this signed:
-------------------------------------------------------------------------------
Red Hat, Inc.

-------------------------------------------------------------------------------
What product or service is this for:
-------------------------------------------------------------------------------
CentOS Linux 7.7.1908

-------------------------------------------------------------------------------
What's the justification that this really does need to be signed for the whole world to be able to boot it:
-------------------------------------------------------------------------------
CentOS Linux is deployed on a high number of nodes already using it in SecureBoot mode enabled

-------------------------------------------------------------------------------
Who is the primary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Johnny Hughes
- Position: Software Engineer
- Email address: jhughes@redhat.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: https://github.com/CentOS/shim-review/blob/7.9.2009/hughesjr.pub

-------------------------------------------------------------------------------
Who is the secondary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Carl W. George
- Position: Manager
- Email address: carlwgeorge@redhat.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: https://github.com/CentOS/shim-review/blob/7.9.2009/carlwgeorge.pub

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
- 9999-Add-vendor-esl.patch: We had to patch shim to allow it to boot previous CentOS kernels (built with a now expired key/crt) and also with a new one
- 9998-MokListRT-Fatal.patch: corresponding to https://github.com/rhboot/shim/pull/157
- Five other patches in upstream RHEL 7.7 shim, added by pjones
-------------------------------------------------------------------------------
What OS and toolchain must we use to reproduce this build?  Include where to find it, etc.  We're going to try to reproduce your build as close as possible to verify that it's really a build of the source tree you tell us it is, so these need to be fairly thorough. At the very least include the specific versions of gcc, binutils, and gnu-efi which were used, and where to find those binaries.
-------------------------------------------------------------------------------
It can be built on the centos 7.6 docker image, plus the 7.7.1908 packages available and signed in our CR repository, so on http://mirror.centos.org/centos/7/cr/x86_64/ .  
For your convenience, a Dockerfile has been supplied at
https://github.com/centos/shim-review/blob/7.7.1908/Dockerfile that can be
used to reproduce the entire build using the release tarball from github.  Use
it like this:

`sudo docker build -f Dockerfile -t centos-7.7.1908-shim-review .`

-------------------------------------------------------------------------------
Which files in this repo are the logs for your build?   This should include logs for creating the buildroots, applying patches, doing the build, creating the archives, etc.
-------------------------------------------------------------------------------
https://github.com/centos/shim-review/blob/7.7.1908/root.log
https://github.com/centos/shim-review/blob/7.7.1908/build.log

-------------------------------------------------------------------------------
Put info about what bootloader you're using, including which patches it includes to enforce Secure Boot here:
-------------------------------------------------------------------------------
It's grub2 with the well known set of secure boot patches (among other patches.)

-------------------------------------------------------------------------------
Put info about what kernel you're using, including which patches it includes to enforce Secure Boot here:
-------------------------------------------------------------------------------
It's the CentOS 7.7.1908 kernel, which has the well known set of secure boot patches.


