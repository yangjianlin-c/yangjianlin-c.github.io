![封面图片](https://img-blog.csdnimg.cn/img_convert/102086352e0bd02d69f749bd8d252226.png)

## 什么是 ESP-NOW？

ESP-NOW 是由乐鑫开发的另一款无线通信协议，可以使多个设备在没有或不使用 Wi-Fi 的情况下进行通信。这种协议类似常见于无线鼠标中的低功耗 2.4GHz 无线连接——设备在进行通信之前要进行配对。配对之后，设备之间的连接是持续的、点对点的，并且不需要握手协议。它是一种短数据传输、无连接的快速通信技术，可以让低功耗控制器直接控制所有智能设备而无需连接路由器，适用于智能灯、遥控控制、传感器数据回传等场景。

使用了 ESP-NOW 通信之后，如果某一个设备突然断电之后，只要它一旦重启，就是自动连接到对应的节点中重新进行通信。

ESP-NOW 支持如下特性：

- 单播包加密或单播包不加密通信；
- 加密配对设备和非加密配对设备混合使用；
- 可携带最长为 250 字节的有效 payload 数据；
- 支持设置发送回调函数以通知应用层帧发送失败或成功。

同样，ESP-NOW 也存在一些限制：

- 暂时不支持广播包；
- 加密配对设备有限制，Station 模式下最多支持10 个加密配对设备；SoftAP 或 SoftAP + Station 混合模式下最多支持 6 个加密配对设备。非加密配对设备支持若干，与加密设备总数和不超过 20 个；
- 有效 payload 限制为 250 字节。

## ESP-NOW 通信方式

ESP-NOW 支持多种通信方式：

- 一对一单向通信

- 一对多单向通信

- 多对一单向通信

- 双向通信

### 一对一单向通信

一对一单向通信是最简单的通信方式，也就是一个设备负责发送数据，另一个设备负责接收数据，如下图所示：

![ESP_NOW_one_way_communication_two_boards](https://img-blog.csdnimg.cn/img_convert/e1d073be8fa80e38ea964fe39f3a7a1f.png)

### 一对多单向通信

一对多单向通信是指一个设备负责发送数据，多个设备负责接收数据。其中数据发送端就类似与遥控器，数据接收端可以负责分别控制不同的设备，如下图所示：

![ESP_NOW_one_master_multiple_slaves](https://img-blog.csdnimg.cn/img_convert/ac86d7935a58467b028f28cdcb979372.png)

### 多对一单向通信

多对一单向通信是指一个设备专门负责接收数据，其余设备则向它发送数据。这种场景主要应用于多个设备采集不同的传感器数据，然后向中心或者总控制器汇总数据，如下图所示：

![ESP_NOW_one_slave_multiple_masters](https://img-blog.csdnimg.cn/img_convert/71bbdee3b3ca518293ba2e55cb72f3a4.png)

### 双向通信

相对于单向通信，双向通信是指通信的双方既可以发送数据、又可以接收数据。一对一双向通信如下图所示：

![ESP_NOW_two_way_communication_two_boards](https://img-blog.csdnimg.cn/img_convert/af14ae57f54355e258e76761b3d1b292.png)

在双向通信中，也可以加入更多的设备，进行两两之间的数据交互，如下图所示：

![ESP_NOW_multiple_boards_two_way_communication](https://img-blog.csdnimg.cn/img_convert/c27111fbefd99aa0c7e8c57bfdcf7615.png)

当然以上的这些通信，不仅仅限于 ESP32 开发板之间的通信，所有支持 ESP-NOW 的设备之间都可以进行通信，比如 ESP32 与 ESP32 之间、ESP8266 与 ESP8266 之间、甚至 ESP32 与 ESP8266 之间，都可以进行 ESP-NOW 无线通信。

## 实例

下面我们将通过实际程序来介绍如何使用 ESP-NOW 进行通信，此处以 ESP32 为例，其他开发板方法类似。

### 获取设备 MAC 地址

ESP-NOW 是点对点的通讯方式，在发送数据时需要指定接收设备，这好比你给对方发送 QQ 消息必须知道对方的 QQ 号一样。在这里我们一般通过设备的 MAC 地址作为区分不同接收设备的凭证。那什么是 MAC 地址呢？MAC 地址也叫物理地址、硬件地址，每个设备的 MAC 地址在出厂时都是不同的。

下面我们通过 Arduino 代码来获取 ESP32 开发板的 MAC 地址：

```arduino
#include <WiFi.h>

void setup() {
  Serial.begin(9600);
  Serial.println();
#ifdef ESP8266
  Serial.print("ESP8266 Board MAC Address:  ");
  Serial.println(WiFi.macAddress());
#elif defined ESP32
  WiFi.mode(WIFI_MODE_STA);
  Serial.print("ESP32 Board MAC Address:  ");
  Serial.println(WiFi.macAddress());
#endif
}

void loop() {

}
```

上传程序，打开串口监视器，就可获得不同开发板的 MAC 地址：

![获取ESP32的MAC地址](https://img-blog.csdnimg.cn/img_convert/d5b684feff35ae8f0cf479c0fc9e2e14.png)

其中 24:6F:28:88:62:80 就是该 ESP32 开发板的 MAC 地址，该地址由 6 位 16 进制数构成，每一块开发板都有对应独一无二的 MAC 地址。我们记录下这个 MAC 地址，后面会用到。

当然在 ESP-NOW 通信中，不止一块开发板，我们用同样的方式，记录下其他开发板的 MAC 地址。

### ESP-NOW 数据发送

获取到 MAC 地址后，我们先来看看如何编写发送数据的程序。

这里以掌控板为例，分别将掌控板上的光线传感器和声音传感器数据发送到另一块掌控板上。先来看一下完整的程序再进行讲解：

```arduino
#include <WiFi.h>
#include <esp_now.h>

// 设置掌控板声音传感器与光线传感器引脚编号
const int soundPin = 36;
const int lightPin = 39;

// 设置数据结构体
typedef struct struct_message {
  String board_name;
  double light;
  double sound;
} struct_message;

struct_message myData;

// 接收设备的 MAC 地址
uint8_t broadcastAddress[] = {0x24, 0x6F, 0x28, 0x88, 0x62, 0x80};

// 数据发送回调函数
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  char macStr[18];
  Serial.print("Packet to: ");
  snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x",
           mac_addr[0], mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
  Serial.println(macStr);
  Serial.print("Send status: ");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
  Serial.println();
}

void setup() {
  Serial.begin(9600);

  // 初始化 ESP-NOW
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // 设置发送数据回调函数
  esp_now_register_send_cb(OnDataSent);

  // 绑定数据接收端
  esp_now_peer_info_t peerInfo;
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  // 检查设备是否配对成功
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  // 设置要发送的数据
  myData.board_name = "mPython_#1";
  myData.light = analogRead(lightPin);
  myData.sound = analogRead(soundPin);

  // 发送数据
  esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

  // 检查数据是否发送成功
  if (result == ESP_OK) {
    Serial.println("Sent with success");
  }
  else {
    Serial.println("Error sending the data");
  }
  delay(1000);
}
```

该例子演示的是将其中一块 ESP32 开发板（此处以掌控板为例）检测到的数据发送给另一块 ESP32 开发板。

首先在开头引入了 ESP-NOW 相关的头文件：WiFi.h 与 esp_now.h。然后定义了传感器的引脚和一个名为 myData 的结构体，该结构体由 3 个不同数据组成，分别是开发板名称（board_name），光线值（light）与声音值（sound），其中开发板名称为字符串类型，光线值与声音值为浮点型数据。若我们同时有多个传感器数据检测端，可以通开发板名称来区分来自设备的数据。

接着用uint8_t broadcastAddress[] = {0x24, 0x6F, 0x28, 0x88, 0x62, 0x80} 定义了接收设备的 MAC 地址。

除此之外，我们注册了一个 OnDataSent() 的数据发送回调函数，该函数反馈了 ESP-NOW 数据的发送状态，该例子每隔一秒将光线值和声音值发送到指定 MAC 地址的开发板。

在 setup() 中，我们先是初始化了 ESP-NOW 相关的功能，然后设置了发送数据的回调函数、以及绑定了数据接收端的 MAC 地址。

在 loop() 中，我们不断读取光线值和声音值，并将他们赋值给 myData 结构体，然后将它们发送到接收端，并且去判断数据是否发送成功。

### ESP-NOW 数据接收

接下来我们看看接收端的程序如何编写。

编写如下程序，上传到另一块掌控板（前面打印过 MAC 地址的那块掌控板）中。

```arduino
#include <WiFi.h>
#include <esp_now.h>

// 设置数据结构体
typedef struct struct_message {
  String board_name;
  double light;
  double sound;
} struct_message;

struct_message myData;

// 数据接收回调函数
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));
  Serial.print("board_name: ");
  Serial.println(myData.board_name);
  Serial.print("light: ");
  Serial.println(myData.light);
  Serial.print("sound:");
  Serial.println(myData.sound);
  Serial.println();
}

void setup() {
  Serial.begin(9600);

  // 初始化 ESP-NOW
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // 设置接收数据回调函数
  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {

}
```

同样，我们在开头引入了 ESP-NOW 相关的头文件：WiFi.h 与 esp_now.h。然后定义了传感器的引脚和一个名为 myData 的结构体，该结构体由 3 个不同数据组成，分别是开发板名称（board_name），光线值（light）与声音值（sound），与数据发送端定义的一模一样。

我们注册了一个 OnDataRecv() 的数据接收回调函数，该函数反馈了 ESP-NOW 数据的接收状态，当接收到来自其他开发板的消息时，将消息保存到结构体 myData 中，并在串口中打印出接收到的消息。

这里 ESP-NOW 的消息的接收属于无阻塞的接收方式，不受延时函数 delay() 的影响，这意味着 loop() 里面可以执行其他任务而不会影响到板间的通讯，同一块板子既可以当做接收方亦可以当做发送方互不影响。这里可以同时接收来自多块板子的信息，但前提是保持相同的结构体，当然你也可以不用结构体用普通的单一类型的数据类型比如字符串之类的，这里用结构体的原因是需要发送的数据类型有多个，使用结构体相对灵活。

### 实验结果

在两块 ESP32 开发板中分别上传发送和接收的程序，然后打开串口监视器来查看一下效果。

发送端串口监视器如下图：

![发送端数据效果](https://img-blog.csdnimg.cn/img_convert/d9a5c7d752c55d48ca76377c2c27b6cb.png)

接收端串口监视器如下图：

![接收端数据效果](https://img-blog.csdnimg.cn/img_convert/f7c264ed333e8f482a0a4d134c4232aa.png)

可以看到发送端设备和接收端设备都正常运行，并且在串口中输出了相应的信息。

## 小结

至此，ESP-NOW 的简单应用已经讲完了，我们又学了一种新的无线通信方式。上面只是简单演示了一对一数据发送和接收的示例，其实一对多、多对一、多对多的数据发送和接收也是一样的道理，只需增加相应的代码即可。

你可以试试将教程里的数据发送时间间隔改小一点，看看 ESP-NOW 速度究竟有多快。在以后的项目中，如果需要大量运用 ESP 系列开发板时，可以借助 ESP-NOW 技术可以让所有的 DIY 项目有机的联系起来，从而实现真正的万物相连，这个具体的应用我们将在以后的学习中逐步为大家进行讲解。
