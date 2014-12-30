linux_binary
============

Python code to create shell script to download and install a particular set of 64-bit linux images. Relies on a database of
version information stored in the file.

Requirements
============

1. docopt library

Usage
=====

Running `-i` writes on `stdout` the shell script to install a particular version, so installation can be done by piping to `sh`:

```bash
./linux_binary.py -i 3.18.1 | sh
```