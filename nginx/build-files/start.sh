#!/bin/bash

rm -rf /var/run/rsyslogd.pid
service rsyslog start
# Work around fix cron not working on overlayfs as describe here
# https://github.com/docker/docker/issues/16813
touch /etc/crontab
cron
nginx
