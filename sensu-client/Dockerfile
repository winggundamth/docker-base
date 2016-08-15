# Sensu Client
#
# Monitor servers, services, application health, and business KPIs
# This is Sensu Client image

FROM winggundamth/sensu-base:xenial
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=xenial-20160809

# 1) Install required package for Sensu Client Plugins
# 2) Install Sensu Client Plugins
# 3) Remove packages and files to reduce Docker Image
ENV PATH=/opt/sensu/embedded/bin:$PATH \
    GEM_PATH=/opt/sensu/embedded/lib/ruby/gems/2.0.0:$GEM_PATH
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \
      > /etc/apt/apt.conf.d/11proxy || true; \
    apt-get update && \
    apt-get install -y bc build-essential libmysqlclient-dev libsasl2-dev && \
    sensu-install -P disk-checks,process-checks,cpu-checks,memory-checks, \
      mysql,http,load-checks,mongodb,docker,network-checks,redis, \
      filesystem-checks,execute && \
    apt-get remove --purge --auto-remove -y \
      binutils build-essential cpp cpp-4.8 dpkg-dev fakeroot g++ g++-4.8 gcc \
      gcc-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl libgcc-4.8-dev \
      libalgorithm-merge-perl libasan0 libatomic1 libc-dev-bin libc6-dev \
      libcloog-isl4 libdpkg-perl libfakeroot libfile-fcntllock-perl \
      libgmp10 libgomp1 libitm1 libmpc3 libmpfr4 libquadmath0 \
      libstdc++-4.8-dev libtimedate-perl libtsan0 linux-libc-dev make manpages \
      manpages-dev patch xz-utils libmysqlclient-dev libsasl2-dev && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \
      /etc/apt/apt.conf.d/11proxy \
      /opt/sensu/embedded/lib/ruby/gems/2.2.0/cache/*

# 1) Create configuration file
RUN cp /etc/sensu/config.json.example /etc/sensu/config.json

# Must specify VOLUME on each child Dockerfile because config.json will lost
VOLUME ["/etc/sensu", "/var/log"]
EXPOSE 3030
CMD ["/opt/sensu/embedded/bin/ruby", "/opt/sensu/bin/sensu-client", \
     "-c", "/etc/sensu/config.json", "-d", "/etc/sensu/conf.d", \
     "-e", "/etc/sensu/extensions"]
