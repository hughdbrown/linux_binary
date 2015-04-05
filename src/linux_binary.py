#!/usr/bin/env python
"""
usage: linux_binary (-h | -r <VERSION> | -i <VERSION> | -v)

optional arguments:
  -h, --help
                        Show this help message and exit
  -i <VERSION>, --install <VERSION>
                        Create installation script
  -r <VERSION>, --remove <VERSION>
                        Create removal script
  -v, --versions
                        List versions
"""
from __future__ import print_function

from docopt import docopt

from src.versions import VERSIONS


def print_exec_header():
    print("#!/bin/sh -e\n")

def wget_file(filename):
    http_address = "http://kernel.ubuntu.com/~kernel-ppa/mainline/v${{SHORT_VERSION}}-${{NAME}}/{0}".format(filename)
    print("wget {0}".format(http_address))

def install_script(version):
    x = VERSIONS[version]
    print_exec_header()
    for k, v in x.items():
        print("export {0}={1}".format(k, v))
    print("export VERSION=${SHORT_VERSION}-${SHORT_STRING}")
    print("export FULL_VERSION=${VERSION}.${RELEASE_DATE}")
    print()
    wget_file("linux-headers-${VERSION}_${FULL_VERSION}_all.deb")
    wget_file("linux-headers-${VERSION}-generic_${FULL_VERSION}_amd64.deb")
    wget_file("linux-image-${VERSION}-generic_${FULL_VERSION}_amd64.deb")
    print()
    print("sudo dpkg -i linux-headers-${SHORT_VERSION}-*.deb linux-image-${SHORT_VERSION}-*.deb")
    print("sudo update-grub")
    print("sudo reboot")

def remove_script(version):
    x = VERSIONS[version]
    print_exec_header()
    for k, v in x.items():
        print("export {0}={1}".format(k, v))
    print("sudo apt-get remove linux-headers-${SHORT_VERSION}-* linux-image-${SHORT_VERSION}-*")

def print_versions():
    for key in VERSIONS:
        print(key)

def main():
    options = docopt(__doc__)
    if options['--versions']:
        print_versions()
    else:
        options_remove, options_install = [options.get(key) for key in ("--remove", "--install")]
        if options_remove:
            remove_script(options_remove)
        elif options_install:
            install_script(options_install)

if __name__ == '__main__':
    main()
