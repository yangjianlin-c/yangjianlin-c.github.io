
## 一、编码器简介

编码器一般分为霍尔式的和光栅式的编码器，我这里使用的式SIQ-02FVS3这种迷你编码器，和EC11的驱动方法差不多，但是这种编码器体积比较小，但是价格比价贵。下面是编码器的实物图。SIQ-02FVS3还带有按压按键，实现多功能。

![[Pasted image 20230211122538.png]]

那么我们该怎样去使用这个编码器呢，从给出的数据手册上面我们看到一个波形，我们就是通过这个波形去判断编码器是否转动以及编码器转动的方向，可以从图中可以看出当从CW方向转动的时候，A的波形上升沿比B波形的上升沿快，具体快多少，这里数据手册给出24±3°，当从CCW方向转动的这个时候恰好相反，B的相位上升沿快于A的上升沿。这样可以通过捕获上升沿的顺序来判断编码器的方向。

![[Pasted image 20230211122604.png]]

了解编码器的工作机制以后我们就可以有以下几种方法实现编码器的状态捕获，以CW方向为例。

1、当检测到A项上升沿的时候，检测B项的状态，可以A上升沿中断，在中断中检测B的电平状态。
2、同时检测A、B项的上升沿，然后根据上升沿的顺序判断方向。
3、可以捕获一个项(例如A项)的边沿，然后判断A项第一个边沿中断时候获取B和A项的电平，再第二个边沿触发中断的时候捕获B和A项的电平，根据两次捕获B和A项的值就可以知道旋转的方向。

## 二、硬件设计

硬件设计值得注意的是使用中断的方式检测的话，硬件上最好使用0.1uF的滤波电容滤波，不然转动的时候就会出现一些毛刺出发中断，要么就使用软件滤波，但是比较麻烦，检测两次上升沿的间隔时间来判断时候接收处理中断信号的有效值。

以下两张图片是通过逻辑分析仪捕捉到转转时候的电平，第一张看起来不错有中断比较明显，但是通过放大以后发现第二张图中就有毛刺，这个是没有硬件滤波的电路。


原理图

![[Pasted image 20230211122723.png]]

## 三、实现代码

我这里使用的是第三种方法实现对编码器状态的捕获的，加上硬件的滤波，目前用起来是比较准确的，使用队列在中断中将数据发送出去。从第三种情况来看捕获边缘有两种情况，以A边缘中断,然后在A中断中捕获A、B的状态。两种情况。

CW方向为例，第一次捕获A项的的边缘位上升沿，此时A = 1，B = 0；那么第二次就必须捕获下降沿，A = 0，B = 1。假如A第一次没有在边沿捕获到上升沿的时候，捕获的是下降沿，第二次就一定捕获到上升沿。CCW方向也是如此的，这样我们就判断这四种情况，其他的都不用管，这样可以过滤掉干扰，从而实现更准确的控制。

Encoder.c文件

