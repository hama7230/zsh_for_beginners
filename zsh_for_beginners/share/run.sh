#!/bin/sh

cd /home/zsh/chroot/tmp/_your_tar_file_is_extracted_here_plz_enjoy
/usr/bin/python2.7 -u /home/zsh/server.py && /usr/sbin/chroot /home/zsh/chroot /_bin_/zsh -r
