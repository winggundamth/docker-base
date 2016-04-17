# devpi server
#
# PyPI server and packaging/testing/release tool

FROM winggundamth/ubuntu-base:latest
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=trusty-20160412

# 1) Install curl and python
# 2) Install pip latest version
# 3) Install devpi-server and devpi-web with pip
# 4) Clean to reduce Docker image size
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \
      > /etc/apt/apt.conf.d/11proxy || true; \
    apt-get update && \
    apt-get install -y curl python && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install devpi-server devpi-web && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy /root/.cache

CMD ["devpi-server", "--serverdir", "/var/lib/devpi/server", "--host", "0.0.0.0"]
EXPOSE 3141
VOLUME ["/var/log", "/var/lib/devpi/server"]
