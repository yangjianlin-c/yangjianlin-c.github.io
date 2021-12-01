# ESP32睡眠

结合ESP32的休眠功能可以达到省电的目的。代码设计主要有两步：

- 进入睡眠模式

- 唤醒

## ESP32睡眠模式

ESP32 几种睡眠模式对比。

|            | Modem-Sleep | Light-Sleep | Deep-Sleep | Hibernation |
| ---------- | ----------- | ----------- | ---------- | ----------- |
| WiFi       | 不活动         | 不活动         | 不活动        | 不活动         |
| Bluetooth  | 不活动         | 不活动         | 不活动        | 不活动         |
| Radio      | 不活动         | 不活动         | 不活动        | 不活动         |
| 外设         | 不活动         | 不活动         | 不活动        | 不活动         |
| ESP32 Core | 活动          | 暂停          | 不活动        | 不活动         |
| ULP协处理器    | 活动          | 活动          | 活动         | 不活动         |
| RTC        | 活动          | 活动          | 活动         | 活动          |

### Modem-Sleep

在Modem-Sleep模式下，CPU 供电，ESP32 根据 WiFi 通信的使用情况在主动模式和调制解调器睡眠模式之间切换。切换是自动完成的，CPU 频率也会自动更改，具体取决于 CPU 负载和外围设备的使用。

由于ESP32会**自动**进入modem-sleep模式，因此没有Arduino功能可以进入该模式。

这就是说在没有使用Wifi，蓝牙功能时，ESP32会将其自动关闭，以达到省电的目的。不需要用户干预。

### Light-Sleep

light-sleep 模式下 ESP32 Core暂停。这意味着大部分 RAM 和 CPU 都遵循睡眠模式。在这种模式下，内部触发器不会切换状态，因为这种切换会消耗功率。

在轻度睡眠模式下，WiFi 基带被禁用，但 WiFi 连接本身保持活动状态。

### Deep-Sleep模式

在浅睡眠模式下，ESP32 Core 暂停并遵循睡眠模式，而在深度睡眠电源模式下，ESP32 Core 完全不活动。只有 ULP 协处理器和 RTC 保持活动状态。

在深度睡眠模式下，WiFi 连接不活跃，但 WiFi 配置数据存储在实时时钟的内存中。因此，ESP32 从深度睡眠模式唤醒后重新建立 WiFi 连接非常快。

### Hibernation模式

休眠电源模式是电流消耗最低的电源模式。空白的 ESP32 微控制器仅消耗 5μA。内部 8 MHz 振荡器和 ULP 协处理器被禁用，RTC 恢复存储器断电。慢速时钟上只有一个 RTC 定时器和某些 RTC GPIO 处于活动状态。RTC 定时器或 RTC GPIO 可以将芯片从休眠模式唤醒。

## 进入休眠状态

使ESP32进入休眠状态的代码很简单：

```arduino
esp_light_sleep_start(); //进入Light-Sleep模式
esp_deep_sleep_start(); //进入Deep-Sleep模式
esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_OFF); //停用所有 RTC 外设，即进入Hibernation模式
```

## 睡眠唤醒

ESP32睡眠后，有多种唤醒方式。

```arduino
esp_sleep_enable_ulp_wakeup();
esp_sleep_enable_timer_wakeup(uint64_t time_in_us);
esp_sleep_enable_touchpad_wakeup();
esp_sleep_enable_ext0_wakeup(gpio_num_t gpio_num, int level);
esp_sleep_enable_ext1_wakeup(uint64_t mask, esp_sleep_ext1_wakeup_mode_t mode);
esp_sleep_enable_gpio_wakeup();
esp_sleep_enable_uart_wakeup();
```

### ULP 协处理器唤醒唤醒

唤醒代码：

```arduino
esp_sleep_enable_ulp_wakeup();
```

ULP 协处理器可以在芯片处于睡眠模式时运行，并且可以用于轮询传感器，监视 ADC 或触摸传感器值，并在检测到特定事件时唤醒芯片。

### 定时器唤醒

唤醒代码：

```arduino
esp_sleep_enable_timer_wakeup(uint64_t time_in_us);
```

在预定义的时间后唤醒芯片。时间以微秒精度指定。

因为ESP32 是32位MCU，所以它的最大睡眠时间是32位的整数，即0xFFFF FFFF 或 4294967295 毫秒，约71分钟。

### Touch pad唤醒

唤醒代码：

```arduino
esp_sleep_enable_touchpad_wakeup();
```

### External 唤醒(ext0)唤醒

唤醒代码：

```arduino
esp_sleep_enable_ext0_wakeup(gpio_num_t gpio_num, int level);
```

* gpio_num: GPIO number used as wakeup source. Only GPIOs which are have RTC functionality can be used: 0,2,4,12-15,25-27,32-39.

* level: input level which will trigger wakeup (0=low, 1=high)

当 GPIO 的电平为预定义的逻辑电平时触发唤醒。必须使用有RTC功能的GPIO: 0,2,4,12-15,25-27,32-39.

### External 唤醒(ext1)唤醒

唤醒代码：

```arduino
esp_sleep_enable_ext1_wakeup(uint64_t mask, esp_sleep_ext1_wakeup_mode_t mode);
```

使用多个GPIO 触发唤醒。

- mask。bit mask of GPIO numbers。必须使用有RTC功能的GPIO: 0,2,4,12-15,25-27,32-39.

