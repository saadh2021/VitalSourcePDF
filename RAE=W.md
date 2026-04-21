



ammarhanif@Ammars-MacBook-Air ~ % arch -arm64 brew install make automake autoconf libtool pkg-config gcc libimobiledevice usbmuxd

✔︎ JSON API cask.jws.json                         Downloaded   15.5MB/ 15.5MB
✔︎ JSON API formula.jws.json                      Downloaded   32.0MB/ 32.0MB
autoconf 2.72 is already installed but outdated (so it will be upgraded).
pkgconf 0.29.2_3 is already installed but outdated (so it will be upgraded).
Warning: libimobiledevice 1.4.0 is already installed and up-to-date.
To reinstall 1.4.0, run:
  brew reinstall libimobiledevice
Warning: libusbmuxd 2.1.1 is already installed and up-to-date.
To reinstall 2.1.1, run:
  brew reinstall libusbmuxd
==> Fetching downloads for: make, automake, autoconf, libtool, pkgconf and gcc
✔︎ Bottle Manifest make (4.4.1)                   Downloaded   13.1KB/ 13.1KB
✔︎ Bottle Manifest automake (1.18.1)              Downloaded   18.2KB/ 18.2KB
✔︎ Bottle Manifest autoconf (2.73)                Downloaded   14.9KB/ 14.9KB
✔︎ Bottle Manifest libtool (2.5.4)                Downloaded   13.8KB/ 13.8KB
✔︎ Bottle Manifest pkgconf (2.5.1)                Downloaded   12.2KB/ 12.2KB
✔︎ Bottle Manifest gcc (15.2.0_1)                 Downloaded   23.5KB/ 23.5KB
✔︎ Bottle Manifest m4 (1.4.21)                    Downloaded    9.5KB/  9.5KB
✔︎ Bottle Manifest gmp (6.3.0)                    Downloaded   13.3KB/ 13.3KB
✔︎ Bottle Manifest mpfr (4.2.2)                   Downloaded   12.7KB/ 12.7KB
✔︎ Bottle Manifest isl (0.27)                     Downloaded   14.5KB/ 14.5KB
✔︎ Bottle Manifest libmpc (1.4.1)                 Downloaded   12.0KB/ 12.0KB
✔︎ Bottle Manifest lz4 (1.10.0)                   Downloaded   13.8KB/ 13.8KB
✔︎ Bottle autoconf (2.73)                         Downloaded    1.1MB/  1.1MB
✔︎ Bottle Manifest xz (5.8.3)                     Downloaded   11.8KB/ 11.8KB
✔︎ Bottle pkgconf (2.5.1)                         Downloaded  121.9KB/121.9KB
✔︎ Bottle Manifest zstd (1.5.7_1)                 Downloaded   13.2KB/ 13.2KB
✔︎ Bottle make (4.4.1)                            Downloaded  429.9KB/429.9KB
✔︎ Bottle m4 (1.4.21)                             Downloaded  284.0KB/284.0KB
✔︎ Bottle libmpc (1.4.1)                          Downloaded  156.9KB/156.9KB
✔︎ Bottle automake (1.18.1)                       Downloaded    1.1MB/  1.1MB
✔︎ Bottle gmp (6.3.0)                             Downloaded    1.0MB/  1.0MB
✔︎ Bottle lz4 (1.10.0)                            Downloaded  276.1KB/276.1KB
✔︎ Bottle xz (5.8.3)                              Downloaded  771.2KB/771.2KB
✔︎ Bottle libtool (2.5.4)                         Downloaded    1.1MB/  1.1MB
✔︎ Bottle isl (0.27)                              Downloaded    1.7MB/  1.7MB
✔︎ Bottle zstd (1.5.7_1)                          Downloaded  794.7KB/794.7KB
✔︎ Bottle mpfr (4.2.2)                            Downloaded    1.1MB/  1.1MB
✔︎ Bottle gcc (15.2.0_1)                          Downloaded  154.1MB/154.1MB
==> Pouring make--4.4.1.arm64_sequoia.bottle.1.tar.gz
==> Caveats
GNU "make" has been installed as "gmake".
If you need to use it as "make", you can add a "gnubin" directory
to your PATH from your bashrc like:

    PATH="/opt/homebrew/opt/make/libexec/gnubin:$PATH"
