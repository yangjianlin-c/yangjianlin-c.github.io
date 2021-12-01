## 收集数据

Edge Impulse支持多种数据收集方式。

![](C:\Project\Website\docs\docs\images\2021-06-08-08-51-20-image.png)

这里使用Data from any device with the data forwarder这种方式。也就是利用EDGE IMPULSE CLI工具将设备串口数据通过电脑上传到Edge Impulse。

### 安装edge-impulse-cli工具

电脑安装python和Node.js。

```powershell
npm install -g edge-impulse-cli --force
```

设置连接代理

```powershell
set HTTPS_PROXY=http://10.144.1.10:8080
edge-impulse-daemon
```

### 数据转发Data forwarder

device串口输出数据格式。以`,` 或 `TAB`分隔。

> -0.12,-6.20,7.90
> -0.13,-6.19,7.91
> -0.14,-6.20,7.92
> -0.13,-6.20,7.90
> -0.14,-6.20,7.91

通过串口连接设备，运行edge-impulse-cli工具

```powershell
edge-impulse-data-forwarder
```

在网页端采集数据，标签。训练模型。下载模型。

PlatformIO中安装模型

pio lib install ei-colin-project-1-arduino-1.0.1.zip

