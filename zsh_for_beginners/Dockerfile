FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install xinetd python2.7 -y

RUN cd /root
RUN useradd -m zsh
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:root /home/zsh
RUN setcap cap_sys_chroot+ep /usr/sbin/chroot 

CMD ["/usr/sbin/xinetd", "-dontfork"]