==> Summary
🍺  /opt/homebrew/Cellar/make/4.4.1: 17 files, 1.3MB
==> Running `brew cleanup make`...
Disable this behaviour by setting `HOMEBREW_NO_INSTALL_CLEANUP=1`.
Hide these hints with `HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
==> Installing automake dependency: m4
==> Pouring m4--1.4.21.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/m4/1.4.21: 14 files, 817.6KB
==> Pouring automake--1.18.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/automake/1.18.1: 134 files, 3.6MB
==> Running `brew cleanup automake`...
==> Upgrading autoconf
  2.72 -> 2.73 
==> Pouring autoconf--2.73.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/autoconf/2.73: 73 files, 3.8MB
==> Running `brew cleanup autoconf`...
Removing: /opt/homebrew/Cellar/autoconf/2.72... (71 files, 3.8MB)
==> Pouring libtool--2.5.4.arm64_sequoia.bottle.tar.gz
==> Caveats
All commands have been installed with the prefix "g".
If you need to use these commands with their normal names, you
can add a "gnubin" directory to your PATH from your bashrc like:
  PATH="/opt/homebrew/opt/libtool/libexec/gnubin:$PATH"
==> Summary
🍺  /opt/homebrew/Cellar/libtool/2.5.4: 76 files, 4.1MB
==> Running `brew cleanup libtool`...
==> Upgrading pkg-config
  -> 2.5.1 
==> Pouring pkgconf--2.5.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pkgconf/2.5.1: 28 files, 533.5KB
==> Running `brew cleanup pkgconf`...
Removing: /opt/homebrew/Cellar/pkg-config/0.29.2_3... (11 files, 692.9KB)
==> Installing dependencies for gcc: gmp, isl, mpfr, libmpc, lz4, xz and zstd
==> Installing gcc dependency: gmp
==> Pouring gmp--6.3.0.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gmp/6.3.0: 22 files, 3.4MB
==> Installing gcc dependency: isl
==> Pouring isl--0.27.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/isl/0.27: 74 files, 8.0MB
==> Installing gcc dependency: mpfr
==> Pouring mpfr--4.2.2.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpfr/4.2.2: 31 files, 3.3MB
==> Installing gcc dependency: libmpc
==> Pouring libmpc--1.4.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libmpc/1.4.1: 14 files, 545.7KB
==> Installing gcc dependency: lz4
==> Pouring lz4--1.10.0.arm64_sequoia.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/lz4/1.10.0: 24 files, 730.7KB
==> Installing gcc dependency: xz
==> Pouring xz--5.8.3.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xz/5.8.3: 96 files, 2.7MB
==> Installing gcc dependency: zstd
==> Pouring zstd--1.5.7_1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/zstd/1.5.7_1: 32 files, 2.3MB
==> Installing gcc
==> Pouring gcc--15.2.0_1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gcc/15.2.0_1: 1,602 files, 462.7MB
==> Running `brew cleanup gcc`...
==> Upgrading 2 dependents of upgraded formulae:
Disable this behaviour by setting `HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK=1`.
Hide these hints with `HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
rbenv 1.2.0 -> 1.3.2, ruby-build 20240501 -> 20260412
==> Fetching downloads for: ruby-build and rbenv
✔︎ Bottle Manifest readline (8.3.3)               Downloaded   10.0KB/ 10.0KB
✔︎ Bottle rbenv (1.3.2)                           Downloaded   20.8KB/ 20.8KB
✔︎ Bottle readline (8.3.3)                        Downloaded  758.1KB/758.1KB
✔︎ Bottle ruby-build (20260412)                   Downloaded   78.2KB/ 78.2KB
==> Upgrading ruby-build
  20240501 -> 20260412 
==> Installing ruby-build dependency: readline
==> Pouring readline--8.3.3.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/readline/8.3.3: 56 files, 2.7MB
==> Pouring ruby-build--20260412.all.bottle.tar.gz
🍺  /opt/homebrew/Cellar/ruby-build/20260412: 687 files, 393.3KB
==> Running `brew cleanup ruby-build`...
Removing: /opt/homebrew/Cellar/ruby-build/20240501... (611 files, 331.8KB)
==> Upgrading rbenv
  1.2.0 -> 1.3.2 
