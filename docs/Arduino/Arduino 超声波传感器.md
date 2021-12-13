# 超声波传感器

超声波传感器是一种使用**声波**测量物体距离的设备。它的工作原理是发出超声波频率的声波并等待它从物体反弹回来。然后，使用声音传输和声音接收之间的时间延迟来计算距离。

使用公式 **Distance =（声速\*时间延迟）/ 2来完成**

我们将距离公式除以2，因为声波沿着往返行进，即从传感器返回传感器，使实际距离加倍。

HC-SR04超声波传感器使用声纳来确定物体的距离，就像蝙蝠一样。它提供了非常好的非接触范围检测，准确度高，读数稳定，易于使用，尺寸从2厘米到400厘米或1英寸到13英尺不等。

其操作不受阳光或黑色材料的影响，尽管在声学上，柔软的材料（如布料等）可能难以检测到。它配有超声波发射器和接收器模块。



![超声波传感器](https://atts.w3cschool.cn/attachments/tuploads/arduino/ultrasonic_sensor.jpg)



![超声波](https://atts.w3cschool.cn/attachments/tuploads/arduino/ultrasonic_sensor_radiations.jpg)

## 技术规格

- 工作电压：5V DC
- 工作电流：15mA
- 静态电流：<2mA
- 测量角度：<15°
- 测距：2cm – 4m
- 分辨率：0.3厘米

## 使用说明

HC-SR04上有四个针脚。他们是 ：

- Vcc（5V电源）
- Gnd（地面）
- Trig（触发器）
- 回声（接收）

Trigger 和 Echo 分别接到控制板的两个数字引脚。

- 将Trig引脚设置为高电平，至少10us，触发模块测距功能。
- 触发等待约200us后，模块会自动发送 8 个 40KHz 的超声波脉冲。

- 脉冲发送完成后，Echo 引脚立即输出高电平。
- 当模块检测到返回的完整的8个40KHz 的超声波脉冲后，Echo 引脚变为低电平。这步会由模块内部自动完成。
- 因此，Echo 引脚高电平持续的时间就是超声波从发射到返回的时间。使用 pulseIn() 函数获计算Echo高电平持续的时间，乘以声波在空气中的传播速度，就可以计算出这段超声波脉冲从发射到接收经历的距离。

![ultrasonic distance](assets/ultrasonic%20distance.png)

## Arduino代码

```c
/*
* Ultrasonic Sensor HC-SR04 interfacing with Arduino.
*/
// defining the pins
const int trigPin = 9;
const int echoPin = 10;
// defining variables
long duration;
int distance;
void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
}
void loop() {
// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance, mm
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
}
```

## 代码说明

Arduino中，提供了一个函数pulseIn()。

pulseIn()函数用来读取一个引脚的电平持续时间（HIGH或LOW）。例如，如果value是HIGH，pulseIn()会等待引脚变为HIGH，开始计时，再等待引脚变为LOW并停止计时。返回脉冲的长度，单位毫秒。如果在指定的时间内无脉冲函数返回。

计时范围从10微秒至3分钟。（1秒=1000毫秒=1000000微秒）
