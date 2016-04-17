# apt-cacher-ng
#
# If you want to use apt-cacher-ng to speed up downloading packages
# This need to run apt-cacher-ng container by these command before build first
# docker run -d -p 172.17.0.1:3142:3142 --name=apt-cacher-ng \
#   --hostname=apt-cacher-ng --restart=unless-stopped \
#   winggundamth/apt-cacher-ng
# and build with command
# docker build --build-arg APT_CACHER_NG=true
# Required Docker 1.9.0+ since ip address on docker0 has been changed

FROM winggundamth/ubuntu-base:latest
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=trusty-20160412

# 1) Install apt-cacher-ng
# 2) Clean to reduce Docker Image size
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo 'Acquire::http::Proxy "http://172.17.0.1:3142";' \
      > /etc/apt/apt.conf.d/11proxy || true; \
    apt-get update && \
    apt-get install -y apt-cacher-ng && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy

# 1) Configure apt-cacher-ng to make sure it won't proxy https
# 2) Link stdout and stderr to apt-cacher-ng log files
RUN echo "PassThroughPattern: .*:443$" >> /etc/apt-cacher-ng/acng.conf && \
    ln -sf /dev/stdout /var/log/apt-cacher-ng/apt-cacher.log && \
    ln -sf /dev/stderr /var/log/apt-cacher-ng/apt-cacher.err

VOLUME ["/var/log", "/var/cache/apt-cacher-ng"]

# How to run apt-cacher as foreground process
CMD ["/usr/sbin/apt-cacher-ng", "-c", "/etc/apt-cacher-ng/", "ForeGround=1"]

# Expose port
EXPOSE 3142
