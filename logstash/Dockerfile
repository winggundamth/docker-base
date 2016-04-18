# Logstash
#
# Collect, Enrich & Transport Data

FROM winggundamth/ubuntu-java:latest
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=trusty-20160412

# 1) Install Logstash
# 2) Clean to reduce Docker Image size
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \
      > /etc/apt/apt.conf.d/11proxy || true; \
    apt-get update && \
    apt-get install -y wget && \
    wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | \
      apt-key add - && \
    echo "deb http://packages.elastic.co/logstash/2.3/debian stable main" \
      > /etc/apt/sources.list.d/logstash-$(lsb_release -cs).list && \
    apt-get update && \
    apt-get install -y logstash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy
