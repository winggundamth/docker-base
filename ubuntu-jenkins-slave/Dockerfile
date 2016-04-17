# Ubuntu ready to be Jenkins Slave

FROM winggundamth/ubuntu-java:latest
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=trusty-20160412

# 1) Install Git, Ansible, OpenSSH and necessary packages
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
    apt-get install -y git ansible curl wget openssh-server vim tmux rsync \
      byobu && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install boto docker-py && \
    wget -O /usr/local/bin/docker.tgz \
      https://get.docker.com/builds/Linux/x86_64/docker-1.11.0.tgz && \
    wget -O /usr/local/bin/docker-compose \
      https://github.com/docker/compose/releases/download/1.7.0/docker-compose-`uname -s`-`uname -m` && \
    wget -O /usr/local/bin/docker-machine \
      https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` && \
    tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ --strip=1 && \
    chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy /root/.cache \
      /root/.pip /usr/local/bin/docker.tgz

CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 22

# 1) Configure OpenSSH
# 2) Create jenkins user
# 3) Prepare authorized_keys file for ssh
ENV JENKINS_HOME=/var/jenkins
RUN sed -i "/env_reset/a \Defaults        env_keep+=SSH_AUTH_SOCK" \
      /etc/sudoers && \
    sed -i 's/required     pam_loginuid.so/optional     pam_loginuid.so/g' \
      /etc/pam.d/sshd && \
    echo 'export LC_ALL=en_US.UTF-8' > /root/.bash_profile && \
    useradd -s /bin/bash -d $JENKINS_HOME -m jenkins && \
    mkdir -p /var/run/sshd /root/.ssh $JENKINS_HOME/.ssh && \
    touch $JENKINS_HOME/.ssh/authorized_keys /root/.ssh/authorized_keys && \
    chown -R root:root /root/.ssh && \
    chown -R jenkins:jenkins $JENKINS_HOME/.ssh && \
    chmod 700 $JENKINS_HOME/.ssh /root/.ssh && \
    chmod 600 $JENKINS_HOME/.ssh/authorized_keys /root/.ssh/authorized_keys
