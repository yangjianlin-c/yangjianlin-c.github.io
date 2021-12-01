---
title: 批处理模式运行FloTHERM
date: 2018-1-18
tags: Flotherm
categories: Thermal
---
有时候我们希望Flotherm能够自动求解多个项目，例如白天建好模型，晚上让其求解。或在笔记本中建好模型，然后送到服务器中求解。这时候就可以使用批处理模式运行FloTHERM。

<!-- more -->

方法很简单，因为flotherm是一个可执行命令。d

1. 在项目文件夹上级目录创建批处理文件xxx.bat

内容如下：

```
@echo off
call "C:\Program Files\MentorMA\flosuite_v12\flotherm\WinXP\bin\flotherm" -b \"ProjectA\"
call "C:\Program Files\MentorMA\flosuite_v12\flotherm\WinXP\bin\flotherm" -b \"ProjectB\"
:end
```

其中，为flotherm的路径，如果找不到可以右键点击Flotherm启动图标，查看属性
![](http://oozvwxvcz.bkt.clouddn.com//18-1-18/97465869.jpg)

ProjectA，ProjectB为项目名称。

2. 双击运行此批处理文件`xxx.bat`即可开始求解。

运行后目录下会生成一个`floerror.log`文件，里面有简单摘要信息，内容与普通求解中Message对话框的内容一样。

剩下的事情就是安心睡觉，一觉到天亮再接着干。

## 中止求解

创建一个名为`stopnow`的空文件，放到目录`<solution_dir>/project_set_dir/DataSets/BaseSolution/`，等待FloTHERM继续求解两步后会终止求解，并删除stopnow文件 。

## 在批处理模式下监控

如果需要在批处理模式下解决问题时检查项目，请检查`logit`文件。该文件位于

```
project_set_dir/DataSets/BaseSolution/PDTemp 
```

`logit`文件中有残差数据记录

如果logit文件的大小在增加，那么这个项目还在解决之中。


## 进阶介绍
如果希望进一步了解flotherm命令，实现更高级的功能可以参考下面内容。

Flotherm命令的格式如下：

flotherm -b|-p project [options] | -env] | [-f floscript]

- -b 批处理模式运行

- -p 交互模式运行

- project 项目名称。项目PDML或FloXML文件的名称。项目名称必须用单引号或双引号，其中\是Dos命令的转义符。

- -i 另一个项目

  将批处理的项目文件之初场设为项目projecta的结果

- -X 只计算项目中的辐射交换系数

- -s 只计算项目中的CFD方程，不计算辐射

- -z pack_filename 将求解的项目导出为压缩文件，以便存档或传输到其他系统。

- -r htmfile 将所有Tables规范和结果数据导出到指定的html文件。

- -C 不但求解批处理中的项目文件，同时求解项目文件所包括的优化Command Center。

  要在解决方案时使用并行处理以及Command Center项目的基本情况，必须使用CCNUMBERTHREADS环境变量（忽略“用户首选项”对话框中的处理器数量设置）指定处理器的数量。使用FLOVOLUNTEERMAXJOBS环境变量来设置要同时解决的最大项目数量。

- -o output_directory

以CSV文件格式输出表格结果数据到指定的目录output_directory。[表1]列出了输出的可能文件。

表1.结果表输出CSV文件

