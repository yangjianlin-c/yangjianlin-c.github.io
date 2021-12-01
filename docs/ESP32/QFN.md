---
title: QFN Package
---

QFN封装散热

<!--more-->

测试板遵循标准

- JESD 51-3 ，1S0P 只有一个信号层，无内部金属层
- JESD 51-5 ，1S2P有两个内部金属层和将上层连接到导热垫的散热过孔。 过孔直径为0.30mm，中心距中心为1.2mm。 允许过孔仅填充由散热垫周边界定的区域，并且不能超出周界。 这被称为直接附加方法。
- JESD 51-7，1S2P，和JESD 51-5 有两层金属内层，但没有过孔。

这些标准允许背面有信号线层 (2S2P or 2S0P)，但影响比较小(<2%) 。

20-Pin QFN 无风环境下热阻模拟值：

| 测试标准                              | θJA (°C/W) | θJC (°C/W) | θJP (°C/W) | θJB (°C/W) |
| ------------------------------------- | ---------- | ---------- | ---------- | ---------- |
| JESD 51-5 (1S2P Direct-Attach Method) | 29.9       | 15.2       | 0.52       | 5.2        |
| JESD 51-7 (1S2P)                      | 46.8       | 15.2       | -          | 8.7        |
| JESD 51-3 (1S0P)                      | 77.5       | 15.2       | -          | -          |

NOTES: 

- θJB is neither applicable nor defined for JESD 51-3 test cards.
- θJP is junction-to-pad thermal impedance.  