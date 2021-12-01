# ESP32 使用MQTT

```flow
op1=>operation: 生成实例 
wiFiclient, wifi实例
PubSubclient, MQTT实例

op2=>operation: 初始化
setup_wifi()
client.setserver()
client.setcallback()

cond=>condition: 连接到
MQTT服务器?
c1=>operation: 重新连接
订阅主题
c2=>operation: client.loop()

pb=>operation: 发布主题

op1->op2->cond
cond(yes)->c2
cond(no)->c1->c2
c2->pb(left)->cond
```



关于MQTT的几个操作：

- `client.loop()` 会更新状态，执行callback函数的内容
- 连接服务器 `client.connect(clientID)`
- 订阅主题 `client.subscribe(topic_A)`
- 发布主题 `client.publish(topic_B, “内容”)`
- 接收到的内容处理 `callback(topic, payload, length)`



## 连接阿里云MQTT

TCP直连：Client ID中`securemode=3`，无需设置SSL/TLS信息。



|                | 阿里云                                                       |
| -------------- | ------------------------------------------------------------ |
| Broker Address | 连接域名。格式：`${YourProductKey}.iot-as-mqtt.${region}.aliyuncs.com`。其中，${region}需替换为您物联网平台服务所在地域的代码。地域代码，请参见[地域和可用区](https://www.alibabacloud.com/help/zh/doc-detail/40654.htm#concept-h4v-j5k-xdb)。如：`alxxxxxxxxxx.iot-as-mqtt.cn-shanghai.aliyuncs.com`。 |
| Broker Port    | 1883                                                       |
| Client ID      | 填写mqttClientId，用于MQTT的底层协议报文。格式固定：`${clientId}|securemode=3,signmethod=hmacsha1|`。完整示例：`12345|securemode=3,signmethod=hmacsha1|`。其中，${clientId}为设备的ID信息。可取任意值，长度在64字符以内。建议使用设备的MAC地址或SN码。securemode为安全模式，TCP直连模式设置为`securemode=3`，TLS直连为`securemode=2`。signmethod为算法类型，支持hmacmd5和hmacsha1。 |
| User Name | 由设备名DeviceName、符号（&）和产品ProductKey组成。固定格式：`${YourDeviceName}&${YourPrductKey}`。完整示例如：`device&alxxxxxxxxxx`。 |
| Password  | 密码由参数值拼接加密而成。手动生成方法如下：拼接参数。提交给服务器的**clientId**、**deviceName**、**productKey**和**timestamp**（timestamp为非必选参数）参数及参数值依次拼接。本例中，**clientId**值为12345，**deviceName**值为device，**productKey**值为alxxxxxxxxx，拼接结果为：`clientId12345deviceNamedeviceproductKeyalxxxxxxxxx`加密。通过**Client ID**中确定的加密方法，使用设备**deviceSecret**，将拼接结果加密。假设设备的**deviceSecret**值为abc123，加密计算格式为`hmacsha1(abc123,clientId12345deviceNamedeviceproductKeyalxxxxxxxxxx)` |







```c++
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#include "aliyun_mqtt.h"

// GPIO 13, D7 on the Node MCU v3
#define SENSOR_PIN 13

#define WIFI_SSID "iPhone"
#define WIFI_PASSWD "12345678"

#define PRODUCT_KEY "a1dFPZBlZKe"
#define DEVICE_NAME "ESP32"
#define DEVICE_SECRET "YvhVGrIFI3qTcS6wM7n4IDC14ba0jNpq"


#define ALINK_BODY_FORMAT "{\"id\":\"123\",\"version\":\"1.0\",\"method\":\"%s\",\"params\":%s}"
#define ALINK_TOPIC_PROP_POST "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post"
#define ALINK_TOPIC_PROP_POSTRSP "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post_reply"
#define ALINK_TOPIC_PROP_SET "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/service/property/set"
#define ALINK_METHOD_PROP_POST "thing.event.property.post"

unsigned long lastMs = 0;

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void initWifi(const char *ssid, const char *password)
{
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.println("WiFi does not connect, try again ...");
        delay(3000);
    }

    Serial.println("Wifi is connected.");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void callback(char *topic, byte *payload, unsigned int length)
{
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    payload[length] = '\0';
    Serial.println((char *)payload);

    // if (strstr(topic, ALINK_TOPIC_PROP_SET))
    // {
    //     StaticJsonBuffer<100> jsonBuffer;
    //     JsonObject &root = jsonBuffer.parseObject(payload);
    //     if (!root.success())
    //     {
    //         Serial.println("parseObject() failed");
    //         return;
    //     }
    // }
}

void mqttCheckConnect()
{
    while (!connectAliyunMQTT(mqttClient, PRODUCT_KEY, DEVICE_NAME, DEVICE_SECRET))
    {
    }

    Serial.println("MQTT connect succeed!");
    // client.subscribe(ALINK_TOPIC_PROP_POSTRSP);
    mqttClient.subscribe(ALINK_TOPIC_PROP_SET);
    Serial.println("subscribe done");
}

void mqttIntervalPost()
{
    char param[32];
    char jsonBuf[128];

    sprintf(param, "{\"MotionAlarmState\":%d}", digitalRead(13));
    sprintf(jsonBuf, ALINK_BODY_FORMAT, ALINK_METHOD_PROP_POST, param);
    Serial.println(jsonBuf);
    mqttClient.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
}

void setup()
{

    pinMode(SENSOR_PIN, INPUT);
    /* initialize serial for debugging */
    Serial.begin(115200);

    Serial.println("Demo Start");

    initWifi(WIFI_SSID, WIFI_PASSWD);

    mqttClient.setCallback(callback);
}

// the loop function runs over and over again forever
void loop()
{
    if (millis() - lastMs >= 5000)
    {
        lastMs = millis();
        mqttCheckConnect();

        /* Post */
        mqttIntervalPost();
    }

    mqttClient.loop();

    unsigned int WAIT_MS = 2000;
    if (digitalRead(SENSOR_PIN) == HIGH)
    {
        Serial.println("Motion detected!");
    }
    else
    {
        Serial.println("Motion absent!");
    }
    delay(WAIT_MS); // ms
    Serial.println(millis() / WAIT_MS);
}
```

