# 批处理模式运行Flotherm

有时候我们希望Flotherm能够自动求解多个项目，例如白天建好模型，晚上让其求解。或在笔记本中建好模型，然后送到服务器中求解。这时候就可以使用批处理模式运行Flotherm。

方法很简单，Flotherm是一个可执行命令。

!!! tip

    在运行批处理命令前，需要检查所有模型中是否有错误。用Flotherm打开项目，并执行sanity check，然后 re-initialize 项目，然后可退出Flotherm。

## 创建批处理命令

在项目文件夹上级目录创建批处理文件xxx.bat

内容如下：

```
@echo off
call "C:\Program Files\MentorMA\flosuite_v2021.1\flotherm\WinXP\bin\flotherm" -b \"ProjectA\"
call "C:\Program Files\MentorMA\flosuite_v2021.1\flotherm\WinXP\bin\flotherm" -b \"ProjectB\"
:end
```

其中，`C:\Program Files\MentorMA\flosuite_v12\Flotherm\WinXP\bin\Flotherm`为Flotherm的安装路径，如果找不到可以右键点击Flotherm启动图标，查看属性找到相应的路径。
![image-20220104143458954](http://cdn.mekesim.com/assets/image-20220104143458954.png)

ProjectA，ProjectB为项目名称。如果不确定项目名称是什么，可以打开文件`group.cat`找到正确的项目名称。

双击运行此批处理文件`xxx.bat`即可开始求解。

运行后目录下会生成一个`floerror.log`文件，里面有简单摘要信息，内容与普通求解中Message对话框的内容一样。

剩下的事情就是安心睡觉，睡到自然醒再接着干。

如果求解完成，当再打开Flotherm load项目界面时，对应项目的图标会变成彩色的，表示已经有求解结果了。

![image-20220104150944614](http://cdn.mekesim.com/assets/image-20220104150944614.png)

## 中止求解

创建一个名为`stopnow`的空文件，放到目录`project_set_dir/DataSets/BaseSolution/`，Flotherm继续求解两步后会终止求解，然后就可以删除`stopnow`文件 。

## 在批处理模式下查看收敛情况

如果需要在批处理求解模式下查看项目收敛情况，可以检查`logit`文件。该文件位于`project_set_dir/DataSets/BaseSolution/PDTemp/logit`文件中有残差数据记录

如果logit文件的大小在增加，那么这个项目还在求解之中。

## 进阶介绍
如果希望进一步了解Flotherm命令，实现更高级的功能可以参考下面内容。

Flotherm命令的格式如下：

Flotherm -b|-p project [options] | -env] | [-f floscript]

- -b 批处理模式运行

- -p 交互模式运行。会打开Flotherm GUI界面。

- project 项目名称。项目PDML或FloXML文件的名称。项目名称必须用单引号或双引号，其中\是Dos命令的转义符。

- -X 只计算项目中的辐射交换系数

- -s 只计算项目中的CFD方程，不计算辐射

- -z pack_filename 将求解的项目导出为压缩文件，以便存档或传输到其他系统。

- -r htmfile 将所有Tables规范和结果数据导出到指定的html文件。

- -C 不但求解批处理中的项目文件，同时求解项目文件所包括的优化Command Center。

  要在解决方案时使用并行处理以及Command Center项目的基本情况，必须使用CCNUMBERTHREADS环境变量（忽略“用户首选项”对话框中的处理器数量设置）指定处理器的数量。使用FLOVOLUNTEERMAXJOBS环境变量来设置要同时解决的最大项目数量。

- -o output_directory

  以CSV文件格式输出表格结果数据到指定的目录output_directory。能够输出哪些表格，可以查看帮助手册。

## 实例

- 交互式启动Flotherm，加载项目myproject ：

  ```
  Flotherm -p myproject
  ```

  省略-p选项会导致Flotherm正在使用随软件一起安装的默认项目加载。

- 将结果输出到一个html文件：

  ```
  Flotherm -b  \"my project\" -r \"result.html\"
  ```

- 要从FloSCRIPT文件`My_logFile_saved.xml`运行Flotherm，：

  ```
  Flotherm -f \"<install_dir>\flosuite_v<version>\Flotherm\WinXP\bin\LogFiles\
  My_logFile_saved.xml\"
  ```

  