---
typora-copy-images-to: image
typora-root-url: image
---

## Heatsink 网格划分

Heat sink fins are not key-pointed.

The fluid flow and heat transfer in the narrow channels between the fins is not modeled accurately.

Heat sinks are extruded surfaces which help in spreading the heat over a greater surface area so that the heat can be dissipated more effectively [Q=h **A **(Ts-Tfluid)]. Modeling the flow within these narrow channels is critical to capture the *pressure loss* and *heat transfer*. When performing analysis using CFD software such as FloTHERM, this translates to having a good mesh resolution for the regions between and around the fins.

The most efficient way of modeling a heat sink in FloTHERM is to use a heat sink smart part.

When you open the Heat sink smart construction dialog box, review the value for number of cells between fins, the default value is 3 cells. If higher accuracy of pressure drop is desired, you may want to increase this number to 5 cells between the fins.

Next step is to set grid constraints on the heat sink.

1. Along the length of Heat Sink fins set an inflation to resolve the entry and exit pressure losses.
2. Set a grid constraint to resolve the thickness of the fins. Max size = fin thickness, min size allowed < (1/3)*channel width.
3. Localize the grid on the Heat Sink. You will note that the fine grid is set only for the heat sink region along with the inflated region.

Plesae refer to Tech-Note** **[**MG576603**](https://supportnet.mentor.com/portal?do=reference.tutorial&id=MG576603&lang=en&prod=C127-S212-G287-P11534) : **FloTHERM - Gridding Tools and Recommendations.**

See the attached snapshots illustrating the same.

![img](https://support.mentor.com/kbassets/external/MG516365/images/heatsinkgrid.png)

 

![3 cells in the Narrow channel](https://support.mentor.com/kbassets/external/MG516365/images/plotplaneview.png)

Heat sink smart part allows the user to conveniently set the number of cells between the fins. It is recommended to have atleast 3 cells (which is the default) between the fins to resolve the fluid flow and heat transfer within the narrow channels (refer to **MG516365).**

However there isn't an analogous way to enter the number of cells across fin thickness or heat sink base thickness in the smart part construction dialog box.

For most scenarios having a single grid cell across the fin thickness gives reasonably accurate results  because the temperature gradient within the thickness is not significant. However there could be some exceptions where the user wants to have more than 1 cell across the fin thickness to resolve the temperature gradient within the fin thickness, especially for the end fins.

There is a trick users can use to specify the number of cells within the thickness of individual components of heat sink i.e. fins and heat sink base.

1. Create a default heat sink smart part which already has setting for 3 cells between the fins.
2. Make a copy of the heat sink smart part in the same assembly & same location as original smart part.
3. Select this copy and go to **Geometry>Decompose** to decompose the smart part into its individual cuboids. You will see a new subassembly 'HeatSink:1' created containing the individual cuboid for all the fins and base.
4. Multiple select all the heat sink fins (*HSInnerFin 1:1* , *HSInnerFin 2:1* ....) and attach a grid constraint in the Yo direction ( ie. thickness) with min number = 2. Make sure you activate the Min size under the grid constraint so that this Min size overrides the system grid Min size.
5. If the heat spreading within heat sink base is significant attach a grid constraint to the Zo direction of *HSBase* cuboid with min number =3 and Min size activated.
6. Rename this newly created sub-assembly to 'Heat Sink: Fin Gridding' for ease of understanding and then deactivate it (please refer to Fig. 2 below). When an assembly/object is deactivated the grid associated with it (grid constraints etc.) is still applied in the model even though the object itself is not active in the simulation.

![1 cell for fin thickness](https://support.mentor.com/kbassets/external/MG567125/images/heatsink_default2.png)

**Figure 1**. There is only one grid cell resolving the fin thickness

![2 cells for fin thickness](https://support.mentor.com/kbassets/external/MG567125/images/heatsink_2cells.png)

**Figure 2.** Using deactivated assembly 2 cells were obtained across fin thickness.

## Enclosure walls 网格划分

When modeling enclosure walls as thick, the wall thickness is usually an order of magnitude smaller than the overall dimension of the enclosure. It is important to review the grid closely to make sure that there is at least one grid cell to resolve the wall thickness. In order to capture heat spreading effects it is recommended to have at least three cells within the wall thickness.

When chassis walls are modeled using enclosure smart part a user can specify grid constraints to specify the Max size or Min. no. of cells in any of the specified directions for the enclosure smart part, but this applies to the overall dimensions of the enclosure and does not always ensure that the enclosure walls (when modeled thick) thickness is resolved.

If the user is modeling the enclosure walls as thick and wants to capture the heat spreading effects within the walls of the enclosure it is recommended to have at least 3 cells within the thickness of the enclosure walls. In the current version of FloTHERM there isn't an option to specify or constrain the no. of grid cells for the enclosure wall thickness.

Below are some modeling/gridding techniques to resolve enclosure walls

- Create a volume region the size of inner volume of the enclosure and specify a grid inflation same as the wall thickness 't' and min no. = 3 or Max size <= 't'/3 for both the low and high sides. Attach this grid constraint to all the three directions. After attaching this grid constraint localize the mesh on the volume region to truncate this fine mesh, right at the edge of the inflated boundary which in this case is the enclosure smart part itself.

Below is an example of setting grid constraint to have a minimum of 3 cells within the enclosure walls which have thickness 't = 6 mm'.

![e](https://support.mentor.com/kbassets/internal/MG526524/images/11.jpg)

![q](https://support.mentor.com/kbassets/internal/MG526524/images/22.jpg)

 

- Another option is to decompose the enclosure smart part into its individual cuboids and then attach a grid constraint to each of the six cuboids to have at least 3 or more cells to resolve the wall thickness. This modeling option however is more tedious than the former.

# inflation on a localized grid

When an object/geometry touches the boundary of a localized grid, the keypoint grid associated with it bleeds beyond the localized region.

When an object/geometry touches the boundary of a localized grid, the fine grid associated with it bleeds beyond the edges of the region being localized. Setting an inflation under the grid constraints, inflates the size of this localized region (prevents the geometry from touching the localized boundary) thus preventing the fine grid from bleeding.

This can be best illustrated by Figure 1 shown below. Three identical assemblies of a detailed component with heat sinks mounted on them are placed next to each other.

- the assembly on the left is not localized
- the assembly in the center is localized, but you will notice that the keypoint grid from the heat sink fins and detailed component bleeds beyond the localized region.
- the last assembly on the right has a grid constraint with inflation set in all the three directions. The fine grid in this case truncates right at the edge of inflated grid.

![img](https://support.mentor.com/kbassets/internal/MG531465/images/localized%20grid.png)

​        Figure 1: Localizing with inflation prevents keypoint grid from bleeding

Sometimes setting an inflation has an added advantage of capturing physics of the problem. For example:

1. Having a fine grid at the entry & exit of heat sinks fins helps capture the pressure losses with greater accuracy (see Fig. 2 below)
2. It is strongly recommended to have grid inflation on boards and high power components to resolve the convective heat transfer close to their external surface.

![img](https://support.mentor.com/kbassets/internal/MG531465/images/visual%20editor_inflation.png)

 Figure 2: Grid inflation helps resolve the entry/exit losses associated with heat sinks.



## TIM建模

When two solid surfaces are in contact there are small air gaps at interface due to imperfections on the surface smoothness. A thermal interface material (TIM) is placed between the two solid surfaces to fill in the air gaps and enable better heat transfer across this interface. Hence modeling the effect of TIM is critical.

In FloTHERM when modeling TIMs there are two approaches the user can take.

1. Create a collapsed cuboid of thickness 't' between the two surfaces in contact and assign a material property (conductivity **k**) to this collapsed cuboid. FloTHERM calculates the through plane resistance of this collapsed cuboid R_th_throughPlane = (t/k), then it takes into account this R_th for heat transfer (1D) normal to the contact surface. The in-plane conductivity (heat spreading) of the TIM cuboid is ignored.
2. Assign a surface attribute to one of the surfaces in contact and specify a value of Rsurf-solid ( SI units Km^2/W). The advantage of this approach over approach 1 is that project tree is simpler. When using this approach to model TIM between component and heat sink it is best to attach the surface property to the component surface. This is assuming the entire component surface is in contact with the heat sink.

When using option #1 above it is important to make sure that the TIM collapsed cuboid is placed lower in the hierarchy below the two objects in contact to make sure it is not overwritten by one of the non-collapsed cuboids in contact.

In order to model contact resistance between two solid surfaces the modeling approach is to attach a surface attribute to one of the surfaces in contact and specify a value of Rsurf-solid resistance value ( units = K m^2/W or C in^2/W).

In order to do this - select one of the two objects (cuboid or smart part) Right Click>Surface =>Rsurf-solid ; you can attach this surface resistance to the appropriate surface of the object.

One practical application of this is when modeling the thermal interface material (TIM) between a component top surface and heat sink base.A surface resistance Rsurf-solid can be attached to either of the surfaces to model the thermal resistance of the TIM when heat moves from the component into the heat sink base.

The advantage of this approach is that typically the TIM thickness is very very small when compared with the other objects. If TIM was to be modeled discretely as a cuboid it can lead to very thin grid cells leading to high aspect ratios. Using the Rsurf-solid approach this can be avoided.

![Two cuboids in contact](https://support.mentor.com/kbassets/internal/MG514364/images/contact_resistance.png)

![image](https://support.mentor.com/kbassets/internal/MG514364/images/MG514364.png)

## Compact模型的表面温度

When a package is modeled as 2 Resistor or Delphi compact component smart part and if its top surface (Zo high) was tocuhing a solid object for example a heat sink base then a surface temperature plot of the compact component does not show the top surface of compact component.

A workaround for this is to place a collapsed cuboid between the compact component top surface and the solid object say heat sink base. You can attach a really high conductivity (k = 1000 W/m-K) to the collapsed cuboid so that its through plane resistance is negligibly small.

Below is an example comparing two identical 2 resistor components. Component 2 has a solid heat sink base touching its top surface- when surface temperature is generated on both the components the top surface of component 2 becomes invisible (Fig.1).

![2R Surface temp](https://support.mentor.com/kbassets/internal/MG561597/images/2r_components_surfacetemp.png)

**Figure 1: Component 2 top surface is invisible**

In order to avoid above, create a collapsed cuboid sandwiched between Comp 2 top surface and Heat sink base. After the simulation is re-run, generate the surface temperarure on the compact component and also on the collapsed cuboid we created. Since the collapsed cuboid has high conductivity material attached to it, its surface temperature is almost same as Tcase of component 2 as seen in the Fig.2 below.

**Note**: Please make sure that the collapsed cuboid is placed lower in the project tree than both the compact component and the Heat sink base. This ensures that the collapsed cuboid is not overwritten by the two solid objects in contact.

 

![Top surface seen](https://support.mentor.com/kbassets/internal/MG561597/images/2r_components_surfacetemp2.png)

**Figure 2: Component 2 top surface has a collapsed cuboid ( high k) on its top surface**

Tables Results for the model can be seen below.

![Tables Results](https://support.mentor.com/kbassets/internal/MG561597/images/2r_components_tables.png)

## System grid settings

No "minimum size" has been defined on the local mesh.

Make it simple to guarantee a success in the mesh strategy:

1. Always add a "grid constraint" to each localized region to ensure grid quality in all three direction Xo, Yo and Zo.
2. Always define a "minimum size" and "maximum size" for the system grid and each local grid: 

-  "maximum size" guarantees to obtain a regular mesh on the local region. The minimum size guaranties the minimum solid grid and minimum fluid grid in channel in the area that is needed in this area.

\- "minimum size" on the local grid guarantees to be independent from the system grid. Try to adjust the parameters as closest to the needs to gain some grid cells and to improve the grid ratios. The "minimum size" of the grid constraint will have only an effect if it is smaller than the system minimum size, but as local grid is used to get smaller mesh than the system, then always specify this local "minimum size" parameter.

# Modeling FAQs

Answers to frequently asked questions (FAQs) about modeling.

1. Q: What is the difference between global and ambient?

   A: The external ambient temperature settings made in the Model Setup Tab - Global System Settings Section is used for the following:

   - As a reference temperature for buoyancy calculations
   - As the initial condition at the start of a solution
   - As a default temperature of air convected into the model

   The external radiant temperature is used as a default external temperature that is radiated to, from any object within the solution domain that is part of the radiation calculation and can ‘see through’ to the outside of the solution domain.

   Ambient attributes attached to the sides of the solution domain or a solution domain cutout can be used to override the Global temperature values.

2. Q: When do I have to use a source?

   A: A source attribute attached to a source primitive, as opposed to a thermal attribute attached to a cuboid, is useful for the following reasons:

   - Definition of a source of heat in a portion of a cuboid.
   - Ability to define heat dissipation in terms of W/m3 (for an uncollapsed source), W/m2 (for a collapsed source) or as a linear function of the temperature.

   In addition to this, a source can be placed in air and values of pressure, velocity, and so on, defined for that portion of air space.

## flotherm如何取消全部隐藏？

flotherm隐藏和取消隐藏的快捷键分别是F12和Shit+F12。

有时候希望显示全部隐藏对象，在Project Manager界面下没有这种操作。不过可以打开Visual Editor，按Ctrl+F12取消隐藏，再返回Project Manager界面就行了。

![1515726746421](image/1515726746421.png)

## 修改模型时加载很慢

 对于有大量网格模型需要时间重新计算网格，会有停滞感。

下列任何形式显示网格时就会重新计算网格： 

- 在绘图板中显示网格
- 显示“网格摘要”对话框
- 系统网格属性表显示
- 显示 de-keypointed 摘要列

所以，如果需要进行多项修改，建议关闭以上选项，使得不重新计算网格。

## Batch Mode

打开项目文件，sanity check 并 re-initialize

在项目文件夹上级目录创建批处理文件xxx.bat

内容

```
@echo off
call "C:\Program Files\MentorMA\flosuite_v12\flotherm\WinXP\bin\flotherm" -b \"ProjectA\"
call "C:\Program Files\MentorMA\flosuite_v12\flotherm\WinXP\bin\flotherm" -b \"ProjectB\"
:end
```

双击运行此批处理文件xxx.bat即可开始求解。

运行后目录下会生成一个`floerror.log`文件，里面有简单摘要信息。

## 计算热辐射

需要进行项目设置和面属性设置。

1. [Model/Modeling] 选中 “**Radiation On**”
2. 指定对象**面属性**中的辐射率
3. 指定**辐射**属性，定义辐射离散化的像素大小。
4. Specify [**Radiation**] attribute (to define the pixel size for the radiation discretization). On each pixel, FloVENT or FloTHERM will consider a uniform temperature for ray tracing method. This pixel is at least the size of the cells, but the pixel can be and will often be wider than the local cell size.
   1. “Single Radiating” : create a single pixel on the surface.
      1. Define “Single Radiating” for small parts of the models or low temperature gradient on the surface of this part.
   2. “Subdivided radiating”: create multiple pixel on the surfaces based on your criteria.
      1. Define “Subdivided radiating” for big surface or when the temperature gradients are high on the surface of this part.

Flotherm使用射线追踪法计算辐射





# JESD51-14

用电气测试方法得到元器件的$R_{\theta-JC}$

文档可以从JEDEC官网免费获取。

sec4， 测试需求，定义了两种测试方法：干界面，导热胶界面

Sec 5，测试结果分析



## 空气温度设置的区别

Why do I see two different places to specify ambient temperature? Which one takes precedence if they are different?

What is the temperature of the air coming into the computational domain?

What is the temperature of my surroundings outside the computational domain?

System Ambients: These settings prescribe the boundary conditions at each face of the domain.

![img](https://support.mentor.com/kbassets/external/MG245395/images/system_ambient.png)

- Any air entering the system across an open boundary will be at the temperature set by the ambient attached to that face of the computational domain.
- If a solid touches the edge of the solution domain that is defined as open boundary. The heat removed from that surface will be determined by the value of heat transfer coefficient (HTC) that is set under the ambient. For example if the domain size is the same as the enclosure, then the ambient set on domain face defines the heat transfer coefficient on the external surface of enclosure walls.

If a face of the domain is open, but does not have an ambient attached to it, then the user is given a WARN about it. The solver will use the values set under **Model Setup>Default Ambient Temperature** as the temperature for the air entering through that open face.

![img](https://support.mentor.com/kbassets/external/MG245395/images/ambient_temp.png)

Model Setup: This setting is used by the software for several purposes:

- To provide defaults used at the beginning of a solve to give all of the grid cells a reasonable start value for temperature, pressure and velocities.
- To provide default values to be used if an open boundary is defined without a **System>Ambient** attached.
-  To provide a reference on which to calculate buoyancy. (i.e. fluid at a temperature higher than the **Model Setup> Default Ambient** **Temperature** will rise and fluid at a lower temperature will sink).
- To provide a background (External Radiant Temperature) temperature value to which all objects can radiate to, if radiation is activated under modeling options.


## 自然散热求解域

Natural convection model for a sealed system does not converge.

Residuals do not converge (Natural convection scenario)

- The domain size should be larger than the sealed system.
- No material attached to the enclosure.
- Radiation is not activated

When modeling natural convection for a sealed system it is important to have the solution domain size larger than the sealed system. This allows the CFD solver to simulate the fluid flow around the chassis and in turn calculate the **heat transfer coefficient** on the chassis walls.

The rule of thumb is to have the domain size larger by a minimum of two heights above and one height below the sealed system assuming gravity acts vertically down (say -Y) and height refers to the dimension parallel to gravity (along Y). On the sides the domain size has to be larger by at least half the width and length.

So if gravity was acting along -Y direction the domain size has to be **+2Y above** and **1Y below** the box. On the sides it has to be larger by 0.5X and 0.5Z. This ensures that the hot plume rising due to buoyancy effects gets enough height to rise and expand into the still air around it. The extended domain on the sides allows for air to enter the solution domain through the side faces. Please check to see if these side faces are modeled as open or symmetry faces ( Right Click on **System > Faces**).

Also it is important to attach a **material attribute** to the enclosure to ensure that there is heat transfer across the walls of the enclosure.

The walls of the enclosure need to be modeled as thick rather than thin or collapsed (default) if

- Heat spreading effects within the wall are important
- Radiation is activated and a **radiation attribute** is attached to the enclosure.

Suggested further reading

Tech Note : **MG245386** 

 App Note: [**MG575808**](https://supportnet.mentor.com/portal?do=reference.appnote&id=MG575808&lang=en&prod=C127-S212-G287-P11534)

![Natural Convection Domain size](https://support.mentor.com/kbassets/external/MG516036/images/natconvection_domainsize3.png)

![Plot plane for temperature](https://support.mentor.com/kbassets/external/MG516036/images/mg516036_temp_natconvection.png)