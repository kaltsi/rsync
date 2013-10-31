Name:       rsync
Summary:    A program for synchronizing files over a network
Version: 3.1.0
Release: 1
Group:      Applications/Internet
License:    GPLv3+
URL:        http://rsync.samba.org/
Source0:    http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
Patch1:	0001-mer-tools-Add-pre-generated-man-pages-and-mer-xinetd.patch
BuildRequires:  pkgconfig(popt)
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.


%package support
Summary:    Support files for rsync
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description support
Support files for rsync

%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q -n %%{name}-%%{version}
%setup -q -n src
%patch1 -p1

%build

%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

# rename the pre-generated man pages
cp rsync.man rsync.1
cp rsyncd.conf.man rsyncd.conf.5

%make_install
mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync

%files
%defattr(-,root,root,-)
%doc COPYING README
%config(noreplace) /etc/xinetd.d/rsync
%{_prefix}/bin/rsync
%doc %{_mandir}/man1/rsync.1*
%doc %{_mandir}/man5/rsyncd.conf.5*

%files support
%defattr(-,root,root,-)
