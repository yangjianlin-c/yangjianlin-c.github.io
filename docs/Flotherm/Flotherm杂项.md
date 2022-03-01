## 项目文件无法打开怎么办

在项目文件夹下找到`PDProject`文件夹下一般会有三个文件

- group
- group.bak
- groupTrans

将其中的任意一个文件重命名为.pdml文件。

然后在Flotherm中导入这个.pdml文件，尝试恢复项目。

这种方式同样适用于打包的.pack文件。因为.pack文件只是将这个项目命令打包成一个压缩文件，用常用解压软件解压，即可得到一个完整的项目目录。

## 如何修改打开帮助手册的默认浏览器

修改windows环境变量

MGC_HTML_BROWSER: C:\Program Files\Google\Chrome\Application\chrome.exe