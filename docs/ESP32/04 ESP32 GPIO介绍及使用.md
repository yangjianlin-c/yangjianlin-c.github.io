本文以ESP32 WROOM 模块为例介绍ESP32 GPIO的使用。

WROOM模块引脚命名，及功能如下图。

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/esp32-pinout-chip-ESP-WROOM-32.png)

## ESP32外设包括：

- 18 Analog-to-Digital Converter (ADC) channels
- 3 SPI interfaces
- 3 UART interfaces
- 2 I2C interfaces
- 16 PWM output channels
- 2 Digital-to-Analog Converters (DAC)
- 2 I2S interfaces
- 10 Capacitive sensing GPIOs

## Pin的输入输出功能

| **GPIO** | **Input** | **Output** | **Notes**                             |
| -------- | --------- | ---------- | ------------------------------------- |
| **0**    | pulled up | OK         | outputs PWM signal at boot            |
| **1**    | TX pin    | OK         | debug output at boot                  |
| **2**    | OK        | OK         | connected to on-board LED             |
| **3**    | OK        | RX pin     | HIGH at boot                          |
| **4**    | OK        | OK         |                                       |
| **5**    | OK        | OK         | outputs PWM signal at boot            |
| **6**    | x         | x          | connected to the integrated SPI flash |
| **7**    | x         | x          | connected to the integrated SPI flash |
| **8**    | x         | x          | connected to the integrated SPI flash |
| **9**    | x         | x          | connected to the integrated SPI flash |
| **10**   | x         | x          | connected to the integrated SPI flash |
| **11**   | x         | x          | connected to the integrated SPI flash |
| **12**   | OK        | OK         | boot fail if pulled high              |
| **13**   | OK        | OK         |                                       |
| **14**   | OK        | OK         | outputs PWM signal at boot            |
| **15**   | OK        | OK         | outputs PWM signal at boot            |
| **16**   | OK        | OK         |                                       |
| **17**   | OK        | OK         |                                       |
| **18**   | OK        | OK         |                                       |
| **19**   | OK        | OK         |                                       |
| **21**   | OK        | OK         |                                       |
| **22**   | OK        | OK         |                                       |
| **23**   | OK        | OK         |                                       |
| **25**   | OK        | OK         |                                       |
| **26**   | OK        | OK         |                                       |
| **27**   | OK        | OK         |                                       |
| **32**   | OK        | OK         |                                       |
| **33**   | OK        | OK         |                                       |
| **34**   | OK        |            | input only                            |
| **35**   | OK        |            | input only                            |
| **36**   | OK        |            | input only                            |
| **39**   | OK        |            | input only                            |

## 一、中断

### 1、中断触发方式

ESP32 Arduino 有以下四种触发方式：

- LOW              低电平触发
- CHANGE       电平变化
- RISING         上升沿触发
- FALLING       下降沿触发
- HIGH             高电平触发

### 2、配置中断

在定义中断函数后，需要在 setup 函数配置中断函数

// interrupt=中断通道编号，function=中断函数，mode=中断触发模式
attachInterrupt(interrupt, function, mode); 

// pin=中断引脚，function=中断函数，mode=中断触发模式
attachInterrupt(pin, function, mode);

如果在程序运行过程不需要使用外部中断了，可以用中断分离函数来取消这一中断设置：

detachInterrupt(interrupt); 
detachInterrupt(Pin);。

### 3、示例

```arduino
void setup()
{
  // 初始化日志打印串口
  Serial.begin(115200);

  // 配置中断引脚
  pinMode(26, INPUT|PULLUP );

  // 检测到引脚 26 下降沿，触发中断函数 blink
  attachInterrupt(26, blink, FALLING);

  Serial.println("\nstart irq test");
}

void loop()
{

}

// 中断函数
void blink()
{
  Serial.println("IRQ");
}
```

## 二、IIC 使用

示例：

```arduino
#include <Wire.h>

void setup() {
  // 启动 i2c 总线
  Wire.begin();

  // 初始化串口
  Serial.begin(9600);
}

int reading = 0;

void loop() {
  // step 1: 启动与从设备 #112 0x70 的数据交互
  Wire.beginTransmission(112);

  // 发送数据
  Wire.write(byte(0x00));
  Wire.write(byte(0x50));

  // 结束通信
  Wire.endTransmission();

  // step 2: 等待读数据
  delay(70);

  // step 3: 读取指定寄存器
  Wire.beginTransmission(112);
  Wire.write(byte(0x02));
  Wire.endTransmission();

  // step 4: 请求读 2 字节数据
  Wire.requestFrom(112, 2);

  // step 5: 接收数据
  if (2 <= Wire.available()) {
    reading = Wire.read();
    reading = reading << 8;
    reading |= Wire.read();
    Serial.println(reading);
  }

  delay(250);
}
```

## 三、SPI 使用简析

示例：

/* The ESP32 has four SPi buses, however as of right now only two of

```arduino
* them are available to use, HSPI and VSPI. Simply using the SPI API 
* as illustrated in Arduino examples will use HSPI, leaving VSPI unused.
* 
* However if we simply intialise two instance of the SPI class for both
* of these buses both can be used. However when just using these the Arduino
* way only will actually be outputting at a time.
* 
* Logic analyser capture is in the same folder as this example as
* "multiple_bus_output.png"
* 
* created 30/04/2018 by Alistair Symonds
  */
* 

#include <SPI.h>

static const int spiClk = 1000000; // 1 MHz

//uninitalised pointers to SPI objects
SPIClass * vspi = NULL;
SPIClass * hspi = NULL;

void setup() {
  // 初始化 SPI 实例 VSPI、HSPI
  vspi = new SPIClass(VSPI);
  hspi = new SPIClass(HSPI);

  //clock miso mosi ss

  //使用默认 VSPI 引脚：SCLK = 18, MISO = 19, MOSI = 23, SS = 5
  vspi->begin();

  // alternatively route through GPIO pins of your choice
  //vspi->begin(0, 2, 4, 33); // SCLK, MISO, MOSI, SS

  //使用默认引脚初始化 HSPI
  //SCLK = 14, MISO = 12, MOSI = 13, SS = 15
  hspi->begin(); 

  //alternatively route through GPIO pins
  //hspi->begin(25, 26, 27, 32); //SCLK, MISO, MOSI, SS

  // 初始化 ss 片选引脚，默认为低电平
  pinMode(5, OUTPUT); //VSPI SS
  pinMode(15, OUTPUT); //HSPI SS

}

// the loop function runs over and over again until power down or reset
void loop() {
  //use the SPI buses
  vspiCommand();
  hspiCommand();
  delay(100);
}

void vspiCommand() {
  // 模拟数据
  byte data = 0b01010101;

  // 启动 VSPI 传输
  vspi->beginTransaction(SPISettings(spiClk, MSBFIRST, SPI_MODE0));
  digitalWrite(5, LOW);
  vspi->transfer(data);  
  digitalWrite(5, HIGH);
  vspi->endTransaction();
}

void hspiCommand() {
  byte stuff = 0b11001100;

  hspi->beginTransaction(SPISettings(spiClk, MSBFIRST, SPI_MODE0));
  digitalWrite(15, LOW);
  hspi->transfer(stuff);
  digitalWrite(15, HIGH);
  hspi->endTransaction();
}
```