==> Pouring rbenv--1.3.2.all.bottle.tar.gz
🍺  /opt/homebrew/Cellar/rbenv/1.3.2: 36 files, 76.6KB
==> Running `brew cleanup rbenv`...
Removing: /opt/homebrew/Cellar/rbenv/1.2.0... (35 files, 129.4KB)
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
==> make
GNU "make" has been installed as "gmake".
If you need to use it as "make", you can add a "gnubin" directory
to your PATH from your bashrc like:

    PATH="/opt/homebrew/opt/make/libexec/gnubin:$PATH"
==> libtool
All commands have been installed with the prefix "g".
If you need to use these commands with their normal names, you
can add a "gnubin" directory to your PATH from your bashrc like:
  PATH="/opt/homebrew/opt/libtool/libexec/gnubin:$PATH"
ammarhanif@Ammars-MacBook-Air ~ % git clone https://github.com/corellium/usbfluxd.git

Cloning into 'usbfluxd'...
remote: Enumerating objects: 773, done.
remote: Counting objects: 100% (171/171), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 773 (delta 157), reused 159 (delta 156), pack-reused 602 (from 1)
Receiving objects: 100% (773/773), 1.99 MiB | 4.99 MiB/s, done.
Resolving deltas: 100% (487/487), done.
ammarhanif@Ammars-MacBook-Air ~ % cd usbfluxd

ammarhanif@Ammars-MacBook-Air usbfluxd % ./autogen.sh

make

glibtoolize: putting auxiliary files in '.'.
glibtoolize: linking file './ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
glibtoolize: linking file 'm4/libtool.m4'
glibtoolize: linking file 'm4/ltoptions.m4'
glibtoolize: linking file 'm4/ltsugar.m4'
glibtoolize: linking file 'm4/ltversion.m4'
glibtoolize: linking file 'm4/lt~obsolete.m4'
configure.ac:13: installing './compile'
configure.ac:16: installing './config.guess'
configure.ac:16: installing './config.sub'
configure.ac:6: installing './install-sh'
configure.ac:6: installing './missing'
tools/Makefile.am: installing './depcomp'
configure.ac:16: warning: The macro 'AC_PROG_LIBTOOL' is obsolete.
configure.ac:16: You should run autoupdate.
m4/libtool.m4:100: AC_PROG_LIBTOOL is expanded from...
configure.ac:16: the top level
configure.ac:45: warning: The macro 'AC_HEADER_STDC' is obsolete.
configure.ac:45: You should run autoupdate.
./lib/autoconf/headers.m4:664: AC_HEADER_STDC is expanded from...
configure.ac:45: the top level
configure.ac:108: warning: The macro 'AC_TRY_COMPILE' is obsolete.
configure.ac:108: You should run autoupdate.
./lib/autoconf/general.m4:2903: AC_TRY_COMPILE is expanded from...
m4/as-compiler-flag.m4:37: AS_COMPILER_FLAGS is expanded from...
configure.ac:108: the top level
configure.ac:113: warning: AC_OUTPUT should be used without arguments.
configure.ac:113: You should run autoupdate.
checking for a BSD-compatible install... /usr/bin/install -c
checking whether sleep supports fractional seconds... yes
checking filesystem timestamp resolution... 2
checking whether build environment is sane... yes
checking for a race-free mkdir -p... mkdir -p
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking xargs -n works... yes
checking whether UID '501' is supported by ustar format... yes
checking whether GID '20' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C23 features... -std=gnu23
checking whether gcc -std=gnu23 understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of gcc -std=gnu23... gcc3
checking for g++... g++
checking whether the compiler supports GNU C++... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking build system type... x86_64-apple-darwin24.6.0
checking host system type... x86_64-apple-darwin24.6.0
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc -std=gnu23... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld
checking if the linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) is GNU ld... no
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 786432
checking how to convert x86_64-apple-darwin24.6.0 file names to x86_64-apple-darwin24.6.0 format... func_convert_file_noop
checking how to convert x86_64-apple-darwin24.6.0 file names to toolchain format... func_convert_file_noop
checking for /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld option to reload object files... -r
checking for file... file
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ranlib... ranlib
checking for ar... ar
checking for archiver @FILE support... no
checking for strip... strip
checking command to parse /usr/bin/nm -B output from gcc -std=gnu23 object... ok
checking for sysroot... no
checking for a working dd... /bin/dd
checking how to truncate binary pipes... /bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking for dsymutil... dsymutil
checking for nmedit... nmedit
checking for lipo... lipo
checking for otool... otool
checking for otool64... no
checking for -single_module linker flag... ld: warning: -single_module is obsolete
no
checking for -no_fixup_chains linker flag... yes
checking for -exported_symbols_list linker flag... yes
checking for -force_load linker flag... yes
checking for stdio.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for strings.h... yes
checking for sys/stat.h... yes
checking for sys/types.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc -std=gnu23 supports -fno-rtti -fno-exceptions... yes
checking for gcc -std=gnu23 option to produce PIC... -fno-common -DPIC
checking if gcc -std=gnu23 PIC flag -fno-common -DPIC works... yes
checking if gcc -std=gnu23 static flag -static works... no
checking if gcc -std=gnu23 supports -c -o file.o... yes
checking if gcc -std=gnu23 supports -c -o file.o... (cached) yes
checking whether the gcc -std=gnu23 linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin24.6.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld
checking if the linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) is GNU ld... no
checking whether the g++ linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking for g++ option to produce PIC... -fno-common -DPIC
checking if g++ PIC flag -fno-common -DPIC works... yes
checking if g++ static flag -static works... no
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin24.6.0 dyld
checking how to hardcode library paths into programs... immediate
checking for pkg-config... /opt/homebrew/bin/pkg-config
checking pkg-config is at least version 0.9.0... yes
checking for libplist >= 2.2.0... no
checking for libplist-2.0 >= 2.2.0... yes
checking for gcc -std=gnu23 options to detect undeclared functions... none needed
checking for gcc -std=gnu23 options to ignore future-version functions... -Werror=unguarded-availability-new
checking whether plist_format_typedef is declared... yes
checking for pthread_create, pthread_mutex_lock in -lpthread... yes
checking for library containing fmin... none required
checking for egrep... (cached) /usr/bin/grep -E
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for an ANSI C-conforming const... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint8_t... yes
checking whether malloc (0) returns nonnull... yes
checking whether realloc (0, 0) returns nonnull... yes
checking for strcasecmp... yes
checking for strdup... yes
checking for strerror... yes
checking for strndup... yes
checking for stpcpy... yes
checking for localtime_r... yes
checking for ppoll... no
checking for clock_gettime... yes
checking whether to enable WIN32 build settings... no
checking for supported compiler flags...  -g -Wall -Wextra -Wmissing-declarations -Wredundant-decls -Wshadow -Wpointer-arith -Wwrite-strings -Wswitch-default -Wno-unused-parameter
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating usbfluxd/Makefile
config.status: creating tools/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands

