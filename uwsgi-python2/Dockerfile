# uWSGI with Python 2.7

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
    apt-get install -y curl git python libpython2.7 python-dev \
      build-essential && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install uwsgi && \
    apt-get remove --purge --auto-remove -y \
      binutils build-essential cpp cpp-4.8 dpkg-dev fakeroot g++ g++-4.8 gcc \
      gcc-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl libgcc-4.8-dev \
      libalgorithm-merge-perl libasan0 libatomic1 libc-dev-bin libc6-dev \
      libcloog-isl4 libdpkg-perl libfakeroot libfile-fcntllock-perl \
      libgmp10 libgomp1 libisl10 libitm1 libmpc3 libmpfr4 libquadmath0 \
      libstdc++-4.8-dev libtimedate-perl libtsan0 linux-libc-dev make manpages \
      manpages-dev patch xz-utils curl python-dev && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \
      /etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip

CMD ["/start.py"]
EXPOSE 5000

# 1) Copy initial uwsgi ini file
# 2) Prepare log and logrotate for uwsgi log file
# 3) Add start.py as first process
COPY build-files /build-files
RUN mv /build-files/uwsgi.ini /etc/uwsgi.ini && \
    mkdir -p /var/log/uwsgi && \
    mv /build-files/uwsgi-logrotate /etc/logrotate.d/uwsgi && \
    mv /build-files/start.py /start.py && \
    chown root:root /start.py && \
    chmod 700 /start.py && \
    rm -rf /build-files

VOLUME ["/var/log"]
