# My based Dockerfile
This is all my based Dockerfile for my works. Each directory means each Docker Image that will automated build on my [Docker Hub account](https://hub.docker.com/u/winggundamth/).

Feel free to send pull request, add comment or open issue.

## Speed up local build
All my base Dockerfile come with build argument that can speed up local build
- ```APT_CACHER_NG``` available on all Dockerfile
- ```DEVPI_SERVER``` only available on ```ansible-docker```, ```devpi-server``` and ```uwsgi-python2```

When build you just specify ```--build-arg``` to your own apt-cacher-ng and devpi-server
```bash
# Building uwsgi-python2
docker build --build-arg APT_CACHER_NG=https://apt-cacher-ng.example.com \
  --build-arg DEVPI_SERVER=https://devpi.example.com/root/pypi/+simple \
  -t winggundamth/uwsgi-python2 uwsgi-python2
```

Don't forget that if you specify the argument that does not exist in Dockerfile. The build will fail.

## Run your own local apt-cacher-ng server on your build station
You can run apt-cacher-ng container to cache apt-get downloaded packages by running command
```bash
# Remove 172.17.0.1: if you want anyone can access this
docker run -d -p 172.17.0.1:3142:3142 --name=apt-cacher-ng \
  --hostname=apt-cacher-ng --restart=unless-stopped \
  winggundamth/apt-cacher-ng
```

Then when build you can use ```--build-arg APT_CACHER_NG=http://172.17.0.1:3142```

## Run your own local devpi server on your build station
Also you can run devpi-server container to cache downloaded packages from pip install
```bash
# Remove 172.17.0.1: if you want anyone can access this
docker run -d -p 172.17.0.1:3141:3141 --name=devpi-server \
  --hostname=devpi-server --restart=unless-stopped \
  winggundamth/devpi-server
```

Then when build you can use ```--build-arg DEVPI_SERVER=http://172.17.0.1:3141/root/pypi/+simple```

## Update apt-cacher-ng and devpi-server container without losing your caching data
You can use script ```update-aptcacher-devpi-container.sh``` script to update apt-cacher-ng and devpi-server container and not worry about losing your caching data by running command
```bash
./update-aptcacher-devpi-container.sh
```