Configuration for usbfluxd 1.2.1:
-------------------------------------------

  install prefix ............: /usr/local

  Now type 'make' to build usbfluxd 1.2.1,
  and then 'make install' for installation.

ammarhanif@Ammars-MacBook-Air usbfluxd % make
/Applications/Xcode.app/Contents/Developer/usr/bin/make  all-recursive
Making all in usbfluxd
  CC       usbfluxd-client.o
  CC       usbfluxd-socket.o
  CC       usbfluxd-usbmux_remote.o
  CC       usbfluxd-log.o
  CC       usbfluxd-utils.o
  CC       usbfluxd-main.o
  CCLD     usbfluxd
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(node_list.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(node.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(plist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-limd.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-plutil.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-default.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(oplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(jplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(jsmn.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(bplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(xplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(time64.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(ptrarray.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(hashtable.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(bytearray.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(base64.o)': found architecture 'arm64', required architecture 'x86_64'
Undefined symbols for architecture x86_64:
  "_plist_access_path", referenced from:
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _match_device in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
  "_plist_array_append_item", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
  "_plist_array_get_item", referenced from:
      _start_listen in usbfluxd-client.o
  "_plist_array_get_size", referenced from:
      _start_listen in usbfluxd-client.o
      _start_listen in usbfluxd-client.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_copy", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_connect in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
  "_plist_dict_get_item", referenced from:
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      ...
  "_plist_dict_new_iter", referenced from:
      _usbmux_remote_read_buid in usbfluxd-usbmux_remote.o
      _plist_dict_foreach in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
  "_plist_dict_next_item", referenced from:
      _usbmux_remote_read_buid in usbfluxd-usbmux_remote.o
      _plist_dict_foreach in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
  "_plist_dict_remove_item", referenced from:
      _remote_device_notify_remove in usbfluxd-usbmux_remote.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
  "_plist_dict_set_item", referenced from:
      _send_result in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      ...
  "_plist_free", referenced from:
      _client_close in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      ...
  "_plist_from_bin", referenced from:
      _plist_read_from_filename in usbfluxd-utils.o
  "_plist_from_xml", referenced from:
      _client_process in usbfluxd-client.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
      _plist_read_from_filename in usbfluxd-utils.o
  "_plist_get_node_type", referenced from:
      _client_process in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      ...
  "_plist_get_string_val", referenced from:
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      ...
  "_plist_get_uint_val", referenced from:
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      ...
  "_plist_new_array", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_new_bool", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_new_dict", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_device_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_new_string", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_new_uint", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_to_bin", referenced from:
      _plist_write_to_filename in usbfluxd-utils.o
  "_plist_to_xml", referenced from:
      _client_send_plist_pkt in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _send_device_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_instances in usbfluxd-client.o
      ...
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [usbfluxd] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
ammarhanif@Ammars-MacBook-Air usbfluxd % 
ammarhanif@Ammars-MacBook-Air usbfluxd % make

/Applications/Xcode.app/Contents/Developer/usr/bin/make  all-recursive
Making all in usbfluxd
  CCLD     usbfluxd
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(node_list.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(node.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(plist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-limd.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-plutil.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(out-default.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(oplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(jplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(jsmn.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(bplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(xplist.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(time64.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(ptrarray.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(hashtable.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(bytearray.o)': found architecture 'arm64', required architecture 'x86_64'
ld: warning: ignoring file '/opt/homebrew/Cellar/libplist/2.7.0/lib/libplist-2.0.a(base64.o)': found architecture 'arm64', required architecture 'x86_64'
Undefined symbols for architecture x86_64:
  "_plist_access_path", referenced from:
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _match_device in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
  "_plist_array_append_item", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
  "_plist_array_get_item", referenced from:
      _start_listen in usbfluxd-client.o
  "_plist_array_get_size", referenced from:
      _start_listen in usbfluxd-client.o
      _start_listen in usbfluxd-client.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_copy", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_connect in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _remote_device_get_for_instance in usbfluxd-usbmux_remote.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
  "_plist_dict_get_item", referenced from:
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      ...
  "_plist_dict_new_iter", referenced from:
      _usbmux_remote_read_buid in usbfluxd-usbmux_remote.o
      _plist_dict_foreach in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
  "_plist_dict_next_item", referenced from:
      _usbmux_remote_read_buid in usbfluxd-usbmux_remote.o
      _plist_dict_foreach in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
  "_plist_dict_remove_item", referenced from:
      _remote_device_notify_remove in usbfluxd-usbmux_remote.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
  "_plist_dict_set_item", referenced from:
      _send_result in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      ...
  "_plist_free", referenced from:
      _client_close in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      ...
  "_plist_from_bin", referenced from:
      _plist_read_from_filename in usbfluxd-utils.o
  "_plist_from_xml", referenced from:
      _client_process in usbfluxd-client.o
      _usbmux_remote_process in usbfluxd-usbmux_remote.o
      _plist_read_from_filename in usbfluxd-utils.o
  "_plist_get_node_type", referenced from:
      _client_process in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      ...
  "_plist_get_string_val", referenced from:
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _plist_dict_copy_string_val in usbfluxd-client.o
      ...
  "_plist_get_uint_val", referenced from:
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      ...
  "_plist_new_array", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_device_list in usbfluxd-usbmux_remote.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_new_bool", referenced from:
      _send_listener_list in usbfluxd-client.o
      _usbmux_remote_copy_instances in usbfluxd-usbmux_remote.o
  "_plist_new_dict", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_device_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_new_string", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_new_uint", referenced from:
      _send_result in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_process in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _update_client_info in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      ...
  "_plist_to_bin", referenced from:
      _plist_write_to_filename in usbfluxd-utils.o
  "_plist_to_xml", referenced from:
      _client_send_plist_pkt in usbfluxd-client.o
      _send_result in usbfluxd-client.o
      _notify_device_add in usbfluxd-client.o
      _client_device_remove in usbfluxd-client.o
      _send_device_list in usbfluxd-client.o
      _send_listener_list in usbfluxd-client.o
      _send_instances in usbfluxd-client.o
      ...
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [usbfluxd] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
ammarhanif@Ammars-MacBook-Air usbfluxd % 
ammarhanif@Ammars-MacBook-Air usbfluxd % 