```C
#include "Encoder.h"
#define ESP_INTR_FLAG_DEFAULT 0

xQueueHandle encoder_gpio_event_queue = NULL;   //编码器队列
static unsigned int Value_count = 0;            //状态计数
static int Encoder_A_Last_Value = 0;            //第一次A项的值
static int Encoder_B_Last_Value = 0;            //第一次B项的值
static int Encoder_A_Value = 0;                 //第二次A项的值
static int Encoder_B_Value = 0;                 //第二次B项的值
#define TAG "Encoder"
/*****************************************
 * @brief GPIO中断处理
 * @author wsp
 * @date  2022-2-21
 * ***************************************/
static void IRAM_ATTR encoder_gpio_isr_handler(void * arg)
{
    uint32_t GPIO_Queue_Data = 0;       //发送队列变量
    if(Value_count == 0){               //边缘计数值，计数两次边缘值
        Encoder_A_Last_Value = gpio_get_level(Encoder_A);   //捕获A项的值
        Encoder_B_Last_Value = gpio_get_level(Encoder_B);   //捕获B项的值
        Value_count  = 1;               //开始第一次计数
    }else if(Value_count == 1){         //完成一个边缘捕获
        Encoder_A_Value = gpio_get_level(Encoder_A);        //捕获A项的值
        Encoder_B_Value = gpio_get_level(Encoder_B);        //捕获B项的值
        //状态判断处理
        if(((Encoder_A_Last_Value == 0 && Encoder_A_Value == 1) && (Encoder_B_Last_Value == 1 && Encoder_B_Value == 0)) || ((Encoder_A_Last_Value == 1 && Encoder_A_Value == 0) && (Encoder_B_Last_Value == 0 && Encoder_B_Value == 1))){        //顺时针旋转
            GPIO_Queue_Data = 1;        //右一
        }else if(((Encoder_A_Last_Value == 0 && Encoder_A_Value == 1) && (Encoder_B_Last_Value == 0 && Encoder_B_Value == 1)) || ((Encoder_A_Last_Value == 1 && Encoder_A_Value == 0) && (Encoder_B_Last_Value == 1 && Encoder_B_Value == 0))){  //逆时针旋转
            GPIO_Queue_Data = 2;        //左二
        }
        Encoder_B_Last_Value = 2;       //清除状态值，不初始化0原因是在全局第一次初始化就是0，为了区别
        Encoder_A_Last_Value = 2;       //清除状态值
        Value_count  = 0;               //清除状态值
    }
    if(GPIO_Queue_Data != 0)            //状态改变的时候 发送队列
        xQueueSendFromISR(encoder_gpio_event_queue, &GPIO_Queue_Data, NULL);  
}
/*****************************************
 * @brief 编码器初始化
 * @author wsp
 * @date  2022-2-21
 * ***************************************/
void Encoder_init(void)
{
    gpio_config_t io_conf;                                  //配置GPIO结构体
    io_conf.intr_type = GPIO_INTR_DISABLE;                  //不使能GPIO中断
    io_conf.mode = GPIO_MODE_INPUT;                         //GPIO输入模式
    io_conf.pull_down_en = 0;                               //下拉使能
    io_conf.pull_up_en = 1;                                 //上拉不使能
    io_conf.pin_bit_mask = Encoder_CHB_GPIO_INPUT_PIN_SEL;  //GPIO输入引脚选择
    gpio_config(&io_conf);                                  //配置IO参数

    io_conf.intr_type = GPIO_INTR_ANYEDGE;                  //边沿触发中断
    io_conf.pin_bit_mask = Encoder_CHA_GPIO_INPUT_PIN_SEL;  //GPIO输入引脚选择
    gpio_config(&io_conf);                                  //配置IO参数

    io_conf.intr_type = GPIO_INTR_DISABLE;                  //不使能GPIO中断
    io_conf.pin_bit_mask = Encoder_KEY_GPIO_INPUT_PIN_SEL;  //GPIO输入引脚选择
    gpio_config(&io_conf);                                  //配置IO参数

    gpio_install_isr_service(ESP_INTR_FLAG_DEFAULT);        //安装GPIO中断服务
    gpio_isr_handler_add(Encoder_A,encoder_gpio_isr_handler,(void * )Encoder_A);//添加中断服务    
    
    encoder_gpio_event_queue = xQueueCreate(1,sizeof(uint32_t));                //创建队列
}
void Encoder_Test(void)
{
    char Capure_Enconder_State = 0;
    while(1){
        //获取队列信息
        if (pdTRUE == xQueueReceive(encoder_gpio_event_queue, & Capure_Enconder_State, (portTickType)portMAX_DELAY)){
            printf("Capure_Enconder_State:%d\n\r",Capure_Enconder_State);
        }
    }   
}
```

Encoder.h文件

```c
#ifndef _Encoder_H_
#define _Encoder_H_
#include "lvgl/lvgl.h"
#include <stdio.h>
#include "lv_port_indev_Key.h"
#include "lvgl_function.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/ledc.h"
#include "esp_err.h"
#include "sdkconfig.h"

#define     Encoder_A     34    //编码器通道一
#define     Encoder_B     35    //编码器通道二
#define     Encoder_K     13    //编码器按键通道

#define     Encoder_CHA_GPIO_INPUT_PIN_SEL      ((1ULL<<Encoder_A))
#define     Encoder_CHB_GPIO_INPUT_PIN_SEL      ((1ULL<<Encoder_B))
#define     Encoder_KEY_GPIO_INPUT_PIN_SEL      ((1ULL<<Encoder_K))

extern xQueueHandle encoder_gpio_event_queue;
void Encoder_init(void);
void Encoder_Test(void);
#endif
```

main函数

```c
void app_main(void)
{
    Encoder_init();
    Encoder_Test();
}

```


## 四、显示结果

最后的显示结果是相当的准确的，不会出现快速转动的时候出问题。

![[Pasted image 20230211122934.png]]


————————————————
版权声明：本文为CSDN博主「请叫我啸鹏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/believe666/article/details/123635445