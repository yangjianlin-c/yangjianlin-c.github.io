title: Flotherm中加入热管模型后收敛困难
date: 2018/6/11
---

## Flotherm中加入热管模型后收敛困难。

热管具有非常高的有效导热率。因此，当涉及使用温度变量收敛时，可能产生问题。

为避免这些问题，建议用户：

使用双精度求解器（double precision solver “求解器控制”选项卡）
使用“共轭残差”选项（conjugate residual “求解器控制”选项卡）

将温度的错误时间步长增加~x20（在“求解器控制”选项卡下）

使用环境变量FLOMAXITFORTEMP
定义新的环境变量FLOMAXITFORTEMP并将其设置为等于任何值

### Collapsed object

Radiation is calculated based on the temperature difference between objects. Therefore for the software to compute these temperature differences it must know the temperatures of the objects partaking in the Radiative exchange. In fixed temperature cuboids (collapsed or uncollapsed) the temperature of the object is explicitly set. Therefore these objects partake in Radiation but can only pass heat to other objects cooler than themselves. They cannot become warmer or cooler because their temperature is fixed by you. Objects set to have a fixed heatflow give out energy to the neighbouring grid cells but do not have a temperature calculated within them. Therefore there is insufficient data for the software to compute its radiation calculation and therefore they will not partake in the radiative exchange. Collapsed objects can only take part in the radiation calculation if they are set to be fixed temperature. If set to be conducting they cannot take part in the radiation calculation because they don't have grid-cells within them to store the temperature data.

Note: These objects will all act as obstructions to radiation, inhibitting the view factor between other radiating objects.

### Open Domain

运行辐射模型时，开放边界如何影响辐射传输？是否计算出交换因子？什么是辐射温度？

- All radiating geometry inside the domain will radiate towards “infinity outside the domain”, the domain boundaries.
- Therefore exchanges factor are calculated.
- Domain boundaries are ideally “black”.
- Radiation is always a two-way process. Hence, if the radiation temperature of the domain boundary is higher than the body temperatures inside there will be a positive net radiation heat flow into the domain and heat will be added. If the radiation temperature is lower than the body temperatures heat will be extracted from the system.
- The temperature used to calculate the radiation of each domain boundary is set in the Project Manager in

o   [Model Setup] – Default Radiant Temperature

- Ambient Attributes may be used to overwrite the above settings with Radiation Temperature other than the Default Radiant Temperature. You may use different Ambient Attributes for different sides and hence different Radiation Temperatures on different sides of the domain.
- Domain boundaries which are set to “Symmetry” are adiabatic. To prevent violation of the energy conservation, one side will be opened to radiation transfer (but only for radiation transfer!) automatically. In this case there will be a warning displayed in the Message Window.

- 域内的所有辐射几何体都将向“域外无限域”（域边界）辐射。
- 因此计算交换因子。
- 域边界理想地是“黑色”。
- 辐射始终是一个双向过程。因此，如果畴边界的辐射温度高于体内的体温，则将有正的净辐射热流进入区域并且将加热。如果辐射温度低于体温，则将从系统中提取热量。
- 用于计算每个域边界辐射的温度在项目中设置[Model Setup] – Default Radiant Temperature

- 环境属性可用于使用除默认辐射温度之外的辐射温度覆盖上述设置。您可以针对不同侧面使用不同的环境属性，从而在域的不同侧面上使用不同的辐射温度。
- 设置为“对称”的域边界是绝热的。为了防止违反节能措施，一方将自动开放辐射传输（但仅用于辐射传输！）。在这种情况下，消息窗口中将显示警告。



## 求解

Insufficient Memory < Exchange Factor Calculation performed abnormal exit >
The total radiating faces is above the limit.

The number of radiating faces is limitating to 120000 radiating faces by default. If the number of radiating surfaces exceeds this value, an exception is thrown and the EFG aborted.

To increase the number of radiating faces using Environment variable, you can set

System environment variable: EFGFACELIMIT 
System environment value: Number

When the calculation is done, the number of radiating faces can be found on the first line of the following file: BaseSolution\Exchange\facelist (Open with Wordpad)