| 文件名                                      | 描述                    |
| ---------------------------------------- | --------------------- |
| 对于几何表格：                                  |                       |
| collapsed_resistances.csv                | 折叠的阻力                 |
| Component_Fluxes.csv                     | 组件和网络组装节点的导热，对流和辐射热通量 |
| Component_Nodes.csv                      | 组件和网络组装节点的温度          |
| Cooler_smartparts.csv                    | 散热器SmartParts         |
| Cutouts_Overall.csv                      | 剪切和整体解决方案领域           |
| Die_smartparts.csv                       | 模具SmartParts          |
| fans_smartparts.csv                      | 风扇SmartParts          |
| Fixed_Flows_smartparts.csv               | 固定流量SmartParts        |
| Heat_Pipe_smartparts.csv                 | 热管SmartParts          |
| input_geometry.csv                       | 几何模型                  |
| Network_Assembly_smartparts.csv          | 网络组件                  |
| Powermap_smartparts.csv                  | Powermap SmartParts   |
| Rack_smartparts.csv                      | Rack SmartParts       |
| Recirculation_smartparts.csv             | 再循环装置SmartParts       |
| TEC_smartparts.csv                       | TEC SmartParts        |
| 对于属性表：                                   |                       |
| Ambient.csv                              | 环境/对象                 |
| Fluid.csv                                | 流体属性                  |
| GridConstraint.csv                       | 网格约束/对象               |
| Material.csv                             | 材料/对象                 |
| Object_Properties.csv                    | 对象/属性                 |
| RadiationProperty.csv                    | 辐射/对象                 |
| ResistanceProperty.csv                   | 电阻/对象                 |
| SourceProperty.csv                       | 源/目的                  |
| SurfaceExchange.csv                      | 表面交换                  |
| SurfaceFinish.csv                        | 表面光洁度/物体              |
| Thermal.csv                              | 热/对象                  |
| TranisentProperty.csv                    | 瞬态属性                  |
| 文件名                                      | 描述                    |
| 对于所有长方体：                                 |                       |
| cubvol_Temperature.csv                   | 长方体名称和温度              |
| 监视点存在时：                                  |                       |
| mon_Density.csv                          | 监视点的密度                |
| mon_DissTurb.csv                         | 在监测点消除湍流              |
| mon_KETurb.csv                           | 监测点的湍流动能              |
| mon_Potential.csv                        | 监视点的电位（焦耳加热开启）        |
| mon_Pressure.csv                         | 监视点的压力                |
| mon_Temperature.csv                      | 监视点的温度                |
| mon_TurbVis.csv                          | 监测点的湍流粘度              |
| mon_XVelocity.csv，mon_YVelocity.csv和mon_ZVelocity.csv | 监视点的速度                |
| 当卷区域存在时：                                 |                       |
| regvol_Bn.csv                            | 卷区域的瓶颈号码              |
| regvol_Density.csv                       | 体积密度                  |
| regvol_DissTurb.csv                      | 体积区域的湍流耗散             |
| regvol_FieldError.csv                    | 错误字段值                 |
| regvol_Generation.csv                    | 动荡的来源                 |
| regvol_KETurb.csv                        | 体积区域的湍流动能             |
| regvol_MagGradT.csv                      | 体积区域的温度梯度             |
| regvol_MagHeatFlux.csv                   | 体积区域的热通量              |
| regvol_MagMassFlux.csv                   | 体积区域的质量流量             |
| regvol_PowerDensity                      | 体积区域的功率密度             |
| regvol_Pressure.csv                      | 压力的地区                 |
| regvol_Sc.csv                            | 卷区域的快捷号码              |
| regvol_SolarViz.csv                      | 无量纲SolarViz标量字段值      |
| regvol_Speed.csv                         | 速度在地区                 |
| regvol_Temperature.csv                   | 体积区域的温度               |
| regvol_TurbVis.csv                       | 体积区域的湍流粘度             |
| regvol_xGradT.csv，regvol_yGradT.csv和regvol_zGradT.csv | 定向温度梯度                |
| regvol_XHeatFlux.csv，regvol_YHeatFlux.csv和regvol_ZHeatFlux.csv | 定向热通量                 |
| regvol_XMassFlux.csv，regvol_YMassFlux.csv和regvol_ZMassFlux.csv | 定向质量流量                |
| regvol_XVelocity.csv，regvol_YVelocity.csv和regvol_ZVelocity.csv | 体积区域的速度               |
| 当平面区域存在时：                                |                       |
| planar_regions.csv                       | 在平面区域上的场结果            |
| 对于所有导电立方体：                               |                       |
| solidcuboid_conduct.csv                  | 长方体通量                 |
| 对于解决方案领域：                                |                       |
| Cutouts_Overall.csv                      | 剪切和整体解决方案领域           |

- -env
  设置运行FloTHERM及其实用程序所需的路径和环境变量，但不运行FloTHERM本身。这取代了可用于早期版本的FloTHERM的安装命令行工具。请注意，当FloTHERM以交互模式运行时，或者从“开始”菜单的“环境外壳”选项打开命令窗口时，将为您设置此环境。

- floscript
  在启动时运行文件floscript，其中floscript是FloSCRIPT文件。

描述

典型的安装将flotherm放入文件夹中：

```
<install_dir>\flosuite_v<version>\flotherm\WinXP\bin\
```

有一个为并发命令行选项定义的优先级规则。-p选项覆盖-b。如果-p  项目选项失败，则加载默认项目。如果指定的批处理项目加载失败，程序将退出。

注意：

如果同时使用-x和-s，程序将在CFD解决方案之前计算辐射交换因子。

默认：省略-x和-s强制程序决定是否在CFD解决方案之前执行辐射交换因子计算。也就是说，如果辐射开启，并且没有一个有效的视角因子，那么将会计算视角因子。

实例：

- 以已经加载的项目myproject交互式启动FloTHERM ：

  ```
  flotherm -p myproject
  ```

  省略-p选项会导致FloTHERM正在使用随软件一起安装的默认项目加载。

- 将结果输出到一个html文件：

  ```
  flotherm -b  \"my project\" -r \"my html file\"
  ```

- 要从FloSCRIPT文件`My_logFile_saved.xml`运行FloTHERM，：

  ```
  flotherm -f \"<install_dir>\flosuite_v<version>\flotherm\WinXP\bin\LogFiles\
  My_logFile_saved.xml\"
  ```

  ​