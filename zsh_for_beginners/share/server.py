#! /usr/bin/python2.7
import os
import sys
import tempfile
import subprocess


max_size = 0x100000000
size_file = int(raw_input('Size: '))
if max_size < size_file:
    sys.exit(1)

count = 0
buf = ''
while size_file >= count:
    buf += sys.stdin.read(size_file-count)
    count += len(buf)

try:
    temp = tempfile.NamedTemporaryFile(dir="./", suffix=".tar.gz")
    temp.write(buf)
    ret = subprocess.check_call(["tar", "xf", temp.name])
    temp.close()
    if ret != 0:
        sys.exit(1)
except :
    temp.close()
    sys.exit(1)

print "please enjoy your shell :)"
