---
title: 固态界面材料热特性测量
---

测试标准ASTM-D5470 

![1526264186679](../images/1526264186679.png)

1. 加热板电流$I_H$，待平衡状态

2. 减小加热板电流到$I_S$

3. 计算两种状态下加热二极管的温度差$\Delta T_j$，和加热功率差$\Delta P$。得到整个链路的热阻
   $$
   \theta_{total}=\frac{\Delta T_j}{\Delta P}
   $$
   其中$\theta_{total}$包含测试样品的热阻，测试设备热阻，接触界面热阻。

4. 改变TIM厚度，重复同样测试计算热阻差$\Delta \theta_{total}$，即可得出
   $$
   \Delta \theta_{total}=\Delta \theta_{TIM}
   $$
   测量的厚度差为$\Delta t$。

5. 计算TIM的导热率$k$，thermal conductivity 
   $$
   k=\frac{\Delta \theta_{total}}{\Delta t A}
   $$
   
测试过程完成。

需注意加热二极管总会有一部分热量会从其他途径散发到周围环境中，因此上面的计算中用到的$\Delta P$会存在误差，这部分热量称为寄生损失热量parasitic heat loss。

通过热通量传感器测量寄生热量。
下图显示了总热阻与寄生热量之间的关系。可以看到当测量系统总热阻为15K/W时，大约有28%的热量从其它通道散走。

此关系跟具体测试设备相关，只做参考。
![a](../images/a.png)

文章来源：mentor.com