- mode。可选项项：
  
  - ESP_EXT1_WAKEUP_ALL_LOW: 所有选定的引脚都为低电平，则唤醒
  
  - ESP_EXT1_WAKEUP_ANY_HIGH: 任何所选引脚为高电平，则唤醒

### GPIO 唤醒(仅 light sleep)

除了上面描述的 EXT0 和 EXT1 唤醒源之外，在轻度睡眠模式下还有一种从外部输入唤醒的方法。通过该唤醒源，每个引脚可以单独使用 gpio_wakeup_enable() 函数配置为高电平或低电平唤醒。与 EXT0 和 EXT1 唤醒源（只能与 RTC IO 一起使用）不同，此唤醒源可用于任何 IO（RTC 或数字）。

esp_sleep_enable_gpio_wakeup() 函数可用于启用此唤醒源。

### UART 唤醒(仅 light sleep)

当 ESP32 从外部设备接收 UART 输入时，通常需要在输入数据可用时唤醒芯片。UART 外设包含一项功能，当看到 RX 引脚上的一定数量的上升沿时，可以将芯片从轻度睡眠状态唤醒。可以使用 uart_set_wakeup_threshold() 函数设置此上升沿数。请注意，唤醒后 UART 不会接收触发唤醒的字符（及其前面的任何字符）。 这意味着外部设备通常需要在发送数据之前向 ESP32 发送额外字符以触发唤醒。

esp_sleep_enable_uart_wakeup() 函数可用于启用此唤醒源。

## RTC外设和存储器掉电

默认情况下，esp_deep_sleep_start() 和 esp_light_sleep_start() 函数将关闭所有启用的唤醒源不再需要的 RTC 电源域。要覆盖此行为，请提供 esp_sleep_pd_config() 函数。

注意：在 ESP32 的版本 0 中，RTC 快速存储器将始终在深度睡眠中保持启用状态，以便深度睡眠存根可以在复位后运行。 如果应用程序在深度睡眠后不需要干净的重置行为，则可以覆盖此项。

如果程序中的某些变量放入RTC慢速存储器（例如，使用 RTC_DATA_ATTR 属性），RTC 慢速存储器将默认保持通电状态。 如果需要，可以使用 esp_sleep_pd_config() 函数覆盖它。

## 实例：ESP32 深度睡眠程序代码

```arduino
#define uS_TO_S_FACTOR 1000000  /* Conversion factor for micro seconds to seconds */
#define TIME_TO_SLEEP  5        /* Time ESP32 will go to sleep (in seconds) */

void print_wakeup_reason(){
  esp_sleep_wakeup_cause_t wakeup_reason;
  wakeup_reason = esp_sleep_get_wakeup_cause();

  switch(wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_IO"); break;
    case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
    default : Serial.printf("Wakeup was not caused by deep sleep: %d\n",wakeup_reason); break;
  }
}

void setup(){
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }

  print_wakeup_reason(); //Print the wakeup reason for ESP32

  delay(5000);

  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR); // ESP32 wakes up every 5 seconds

  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_ON); // all RTC Peripherals are powered

  Serial.println("Going to deep-sleep now");
  Serial.flush(); 
  esp_deep_sleep_start();
}

void loop(){
}
```

深度睡眠电源模式从函数`esp_deep_sleep_start`开始。

每次微控制器从深度睡眠模式唤醒时，ESP32 都会启动 setup 函数，所以我们在 setup 函数中定义了我们所有的代码，不使用循环函数。

对于深度睡眠模式，我们可以定义所有 RTC 外设是活动还是断电。在睡眠配置文件中，我们定义 RTC IO、传感器和 ULP 协处理器等 RTC 模块保持活动状态。

如果将睡眠配置文件更改为：

```arduino
esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_OFF);
```

就将进入Hibernation模式。

## 增加睡眠时间以降低功耗

我们从上一章中获得了两个重要的见解，这有助于我们进一步降低整个 ESP32 项目的功耗。

1. 建立WiFi连接并通过WiFi发送数据具有非常高的功耗
2. 在深度睡眠或休眠模式下，ESP32 的功耗显著降低。

因此，如果精确规划各个阶段（唤醒、通过 WiFi 发送数据、睡眠），则可以降低功耗。

下表列出两种开发板在各种状态下的电流，供参考。

|                  | Reference [mA] | Light-Sleep [mA] | Deep-Sleep [mA] | Hibernation [mA] |
| ---------------- | -------------- | ---------------- | --------------- | ---------------- |
| ESP32 – DevKitC  | 51             | 10               | 9               | 9                |
| FireBeetle ESP32 | 39             | 1.94             | 0.011           | 0.008            |

![loading-ag-1204](.\images\e1613c426304ea9767a57ab7a363d266b68c9222.svg)

以气象站为例，可以清楚地描述各个阶段：

ESP32 连接到 DHT22 温度和湿度传感器。如果我们每 10 秒传输一次温度和湿度，功耗将不必要地高，因为传输的测量值大多相同。

可以通过每 10 分钟而不是每 10 秒传输读数来降低功耗。有了这个，我们延长了绵羊时间。为了减少 WiFi 连接的数量，每次从睡眠模式唤醒时，可以将当前传感器值与上次发送的值进行比较，只有在温度或湿度发生变化时才通过 WiFi 发送新数据。

要在睡眠模式下存储变量，它们必须加载到 RTC 内存中，在 ESP32 上只有 8kB。您只需在变量前添加*RTC_DATA_ATT 即可*。

```arduino
RTC_DATA_ATT int temperature;
RTC_DATA_ATT int humidity;
```
