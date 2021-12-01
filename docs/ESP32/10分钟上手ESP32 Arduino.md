# 10分钟上手ESP32 Arduino

本文是ESP32开发板的入门指南。ESP32是它ESP8266的后继产品，显著的区别是ESP32拥有双核，及支持蓝牙。ESP32与ESP8266之间的差异： [ESP32与ESP8266 –优缺点](https://makeradvisor.com/esp32-vs-esp8266/)

## ESP32 DEVKIT DOIT

在本文中，我们将使用ESP32 DEVKIT DOIT开发板。但是此页面上的信息也与其他使用ESP-WROOM-32芯片的ESP32开发板兼容。

## 技术指标

关于ESP32关键参数：

- ESP32是双核，这意味着它有2个处理器。
- 具有Wi-Fi和内置蓝牙。
- 运行32位程序。
- 时钟频率可以高达240MHz，并且具有512 kB RAM。
- 该特定板有30或36个引脚，每行15个。
- 它还具有多种可用的外设，例如：电容式触摸，ADC，DAC，UART，SPI，I2C等。
- 它带有内置霍尔效应传感器和内置温度传感器。

要了解有关ESP32 GPIO的更多信息，请阅读我们的GPIO参考指南： ESP32引脚参考。

## 软件开发环境

ESP32可以在不同的编程环境中进行编程。您可以使用：

- Arduino IDE
- Espressif IDF（IoT开发框架）
- Micropython
- JavaScript
- LUA
- …

在我们的项目中，我们主要使用Arduino IDE或MicroPython对ESP32进行编程。

### 在Arduino IDE中准备ESP32开发板

Arduino IDE有一个附加开发板选项，可让您使用Arduino IDE及其编程语言对ESP32进行编程。请遵循以下教程之一来准备Arduino IDE：

- **Windows**版–在Arduino IDE中安装ESP32开发板
- **Mac和Linux**版–在Arduino IDE中安装ESP32开发板

## ESP32引脚指南

使用ESP32开发板首先需了解其引脚的分布及对应编号。ESP32 Devkit V1有两种版本，32引脚和36引脚的版本。两种版本对应的引脚名称如下：

**具有30个GPIO的版本**

![ESP32-DOIT-DEVKIT-V1-Board-Pinout-30-GPIOs](img/ESP32-DOIT-DEVKIT-V1-Board-Pinout-30-GPIOs.png)

**具有36个GPIO的版本**

![ESP32-DOIT-DEVKIT-V1-Board-Pinout-36-GPIOs](img/ESP32-DOIT-DEVKIT-V1-Board-Pinout-36-GPIOs.jpg)

!!! tip
    开发板上印的引脚编号为D0, D1, ...，它代表的含义就是GPIO0, GPIO1, ...

## 使用Arduino IDE将代码上传到ESP32

为了演示如何将代码上传到ESP32开发板，我们将构建一个简单的示例来使LED闪烁。

将以下代码复制到您的Arduino IDE中：

```c
/*
  Blink
*/

// ledPin refers to ESP32 GPIO 23
const int ledPin = 23;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin ledPin as an output.
  pinMode(ledPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                  // wait for a second
  digitalWrite(ledPin, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                  // wait for a second
}
```

将ESP32开发板插入计算机，然后按照以下说明进行操作：

![img](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/select-board.jpg?w=840&ssl=1)

1）转到**Tools** > **Board**，向下滚动到ESP32部分，然后选择您的ESP32板的名称。就我而言，它是DOIT ESP32 DEVKIT V1开发板。

2）转到  **Tools** > **Port**，然后选择可用的COM端口。

![img](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/com-port-selected.jpg?w=840&ssl=1)

3）按下上传按钮。

![img](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2016/12/arduino-ide-upload-button.png?w=840&ssl=1)



**注意：**如果您在尝试上传代码时遇到以下错误，则说明您的ESP32未处于刷新/上传模式。

```
Failed to connect to ESP32: Timed out... Connecting...
```

如果你的开发板没有选择错误的话，要上传代码，需要执行以下步骤：

- 按住ESP32开发板中的“ **BOOT** ”按钮

![img](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/boot-button-1.jpg?w=840&ssl=1)

- 当Arduino IDE中显示**Connecting….** 消息，即可松开“ **BOOT** ”按钮

![img](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/uploading-esp32.png?w=840&ssl=1)

- 之后，您应该会看到“ **Done uploading** ”消息。

上载新代码后，您可以按“ **EN** ”按钮重启ESP32并运行新上载的代码。

## 演示结果

上载代码后，连接到GPIO 23的LED应该每隔一秒闪烁一次。

![img](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/esp32-blink-an-led.jpg?w=840&ssl=1)https://www.mediavine.com/)

## 总结

我们希望您发现本入门指南很有用。LED闪烁只是一个简单的项目，可让您开始使用ESP32。这也是学习将代码上传到板上所需的过程的好方法。