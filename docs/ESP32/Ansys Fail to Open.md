---
title: ANSYS过段时间出现License错误的解决办法
date: 2014-09-15
---

如果 ANSYS 以前可以用，但不知何原因出现License错误，可能是Licesen服务器没有启动。

<!-- more -->

可以查看安装目录下的ANSYS Inc\Shared Files\Licensing\license.log查看具体原因。 

极有可能是由于1055端口被占用，导致FLEXl not running，解决办法： 

开cmd，输入： 

    netstat -a -n -o


```
Active Connections
Proto  Local Address          Foreign Address        State           PID
TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       984
TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
TCP    0.0.0.0:1055           0.0.0.0:0              LISTENING       1116
TCP    0.0.0.0:2325           0.0.0.0:0              LISTENING       8556
TCP    0.0.0.0:5357           0.0.0.0:0              LISTENING       4
TCP    0.0.0.0:9145           0.0.0.0:0              LISTENING       10648
TCP    0.0.0.0:24800          0.0.0.0:0              LISTENING       6004
```

后面省略 找到1055端口 对应的 pid值（比如2036）。 

找到后打开任务管理器查看进程，找到PID值对应的映像名称关闭即可，则FLExlm 则自动运行，如果在任务管理器的进程里找不到PID值 ，那么打开“查看”-“选项列”，勾选PID选项即可。 

如果在任务管理器里面没有找到对应的PID，则用**管理员权限**运行 `C:\windows\system32\cmd.exe` 输入：

    taskkill /pid 2036 /f

关闭此进程。 再次stop, start License服务，试试，应该没问题了。