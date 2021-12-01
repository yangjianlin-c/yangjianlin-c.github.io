title: FloSCRIPT使用
date: 2018/7/13
---

用户在Project Manager, Drawing Board 和 FloMCAD Bridge的所有动作都自动记录为FloSCRIPT log 文件，位于：

```
.\flosuite_v12\flotherm\WinXP\bin\LogFiles\
```

可以打开XML文件了解文件结构。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xml_log_file version="1.0">
    <!--Copyright 2017 Mentor Graphics Corporation-->
    <!--All Rights Reserved-->
    <select_geometry>
        <selected_geometry_name>
            <geometry name="Root Assembly"/>
        </selected_geometry_name>
    </select_geometry>
    <create_geometry geometry_type="cuboid">
        <source_geometry>
            <geometry name="Root Assembly"/>
        </source_geometry>
    </create_geometry>
    <select_geometry>
        <selected_geometry_name>
            <geometry name="Root Assembly">
                <geometry name="Cuboid" position_in_parent="0"/>
            </geometry>
        </selected_geometry_name>
        <deselected_geometry_name>
            <geometry name="Root Assembly"/>
        </deselected_geometry_name>
    </select_geometry>
    <modify_geometry new_value="440" property_name="sizeX">
        <geometry_name>
            <geometry name="Root Assembly">
                <geometry name="Cuboid" position_in_parent="0"/>
            </geometry>
        </geometry_name>
    </modify_geometry>
    <modify_geometry new_value="Mentor" property_name="name">
        <geometry_name>
            <geometry name="Root Assembly">
                <geometry name="Cuboid" position_in_parent="0"/>
            </geometry>
        </geometry_name>
    </modify_geometry>
```

## 运行FloSCRIPT log文件

有两种方式，从Floterm里运行或使用命令行方式运行。

1. 从Floterm里运行。

   Macro -- Play FloSCRIPT.

2. 命令行方式。

   ```
   flotherm.bat –f [FloSCRIPT File]
   ```

   