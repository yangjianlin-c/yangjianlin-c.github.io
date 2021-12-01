---
title: Centos安装Python3
date: 2018-07-27
---

## 安装Python3
```
sudo yum install gcc openssl-devel zlib-devel

cd /usr/src
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz

tar -xvJf Python-3.7.0.tar.xz

cd Python-3.7.0

./configure prefix=/usr/local/python3
make altinstall
ln -s /opt/python3/bin/python3.6 /usr/bin/python3.6


yum install python34-pip

sudo nohup python mqtt_simulator.py &

chomd +x mqtt_simulator.py

nohup python3 mqtt_simulator.py &

```

