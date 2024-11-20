This repo is for review of requests for signing shim.  To create a request for review:

- clone this repo
- edit the template below
- add the shim.efi to be signed
- add build logs
- add any additional binaries/certificates/SHA256 hashes that may be needed
- commit all of that
- tag it with a tag of the form "myorg-shim-arch-YYYYMMDD"
- push that to github
- file an issue at https://github.com/rhboot/shim-review/issues with a link to your tag
- approval is ready when the "accepted" label is added to your issue
Note that we really only have experience with using GRUB2 or systemd-boot on Linux, so
asking us to endorse anything else for signing is going to require some convincing on
your part.

Check the docs directory in this repo for guidance on submission and
getting your shim signed.

Here's the template:

*******************************************************************************
### What organization or people are asking to have this signed?
*******************************************************************************
The CentOS Project


*******************************************************************************
### What's the legal data that proves the organization's genuineness?
The reviewers should be able to easily verify, that your organization is a legal entity, to prevent abuse.
Provide the information, which can prove the genuineness with certainty.
*******************************************************************************

```
Issuer: C=US, O=DigiCert, Inc., CN=DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1
Subject: jurisdictionC=US, jurisdictionST=Delaware, businessCategory=Private Organization, serialNumber=2945436, C=US, ST=North Carolina, L=Raleigh, O=Red Hat, Inc., CN=Red Hat, Inc.
```

*******************************************************************************
### What product or service is this for?
*******************************************************************************
CentOS Stream 10

*******************************************************************************
### What's the justification that this really does need to be signed for the whole world to be able to boot it?
*******************************************************************************
CentOS Stream is a Linux distribution with many users and developers. 

*******************************************************************************
### Why are you unable to reuse shim from another distro that is already signed?
*******************************************************************************
We have our own separate certificates to distinguish from RHEL or Fedora

*******************************************************************************
### Who is the primary contact for security updates, etc.?
- Name: Brian Stinson
- Position: Developer
- Email address: bstinson@redhat.com
- PGP key fingerprint: 7672AABAC1A2874C746BBC728306BCD2B30B078C
  
*******************************************************************************
### Who is the secondary contact for security updates, etc.?
*******************************************************************************
- Name: Fabian Arrotin
- Position: Systems Administrator
- Email address: arrfab@redhat.com
- PGP key fingerprint: 7A38A620E0B50E9FF919407B9D5907A356BEC54E
    
*******************************************************************************
### Were these binaries created from the 15.8 shim release tar?
Please create your shim binaries starting with the 15.8 shim release tar file: https://github.com/rhboot/shim/releases/download/15.8/shim-15.8.tar.bz2
This matches https://github.com/rhboot/shim/releases/tag/15.8 and contains the appropriate gnu-efi source.
*******************************************************************************

SHA512 (shim-15.8.tar.bz2) = 30b3390ae935121ea6fe728d8f59d37ded7b918ad81bea06e213464298b4bdabbca881b30817965bd397facc596db1ad0b8462a84c87896ce6c1204b19371cd1

*******************************************************************************
### URL for a repo that contains the exact code which was built to get this binary:
*******************************************************************************
https://github.com/rhboot/shim/tree/15

*******************************************************************************
### What patches are being applied and why:
*******************************************************************************

None

*******************************************************************************
### Do you have the NX bit set in your shim? If so, is your entire boot stack NX-compatible and what testing have you done to ensure such compatibility?
See https://techcommunity.microsoft.com/t5/hardware-dev-center/nx-exception-for-shim-community/ba-p/3976522 for more details on the signing of shim without NX bit.
*******************************************************************************

No

*******************************************************************************
### If shim is loading GRUB2 bootloader what exact implementation of Secureboot in GRUB2 do you have? (Either Upstream GRUB2 shim_lock verifier or Downstream RHEL/Fedora/Debian/Canonical-like implementation)
*******************************************************************************

RHEL Like

*******************************************************************************
### If shim is loading GRUB2 bootloader and your previously released shim booted a version of GRUB2 affected by any of the CVEs in the July 2020, the March 2021, the June 7th 2022, the November 15th 2022, or 3rd of October 2023 GRUB2 CVE list, have fixes for all these CVEs been applied?

