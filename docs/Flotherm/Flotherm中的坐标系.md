# Flotherm中的坐标系

Flotherm软件中有全局坐标系，而每个器件又有自己的坐标系，经常让人摸不着头脑。这里总结下在各种情况下到底用的是什么坐标系。

## 坐标系的显示

在Edit -- User Preferences （`F11`）面板中可以设置是否显示全局坐标系和对象的局部坐标系。

![image-20211214140012411](http://cdn.mekesim.com/assets/image-20211214140012411.png)

## 对象Location属性面板中的坐标

对象Location属性面板中的坐标为全局坐标。如下图，Cuboid对象的局部坐标和全局坐标系不一致，但是在Position和Size中的数值是按照全局坐标系来的。

![image-20211214140325324](http://cdn.mekesim.com/assets/image-20211214140325324.png)

!!! warning 注意

    需注意的是，虽然这里的位置坐标是以全局坐标系为准，但是X，Y，Z值表示的是对象的局部坐标原点在全局坐标系中的位置。所以有时候我们会发现即使两个对象重合，但他们的位置坐标却无法保持一致。

## Assembly的坐标系

Assembly和其中对象的的坐标系关系比较麻烦，有两种方式定义Assembly中对象的坐标系，一种是绝对坐标系，一种是相关坐标系。

- 绝对坐标系选项下，Assembly中对象的坐标以全局坐标系为准。如果移动Assembly会改变其中对象的位置，同时改变其中对象的坐标值。
- 相对坐标系选项下，Assembly中对象的坐标以Assembly的坐标系为准。如果移动Assembly会改变其中对象的位置，但是其坐标值不会改变，因为它们始终是相对于父节点Assembly的坐标系的。

这里建议还是以软件的默认选项Absolute Coordinates设置。如果采用相对坐标系，一层层Assembly套嵌下去，最后对象的位置可能令人发狂。

![image-20211214213327120](http://cdn.mekesim.com/assets/image-20211214213327120.png)

## 对象网格约束的坐标系

在对象的网格约束中，是按照对象的局部坐标系来定义的。如下图，给对象的Z0网格约束选项设置为Minimum Number为2，结果可以看到它是将局部坐标系的Z向划分成了两个网格。

![image-20211214140813791](http://cdn.mekesim.com/assets/image-20211214140813791.png)

## 材料属性中的坐标系

在Flotherm中可以定义材料导热率为各项异性或者双向性。如下图，将某种材料定义为各向异性，这里的X，Y，Z坐标以对象的局部坐标系为准。因此，在使用这种材料的时候要注意与对象的局部坐标系保持一致。

![image-20211214141246859](assets/image-20211214141246859.png)

## 汇总信息中对象网格提示的坐标系

快捷键 `i` 可以查看对象的汇总信息，这里可以检查对象的各顶点是否有网格。如下图，提示对象的 X High和Z Low 方向上没有网格。结合下图可以看到，这里提示信息使用的是全局坐标系。

![image-20211214142129886](http://cdn.mekesim.com/assets/image-20211214142129886.png)