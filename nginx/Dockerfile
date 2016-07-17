# Nginx
#
# HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP
# proxy server

FROM winggundamth/ubuntu-base:xenial
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>
ENV FROM_BASE=xenial-20160706

# 1) Install Nginx
# 2) Install Python because it required by Ansible
# 3) Clean to reduce Docker Image size
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \
      > /etc/apt/apt.conf.d/11proxy || true; \
    echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu \
      $(lsb_release -cs) main" \
      > /etc/apt/sources.list.d/nginx-$(lsb_release -cs).list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \
    apt-get update && \
    apt-get install -y nginx-extras python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy

CMD ["/start.sh"]
EXPOSE 80 443

# 1) Config Nginx not to run as daemon but foreground instead
# 2) Config Logrotate for Nginx
# 3) Add start.sh as first process
COPY build-files /build-files
RUN sed -i "/pid .*/a \daemon off;" /etc/nginx/nginx.conf && \
    sed -i 's/\trotate .*/\trotate 7/g' /etc/logrotate.d/nginx && \
    sed -i 's/weekly/daily/g' /etc/logrotate.d/nginx && \
    sed -i 's/invoke-rc.d nginx rotate/service nginx rotate/g' \
      /etc/logrotate.d/nginx && \
    mv /build-files/start.sh /start.sh && \
    chown root:root /start.sh && \
    chmod 700 /start.sh && \
    rm -rf /build-files

VOLUME ["/var/log", "/etc/nginx", "/etc/ssl/private"]
