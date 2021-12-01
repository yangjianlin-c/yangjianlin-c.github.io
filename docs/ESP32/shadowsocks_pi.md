# 在树莓派上安装 shadowsocks 客户端

现在来安装客户端到本地服务器，这样的话只要本地服务器开机就可以给全部的本地机器代理上网了。而不必每个本地机器都安装客户端。

## 安装 Shadowsocks 

`pip install shadowsocks`

## 新建配置文件

`sudo nano /etc/shadowsocks.json`

配置文件内容如下。

```python
{
"server":"SS服务器ip地址",
"server_port":443,
"local_address":"192.168.4.13",
"local_port":1080,
"password":"your-passwd",
"timeout":300,
"method":"aes-256-cfb",
"fast_open":false,
"workers":10
}
```

## 配置文件说明

SS服务器ip地址，请填你的服务器 IP 地址。不确定的话，去服务器上查看。

"server_port"，请填写你的 SS服务 端口。不确定的话，去服务器上看你的SS配置。

"local_address":"192.168.4.13",这个是我树莓派在本地的 IP 地址，供给本地机器使用

"local_port":1080,是我供给本地机器使用的端口

"password":"your-passwd",填写服务密码。确保和服务器上写的一样。

"timeout":300,以下全部和远程服务器保持一致

"method":"aes-256-cfb",

"fast_open":false,

"workers":10

## 添加到开机自启动

`sudo nano /etc/rc.local`

在` exit 0 `之前写入这一行

`/usr/local/bin/sslocal -c /etc/shadowsocks.json -d start`

## 重启树莓派

`sudo reboot`

在任一和树莓派**同局域网内的本地机器**

如这个 IP 的机器上：192.168.4.33

打开 Firefox 浏览器，在地址栏输入 

`about:preferences#advanced`

选` 网络 `连接 配置 Firefox 如何连接至国际互联网，`设置(E)..`

`手动配置代理(M)`

选择` SOCKS主机 `

地址为`192.168.4.13`

端口`1080`

版本选 `SOCKSv5`

保存

## 参考

http://wiki.guoruei.org/computer/software/linux/install-shadowsocks-on-ubuntu-vps

https://story.tonylee.name/2016/03/31/yong-shu-mei-pai-da-zao-wu-xian-zhong-ji-ke-xue-shang-wang-lu-you-qi/