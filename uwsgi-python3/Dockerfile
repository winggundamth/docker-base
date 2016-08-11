# uWSGI with Python 3.5.2

FROM winggundamth/ubuntu-base:xenial
MAINTAINER Jirayut Nimsaeng (Dear) <jirayut.n@kaidee.com>
ENV FROM_BASE=xenial-20160706

# 1) Update and install python and required packages to compile library
# 2) Install pip latest version
# 3) Install uwsgi with pip
# 4) Clean to reduce Docker image size
ARG APT_CACHER_NG
ARG DEVPI_SERVER
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
    apt-get install -y curl python3 libpython3.5 python3-dev \
      build-essential && \
    curl https://bootstrap.pypa.io/get-pip.py | python3 && \
    pip install uwsgi && \
    apt-get remove --purge --auto-remove -y \
      binutils build-essential bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc \
      gcc-5 ifupdown iproute2 isc-dhcp-client isc-dhcp-common \
      libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl \
      libasan2 libatm1 libatomic1 libc-dev-bin libc6-dev libcc1-0 libcilkrts5 \
      libdns-export162 libdpkg-perl libfakeroot libfile-fcntllock-perl \
      libgcc-5-dev libgdbm3 libgmp10 libgomp1 libisc-export160 libisl15 libitm1 \
      liblsan0 libmnl0 libmpc3 libmpfr4 libmpx0 libperl5.22 libquadmath0 \
      libstdc++-5-dev libtsan0 libubsan0 libxtables11 linux-libc-dev make \
      manpages manpages-dev netbase patch perl perl-modules-5.22 rename \
      xz-utils curl python3-dev && \
    apt-get -y autoremove && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \
      /etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip

# 1) Add user web and prepare .ssh directory
# 2) Copy initial uwsgi ini file
ENV WEB_USER=web
ENV HOME=/home/$WEB_USER WEB_HOME=/home/$WEB_USER
COPY build-files /build-files
RUN useradd --shell /bin/bash --home-dir $WEB_HOME --create-home \
      --base-dir $WEB_HOME $WEB_USER && \
    mkdir -p $WEB_HOME/.ssh && \
    chmod 700 /$WEB_HOME/.ssh && \
    chown $WEB_USER:$WEB_USER $WEB_HOME/.ssh && \
    mv /build-files/uwsgi.ini /etc/uwsgi.ini && \
    mkdir -p /var/log/uwsgi && \
    rm -rf /build-files

VOLUME ["/var/log"]
WORKDIR $WEB_HOME
USER $WEB_USER
EXPOSE 5000
ENTRYPOINT ["uwsgi"]
CMD ["/etc/uwsgi.ini"]
