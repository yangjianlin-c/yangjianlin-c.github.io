# python matplotlib 支持中文标题

简单来说就是在配置文件中加入中文字体。

找到matplotlib的配置文件`matplotlibrc`的路径，使用如下命令可找出：

```python
import matplotlib
a=matplotlib.matplotlib_fname()
print(a)
```

找到`matplotlibrc`文件中的`font.sans-serif`，将前面的注释符去掉，后面加入`Microsoft YaHei,` 即修改成这样：

```html
font.sans-serif: Microsoft YaHei, DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```

即可!

也可以用系统中的其他字体，如KaiTi，等。