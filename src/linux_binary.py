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

from collections import OrderedDict

from docopt import docopt

def dict_variables(rd, sv):
    return {
        "RELEASE_DATE": rd,
        "SHORT_STRING": "".join(sv),
        "SHORT_VERSION": ".".join(str(int(x)) for x in sv if int(x)),
    }

VERSIONS = OrderedDict([
    ('3.14.5', dict_variables("201405311735", ("03", "14", "05"))),
    ('3.14.6', dict_variables("201406071635", ("03", "14", "06"))),
    ('3.14.7', dict_variables("201406111644", ("03", "14", "07"))),
    ('3.14.8', dict_variables("201406161755", ("03", "14", "08"))),
    ('3.14.9', dict_variables("201406261553", ("03", "14", "09"))),
    ('3.14.10', dict_variables("201406302353", ("03", "14", "10"))),
    ('3.14.11', dict_variables("201407062254", ("03", "14", "11"))),
    ('3.14.12', dict_variables("201407091455", ("03", "14", "12"))),
    ('3.14.13', dict_variables("201407171953", ("03", "14", "13"))),
    ('3.14.14', dict_variables("201407281153", ("03", "14", "14"))),
    ('3.14.15', dict_variables("201407311853", ("03", "14", "15"))),
    ('3.14.16', dict_variables("201408072035", ("03", "14", "16"))),
    ('3.14.17', dict_variables("201408132253", ("03", "14", "17"))),
    ('3.15.1', dict_variables("201406161841", ("03", "15", "01"))),
    ('3.15.2', dict_variables("201406261639", ("03", "15", "02"))),
    ('3.15.3', dict_variables("201407010040", ("03", "15", "03"))),
    ('3.15.4', dict_variables("201407062345", ("03", "15", "04"))),
    ('3.15.5', dict_variables("201407091543", ("03", "15", "05"))),
    ('3.15.6', dict_variables("201407172034", ("03", "15", "06"))),
    ('3.15.7', dict_variables("201407281235", ("03", "15", "07"))),
    ('3.15.8', dict_variables("201407091543", ("03", "15", "08"))),
    ('3.15.9', dict_variables("201408072114", ("03", "15", "09"))),
    ('3.15.10', dict_variables("201408132333", ("03", "15", "10"))),
    ('3.16.1', dict_variables("201408140014", ("03", "16", "01"))),
    ('3.16.2', dict_variables("201409052035", ("03", "16", "02"))),
    ('3.16.3', dict_variables("201409171435", ("03", "16", "03"))),
])


def print_exec_header():
    print("#!/bin/sh -e\n")

def wget_file(filename):
    http_address = "http://kernel.ubuntu.com/~kernel-ppa/mainline/v${{SHORT_VERSION}}-utopic/{0}".format(filename)
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
