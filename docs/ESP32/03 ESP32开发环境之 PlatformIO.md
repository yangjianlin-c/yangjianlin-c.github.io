本文主要介绍使用VSCODE的 platformIO插件进行ESP32开发。

## 软件安装

- 安装VScode
- 安装插件platformIO IDE
- 在platforms中安装esp32插件 Espressif 32
- 开发板型号espressif esp32 dev module

## 新建项目

在platform中新建项目。开发板选择ESP32-DevKitC，可以选择两种开发方式新建项目：

- 基于Arduino框架
- 基于ESP-idf框架

### 基于Ariduino框架

Framework选择Arduino。

![arduino-debugging-unit-testing-2.png](assets/arduino-debugging-unit-testing-2.png)

### 基于ESP32 IDF框架

开发框架选择 Espressif IoT Development Franmework

![image-20201005232836990](assets/image-20201005232836990.png)

## 创建代码

基于Ariduino框架开发简单，以此框架为例，首先在src目录中创建文件main.cpp

```c
#include <Arduino.h>

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    Serial.println("Hello world!");
    delay(1000);
}
```

## 编译，上传

编译

- `ctrl-alt-b`
- 或者左侧工具栏中的build

上传

- `ctrl-alt-u`
- 或者左侧工具栏中的upload

查看串口输出

- 左侧工具栏中的Monitor

如果看到监视器输出Hello world!则说明测试成功。

## 安装第三方包

1. 在Libraries中搜索，然后安装。
2. 直接将库文件放到lib文件夹下。注意文件夹名称和主文件名称一致。

## 调试

进入调试模式需使用JTAG 线连接至开发板，接线方式如下

| ESP32 pin     | JTAG probe pin |
| ------------- | -------------- |
| 3.3V          | Pin 1(VTref)   |
| GPIO 9 (EN)   | Pin 3 (nTRST)  |
| GND           | Pin 4 (GND)    |
| GPIO 12 (TDI) | Pin 5 (TDI)    |
| GPIO 14 (TMS) | Pin 7 (TMS)    |
| GPIO 13 (TCK) | Pin 9 (TCK)    |
| GPIO 15 (TDO) | Pin 13 (TDO)   |

## 实例1 LED闪烁

```c
#include<Arduino.h>
#define LED 5

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED,HIGH); //高电平
  delay(1000); //等待1000毫秒
  digitalWrite(LED, LOW); //低电平
  delay(1000); //等待1000毫秒
}
```

## 实例2 按钮控制LED

```c
#include<Arduino.h>
#define LED 5
#define botton 0  

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
  pinMode(botton,INPUT_PULLUP); //内部上拉
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(botton)){    
    digitalWrite(LED,HIGH); //高电平
    
  }else{
    digitalWrite(LED,LOW); //低电平
  
  }  
  
}
```