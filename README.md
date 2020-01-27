#Token Pooling
Simple Microservice for serving tokens.

## Installation

Install [Dcoker](https://www.linode.com/docs/applications/containers/install-docker-ce-ubuntu-1804/)

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt update

sudo apt install docker-ce
```

Create Docker image from file

```
sudo docker build .
```


Running docker container locally

```
sudo docker run -it -d -p outport:docker_port hash_id

```