* 2020 July - BootHole
*   * Details: https://lists.gnu.org/archive/html/grub-devel/2020-07/msg00034.html
*   * CVE-2020-10713
*   * CVE-2020-14308
*   * CVE-2020-14309
*   * CVE-2020-14310
*   * CVE-2020-14311
*   * CVE-2020-15705
*   * CVE-2020-15706
*   * CVE-2020-15707
* * March 2021
*   * Details: https://lists.gnu.org/archive/html/grub-devel/2021-03/msg00007.html
*   * CVE-2020-14372
*   * CVE-2020-25632
*   * CVE-2020-25647
*   * CVE-2020-27749
*   * CVE-2020-27779
*   * CVE-2021-3418 (if you are shipping the shim_lock module)
*   * CVE-2021-20225
*   * CVE-2021-20233
* * June 2022
*   * Details: https://lists.gnu.org/archive/html/grub-devel/2022-06/msg00035.html, SBAT increase to 2
*   * CVE-2021-3695
*   * CVE-2021-3696
*   * CVE-2021-3697
*   * CVE-2022-28733
*   * CVE-2022-28734
*   * CVE-2022-28735
*   * CVE-2022-28736
*   * CVE-2022-28737
* * November 2022
*   * Details: https://lists.gnu.org/archive/html/grub-devel/2022-11/msg00059.html, SBAT increase to 3
*   * CVE-2022-2601
*   * CVE-2022-3775
* * October 2023 - NTFS vulnerabilities
*   * Details: https://lists.gnu.org/archive/html/grub-devel/2023-10/msg00028.html, SBAT increase to 4
*   * CVE-2023-4693
*   * CVE-2023-4692
*******************************************************************************
Same source code as RHEL

*******************************************************************************
### If shim is loading GRUB2 bootloader, and if these fixes have been applied, is the upstream global SBAT generation in your GRUB2 binary set to 4?
The entry should look similar to: `grub,4,Free Software Foundation,grub,GRUB_UPSTREAM_VERSION,https://www.gnu.org/software/grub/`
*******************************************************************************
Same source code as RHEL

*******************************************************************************
### Were old shims hashes provided to Microsoft for verification and to be added to future DBX updates?
### Does your new chain of trust disallow booting old GRUB2 builds affected by the CVEs?
*******************************************************************************
Yes

*******************************************************************************
### If your boot chain of trust includes a Linux kernel:
### Is upstream commit [1957a85b0032a81e6482ca4aab883643b8dae06e "efi: Restrict efivar_ssdt_load when the kernel is locked down"](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=1957a85b0032a8ommit/?id=75b0cea7bf307f362057cc778efe89af4c615354) applied?
### Is upstream commit [eadb2f47a3ced5c64b23b90fd2a3463f63726066 "lockdown: also lock down previous kgdb use"](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=eadb2f47a3ced5c64b23b90fd2a3463f63726066) applied?
**************************************************************************************************************************************************
Yes, we share sources with the RHEL kernel

*******************************************************************************
### If you use vendor_db functionality of providing multiple certificates and/or hashes please briefly describe your certificate setup.
### If there are allow-listed hashes please provide exact binaries for which hashes are created via file sharing service, available in public with anonymous access for verification.
*******************************************************************************
We don't use this yet

*******************************************************************************
### What changes were made in the distro's secure boot chain since your SHIM was last signed?
For example, signing new kernel's variants, UKI, systemd-boot, new certs, new CA, etc..
*******************************************************************************
We have a kernel-uki variant to sign now 

*******************************************************************************
### What is the SHA256 hash of your final SHIM binary?
*******************************************************************************
$ sha256sum shimx64.efi
1f79899df33ba605e65a2eb431cf23f48a2c3832cf2220f74eb295b469c4ba3d  shimx64.efi

$ pesign -h -P -i shimx64.efi
shimx64.efi 3a2720b158e6fad9a1cdcdef3f21da22df02d59dae84fd51ad882ca036bfd5ad

*******************************************************************************
### How do you manage and protect the keys used in your SHIM?
*******************************************************************************
We store our keys in an HSM

*******************************************************************************
### Do you use EV certificates as embedded certificates in the SHIM?
*******************************************************************************
No

