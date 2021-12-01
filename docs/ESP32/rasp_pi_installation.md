---
typora-copy-images-to: ..\..\static\images
---

+++
date = "2017-05-27"
description = "树莓派安装"
title = "树莓派安装"
+++

## 1. Image下载

官方下载：

https://www.raspberrypi.org/downloads/raspbian/

因为文件较大，可以直接下载.zip文件可能会中断，文件不完整等问题。下载完成后推荐使用fciv工具检查文件。

`fciv xxx.zip -sha1 `

校验文件的 SHA-1和官方网站上给出的是否一致。

## 2. Image刷入SD卡

官方建议使用Etcher (https://etcher.io/) 刷入，操作简单

SD卡插入电脑，启动Etcher，界面如下。选择刚才下载的.zip文件，选择SD卡，Flash!



![1495855306303](C:\Users\q19439\Google Drive\Mekesim\meketool\bookshelf\static\images/1495855306303.png)

写入后还会验证，大概需要15分钟的样子。



預設帳號是pi，密碼是raspberry

## 开机设置

将SD卡插入树莓派，接通电源。

### 连接wifi

### 开启SSH和VNC服务

Perference -- > Raspberry Pi Configuration -- > Interface

输入ifconfig获取树莓派的IP地址。

可以使用SSH终端Putty访问树莓派，默认账号密码是pi/raspberry

也可以使用RealVNC Viewer 从PC上访问RPi了。


## 安装MQTT Client

sudo apt-get install mosquitto-clients