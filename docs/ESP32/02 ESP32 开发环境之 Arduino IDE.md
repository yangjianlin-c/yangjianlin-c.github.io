本文介绍如何使用Arduino IDE对ESP32进行编程。

### 在Arduino IDE中准备ESP32开发板

Arduino IDE有一个附加开发板选项，可让您使用Arduino IDE及其编程语言对ESP32进行编程。请遵循以下教程之一来准备Arduino IDE：

- **Windows**版–在Arduino IDE中安装ESP32开发板
- **Mac和Linux**版–在Arduino IDE中安装ESP32开发板

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