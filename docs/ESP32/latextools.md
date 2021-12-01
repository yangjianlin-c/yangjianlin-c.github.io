

## 安装Latextools

Ctrl+shift+P, Install Package, LaTexTools

## 安装SmartPDF

为了支持反向搜索功能
设置SmartPDF，setting，options,在最下方的逆向搜索命令行，输入

	"C:\Program Files\Sublime Text 3\sublime_text.exe" "%f:%l"

## 编译查看文档

Sublime里面

Ctrl+B,或F7即可编译查看文档了。

## 配置Latextools

默认情况下，LaTeXTools 使用 pdflatex编译，但是现在一般都是用 XeLaTeX，因此，这里还是需要一点改变的。

Preferences, Package Settings, Latex tools, Setting User

增加如下内容：

"builder_settings": 
{
    "program": "xelatex"
}