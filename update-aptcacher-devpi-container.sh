#!/bin/bash

set -xe

docker pull winggundamth/apt-cacher-ng:trusty
docker pull winggundamth/devpi-server:trusty

docker stop apt-cacher-ng devpi-server
docker rename apt-cacher-ng apt-cacher-ng-blue
docker rename devpi-server devpi-server-blue

docker run -d -p 172.17.0.1:3142:3142 --name=apt-cacher-ng \
  --hostname=apt-cacher-ng --restart=unless-stopped \
  --volumes-from apt-cacher-ng-blue winggundamth/apt-cacher-ng:trusty
docker run -d -p 172.17.0.1:3141:3141 --name=devpi-server \
  --hostname=devpi-server --restart=unless-stopped \
  --volumes-from devpi-server-blue winggundamth/devpi-server:trusty

docker rm -f apt-cacher-ng-blue devpi-server-blue
