# Ubuntu with Ansible and Docker client
#
# Ubuntu installed Ansible, Docker client, machine and compose

FROM winggundamth/ubuntu-base:xenial
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=trusty-20160412

# 1) Install Ansible and necessary packages
# 2) Download Docker client, machine and compose
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
    echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu \
      $(lsb_release -cs) main" \
      > /etc/apt/sources.list.d/ansible-$(lsb_release -cs).list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7BB9C367 && \
    apt-get update && \
    apt-get install -y ansible curl wget git && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install boto docker-py && \
    wget -O /usr/local/bin/docker.tgz \
      https://get.docker.com/builds/Linux/x86_64/docker-1.11.1.tgz && \
    wget -O /usr/local/bin/docker-compose \
      https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` && \
    wget -O /usr/local/bin/docker-machine \
      https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` && \
    tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ --strip=1 && \
    chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy /root/.cache \
      /root/.pip /usr/local/bin/docker.tgz
