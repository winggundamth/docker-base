# docker-base
All my Dockerfile for automated build on Docker Hub

# Speed up local build
All my base Dockerfile come with build argument APT_CACHER_NG and DEVPI_SERVER that can speed up build

You can run apt-cacher-ng container to cache apt-get downloaded packages by running command
```
docker run -d -p 172.17.0.1:3142:3142 --name=apt-cacher-ng \
  --hostname=apt-cacher-ng --restart=unless-stopped \
  winggundamth/apt-cacher-ng
```

Also you can run devpi-server container to cache downloaded packages from pip install
```
docker run -d -p 172.17.0.1:3141:3141 --name=devpi-server \
  --hostname=devpi-server --restart=unless-stopped \
  winggundamth/devpi-server
```

When build you just specify --build-arg to those caching servers
```
# Building ubuntu-base
docker build --build-arg APT_CACHER_NG=http://172.17.0.1:3142 \
  --build-arg DEVPI_SERVER=http://172.17.0.1:3141/root/pypi/+simple \
  -t winggundamth/ubuntu-base ubuntu-base
```

Or even you can use your own apt-cacher-ng and devpi-server
```
# Building ubuntu-base
docker build --build-arg APT_CACHER_NG=https://apt-cacher-ng.example.com \
  --build-arg DEVPI_SERVER=https://devpi.example.com/root/pypi/+simple \
  -t winggundamth/ubuntu-base ubuntu-base
```
