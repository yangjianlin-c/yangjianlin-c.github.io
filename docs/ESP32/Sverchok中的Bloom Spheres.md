# Sverchok中的Bloom Spheres

*2015年9月9日星期三*



​         ![img](http://elfnor.com/images/bloom_wobble.png)       

[约翰·埃德马克（John Edmark）](http://www.instructables.com/id/Blooming-Zoetrope-Sculptures/)关于他所谓的绽放球体的这些[视频](http://www.instructables.com/id/Blooming-Zoetrope-Sculptures/)激发了我在Sverchok尝试类似的东西。Edmark设计的3D打印形式在频闪灯下旋转时会出现移动和扭曲。

它可以生成以相同方式工作的计算机动画。[Mangakid](https://www.youtube.com/channel/UClifVGXznefMacC29olhX7g)已经取得了一定的Blender动画基于Edmark的工作。可以在此[stackoverflow问题和答案中](http://blender.stackexchange.com/questions/1371/organic-yet-accurate-modeling-with-the-golden-spiral/26800#26800)找到用于mangakid动画的Python代码片段。

在Sverchok中处理bloom球的第一个阶段是编写一个脚本节点来生成基本网格结构，这是基于绽放的基础。Edmark将此描述为：

> 首先，将一组点一次一个地放置在圆柱形布置中。每个点从前一点开始围绕圆柱轴放置137.5º，并且稍微抬起一点......
>
> 下一步是通过将点投射到球体的中心点，将每个点投影到球体的表面上......
>
> 这些点与线连接以形成四边形网格。

这最好用球坐标计算出来。

黄金角度$g$
$$
\begin{align*}
g=\pi (3-\sqrt{5}) &= 2.399963... \textrm{ radians}\\ 
 &= 137.507...^{\circ}
\end{align*}
$$

球体的半径是$r_0$和$z_h$是“点升一点”的增量。然后 $i=0$绽放球体上的点由下式给出：
$$
\begin{align*}
\theta (i) &= \frac{i}{g}\\
\phi (i) &= \tan^{-1} \frac{r_0}{iz_h}\\
r(i) &= r_0
\end{align*}
$$
我已将其编码为脚本节点。要在Blender中使用bloom sphere节点，请先安装[Sverchok](http://nikitron.cc.ua/sverchok_en.html)插件。从[github](https://github.com/elfnor/bloom_sphere)下载bloom sphere代码。然后将python文件作为文本块加载到混合文件中。添加Scripted Node到Sverchok节点树。在节点上，bloom_sphere.py从下拉列表中选择代码。然后单击此字段右侧的插件图标。节点应该通过一些输入和输出变为蓝色。将输出Verts和Faces输出连接到Viewer Draw节点，您应该看到一些几何。

也可以使用XYZ function surface它是Extra ObjectsBlender 的插件的一部分来生成网格顶点。我发现让插件加入然后形成正确的四边形网格要困难得多。在我的Sverchok脚本节点中执行此操作要容易得多。

该Frame Info节点可以很容易地用于每帧旋转137.5°的布隆球。将结束帧设置为145以进行连续循环动画。

​         ![img](http://elfnor.com/images/bloom_sphere_nodes.png)       

​         ![img](http://elfnor.com/images/bloom_sphere.gif)       

相同的节点图也可用于为John Edmark的stl文件制作动画，这些文件是根据Creative Commons BY NC SA许可证[在此处](https://www.dropbox.com/sh/nsinei7jlu0z3wk/AADsN9wI7IOIF6VOnREx-Tt6a?dl=0)提供的。只需将stl导入Blender并替换Scripted Node为Object Scene节点即可。

或者，在Sverchok外部旋转网格，进行关键帧动画，其中第一帧没有旋转，结束帧围绕z轴旋转137.5°*（帧数-1）。

例如：

- 选择要旋转的对象

- 将结束帧设置为145

- 将活动键控设置更改为“旋转”

- 在第一帧上插入关键帧

- 移动到最后一帧

- 将对象围绕z轴旋转设置为19800度（144 * 137.5°= 19800）

- 在此框架上插入关键帧

- 将当前帧设置回1

- 打开“曲线图编辑器”视图

- 将动画曲线的插值模式更改为线性。使用菜单：Key> Interpolation Mode> Linear或使用键盘T L。

- 检查沿一帧的踩踏将旋转Z角改变137.5°

这将给出无缝的6秒（145帧/ 24帧/秒〜= 6秒）动画。它是无缝的，因为19800是360的整数倍（360°* 55 = 19800°）。

注意：任何旋转角度在哪里

G

n ，m

= n g- 米2 π

Gñ，米=ñG- 米2π

其中Ñ

=

1

，

2

，

。

。



ñ=1，2，。。anf m



米是一个整数，用于将角度映射回间隔-

π



\- π到π



π也会工作。例如，每帧旋转137.5°，-85°，52.5°，170°，-32.5°，105°，-117.5°或20°中的任何一个都可以工作，但对于每个角度，动画看起来会有不同的速度。

现在来到有趣的部分，编辑网格以生成有趣的动画。John Edmark描述：

> *每个四边形都有一个附属物......*

我们可以按照我的[Centers Polygon](https://elfnor.com/simple-sverchok-01-centers-polygons.html)[示例](https://elfnor.com/simple-sverchok-01-centers-polygons.html)执行此操作，但我将使用该Adaptive Polygons节点显示另一种方式以获得不同的外观。

​         ![img](http://elfnor.com/images/bloom_sphere_adaptive_polygon_nodes.png)       

我删除了用于实现旋转的节点，以简化上述节点图。

​         ![img](http://elfnor.com/images/bloom_sphere_ap.gif)       

John Edmark接着描述：

> *为了使附肢看起来在动画时来回移动，它们的尖端在放置时会顺序地左右扭曲（以正弦运动）。*

执行类似操作的最简单方法是在Adaptive Polygons节点之前将每个顶点移动到一侧。在球坐标中最容易想到添加“从一侧到另一侧”的运动。如果我们改变一个点的“phi”极坐标，它将左右移动。

Sverchok现在有节点将顶点的x，y，z坐标更改为极坐标并再次将其更改回来。这里我们对每个顶点应用正弦偏移。通过改变节点的stop值来改变正弦波的频率Float Series。π的

倍数（或分数）

π是明智的。甲Float入口节点被用来改变正弦波的幅度。

​         ![img](http://elfnor.com/images/wobble_vertex_node_tree.png)       

​         ![img](http://elfnor.com/images/wobble_vertex.gif)       

随着更多的想法（和更多的节点！）我们实际上可以摆动我们的附肢 自适应多边形的末端。

首先，我们需要用List Mask (out)节点分离出末端顶点。对于掩模，我们使用每个顶点的长度（带有一个Vector Math节点）来选择那些不在bloom球体表面上的顶点。使用List Length节点需要一些麻烦来获得用作正弦曲线的角度输入的数字范围。这个多级列表需要在单个尖峰结束时为所有点提供相同的角度值，然后为下一个尖峰增加。

两组顶点（具有正弦摆动的末端顶点和球体上的原始顶点）与List Mask Join (in)使用我们用于分离它们的相同掩模的节点一起放回。

[         ![img](http://elfnor.com/images/sc_bloom_sphere_node_11_nodetree_for_post.blend_small.png)       ](http://elfnor.com/images/sc_bloom_sphere_node_11_nodetree_for_post.blend_large_02.png)

得到这样的动画：

​         ![img](http://elfnor.com/images/wobble_color.gif)       