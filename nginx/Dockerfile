# Nginx
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

# 1) Install Nginx
# 2) Clean to reduce Docker Image size
ARG APT_CACHER_NG
RUN [ -n "$APT_CACHER_NG" ] && \
      echo 'Acquire::http::Proxy "http://172.17.0.1:3142";' \
      > /etc/apt/apt.conf.d/11proxy || true; \
    echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu \
      $(lsb_release -cs) main" \
      > /etc/apt/sources.list.d/nginx-$(lsb_release -cs).list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \
    apt-get update && \
    apt-get install -y nginx-extras && \
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