*******************************************************************************
### Do you add a vendor-specific SBAT entry to the SBAT section in each binary that supports SBAT metadata ( GRUB2, fwupd, fwupdate, systemd-boot, systemd-stub, shim + all child shim binaries )?
### Please provide exact SBAT entries for all SBAT binaries you are booting or planning to boot directly through shim.
###
*******************************************************************************
sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
shim,4,UEFI shim,shim,1,https://github.com/rhboot/shim
shim.centos,3,The CentOS Project,shim,15.8,security@centos.org

sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
grub,3,Free Software Foundation,grub,2.12,https//www.gnu.org/software/grub/
grub.rh,2,Red Hat,grub2,2.12-1.el10,mailto:secalert@redhat.com

sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
linux,1,Red Hat,linux,6.12.0-30.el10.x86_64,mailto:secalert@redhat.com
linux.centos,1,Red Hat,linux,6.12.0-30.el10.x86_64,mailto:secalert@redhat.com
kernel-uki-virt.centos,1,Red Hat,kernel-uki-virt,6.12.0-30.el10.x86_64,mailto:secalert@redhat.com
systemd-stub,1,The systemd Developers,systemd,256,https://systemd.io/
systemd-stub.centos,1,CentOS Stream,systemd,256-17.el10,mailto:secalert@redhat.com

NOTE: we haven't signed fwupd yet, but here is the expected sbat
sbat,1,UEFI shim,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
fwupd-efi,1,Firmware update daemon,fwupd-efi,1.9,https://github.com/fwupd/fwupd-efi
fwupd-efi.rhel,1,Red Hat Enterprise Linux,fwupd,1.9.26,mail:secalert@redhat.com

*******************************************************************************
### If shim is loading GRUB2 bootloader, which modules are built into your signed GRUB2 image?
*******************************************************************************
all_video boot blscfg cat configfile cryptodisk
echo ext2 f2fs fat font
gcry_rijndael gcry_rsa gcry_serpent
gcry_sha256 gcry_twofish gcry_whirlpool
gfxmenu gfxterm gzio
halt hfsplus http increment iso9660
jpeg loadenv loopback linux lvm luks
luks2 memdisk mdraid09 mdraid1x minicmd net
normal part_apple part_msdos part_gpt
password_pbkdf2 pgp png reboot regexp search 
search_fs_uuid search_fs_file search_label serial 
sleep squash4 syslinuxcfg test tftp version video xfs zstd

*******************************************************************************
### If you are using systemd-boot on arm64 or riscv, is the fix for [unverified Devicetree Blob loading](https://github.com/systemd/systemd/security/advisories/GHSA-6m6p-rjcq-334c) included?
*******************************************************************************
We don't sign shim for arm and don't have a risc port

*******************************************************************************
### What is the origin and full version number of your bootloader (GRUB2 or systemd-boot or other)?
*******************************************************************************
grub2-2.12.1.el10

*******************************************************************************
### If your SHIM launches any other components, please provide further details on what is launched.
*******************************************************************************
Everything captured in the sbat section above: grub2, kernel, kernel-uki, and fwupd

*******************************************************************************
### If your GRUB2 or systemd-boot launches any other binaries that are not the Linux kernel in SecureBoot mode, please provide further details on what is launched and how it enforces Secureboot lockdown.
*******************************************************************************
grub2 checks kernel signatures. I don't think fwupd does anything else other than updates

*******************************************************************************
### How do the launched components prevent execution of unauthenticated code?
*******************************************************************************
Built in checks

*******************************************************************************
### Does your SHIM load any loaders that support loading unsigned kernels (e.g. GRUB2)?
*******************************************************************************
No

*******************************************************************************
### What kernel are you using? Which patches does it includes to enforce Secure Boot?
*******************************************************************************
kernel-6.12.0-30.el10

*******************************************************************************
### Add any additional information you think we may need to validate this shim.
*******************************************************************************
Input specfiles and macros are here: https://gitlab.com/redhat/centos-stream/rpms/shim-unsigned-x64/-/tree/c10s-centos
Public Build is here: https://kojihub.stream.centos.org/koji/buildinfo?buildID=71794
