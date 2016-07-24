# Ubuntu with various of client application
#
# Ansible
# Docker client
# Docker machine
# Docker compose
# Shade (Clients for OpenStack)

FROM winggundamth/ubuntu-base:xenial
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=xenial-20160706

# 1) Install Ansible and necessary packages
# 2) Download Docker client, machine and compose
# 3) Install Shade
# 3) Clean to reduce size of Docker Image
ARG APT_CACHER_NG
ARG DEVPI_SERVER
ENV ANSIBLE_HOST_KEY_CHECKING=False
RUN [ -n "$APT_CACHER_NG" ] && \
      echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \
      > /etc/apt/apt.conf.d/11proxy || true; \
    [ -n "$DEVPI_SERVER" ] && \
      mkdir -p ~/.pip && \
      echo "[global]\n\
index-url = $DEVPI_SERVER\n\
trusted-host = \
$(echo $DEVPI_SERVER | awk -F/ '{print $3}' | awk -F: '{print $1}')\n\
" >> ~/.pip/pip.conf || true; \
    apt-get update && \
    apt-get install -y python python-dev curl wget git build-essential && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    apt-get install -y libssl-dev libffi-dev && \
    pip install ansible boto docker-py dnspython shade && \
    wget -O /usr/local/bin/docker.tgz \
      https://get.docker.com/builds/Linux/x86_64/docker-1.11.2.tgz && \
    wget -O /usr/local/bin/docker-compose \
      https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` && \
    wget -O /usr/local/bin/docker-machine \
      https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` && \
    tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ --strip=1 && \
    chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \
    apt-get remove --purge --auto-remove -y \
      binutils build-essential bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc \
      gcc-5 ifupdown iproute2 isc-dhcp-client isc-dhcp-common \
      libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl \
      libasan2 libatm1 libatomic1 libc-dev-bin libc6-dev libcc1-0 libcilkrts5 \
      libdns-export162 libdpkg-perl libfakeroot libfile-fcntllock-perl \
      libgcc-5-dev libgdbm3 libgmp10 libgomp1 libisc-export160 libisl15 \
      libitm1 liblsan0 libmnl0 libmpc3 libmpfr4 libmpx0 libperl5.22 \
      libquadmath0 libstdc++-5-dev libtsan0 libubsan0 libxtables11 \
      linux-libc-dev make manpages manpages-dev netbase patch perl \
      perl-modules-5.22 rename xz-utils python-dev libssl-dev libffi-dev && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \
      /etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip
