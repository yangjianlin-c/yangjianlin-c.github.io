# 关于风扇

## 风扇被挡住有什么影响

风扇如果被挡住将影响将使通过风扇的空气流量减小。

对于轴流风扇：

- 风扇的出风口被挡住，会减小流量，但风扇压力不会显著增加。
- 风扇的入风口被挡住，风扇产生的流量和压力均会下降。

如果系统压力非常大，接近风扇的最大静压力，将增加风扇的负担，影响使用寿命。

## 如何模拟风扇失效

在风扇设置面板中讲风扇设置为Failed

![Zoom in](https://support.sw.siemens.com/kbassets/external/MG584750/images/zoomedin.JPG)

## 风扇结果Table中风扇的功率与输入功率不等

首先需明白在风扇参数定义中定义的功率为风扇的电功率$P_{fan}$。

第一，如果设置了风扇的Derating factor，风扇的功率会降额：

$$
P_{fan~Derating}=P_{fan}\times (Derating~factor)^3
$$

第二，风扇的电功率一部分转换为机械能，其它部分才转换为热量。FloTHERM会根据PQ曲线计算风扇的机械效率 $\eta$，风扇的热耗$Q_{fan}$为

$$
Q_{fan}=P_{fan~Derating}\times \eta
$$

这样就不难理解结果Table中各项的含义了

![Fan efficiency](https://support.sw.siemens.com/kbassets/external/MG555847/images/fan_power_tables.png)

风扇的机械能$E$是通过计算风扇出口入口的空气总压力差得到的：

$$
E = (P_{total,outlet} - P_{total,inlet} )
$$

其中，总压力 $P_{total}$ 的计算方式：

$$
P_{total}= P_{static}+ 0.5(\rho v^2)
$$

其中 $v$ 为风扇出口处的平均风速。

## 风扇结果Table中的温度代表什么含义

代表的是风扇入口处的平均温度。

风扇的工作温度会影响风扇的使用寿命，通常风扇厂家会规定风扇的工作温度。

有时候如果风扇自身的功率比较大，可能入口处的温度不能代表风扇hub的温度，这时可以通过截面图，或添加温度监控点，检查风扇hub的温度。

## 带风扇的模型求解后发散

风扇发散有几个潜在的原因：

- 初始流量过高。
- 风扇周围的网格太粗糙。
- 扇形曲线包含的点数不足，变化过于急剧，水平线。如下图风扇的PQ曲线有比较平坦的区域，如果风扇刚好工作在此区域，可能会出现求解振荡的问题，如下图

![Non-linear fan curve](https://support.sw.siemens.com/kbassets/external/MG552644/images/fan-curve.png)

而且观察风扇附近监控点也会有振荡的问题。

![Flat lined residuals](https://support.sw.siemens.com/kbassets/external/MG552644/images/fan_oscillating.png)

可以尝试减小Solver Control中的Fan Relaxation，默认值为1.0，减小到0.7或0.5试试。减小Fan Relaxation会让求解器沿着风扇曲线采取更小的步长移动。如下图，将风扇的Relaxation系数从1.0调整为0.7后求解开始收敛。

![Fan relaxation](https://support.sw.siemens.com/kbassets/external/MG552644/images/fan_oscillating_resolved2.png)

- 风扇曲线中使用了错误的单位。
- 风扇出口，入口被挡住

检查原因：

- 暂停求解，查看风扇的工作点，如果风扇工作的不在PQ曲线上，说明风扇不收敛。
  
  ![Operating point not on Fan curve](https://support.sw.siemens.com/kbassets/external/MG585909/images/1-OperatingPoint1.jpg)

- 创建显示压力/速度的平面图，检查压力/速度梯度。

- 将平面的填充类型从“插值”更改为“单元格填充”。

- 检查风扇周围的标量场

- 尝试“放松”风扇：在 [Solver Control] 中，将风扇松弛设置为 0.7。重新初始化并重新运行。如果解仍然发散（可能迭代次数较多），将其降低到 0.5，最大为 0.3。不建议使用小于0.3。

## swirl

https://support.sw.siemens.com/kbassets/external/MG575744/files/10443.pdf

https://support.sw.siemens.com/kbassets/external/MG575828/files/10539.pdf

reinitialize, then the file is local in
`project dir\ DataSets\BaseSolution\msp_x\PDTemp`
